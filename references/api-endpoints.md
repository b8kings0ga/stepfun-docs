# StepFun API Endpoints / 阶跃星辰 API 端点

Snapshot source: `references/snapshot/pages`, fetched 2026-06-19.

快照来源：`references/snapshot/pages`，抓取时间 2026-06-19。

## Base URLs / 基础地址

- Standard API / 标准 API：`https://api.stepfun.com/v1`
- Step Plan OpenAI-compatible APIs / Step Plan OpenAI 兼容 API：`https://api.stepfun.com/step_plan/v1`
- Step Plan Anthropic-compatible Messages API / Step Plan Anthropic 兼容 Messages API：`https://api.stepfun.com/step_plan`
- Standard Anthropic SDK Messages base URL / 标准 Anthropic SDK Messages 基础地址：`https://api.stepfun.com`; the SDK appends `/v1/messages` / SDK 会自动拼接 `/v1/messages`

## Chat, Messages, Responses / Chat、Messages、Responses

- `POST /v1/chat/completions`: OpenAI-compatible Chat Completions. Supports text, multipart image/video/audio user content, tools, streaming, `response_format`, `reasoning_format`, and `reasoning_effort`.
  - OpenAI 兼容 Chat Completions。支持文本、多段图片/视频/音频用户内容、工具、流式、`response_format`、`reasoning_format` 和 `reasoning_effort`。
- `POST /v1/messages`: Anthropic-compatible Messages. Use only documented fields. Requires `max_tokens`. Supports content blocks, tools, streaming SSE events, and `output_config.effort`.
  - Anthropic 兼容 Messages。只传文档列出的字段。`max_tokens` 必填。支持 content block、工具、SSE 流式事件和 `output_config.effort`。
- `POST /v1/responses`: Responses API. Read `snapshot/pages/zh-api-reference-responses-responses-create.md` for exact item schema before coding.
  - Responses API。编码前读取 `snapshot/pages/zh-api-reference-responses-responses-create.md` 确认精确 item schema。
- `POST /v1/token/count`: OpenAI-style token count. / OpenAI 风格 token 计数。
- `POST /v1/messages/count_tokens`: Anthropic-style token count. / Anthropic 风格 token 计数。

Step Plan `step-router-v1` constraints on Chat/Messages:

Step Plan `step-router-v1` 在 Chat/Messages 中的限制：

- Use Step Plan base URLs only. / 只能使用 Step Plan 基础地址。
- `model` must be `step-router-v1`, otherwise HTTP 400 `request_params_invalid`. / `model` 必须是 `step-router-v1`，否则返回 HTTP 400 `request_params_invalid`。
- `max_tokens` upper bound is 384K. / `max_tokens` 上限为 384K。
- Image/document inputs and `web_search` tools are unsupported and may return `unsupported_content_type`. / 不支持图片/文档输入和 `web_search` 工具，可能返回 `unsupported_content_type`。
- `output_config.effort` is ignored in Messages. / Messages 中 `output_config.effort` 会被忽略。

## API Reference Endpoint Inventory / API 端点清单

- `GET /v1/accounts`: account info / 账户信息。
- `GET /v1/models`, `GET /v1/models/{model}`: model list and lookup / 模型列表和模型查询。
- `POST /v1/chat/completions`: chat completions / 聊天补全。
- `POST /v1/messages`: Anthropic-compatible messages / Anthropic 兼容 messages。
- `POST /v1/responses`: responses / Responses API。
- `POST /v1/search`: search / 搜索。
- `POST /v1/token/count`, `POST /v1/messages/count_tokens`: token counting / token 计数。
- `POST /v1/files`, `GET /v1/files`, `GET /v1/files/{file_id}`, `GET /v1/files/{file_id}/content`, `DELETE /v1/files/{file_id}`: files / 文件。
- `POST /v1/vector_stores`, `GET /v1/vector_stores`, `GET /v1/vector_stores/{vector_store_id}`, `DELETE /v1/vector_stores/{vector_store_id}`: vector stores / 知识库/向量库。
- `POST /v1/vector_stores/{vector_store_id}/files`, `GET /v1/vector_stores/{vector_store_id}/files`, `DELETE /v1/vector_stores/{vector_store_id}/files/{file_id}`: vector-store files / 知识库文件。
- `POST /v1/images/generations`, `POST /v1/images/image2image`, `POST /v1/images/edits`: image generation/editing / 图片生成和编辑。
- `POST /v1/audio/speech`: TTS / 语音合成。
- `POST /v1/audio/voices`, `GET /v1/audio/voices`, `POST /v1/audio/voices/preview`: voice clone/list/preview / 音色复刻、列表、试听。
- `POST /v1/audio/transcriptions`: legacy transcription / 旧版音频转写。
- ASR, streaming ASR, streaming TTS, and realtime voice have separate reference pages; grep `snapshot/pages/zh-api-reference-audio-*` and `zh-api-reference-realtime-chat.md`.
  - ASR、流式 ASR、流式 TTS 和实时语音有独立页面；搜索 `snapshot/pages/zh-api-reference-audio-*` 和 `zh-api-reference-realtime-chat.md`。

## Exact Field References / 精确字段参考

- Chat / 聊天：`snapshot/pages/zh-api-reference-chat-chat-completion-create.md`
- Messages：`snapshot/pages/zh-api-reference-chat-messages-create.md`
- Tool calls / 工具调用：`snapshot/pages/zh-api-reference-tool-call.md`
- Error codes / 错误码：`snapshot/pages/zh-api-reference-error-codes.md`
- Search / 搜索：`snapshot/pages/zh-api-reference-search-search.md`
- Files and vector stores / 文件与知识库：`snapshot/pages/zh-api-reference-files-*` and `snapshot/pages/zh-api-reference-vector-stores-*`
- Audio / 音频：`snapshot/pages/zh-api-reference-audio-*`
- Realtime / 实时语音：`snapshot/pages/zh-api-reference-realtime-chat.md`
- Images / 图像：`snapshot/pages/zh-api-reference-images-*`
