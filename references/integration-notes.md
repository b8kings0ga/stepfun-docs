# StepFun Integration Notes / 阶跃星辰接入笔记

Snapshot source: `references/snapshot/pages`, fetched 2026-06-19.

快照来源：`references/snapshot/pages`，抓取时间 2026-06-19。

## OpenAI Migration / 从 OpenAI 迁移

- Replace the API key and set OpenAI SDK `base_url` / `baseURL` to `https://api.stepfun.com/v1`.
  - 替换 API key，并将 OpenAI SDK 的 `base_url` / `baseURL` 设置为 `https://api.stepfun.com/v1`。
- Keep OpenAI-compatible request shape for Chat Completions, image, audio, files, and vector stores unless a StepFun page documents a field difference.
  - Chat Completions、图像、音频、文件、向量库默认沿用 OpenAI 兼容请求结构；除非 StepFun 文档明确说明字段差异。
- Prefer `step-3.7-flash` for multimodal/reasoning migration, `step-3.5-flash` for text reasoning, and `step-image-edit-2` for image editing.
  - 多模态/推理迁移优先 `step-3.7-flash`；文本推理用 `step-3.5-flash`；图像编辑用 `step-image-edit-2`。
- For exact examples, read `snapshot/pages/zh-guides-developer-openai.md` and `snapshot/pages/zh-quickstart-overview.md`.
  - 精确示例见 `snapshot/pages/zh-guides-developer-openai.md` 和 `snapshot/pages/zh-quickstart-overview.md`。

## Chat And Structured Output / Chat 与结构化输出

- Chat `messages[].content` can be text or multipart objects with `text`, `image_url`, `video_url`, or `input_audio`.
  - Chat 的 `messages[].content` 可以是文本，也可以是包含 `text`、`image_url`、`video_url` 或 `input_audio` 的 multipart 对象。
- Image URL supports http/https or base64 data URLs for jpg/jpeg/png/webp/static gif. `detail` can be `low` or `high`; high uses more tokens and preserves more detail.
  - 图片 URL 支持 http/https 或 base64 data URL，格式包括 jpg/jpeg/png/webp/静态 gif。`detail` 可取 `low` 或 `high`；`high` 消耗更多 token，但保留更多细节。
- Video URL supports mp4 over http/https; docs recommend less than 128 MB and under 5 minutes.
  - 视频 URL 支持 http/https 的 mp4；文档建议小于 128 MB、时长小于 5 分钟。
- Audio input supports base64 mp3/wav via `input_audio`.
  - 音频输入通过 `input_audio` 支持 base64 mp3/wav。
- `response_format.type` can be `text`, `json_object`, or `json_schema`. `json_schema` is documented only for `step-3.5-flash` and `step-3.5-flash-2603`.
  - `response_format.type` 可为 `text`、`json_object` 或 `json_schema`。文档中 `json_schema` 仅适用于 `step-3.5-flash` 和 `step-3.5-flash-2603`。
- `reasoning_format` can be `general` or `deepseek-style`; DeepSeek style exposes `reasoning_content`.
  - `reasoning_format` 可为 `general` 或 `deepseek-style`；DeepSeek 风格会暴露 `reasoning_content`。
- `reasoning_effort` controls depth where supported: `step-3.7-flash` supports `low` / `medium` / `high`; `step-3.5-flash-2603` supports `low` / `high`.
  - `reasoning_effort` 控制推理深度；`step-3.7-flash` 支持 `low` / `medium` / `high`，`step-3.5-flash-2603` 支持 `low` / `high`。

## Messages API

- Use Messages API when the integration wants Anthropic-compatible schema or SDKs.
  - 需要 Anthropic 兼容 schema 或 SDK 时使用 Messages API。
- `max_tokens` is required. / `max_tokens` 必填。
- Content blocks use Anthropic-like `text`, `image`, `tool_use`, and `tool_result` structures.
  - Content block 使用类似 Anthropic 的 `text`、`image`、`tool_use` 和 `tool_result` 结构。
- Streaming uses SSE events such as `message_start`, `content_block_start`, `content_block_delta`, `message_delta`, `message_stop`, and `ping`.
  - 流式返回使用 SSE 事件，例如 `message_start`、`content_block_start`、`content_block_delta`、`message_delta`、`message_stop` 和 `ping`。
- With Anthropic SDK for the standard API, set `base_url="https://api.stepfun.com"`; do not include `/v1/messages`.
  - 标准 API 使用 Anthropic SDK 时，设置 `base_url="https://api.stepfun.com"`；不要手动带 `/v1/messages`。
- With Anthropic SDK for Step Plan, set `base_url="https://api.stepfun.com/step_plan"`.
  - Step Plan 使用 Anthropic SDK 时，设置 `base_url="https://api.stepfun.com/step_plan"`。

## Step Plan Tool Configuration / Step Plan 工具配置

- OpenAI-compatible tools use `https://api.stepfun.com/step_plan/v1`.
  - OpenAI 兼容工具使用 `https://api.stepfun.com/step_plan/v1`。
- Anthropic-compatible tools such as Claude Code use `https://api.stepfun.com/step_plan` because the client appends `/v1/messages`.
  - Claude Code 等 Anthropic 兼容工具使用 `https://api.stepfun.com/step_plan`，因为客户端会自动拼接 `/v1/messages`。
- Recommended validation model in the snapshot is `step-3.7-flash`.
  - 快照中推荐的验证模型是 `step-3.7-flash`。
- Common Step Plan model IDs in integration pages: `step-3.7-flash`, `step-3.5-flash-2603`, `step-3.5-flash`.
  - 集成页常见 Step Plan 模型 ID：`step-3.7-flash`、`step-3.5-flash-2603`、`step-3.5-flash`。
- `step-router-v1` is Step Plan-only and has extra constraints listed in `api-endpoints.md`.
  - `step-router-v1` 仅 Step Plan 可用，额外限制见 `api-endpoints.md`。

## Feature-Specific Pointers / 功能索引

- Web search examples and constraints / Web Search 示例与限制：`snapshot/pages/zh-guides-developer-web-search.md`
- Tool call best practices / 工具调用最佳实践：`snapshot/pages/zh-guides-developer-tool-call.md` and `snapshot/pages/zh-api-reference-tool-call.md`
- JSON mode：`snapshot/pages/zh-guides-developer-json-mode.md`
- Prompt cache / Prompt 缓存：`snapshot/pages/zh-guides-developer-prompt-cache.md`
- Context management / 上下文管理：`snapshot/pages/zh-guides-developer-multiple-round.md`
- Realtime voice / 实时语音：`snapshot/pages/zh-guides-developer-realtime.md` and `snapshot/pages/zh-api-reference-realtime-chat.md`
- TTS / 语音合成：`snapshot/pages/zh-guides-developer-tts.md` and audio API pages / 以及音频 API 页面
- ASR / 语音识别：`snapshot/pages/zh-api-reference-audio-asr*.md`
- Image generation/editing / 图片生成/编辑：`snapshot/pages/zh-guides-developer-image-generate.md`, `snapshot/pages/zh-guides-developer-image-edit.md`, and image API pages / 以及图片 API 页面
- Retrieval/vector stores / 检索与知识库：`snapshot/pages/zh-guides-developer-retrieval.md` and vector-store API pages / 以及知识库 API 页面
- Troubleshooting / 故障排查：`snapshot/pages/zh-guides-developer-troubleshooting.md`

## Known Snapshot Caveat / 已知快照注意事项

The documented OpenAPI link `https://platform.stepfun.com/docs/api-reference/openapi.json` returned a Mintlify sample Plant Store spec during this crawl. Use the Markdown endpoint pages as the authoritative snapshot unless the OpenAPI URL is re-verified.

本次抓取中，文档列出的 OpenAPI 链接 `https://platform.stepfun.com/docs/api-reference/openapi.json` 返回的是 Mintlify Plant Store 示例规格。除非重新验证该 OpenAPI URL，否则以 Markdown 端点页面作为权威快照。
