<!-- title: 语音识别（流式返回文本） -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/asr-sse.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音识别（流式返回文本）

## 产品简介

本接口提供基于 HTTP + SSE 的识别能力，适合一次性提交音频数据，并通过服务端持续推送识别结果。

### 核心特性

* 一次性提交音频
* 通过 SSE 持续返回转录结果
* 支持增量结果和最终结果
* 适合服务端调用、文件转写、准实时处理

### 接入方式总览

| 能力     | HTTP + SSE |
| ------ | ---------- |
| 音频输入   | 一次性提交      |
| 结果返回   | SSE 流式     |
| 连接方式   | HTTP POST  |
| 是否保持会话 | 否          |
| 典型端    | 服务端        |

### 服务地址

| 协议       | 环境   | 地址                                         | 说明     |
| -------- | ---- | ------------------------------------------ | ------ |
| HTTP/SSE | 正式环境 | `https://api.stepfun.com/v1/audio/asr/sse` | 单向流式响应 |

<Note>
  Step Plan 场景请使用 `POST https://api.stepfun.com/step_plan/v1/audio/asr/sse`
</Note>

## HTTP 协议接口

### 时序图

<img src="https://static-openapi.stepfun.com/static/platform-docs/resource/1772200682365_q82s2p.png" width={600} alt="" />

### 鉴权参数

| 参数名           | 必填 | 描述                      | 示例                  |
| ------------- | -- | ----------------------- | ------------------- |
| Content-Type  | 是  | 固定为 `application/json`  | `application/json`  |
| Accept        | 是  | 固定为 `text/event-stream` | `text/event-stream` |
| Authorization | 是  | 认证令牌                    | `Bearer sk-xxxx`    |

### 请求格式

请求示例：

```json theme={null}
{
  "audio": {
    "data": "audioData",
    "input": {
      "transcription": {
        "language": "zh",
        "hotwords": ["热词1", "热词2"],
        "model": "stepaudio-2.5-asr",
        "enable_itn": true,
        "enable_timestamp": true
      },
      "format": {
        "type": "pcm",
        "codec": "pcm_s16le",
        "rate": 16000,
        "bits": 16,
        "channel": 1
      }
    }
  }
}
```

#### 参数说明

| 参数路径                                         | 类型     | 描述                                                | 示例                    |
| -------------------------------------------- | ------ | ------------------------------------------------- | --------------------- |
| `audio.data`                                 | string | Base64 编码的音频数据                                    | `"audioData"`         |
| `audio.input.transcription.language`         | string | 识别语言                                              | `"zh"`                |
| `audio.input.transcription.hotwords`         | array  | 热词列表，形如 `["热词1", "热词2"]`                          | `["热词1", "热词2"]`      |
| `audio.input.transcription.model`            | string | 模型名称，支持 `stepaudio-2.5-asr`、`stepaudio-2-asr-pro` | `"stepaudio-2.5-asr"` |
| `audio.input.transcription.enable_itn`       | bool   | 是否开启 ITN 文本规范化，默认 `true`                          | `true`                |
| `audio.input.transcription.enable_timestamp` | bool   | 是否返回识别文本对应的音频时间戳，默认 `false`                       | `true`                |
| `audio.input.format.type`                    | string | 音频容器格式，支持 `ogg`、`mp3`、`wav`、`pcm`                 | `"pcm"`               |
| `audio.input.format.codec`                   | string | 编码格式；当 `type=pcm` 时通常传 `pcm_s16le`                | `"pcm_s16le"`         |
| `audio.input.format.rate`                    | int    | 采样率；`pcm` 格式必填，其他格式选填                             | `16000`               |
| `audio.input.format.bits`                    | int    | 位深；`pcm` 格式必填，其他格式选填                              | `16`                  |
| `audio.input.format.channel`                 | int    | 通道数；`pcm` 格式必填，其他格式选填                             | `1`                   |

<Info>
  **兼容性说明**：

  * 为兼容老用户，SSE 仍接受 `step-asr-1.1-stream` 作为 `model` 值传入，等同 `stepaudio-2.5-asr`。
  * SSE 不再支持 `full_rerun_on_commit`（二遍识别纠错）参数，历史代码中如仍有传入，将被服务端忽略、不影响识别结果。如需二遍识别能力，请使用 WebSocket 接入（见 [流式语音识别（双向流式）](/zh/api-reference/audio/asr-stream)）。
</Info>

补充说明：

* 音频数据需要使用 Base64 编码。
* 支持的音频格式包括 `ogg`、`mp3`、`wav`、`pcm`。
* 当音频格式为 `pcm` 时，`rate`、`bits`、`channel` 为必填参数。
* 当音频格式为 `ogg`、`mp3`、`wav` 时，`rate`、`bits`、`channel` 为选填参数。

### 响应格式

SSE 流式响应，包含以下事件类型：

#### Delta 事件 (transcript.text.delta)

表示增量转录文本。

```json theme={null}
{
  "type": "transcript.text.delta",
  "meta": {
    "session_id": "sse_1642694400123456789",
    "timestamp": 1642694400123
  },
  "delta": "识别的",
  "item_id": "item_xxx",
  "content_index": 0,
  "start_time": 0,
  "end_time": 500
}
```

| 字段                | 类型     | 描述                               |
| ----------------- | ------ | -------------------------------- |
| `type`            | string | 事件类型，固定为 `transcript.text.delta` |
| `meta.session_id` | string | 会话 ID                            |
| `meta.timestamp`  | int64  | 服务端事件 Unix 时间戳，单位毫秒              |
| `delta`           | string | 增量转录文本                           |
| `item_id`         | string | 对话项 ID                           |
| `content_index`   | int    | 内容索引                             |
| `start_time`      | int64  | 识别文本对应的音频开始时间，单位毫秒               |
| `end_time`        | int64  | 识别文本对应的音频结束时间，单位毫秒               |

<Note>
  当请求参数 `audio.input.transcription.enable_timestamp=true` 时，Delta 事件返回结果中新增 `item_id`、`content_index`、`start_time`、`end_time` 字段；`meta.timestamp` 是服务端事件 Unix 时间戳，`start_time` / `end_time` 是识别文本在音频中的时间位置，二者单位均为毫秒。
</Note>

#### Done 事件 (transcript.text.done)

表示完整转录文本已经生成。

```json theme={null}
{
  "type": "transcript.text.done",
  "meta": {
    "session_id": "sse_1642694400123456789",
    "timestamp": 1642694400456
  },
  "text": "识别的完整文字内容",
  "usage": {
    "type": "realtime_asr",
    "input_tokens": 1000,
    "input_token_details": {
      "text_tokens": 0,
      "audio_tokens": 1000
    },
    "output_tokens": 50,
    "total_tokens": 1050
  }
}
```

| 字段                | 类型     | 描述                              |
| ----------------- | ------ | ------------------------------- |
| `type`            | string | 事件类型，固定为 `transcript.text.done` |
| `meta.session_id` | string | 会话 ID                           |
| `meta.timestamp`  | int64  | Unix 时间戳，毫秒                     |
| `text`            | string | 完整转录文本                          |
| `usage`           | object | 使用统计信息                          |

#### 错误事件 (error)

表示识别过程出错。

```json theme={null}
{
  "type": "error",
  "meta": {
    "session_id": "sse_1642694400123456789",
    "timestamp": 1642694400789
  },
  "message": "错误描述信息"
}
```

| 字段                | 类型     | 描述               |
| ----------------- | ------ | ---------------- |
| `type`            | string | 事件类型，固定为 `error` |
| `meta.session_id` | string | 会话 ID            |
| `meta.timestamp`  | int64  | Unix 时间戳，毫秒      |
| `message`         | string | 错误描述信息           |
