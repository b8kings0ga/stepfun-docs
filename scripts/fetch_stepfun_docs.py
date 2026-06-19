#!/usr/bin/env python3
"""Fetch StepFun docs into this skill's references/snapshot directory."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

try:
    import trafilatura
except Exception:  # pragma: no cover - optional runtime dependency
    trafilatura = None


ROOT = "https://platform.stepfun.com/docs"
LLMS_URL = f"{ROOT}/llms.txt"


def get_url(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "codex-stepfun-skill/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def slug_for(url: str) -> str:
    path = re.sub(r"^https://platform\.stepfun\.com/docs/", "", url)
    path = path.removesuffix(".md").strip("/")
    return re.sub(r"[^A-Za-z0-9._-]+", "-", path) or "index"


def parse_llms(markdown: str) -> list[tuple[str, str]]:
    matches = re.findall(r"^- \[([^\]]+)\]\((https://platform\.stepfun\.com/docs/[^)]+?\.md)\)", markdown, re.M)
    return [(title.strip(), url.strip()) for title, url in matches]


def try_katana(out_dir: Path) -> None:
    try:
        result = subprocess.run(
            [
                "katana",
                "-u",
                f"{ROOT}/zh/welcome",
                "-d",
                "2",
                "-silent",
                "-timeout",
                "10",
                "-retry",
                "1",
                "-fs",
                "fqdn",
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=90,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        (out_dir / "katana-error.txt").write_text(str(exc), encoding="utf-8")
        return
    (out_dir / "katana-urls.txt").write_text(result.stdout, encoding="utf-8")
    if result.stderr:
        (out_dir / "katana-stderr.txt").write_text(result.stderr, encoding="utf-8")


def trafilatura_extract(url: str) -> str:
    if trafilatura is None:
        return ""
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return ""
    return trafilatura.extract(
        downloaded,
        url=url,
        output_format="markdown",
        include_links=True,
        include_tables=True,
    ) or ""


def fetch_page(title: str, md_url: str) -> str:
    try:
        body = get_url(md_url)
        if body.strip():
            return f"<!-- title: {title} -->\n<!-- source: {md_url} -->\n\n{body}"
    except (urllib.error.URLError, TimeoutError):
        pass

    html_url = md_url.removesuffix(".md")
    extracted = trafilatura_extract(html_url)
    if extracted.strip():
        return f"<!-- title: {title} -->\n<!-- source: {html_url} -->\n<!-- extracted: trafilatura -->\n\n{extracted}"
    raise RuntimeError(f"failed to fetch {md_url}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(Path(__file__).resolve().parents[1] / "references" / "snapshot"))
    parser.add_argument("--delay", type=float, default=0.1)
    args = parser.parse_args()

    out_dir = Path(args.out)
    pages_dir = out_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    try_katana(out_dir)
    llms = get_url(LLMS_URL)
    (out_dir / "llms.txt").write_text(llms, encoding="utf-8")

    pages = parse_llms(llms)
    failures: list[str] = []
    for title, url in pages:
        try:
            text = fetch_page(title, url)
            (pages_dir / f"{slug_for(url)}.md").write_text(text, encoding="utf-8")
        except Exception as exc:
            failures.append(f"{url}\t{exc}")
        time.sleep(args.delay)

    manifest = "\n".join(f"- [{title}]({url})" for title, url in pages) + "\n"
    (out_dir / "manifest.md").write_text(manifest, encoding="utf-8")
    if failures:
        (out_dir / "failures.txt").write_text("\n".join(failures) + "\n", encoding="utf-8")
        print(f"Fetched {len(pages) - len(failures)}/{len(pages)} pages; failures: {len(failures)}", file=sys.stderr)
        return 1
    print(f"Fetched {len(pages)} pages into {pages_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
