<!-- title: 语音模型接入 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/audio-api.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音模型接入

Step Plan 除推理大模型外，还支持 **语音合成 (TTS)** 与 **语音识别 (ASR)** 两类语音模型通过专属路径接入。所有请求统一使用 `/step_plan/v1/...` 路径前缀，域名固定为 `https://api.stepfun.com`。

## 前置条件

1. 已订阅 [Step Plan](https://platform.stepfun.com/step-plan) 套餐
2. 已获取 [API Key](https://platform.stepfun.com/interface-key)

***

## 支持的模型

| 类别     | 模型                       | 说明                                                                  |
| ------ | ------------------------ | ------------------------------------------------------------------- |
| 实时语音对话 | `stepaudio-2.5-realtime` | 端到端实时语音对话模型，承接 StepAudio 2.5 TTS 表现力，支持音色复刻、人设定制与极低延迟交互             |
| 语音对话   | `stepaudio-2.5-chat`     | 端到端对话大模型，文本输入、文本返回，支持千万人设完全自定义与高情商副语言感知                             |
| 语音合成   | `stepaudio-2.5-tts`      | 基于语境理解的新一代 Contextual TTS，支持全局语境 + 文中语境双档控制，生成具有呼吸感、轻重主次、情绪弧线的真人级表达 |
| 语音识别   | `stepaudio-2.5-asr`      | 新一代流式 ASR 模型，4B MTP 架构，面向准实时转写场景，在低延迟下保持高识别准确率                      |

<Columns cols={2}>
  <Card title="实时语音对话" href="#实时语音对话">
    WebSocket 双向实时语音
  </Card>

  <Card title="语音对话" href="#语音对话">
    端到端对话补全（文本返回）
  </Card>

  <Card title="语音合成 (TTS)" href="#语音合成">
    非流式 / WebSocket 流式 / 音色试听 / 音色复刻
  </Card>

  <Card title="语音识别 (ASR)" href="#语音识别">
    HTTP + SSE 流式返回识别文本
  </Card>
</Columns>

***

## 实时语音对话

### 接口路径

| 能力     | 请求方式      | Step Plan 路径                                  |
| ------ | --------- | --------------------------------------------- |
| 双向实时语音 | WebSocket | `wss://api.stepfun.com/step_plan/v1/realtime` |

<Info>
  接口参数与开放平台完全一致，详见 [双向实时语音](/zh/api-reference/realtime/chat) 接口文档。
</Info>

### 计费说明

计费逻辑与开放平台一致，最终按开放平台实际计费金额折算为 Step Plan 总额度消耗。具体单价请参考 [定价与限速](/zh/guides/pricing/details)。

### 示例

<Tabs>
  <Tab title="Python (WebSocket)">
    ```python theme={null}
    import json
    import websocket

    headers = {
        "Authorization": "Bearer YOUR_STEP_API_KEY"
    }

    def on_open(ws):
        ws.send(json.dumps({
            "event_id": "event_001",
            "type": "session.update",
            "session": {
                "modalities": ["text", "audio"],
                "instructions": "你是有耐心的陪伴搭子，回答自然、温暖、有人情味",
                "voice": "linjiajiejie",
                "input_audio_format": "pcm16",
                "output_audio_format": "pcm16"
            }
        }))

    def on_message(ws, message):
        print(message)

    if __name__ == "__main__":
        ws = websocket.WebSocketApp(
            # Step Plan 使用 /step_plan/v1 路径
            "wss://api.stepfun.com/step_plan/v1/realtime?model=stepaudio-2.5-realtime",
            header=headers,
            on_open=on_open,
            on_message=on_message,
        )
        ws.run_forever()
    ```
  </Tab>
</Tabs>

***

## 语音对话

### 接口路径

| 能力     | 请求方式 | Step Plan 路径                                            |
| ------ | ---- | ------------------------------------------------------- |
| 文本对话补全 | POST | `https://api.stepfun.com/step_plan/v1/chat/completions` |

<Info>
  接口参数与开放平台完全一致，详见 [对话补全（Chat Completion）](/zh/api-reference/chat/chat-completion-create) 接口文档。`stepaudio-2.5-chat` 仅支持 `text` 模态，`modalities` 不应包含 `audio`。
</Info>

### 计费说明

计费逻辑与开放平台一致，最终按开放平台实际计费金额折算为 Step Plan 总额度消耗。具体单价请参考 [定价与限速](/zh/guides/pricing/details)。

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -X POST 'https://api.stepfun.com/step_plan/v1/chat/completions' \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $STEP_API_KEY" \
    -d '{
        "model": "stepaudio-2.5-chat",
        "modalities": ["text"],
        "messages": [
          {"role": "user", "content": "今天心情有点闷，陪我聊聊"}
        ]
    }'
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/step_plan/v1",
    )

    response = client.chat.completions.create(
        model="stepaudio-2.5-chat",
        modalities=["text"],
        messages=[
            {"role": "user", "content": "今天心情有点闷，陪我聊聊"}
        ],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>
</Tabs>

***

## 语音合成

### 接口路径

| 能力      | 请求方式      | Step Plan 路径                                                |
| ------- | --------- | ----------------------------------------------------------- |
| 非流式语音合成 | POST      | `https://api.stepfun.com/step_plan/v1/audio/speech`         |
| 流式语音合成  | WebSocket | `wss://api.stepfun.com/step_plan/v1/realtime/audio`         |
| 音色试听    | POST      | `https://api.stepfun.com/step_plan/v1/audio/voices/preview` |
| 音色复刻    | POST      | `https://api.stepfun.com/step_plan/v1/audio/voices`         |

<Info>
  接口参数与开放平台完全一致，详见各接口的 API 文档：[语音合成](/zh/api-reference/audio/create-audio)、[流式语音合成](/zh/api-reference/audio/ws-audio)、[复刻试听](/zh/api-reference/audio/voices-preview)、[复刻音色](/zh/api-reference/audio/create-voice)。
</Info>

### 计费说明

计费逻辑与开放平台一致，最终按开放平台实际计费金额折算为 Step Plan 总额度消耗。具体单价请参考 [定价与限速](/zh/guides/pricing/details)。

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -X POST 'https://api.stepfun.com/step_plan/v1/audio/speech' \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $STEP_API_KEY" \
    -d '{
        "model": "stepaudio-2.5-tts",
        "input": "今天天气不错，适合出去走走。",
        "voice": "cixingnansheng",
        "instruction": "语气温柔，语速偏慢",
        "response_format": "mp3"
    }' \
    --output speech.mp3
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/step_plan/v1",
    )

    response = client.audio.speech.create(
        model="stepaudio-2.5-tts",
        input="今天天气不错，适合出去走走。",
        voice="cixingnansheng",
        extra_body={
            "instruction": "语气温柔，语速偏慢",
        },
    )

    response.stream_to_file("speech.mp3")
    ```
  </Tab>

  <Tab title="Python (WebSocket 流式)">
    ```python theme={null}
    import websocket
    import rel
    import json

    headers = {
        "Authorization": "Bearer YOUR_STEP_API_KEY"
    }

    def get_start_event(sid):
        return json.dumps({
            "type": "tts.create",
            "data": {
                "session_id": sid,
                "voice_id": "cixingnansheng",
                "response_format": "wav",
                "volume_ratio": 1.0,
                "speed_ratio": 1.0,
                "sample_rate": 16000,
                "instruction": "语气温柔，语速偏慢"
            },
        })

    def on_message(ws, message):
        data = json.loads(message)
        session_id = data["data"]["session_id"]
        event_type = data["type"]

        if event_type == "tts.connection.done":
            ws.send(get_start_event(session_id))

        print(message)

    def on_error(ws, error):
        print(error)

    if __name__ == "__main__":
        ws = websocket.WebSocketApp(
            # Step Plan 使用 /step_plan/v1 路径
            "wss://api.stepfun.com/step_plan/v1/realtime/audio?model=stepaudio-2.5-tts",
            header=headers,
            on_message=on_message,
            on_error=on_error,
        )

        ws.run_forever(dispatcher=rel, reconnect=5)
        rel.signal(2, rel.abort)
        rel.dispatch()
    ```
  </Tab>
</Tabs>

***

## 语音识别

### 接口路径

| 能力           | 请求方式 | Step Plan 路径                                         |
| ------------ | ---- | ---------------------------------------------------- |
| 语音识别（流式返回文本） | POST | `https://api.stepfun.com/step_plan/v1/audio/asr/sse` |

<Info>
  接口参数与开放平台完全一致，详见 [语音识别（流式返回文本）](/zh/api-reference/audio/asr-sse) 接口文档。
</Info>

### 能力限制

当前 `stepaudio-2.5-asr` 在 Step Plan 下仅支持 HTTP + SSE 调用方式，与开放平台一致——该模型本身不提供 WebSocket 接口。

### 计费说明

计费逻辑与开放平台一致，最终按开放平台实际计费金额折算为 Step Plan 总额度消耗。具体单价请参考 [定价与限速](/zh/guides/pricing/details)。

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -X POST 'https://api.stepfun.com/step_plan/v1/audio/asr/sse' \
    -H 'Content-Type: application/json' \
    -H 'Accept: text/event-stream' \
    -H "Authorization: Bearer $STEP_API_KEY" \
    -d '{
        "audio": {
            "data": "base64_encoded_audio",
            "input": {
                "transcription": {
                    "model": "stepaudio-2.5-asr",
                    "language": "zh",
                    "enable_itn": true
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
    }'
    ```
  </Tab>
</Tabs>
