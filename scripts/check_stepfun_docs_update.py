#!/usr/bin/env python3
"""Check StepFun docs async asset hashes and refresh the snapshot if changed."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DOCS_ROOT = "https://platform.stepfun.com/docs"
WELCOME_URL = f"{DOCS_ROOT}/zh/welcome"
LLMS_URL = f"{DOCS_ROOT}/llms.txt"


def get_url(url: str, timeout: int = 30) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "codex-stepfun-skill/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_async_hashes(html: str) -> dict[str, list[str]]:
    """Extract deployment/build/chunk fingerprints from the Mintlify/Next page."""
    dpl_ids = sorted(set(re.findall(r"[?&]dpl=([^\"'&<>]+)", html)))
    build_ids = sorted(set(re.findall(r'"buildId"\s*:\s*"([^"]+)"', html)))
    chunks = sorted(
        set(
            re.findall(
                r"/docs/_next/static/chunks/([^\"'<>?\s]+\.(?:js|css))",
                html,
            )
        )
    )
    async_scripts = sorted(
        set(
            re.findall(
                r"<script[^>]+src=\"(/docs/_next/static/chunks/[^\"?]+\.js)(?:\?[^\">]+)?\"[^>]*async",
                html,
            )
        )
    )
    return {
        "deployment_ids": dpl_ids,
        "build_ids": build_ids,
        "chunks": chunks,
        "async_scripts": async_scripts,
    }


def current_fingerprint() -> dict[str, Any]:
    html = get_url(WELCOME_URL)
    llms = get_url(LLMS_URL)
    async_hashes = extract_async_hashes(html)
    payload = {
        "welcome_url": WELCOME_URL,
        "llms_url": LLMS_URL,
        "llms_sha256": sha256_text(llms),
        "welcome_async": async_hashes,
    }
    payload["fingerprint_sha256"] = sha256_text(json.dumps(payload, sort_keys=True, ensure_ascii=True))
    return payload


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_state(path: Path, fingerprint: dict[str, Any], changed: bool, refreshed: bool) -> None:
    state = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "changed": changed,
        "refreshed": refreshed,
        **fingerprint,
    }
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def snapshot_llms_hash(snapshot_dir: Path) -> str | None:
    llms_path = snapshot_dir / "llms.txt"
    if not llms_path.exists():
        return None
    return sha256_text(llms_path.read_text(encoding="utf-8"))


def run_refresh(skill_dir: Path) -> int:
    fetch_script = skill_dir / "scripts" / "fetch_stepfun_docs.py"
    return subprocess.run([str(fetch_script)], check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--update-if-changed", action="store_true")
    parser.add_argument("--json", action="store_true", help="Print machine-readable result")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir)
    snapshot_dir = skill_dir / "references" / "snapshot"
    state_path = snapshot_dir / "update-state.json"
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    before = load_json(state_path)
    current = current_fingerprint()
    live_changed = before is not None and before.get("fingerprint_sha256") != current["fingerprint_sha256"]
    snapshot_changed = snapshot_llms_hash(snapshot_dir) not in (None, current["llms_sha256"])
    changed = live_changed or snapshot_changed

    refreshed = False
    refresh_rc = 0
    if args.update_if_changed and changed:
        refresh_rc = run_refresh(skill_dir)
        refreshed = refresh_rc == 0
        current = current_fingerprint()
        changed = False if refreshed else changed

    write_state(state_path, current, changed=changed, refreshed=refreshed)

    result = {
        "changed": changed,
        "refreshed": refreshed,
        "state_path": str(state_path),
        "fingerprint_sha256": current["fingerprint_sha256"],
        "llms_sha256": current["llms_sha256"],
        "refresh_rc": refresh_rc,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        status = "refreshed" if refreshed else "changed" if changed else "current"
        print(f"StepFun docs snapshot is {status}: {current['fingerprint_sha256']}")
    return 0 if refresh_rc == 0 else refresh_rc


if __name__ == "__main__":
    raise SystemExit(main())
