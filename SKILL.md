---
name: stepfun-api
description: Build, debug, or migrate integrations for StepFun / 阶跃星辰 APIs and Step Plan. Use when working with StepFun chat completions, Anthropic-compatible Messages, Responses, reasoning models, multimodal image/video/audio inputs, TTS/ASR/realtime voice, image generation or editing, web search, token counting, files, vector stores, pricing/rate limits, OpenAI migration, or third-party Step Plan tool configuration. 用于构建、调试或迁移 StepFun / 阶跃星辰 API 与 Step Plan 集成，包括聊天、Messages、Responses、推理模型、多模态输入、语音、图像、搜索、计费限速和第三方工具配置。
---

# StepFun API / 阶跃星辰 API

Use this skill to answer implementation questions and write code against the StepFun platform.

使用本 skill 回答 StepFun 平台接入问题，并编写相关代码。

Prefer the local references before relying on memory. The docs were crawled from `https://platform.stepfun.com/docs` on 2026-06-19 with `katana`, `/docs/llms.txt`, and page Markdown snapshots; `trafilatura` is available as the HTML fallback in the fetch script.

优先使用本地 reference，不要只凭记忆回答。当前文档快照于 2026-06-19 从 `https://platform.stepfun.com/docs` 抓取，来源包括 `katana`、`/docs/llms.txt` 和页面 Markdown 快照；抓取脚本中保留 `trafilatura` 作为 HTML 回退抽取方式。

Before each StepFun docs lookup, run the update check:

每次查询 StepFun 文档前，先运行更新检查：

```bash
/Users/a1234/.codex/skills/stepfun-api/scripts/check_stepfun_docs_update.py --update-if-changed
```

This compares the docs page async chunk/deployment hash and `/docs/llms.txt` hash against `references/snapshot/update-state.json`. If either changed, it refreshes the local snapshot before answering.

该脚本会比较文档页异步 chunk / deployment hash 以及 `/docs/llms.txt` hash，并与 `references/snapshot/update-state.json` 中的记录对照。如有变化，先刷新本地快照再回答。

## Core Workflow / 核心流程

1. Identify the integration surface. / 先确认接入面：
   - Standard pay-as-you-go API / 标准按量 API：`https://api.stepfun.com/v1`
   - Step Plan OpenAI-compatible API / Step Plan OpenAI 兼容 API：`https://api.stepfun.com/step_plan/v1`
   - Step Plan Anthropic-compatible Messages API / Step Plan Anthropic 兼容 Messages API：`https://api.stepfun.com/step_plan`
   - Standard Anthropic-compatible Messages API with Anthropic SDK / 标准 Anthropic SDK Messages 接入：`https://api.stepfun.com`; the SDK appends `/v1/messages` / SDK 会自动拼接 `/v1/messages`
2. Load only the reference needed for the task. / 只加载当前任务需要的 reference：
   - API endpoints and protocol choices / API 端点与协议选择：`references/api-endpoints.md`
   - Model selection, pricing, limits, and rate-limit tiers / 模型选择、价格、额度与限速阶梯：`references/models-pricing-limits.md`
   - Migration and implementation pitfalls / 迁移与实现注意事项：`references/integration-notes.md`
3. For exact request/response fields, grep the raw snapshot. / 需要精确请求、响应字段时，grep 原始快照：
   - `references/snapshot/pages/zh-api-reference-chat-chat-completion-create.md`
   - `references/snapshot/pages/zh-api-reference-chat-messages-create.md`
   - `references/snapshot/pages/zh-api-reference-responses-responses-create.md`
   - `references/snapshot/pages/` for the relevant feature page / 在对应功能页中查找
4. Treat `references/snapshot/llms.txt` as the page index. Use `rg` over `references/snapshot/pages` when the question names a model, field, endpoint, or error string.

   将 `references/snapshot/llms.txt` 视为页面索引。问题中出现模型、字段、端点或错误字符串时，用 `rg` 搜索 `references/snapshot/pages`。

## High-Signal Defaults / 高信号默认值

- Use OpenAI SDK compatibility for `/v1/chat/completions`, `/v1/responses`, files, images, audio, and vector-store style workflows unless the user explicitly wants Anthropic Messages format.

  除非用户明确需要 Anthropic Messages 格式，否则 `/v1/chat/completions`、`/v1/responses`、文件、图像、音频、向量库类流程优先使用 OpenAI SDK 兼容方式。

- Use Anthropic SDK compatibility for `/v1/messages` and Claude Code style tool integrations.

  `/v1/messages` 和 Claude Code 类工具集成优先使用 Anthropic SDK 兼容方式。

- Use `step-3.7-flash` as the default multimodal/reasoning model, `step-3.5-flash` or `step-3.5-flash-2603` for text/agent workloads, and `step-router-v1` only through Step Plan.

  默认多模态/推理模型用 `step-3.7-flash`；文本或 Agent 工作负载用 `step-3.5-flash` 或 `step-3.5-flash-2603`；`step-router-v1` 只能通过 Step Plan 调用。

- Do not use the crawled `https://platform.stepfun.com/docs/api-reference/openapi.json` as authoritative unless re-verified; during this snapshot it returned a Mintlify Plant Store sample spec, not StepFun endpoints.

  不要把抓到的 `https://platform.stepfun.com/docs/api-reference/openapi.json` 当作权威规格，除非重新验证；本快照中它返回的是 Mintlify Plant Store 示例规格，不是 StepFun 真实端点。

## Refreshing The Snapshot / 刷新快照

Run the lightweight checker before each query:

每次查询前运行轻量检查：

```bash
/Users/a1234/.codex/skills/stepfun-api/scripts/check_stepfun_docs_update.py --update-if-changed
```

Run the full fetcher manually when the user asks for a forced refresh:

用户要求强制刷新时，手动运行完整抓取：

```bash
/Users/a1234/.codex/skills/stepfun-api/scripts/fetch_stepfun_docs.py
```

The fetcher records `katana` discovery output, reads `/docs/llms.txt`, saves page Markdown under `references/snapshot/pages`, and falls back to `trafilatura` extraction when a Markdown page cannot be fetched.

完整抓取脚本会记录 `katana` 发现结果，读取 `/docs/llms.txt`，将页面 Markdown 保存到 `references/snapshot/pages`，并在 Markdown 页面无法获取时回退到 `trafilatura` 抽取。
