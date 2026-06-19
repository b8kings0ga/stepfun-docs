# StepFun API Skill / 阶跃星辰 API Skill

Bilingual Codex skill for building, debugging, and migrating integrations with StepFun / 阶跃星辰 APIs and Step Plan.

用于构建、调试和迁移 StepFun / 阶跃星辰 API 与 Step Plan 集成的中英双语 Codex skill。

## What It Supports / 支持功能

- Chat Completions / OpenAI-compatible chat
- Anthropic-compatible Messages API
- Responses API
- Reasoning and multimodal model selection
- Image generation, image-to-image, and image editing
- TTS, ASR, streaming ASR, and realtime voice
- Web search
- Token counting
- Files and vector stores
- Step Plan third-party tool configuration
- OpenAI migration notes
- Pricing, model, and rate-limit snapshot lookup
- Local docs snapshot refresh with async page hash checks

## Install / 安装

Clone this repo into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/b8kings0ga/stepfun-docs.git ~/.codex/skills/stepfun-api
```

If you already cloned it, update with:

```bash
cd ~/.codex/skills/stepfun-api
git pull
```

The skill name is `stepfun-api`, so invoke it as:

```text
$stepfun-api
```

## Usage / 使用

Ask Codex to use the skill for StepFun work:

```text
Use $stepfun-api to implement image editing with step-image-edit-2.
```

```text
Use $stepfun-api to migrate this OpenAI chat integration to StepFun.
```

```text
Use $stepfun-api to configure Claude Code for Step Plan.
```

中文示例：

```text
用 $stepfun-api 查一下 step-image-edit-2 怎么调用。
```

```text
用 $stepfun-api 把这个 OpenAI 调用迁移到阶跃星辰。
```

```text
用 $stepfun-api 配置 Claude Code 接入 Step Plan。
```

## Freshness Check / 更新检查

Before each docs lookup, the skill instructs Codex to run:

```bash
~/.codex/skills/stepfun-api/scripts/check_stepfun_docs_update.py --update-if-changed
```

This compares:

- StepFun docs async chunk/deployment/build hashes
- `/docs/llms.txt` content hash
- Local snapshot state in `references/snapshot/update-state.json`

If the hashes changed, it refreshes the local docs snapshot automatically.

## Force Refresh / 强制刷新

Run:

```bash
~/.codex/skills/stepfun-api/scripts/fetch_stepfun_docs.py
```

This fetcher records `katana` discovery output, reads `/docs/llms.txt`, saves Markdown pages under `references/snapshot/pages`, and falls back to `trafilatura` extraction when needed.

## Repo Layout / 仓库结构

```text
SKILL.md
agents/openai.yaml
references/
  api-endpoints.md
  integration-notes.md
  models-pricing-limits.md
  snapshot/
scripts/
  check_stepfun_docs_update.py
  fetch_stepfun_docs.py
```

## Notes / 注意

- The generated OpenAPI URL returned a Mintlify sample spec during the original crawl, so this skill treats Markdown docs as authoritative unless that URL is re-verified.
- Pricing and model availability can change; refresh before cost-sensitive or production decisions.
- The raw snapshot is preserved as crawled documentation evidence.
