# StepFun Models, Pricing, And Limits / 阶跃星辰模型、价格与限速

Snapshot source: `zh-guides-models-*`, `zh-guides-pricing-details.md`, fetched 2026-06-19. Pricing and model availability are drift-prone; refresh the snapshot before high-stakes cost estimates.

快照来源：`zh-guides-models-*` 和 `zh-guides-pricing-details.md`，抓取时间 2026-06-19。价格和模型可用性容易变化；高风险成本估算前先刷新快照。

## Model Selection / 模型选择

- `step-3.7-flash`: default for multimodal reasoning, images, video, agents, coding, and complex planning. Supports `reasoning_effort` `low` / `medium` / `high`. Context listed in model overview as 256K.
  - 默认用于多模态推理、图片、视频、Agent、编码和复杂规划。支持 `reasoning_effort`：`low` / `medium` / `high`。模型总览中上下文为 256K。
- `step-3.5-flash`: flagship text reasoning model for logic, math, software engineering, deep research, and tools.
  - 旗舰文本推理模型，适合逻辑、数学、软件工程、深度研究和工具调用。
- `step-3.5-flash-2603`: agent-optimized variant of `step-3.5-flash`; supports `reasoning_effort` `low` / `high`.
  - `step-3.5-flash` 的 Agent 优化版；支持 `reasoning_effort`：`low` / `high`。
- `step-router-v1`: Step Plan-only router that switches between `deepseek-v4-pro` and `step-3.5-flash` by request characteristics.
  - 仅 Step Plan 可用的路由模型，会按请求特征在 `deepseek-v4-pro` 和 `step-3.5-flash` 间切换。
- `step-1o-turbo-vision`: vision understanding model / 视觉理解模型。
- `stepaudio-2.5-realtime`: realtime voice-to-voice model / 实时语音到语音模型。
- `stepaudio-2.5-chat`: voice conversation model using Chat Completions; text output only according to the Chat API note.
  - 通过 Chat Completions 调用的语音对话模型；按 Chat API 注释，仅支持文本输出。
- `stepaudio-2.5-tts`, `step-tts-2`, `step-tts-mini`: text-to-speech and voice clone related models / TTS 与音色复刻相关模型。
- `stepaudio-2.5-asr`, `stepaudio-2-asr-pro`, `step-asr`, `step-asr-1.1`, `step-asr-1.1-stream`: ASR family / ASR 系列。
- `step-image-edit-2`: lightweight image generation/editing model / 轻量图像生成/编辑模型。
- `step-2x-large`: image generation model / 图片生成模型。

## Pricing Snapshot / 价格快照

Token pricing is per 1M tokens unless noted.

除非另有说明，token 价格均按 1M tokens 计。

- `step-3.7-flash`: input 1.35 yuan, cached input 0.27 yuan, output 8.1 yuan.
  - 输入 1.35 元，缓存命中输入 0.27 元，输出 8.1 元。
- `step-3.5-flash`: input 0.7 yuan, cached input 0.14 yuan, output 2.1 yuan.
  - 输入 0.7 元，缓存命中输入 0.14 元，输出 2.1 元。
- `step-1o-turbo-vision`: input 2.5 yuan, cached input 0.5 yuan, output 8 yuan.
  - 输入 2.5 元，缓存命中输入 0.5 元，输出 8 元。
- `stepaudio-2.5-realtime`: input 10 yuan, cached input 2 yuan, output 70 yuan.
  - 输入 10 元，缓存命中输入 2 元，输出 70 元。
- `stepaudio-2.5-chat`: input 10 yuan, cached input 2 yuan, output 25 yuan.
  - 输入 10 元，缓存命中输入 2 元，输出 25 元。
- `step-1o-audio`: input 25 yuan, cached input 5 yuan, output 60 yuan.
  - 输入 25 元，缓存命中输入 5 元，输出 60 元。
- `step-audio-2`: input 10 yuan, cached input 2 yuan, output 70 yuan.
  - 输入 10 元，缓存命中输入 2 元，输出 70 元。
- `step-audio-r1.1`: listed as free during the snapshot / 快照中显示为限免。

Audio/image unit pricing:

音频/图像按量价格：

- `stepaudio-2.5-tts`: 5.8 yuan / 10k characters / 5.8 元/万字符。
- `step-tts-2`: 2.8 yuan / 10k characters / 2.8 元/万字符。
- `step-tts-mini`: 0.9 yuan / 10k characters / 0.9 元/万字符。
- Voice clone for `stepaudio-2.5-tts`, `step-tts-2`, `step-tts-mini`: 9.9 yuan / voice; preview charges only synthesis cost.
  - `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` 音色复刻：9.9 元/音色；试听仅收合成费用。
- `stepaudio-2.5-asr`: 0.15 yuan / hour / 0.15 元/小时。
- `stepaudio-2-asr-pro`: 2 yuan / hour / 2 元/小时。
- `step-asr`: 0.9 yuan / hour / 0.9 元/小时。
- `step-asr-1.1`: 2.2 yuan / hour / 2.2 元/小时。
- `step-asr-1.1-stream`: 2.6 yuan / hour / 2.6 元/小时。
- `step-2x-large`: 0.1 yuan / image / 0.1 元/张。
- `step-image-edit-2`: 0.02 yuan / image / 0.02 元/张。
- Internet search: 0.04 yuan / call / 互联网搜索 0.04 元/次。
- File storage: 0.5 yuan / GB / day / 文件存储 0.5 元/GB/天。

## Standard API Rate-Limit Tiers / 标准 API 限速阶梯

These apply to standard pay-as-you-go Open Platform API calls, not Step Plan.

以下限制适用于开放平台标准按量 API，不适用于 Step Plan。

| Tier / 等级 | Cumulative recharge / 累计充值 | Concurrency / 并发 | RPM | TPM |
| --- | --- | ---: | ---: | ---: |
| V0 | 0 yuan / 0 元 | 5 | 10 | 5,000,000 |
| V1 | 100 yuan / 100 元 | 100 | 1,000 | 20,000,000 |
| V2 | 500 yuan / 500 元 | 200 | 5,000 | 30,000,000 |
| V3 | 2,000 yuan / 2,000 元 | 400 | 10,000 | 40,000,000 |
| V4 | 5,000 yuan / 5,000 元 | 1,000 | 20,000 | 50,000,000 |
| V5 | 10,000 yuan / 10,000 元 | 10,000 | 200,000 | 100,000,000 |

Step Plan usage is governed by subscribed monthly Credit quota, not the standard tier table.

Step Plan 用量由订阅套餐的月度 Credit 额度管理，不适用标准限速阶梯表。
