<!-- title: 流式语音识别（双向流式） -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/asr-stream.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 流式语音识别（双向流式）

## 产品简介

本接口提供基于 WebSocket 的双向流式 ASR 能力，适合实时发送音频分片并持续接收识别结果。

### 核心特性

* 支持实时音频流输入
* 支持增量文本输出与最终结果输出
* 支持服务端 VAD 语音活动检测
* 支持常见音频格式参数配置
* 适合实时对话、语音助手、会议字幕等场景

### 接入方式总览

| 能力     | WebSocket 双向流式 |
| ------ | -------------- |
| 音频输入   | 流式分片           |
| 结果返回   | 流式增量 + 完成事件    |
| 连接方式   | WebSocket      |
| 是否保持会话 | 是              |
| 典型端    | 前端 / 设备端       |

### 服务地址

| 协议        | 环境   | 地址                                             | 说明    |
| --------- | ---- | ---------------------------------------------- | ----- |
| WebSocket | 正式环境 | `wss://api.stepfun.com/v1/realtime/asr/stream` | 双向实时流 |

<Info>
  如需基于 HTTP + SSE 一次性提交音频并接收流式识别结果，请参考 [语音识别（流式返回文本）](/zh/api-reference/audio/asr-sse)。
</Info>

## Websocket 协议接口

### 时序图

服务端 vad 开启时：

<img src="https://static-openapi.stepfun.com/static/platform-docs/resource/1772198352298_4bdz2h.png" width={600} alt="" />

服务端 vad 未开启时：

<img src="https://static-openapi.stepfun.com/static/platform-docs/resource/1773732064167_a54xmg.png" width={600} alt="" />

## 鉴权参数

| 参数名           | 必填 | 描述   | 示例              |
| ------------- | -- | ---- | --------------- |
| Authorization | 是  | 认证令牌 | Bearer \{token} |

## 客户端消息类型

### 会话更新消息 (session.update)

用于更新会话配置，包括音频格式、转录参数等。

请求示例：

```json theme={null}
{
  "event_id": "event_123",
  "type": "session.update",
  "session": {
    "audio": {
      "input": {
        "format": {
          "type": "pcm",
          "codec": "pcm_s16le",
          "rate": 16000,
          "bits": 16,
          "channel": 1
        },
        "transcription": {
          "model": "step-asr-1.1-stream",
          "language": "zh",
          "prompt": "请记录下你所听到的语音内容。",
          "full_rerun_on_commit": true,
          "enable_itn": true
        },
        "turn_detection": {
          "type": "server_vad",
          "silence_duration_ms": 800,
          "threshold": 0.5
        }
      }
    }
  }
}
```

| 参数路径                                                     | 类型      | 描述                                 | 示例值                     |
| -------------------------------------------------------- | ------- | ---------------------------------- | ----------------------- |
| `event_id`                                               | string  | 当前消息事件 ID                          | `"event_123"`           |
| `type`                                                   | string  | 消息类型，固定为 `session.update`          | `"session.update"`      |
| `session.audio.input.format.type`                        | string  | 音频容器格式，支持 `pcm`、`ogg`              | `"pcm"`                 |
| `session.audio.input.format.codec`                       | string  | 音频编码格式；当 `type=pcm` 时传 `pcm_s16le` | `"pcm_s16le"`           |
| `session.audio.input.format.rate`                        | integer | 音频采样率                              | `16000`                 |
| `session.audio.input.format.bits`                        | integer | 音频位深                               | `16`                    |
| `session.audio.input.format.channel`                     | integer | 音频通道数                              | `1`                     |
| `session.audio.input.transcription.model`                | string  | 转录模型名称，支持 `step-asr-1.1-stream`    | `"step-asr-1.1-stream"` |
| `session.audio.input.transcription.language`             | string  | 识别语言                               | `"zh"`                  |
| `session.audio.input.transcription.prompt`               | string  | 提示词，用于补充上下文或专业术语                   | `"请记录语音内容。"`            |
| `session.audio.input.transcription.full_rerun_on_commit` | boolean | 是否在提交后进行二遍识别纠错，默认 `false`          | `true`                  |
| `session.audio.input.transcription.enable_itn`           | boolean | 是否开启 ITN 文本规范化                     | `true`                  |
| `session.audio.input.turn_detection.type`                | string  | 语音活动检测类型，支持 `server_vad`           | `"server_vad"`          |
| `session.audio.input.turn_detection.silence_duration_ms` | integer | 静音阈值，超过该时长后认为一句话结束                 | `800`                   |
| `session.audio.input.turn_detection.threshold`           | number  | VAD 检测阈值，值越大越严格                    | `0.5`                   |

补充说明：

* 当前支持 `step-asr-1.1-stream`。
* 如果不传 `turn_detection.type=server_vad`，服务端不会自动做 VAD。
* 这时客户端需要主动发送 `input_audio_buffer.commit`。

### 音频数据追加消息 (input\_audio\_buffer.append)

发送音频数据进行实时识别。
请求示例：

```json theme={null}
{
  "event_id": "event_124",
  "type": "input_audio_buffer.append",
  "audio": "base64_encoded_audio_data"
}
```

| 字段         | 类型       | 必需 | 描述                     |
| ---------- | -------- | -- | ---------------------- |
| `event_id` | `string` | 是  | 事件唯一标识                 |
| `audio`    | `string` | 是  | base64 编码的音频数据（WAV 格式） |

### 音频缓冲区提交消息 (input\_audio\_buffer.commit)

仅在关闭了 `server_vad` 时，才需要提交该消息，是指要求服务端提交音频缓冲区，触发转录处理

```json theme={null}
{
  "event_id": "event_125",
  "type": "input_audio_buffer.commit"
}
```

#### 字段说明

| 字段        | 类型     | 必需 | 描述     |
| --------- | ------ | -- | ------ |
| event\_id | string | 是  | 事件唯一标识 |

## 服务端消息类型

### 会话创建确认 (session.created)

确认会话创建成功。

```json theme={null}
{
    "event_id": "319612d9-aede-4456-a1fd-bb9c21493cd9",
    "type": "session.created",
    "meta": {
        "session_id": "test_trace_1766470129914296764",
        "timestamp": 1766468589040
    },
    "session": {
        "audio": {
            "input": {
                "transcription": {
                    "language": "zh"
                },
                "format": {
                    "type": "pcm",
                    "codec": "pcm_s16le",
                    "rate": 16000,
                    "bits": 16,
                    "channel": 1
                },
                "turn_detection": {
                    "type": "server_vad",
                    "silence_duration_ms": 800
                }
            }
        }
    }
}
```

### 会话更新确认 (session.updated)

确认会话配置更新成功。

```json theme={null}
{
    "event_id": "319612d9-aede-4456-a1fd-bb9c21493cd9",
    "type": "session.updated",
    "meta": {
        "session_id": "test_trace_1766470129914296764",
        "timestamp": 1766468589040
    },
    "session": {
        "audio": {
            "input": {
                "transcription": {
                    "language": "zh"
                },
                "format": {
                    "type": "pcm",
                    "codec": "pcm_s16le",
                    "rate": 16000,
                    "bits": 16,
                    "channel": 1
                },
                "turn_detection": {
                    "type": "server_vad",
                    "silence_duration_ms": 800
                }
            }
        }
    }
}
```

### 语音开始事件 (input\_audio\_buffer.speech\_started)

仅在开启了 `server_vad` 时才会返回该事件，指服务端检测到语音开始。

```json theme={null}
{
    "event_id": "319612d9-aede-4456-a1fd-bb9c21493cd9",
    "type": "input_audio_buffer.speech_started",
    "meta": {
        "session_id": "test_trace_1766470129914296764",
        "timestamp": 1766470145337
    },
    "audio_start_ms": 15240,
    "item_id": "item_26cbd6a7-16e8-44c9-b6b4-d4d3b3c87b41"
}
```

### 语音结束事件 (input\_audio\_buffer.speech\_stopped)

仅在开启了 `server_vad` 时才会返回该事件，指服务端检测到语音结束。

```json theme={null}
{
    "event_id": "406d719a-3392-4ca4-88b3-9f12d8189b74",
    "type": "input_audio_buffer.speech_stopped",
    "meta": {
        "session_id": "test_trace_1766470129914296764",
        "timestamp": 1766470143512
    },
    "audio_start_ms": 13480,
    "item_id": "item_8228b4a6-f127-4a60-8f33-20fcb7d9ff7d"
}
```

### 音频缓冲区提交确认 (input\_audio\_buffer.committed)

确认音频缓冲区已提交。

```json theme={null}
{
  "event_id": "event_xxx",
  "type": "input_audio_buffer.committed",
  "meta": {
    "session_id": "sess_xxx",
    "timestamp": 1642694400000
  },
  "item_id": "item_xxx",
  "previous_item_id": "item_yyy"
}
```

### 对话项创建事件 (conversation.item.created)

新的对话项（转录结果）已创建。

```json theme={null}
{
  "event_id": "event_xxx",
  "type": "conversation.item.created",
  "meta": {
    "session_id": "sess_xxx",
    "timestamp": 1642694400000
  },
  "previous_item_id": "item_yyy",
  "item": {
    "id": "item_xxx",
    "object": "realtime.item",
    "type": "message",
    "status": "in_progress",
    "role": "user",
    "content": [
      {
        "type": "input_audio"
      }
    ]
  }
}
```

### 转录增量事件 (conversation.item.input\_audio\_transcription.delta)

返回转录增量结果（流式输出）。

```json theme={null}
{
  "event_id": "event_xxx",
  "type": "conversation.item.input_audio_transcription.delta",
  "meta": {
    "session_id": "sess_xxx",
    "timestamp": 1642694400000
  },
  "item_id": "item_xxx",
  "content_index": 0,
  "text": "你好",
  "start_time": 0,
  "end_time": 500
}
```

#### 字段说明

| 字段             | 类型     | 描述       |
| -------------- | ------ | -------- |
| item\_id       | string | 对话项 ID   |
| content\_index | int    | 内容索引     |
| text           | string | 增量转录文本   |
| start\_time    | int64  | 开始时间（毫秒） |
| end\_time      | int64  | 结束时间（毫秒） |

### 转录完成事件 (conversation.item.input\_audio\_transcription.completed)

返回完整转录结果。

```json theme={null}
{
  "event_id": "event_xxx",
  "type": "conversation.item.input_audio_transcription.completed",
  "meta": {
    "session_id": "sess_xxx",
    "timestamp": 1642694400000
  },
  "item_id": "item_xxx",
  "content_index": 0,
  "transcript": "你好，世界",
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 10,
    "total_tokens": 10
  }
}
```

#### 字段说明

| 字段             | 类型     | 描述     |
| -------------- | ------ | ------ |
| item\_id       | string | 对话项 ID |
| content\_index | int    | 内容索引   |
| transcript     | string | 完整转录文本 |
| usage          | object | 使用统计信息 |

### 错误消息 (error)

返回错误信息。

```json theme={null}
{
  "event_id": "event_xxx",
  "type": "error",
  "meta": {
    "session_id": "sess_xxx",
    "timestamp": 1642694400000
  },
  "error": {
    "type": "invalid_request_error",
    "code": "invalid_value",
    "message": "错误描述",
    "param": "audio",
    "event_id": "event_xxx"
  }
}
```

#### 错误类型

| 类型                      | 描述      |
| ----------------------- | ------- |
| invalid\_request\_error | 请求参数错误  |
| internal\_error         | 服务器内部错误 |
| risk                    | 内容安全风险  |

#### 错误码

| 错误码                | 描述     |
| ------------------ | ------ |
| invalid\_value     | 无效参数值  |
| missing\_param     | 缺少必需参数 |
| internal\_error    | 内部错误   |
| max\_idle\_timeout | 空闲超时   |
| pong\_timeout      | 心跳超时   |
| risk\_blocked      | 内容被拦截  |

## 错误处理

### 常见错误类型

* **invalid\_request\_error**: 请求参数错误
* **internal\_error**: 服务器内部错误
* **risk**: 内容安全风险

### 故障排除

1. **连接失败**: 检查服务是否启动，端口是否正确
2. **音频无识别结果**: 确认音频格式、编码和质量
3. **识别准确性低**: 尝试使用系统提示词或更换模型
4. **延迟过高**: 减少音频分块大小或使用轻量级模型
