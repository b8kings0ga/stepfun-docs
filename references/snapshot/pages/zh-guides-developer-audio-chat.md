<!-- title: 语音对话开发指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/audio-chat.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音对话开发指南

阶跃星辰端到端语音模型支持在对话过程中传入音频内容，并生成语音回复。用户可以通过 Chat Completion API 发送语音输入，模型会同时返回文本和音频响应，实现真正的语音到语音交互体验。

<Info>推荐使用 `step-audio-2` 或 `step-audio-2-mini` 模型，这些模型具备最新的语音理解和生成能力。`step-audio-r1.1` 具有出色的声音理解能力，能够进行并行边想边说，适合需要高精度语音理解的场景。</Info>

## 能力概述

* **语音输入理解**：支持用户通过语音提问，模型可以理解语音中的内容和语调
* **语音输出生成**：模型可以直接生成语音回复，无需额外的 TTS 步骤
* **多种声音选择**：支持多种预置声音风格，满足不同场景需求
* **流式输出**：支持流式返回音频数据，实现低延迟的语音交互
* **工具调用**：支持用户自定义函数调用（`step-audio-r1.1` 模型不支持）

## 核心参数

在调用 chat completions 接口时，指定 model 为以下模型，可以获得语音回复能力。

| 模型名称                | 说明                                               |
| ------------------- | ------------------------------------------------ |
| `step-audio-r1.1`   | 超强语音理解模型，理解各式各样声音文字，边说边想，超高智商                    |
| `step-audio-2`      | 最新的端到端语音模型，支持语音输入输出、toolcall，支持音色复刻（realtime 接口） |
| `step-audio-2-mini` | 轻量版端到端语音模型，轻便快速                                  |
| `step-1o-audio`     | 上一代语音模型，音色多样                                     |

### audio 参数

`audio` 参数用于控制音频输出，只在端到端语音模型下生效。

* `voice` `string` ***required***<br />指定生成音频的声音 ID。对于 `step-audio-2` 系列模型，可用以下声音：

  * `wenrounansheng`（温柔男声）
  * `qingchunshaonv`（青春少女）
  * `livelybreezy-female`（活力少女）
  * `elegantgentle-female`（高雅女声）

  对于 `step-1o-audio` 和 `step-audio-r1.1` 模型，可通过[获取声音列表接口](/zh/api-reference/audio/list-voice)查询可用的声音 ID。

* `format` `string` ***required***<br />指定生成音频的格式：
  * `wav`：在非流式场景下（stream=false）支持
  * `pcm`：在流式场景下（stream=true）使用，格式为 24kHz、单声道、16bit

### modalities 参数

`modalities` 参数指定输出的模态类型，支持 `text`、`audio` 两种类型。

如果需要模型输出音频，则需要将 `audio` 添加到该参数中，例如：`["text", "audio"]`。

## 快速开始

### 文本输入，语音输出

最简单的使用方式是发送文本消息，让模型返回语音回复。

<Tabs defaultValue="python" items={["python", "js", "curl"]}>
  <Tab title="python">
    ```python copy theme={null}
    import base64
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    completion = client.chat.completions.create(
        model="step-audio-2",
        modalities=["text", "audio"],
        messages=[
            {
                "role": "system",
                "content": "你是一个老北京大爷，喜欢用京片子和用户聊天。",
            },
            {
                "role": "user",
                "content": "今儿个北京的天气咋样啊？",
            }
        ],
        audio={
            "voice": "wenrounansheng",
            "format": "wav",
        },
        stream=False,
    )

    # 获取文字回复
    print(completion.choices[0].message.audio.transcript)

    # 保存音频文件
    with open("response.wav", "wb") as f:
        f.write(base64.b64decode(completion.choices[0].message.audio.data))
    # 打开 response.wav 即可收听音频回复
    ```
  </Tab>

  <Tab title="js">
    ```js copy theme={null}
    import OpenAI from "openai";
    import fs from "fs";

    const openai = new OpenAI({
        apiKey: "STEP_API_KEY",
        baseURL: "https://api.stepfun.com/v1",
    });

    async function main() {
        const completion = await openai.chat.completions.create({
            model: "step-audio-2",
            modalities: ["text", "audio"],
            messages: [
                {
                    "role": "system",
                    "content": "你是一个老北京大爷，喜欢用京片子和用户聊天。",
                },
                {
                    "role": "user",
                    "content": "今儿个北京的天气咋样啊？",
                }
            ],
            audio: {
                voice: "wenrounansheng",
                format: "wav",
            },
            stream: false,
        });

        // 获取文字回复
        console.log(completion.choices[0].message.audio.transcript);

        // 保存音频文件
        fs.writeFileSync("response.wav", Buffer.from(completion.choices[0].message.audio.data, 'base64'));
        // 打开 response.wav 即可收听音频回复
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash copy theme={null}
    curl https://api.stepfun.com/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-audio-2",
        "modalities": ["text", "audio"],
        "messages": [
          {
            "role": "system",
            "content": "你是一个老北京大爷，喜欢用京片子和用户聊天。"
          },
          {
            "role": "user",
            "content": "今儿个北京的天气咋样啊？"
          }
        ],
        "audio": {
          "voice": "wenrounansheng",
          "format": "wav"
        },
        "stream": false
      }'
    ```
  </Tab>
</Tabs>

### 语音输入，语音输出

支持用户通过语音提问，模型返回语音回复，实现端到端的语音对话。

<Tabs defaultValue="python" items={["python", "js"]}>
  <Tab title="python">
    ```python copy theme={null}
    import base64
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    # 读取本地音频文件并转换为 base64
    with open("question.wav", "rb") as f:
        audio_data = base64.b64encode(f.read()).decode('utf-8')

    completion = client.chat.completions.create(
        model="step-audio-2",
        modalities=["text", "audio"],
        messages=[
            {
                "role": "system",
                "content": "你是一个动物声音识别专家，请根据用户提供的声音进行识别和回答。",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "听听这是什么声音？",
                    },
                    {
                        "type": "input_audio",
                        "input_audio": {
                            "data": f"data:audio/wav;base64,{audio_data}",
                        }
                    }
                ],
            }
        ],
        audio={
            "voice": "qingchunshaonv",
            "format": "wav",
        },
        stream=False,
    )

    # 获取文字回复
    print(completion.choices[0].message.audio.transcript)

    # 保存音频文件
    with open("response.wav", "wb") as f:
        f.write(base64.b64decode(completion.choices[0].message.audio.data))
    ```
  </Tab>

  <Tab title="js">
    ```js copy theme={null}
    import OpenAI from "openai";
    import fs from "fs";

    const openai = new OpenAI({
        apiKey: "STEP_API_KEY",
        baseURL: "https://api.stepfun.com/v1",
    });

    // 从 URL 下载音频并转换为 base64
    const downloadAudioAsBase64 = async (url) => {
        const response = await fetch(url);
        const arrayBuffer = await response.arrayBuffer();
        const buffer = Buffer.from(arrayBuffer);
        return "data:audio/wav;base64," + buffer.toString('base64');
    }

    async function main() {
        const completion = await openai.chat.completions.create({
            model: "step-audio-2",
            modalities: ["text", "audio"],
            messages: [
                {
                    "role": "system",
                    "content": "你是一个动物声音识别专家，请根据用户提供的声音进行识别和回答。",
                },
                {
                    "role": "user",
                    "content": [
                        {
                            type: "text",
                            text: "听听这是什么声音",
                        },
                        {
                            type: "input_audio",
                            input_audio: {
                                data: await downloadAudioAsBase64("https://stepchat-static.tos-cn-shanghai.volces.com/resource_tmp/cat-meow.wav"),
                            }
                        }
                    ],
                }
            ],
            audio: {
                voice: "qingchunshaonv",
                format: "wav",
            },
            stream: false,
        });

        // 获取文字回复
        console.log(completion.choices[0].message.audio.transcript);

        // 保存音频文件
        fs.writeFileSync("response.wav", Buffer.from(completion.choices[0].message.audio.data, 'base64'));
    }

    main();
    ```
  </Tab>
</Tabs>

## 流式语音输出

当 `stream=true` 时，API 会以流式方式返回音频数据，实现超低延迟的语音交互体验。

<Tabs defaultValue="python" items={["python", "js"]}>
  <Tab title="python">
    ```python copy theme={null}
    import base64
    import struct
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    completion = client.chat.completions.create(
        model="step-audio-2",
        modalities=["text", "audio"],
        messages=[
            {
                "role": "user",
                "content": "请用温柔的语气给我讲一个睡前故事",
            }
        ],
        audio={
            "voice": "elegantgentle-female",
            "format": "pcm",  # 流式场景下使用 pcm 格式
        },
        stream=True,
    )

    audio_chunks = []
    transcript = ""

    for chunk in completion:
        delta = chunk.choices[0].delta

        # 处理音频数据
        if hasattr(delta, 'audio') and delta.audio:
            if hasattr(delta.audio, 'data') and delta.audio.data:
                audio_chunks.append(base64.b64decode(delta.audio.data))
            if hasattr(delta.audio, 'transcript') and delta.audio.transcript:
                transcript += delta.audio.transcript
                print(delta.audio.transcript, end="", flush=True)

    print("\n\n完整文字回复:", transcript)

    # 合并所有 PCM 数据
    pcm_data = b''.join(audio_chunks)

    # 生成 WAV 文件头（24kHz，单声道，16bit）
    def create_wav_header(pcm_size, sample_rate=24000, channels=1, bits_per_sample=16):
        byte_rate = sample_rate * channels * bits_per_sample // 8
        block_align = channels * bits_per_sample // 8
        return struct.pack(
            '<4sI4s4sIHHIIHH4sI',
            b'RIFF',
            36 + pcm_size,       # 文件大小 - 8
            b'WAVE',
            b'fmt ',
            16,                   # fmt chunk 大小
            1,                    # 音频格式 (1 = PCM)
            channels,
            sample_rate,
            byte_rate,
            block_align,
            bits_per_sample,
            b'data',
            pcm_size
        )

    # 保存为 WAV 文件
    with open("response.wav", "wb") as f:
        f.write(create_wav_header(len(pcm_data)))
        f.write(pcm_data)
    # 打开 response.wav 即可收听音频回复
    ```
  </Tab>

  <Tab title="js">
    ```js copy theme={null}
    import OpenAI from "openai";
    import fs from "fs";

    const openai = new OpenAI({
        apiKey: "STEP_API_KEY",
        baseURL: "https://api.stepfun.com/v1",
    });

    // 生成 WAV 文件头（24kHz，单声道，16bit）
    function createWavHeader(pcmSize, sampleRate = 24000, channels = 1, bitsPerSample = 16) {
        const byteRate = sampleRate * channels * bitsPerSample / 8;
        const blockAlign = channels * bitsPerSample / 8;
        const header = Buffer.alloc(44);

        header.write('RIFF', 0);
        header.writeUInt32LE(36 + pcmSize, 4);
        header.write('WAVE', 8);
        header.write('fmt ', 12);
        header.writeUInt32LE(16, 16);           // fmt chunk 大小
        header.writeUInt16LE(1, 20);            // 音频格式 (1 = PCM)
        header.writeUInt16LE(channels, 22);
        header.writeUInt32LE(sampleRate, 24);
        header.writeUInt32LE(byteRate, 28);
        header.writeUInt16LE(blockAlign, 32);
        header.writeUInt16LE(bitsPerSample, 34);
        header.write('data', 36);
        header.writeUInt32LE(pcmSize, 40);

        return header;
    }

    async function main() {
        const completion = await openai.chat.completions.create({
            model: "step-audio-2",
            modalities: ["text", "audio"],
            messages: [
                {
                    "role": "user",
                    "content": "请用温柔的语气给我讲一个睡前故事",
                }
            ],
            audio: {
                voice: "elegantgentle-female",
                format: "pcm",  // 流式场景下使用 pcm 格式
            },
            stream: true,
        });

        const audioChunks = [];
        let transcript = "";

        for await (const chunk of completion) {
            const delta = chunk.choices[0].delta;

            // 处理音频数据
            if (delta.audio) {
                if (delta.audio.data) {
                    audioChunks.push(Buffer.from(delta.audio.data, 'base64'));
                }
                if (delta.audio.transcript) {
                    transcript += delta.audio.transcript;
                    process.stdout.write(delta.audio.transcript);
                }
            }
        }

        console.log("\n\n完整文字回复:", transcript);

        // 合并 PCM 数据并保存为 WAV 文件
        const pcmData = Buffer.concat(audioChunks);
        const wavHeader = createWavHeader(pcmData.length);
        fs.writeFileSync("response.wav", Buffer.concat([wavHeader, pcmData]));
        // 打开 response.wav 即可收听音频回复
    }

    main();
    ```
  </Tab>
</Tabs>

流式返回的音频格式为 24kHz、单声道、16bit 的 PCM 数据，你可以直接将数据流式送入播放器进行实时播放，也可以按上述示例将其保存为标准的 WAV 文件。

## 多轮语音对话

支持在多轮对话中保持语音上下文。你可以将用户的语音历史放入 messages 中，AI 的输出推荐将文字部分作为 assistant 回复填入 content。

```python copy theme={null}
import base64
from openai import OpenAI

client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

# 读取当前轮用户语音
with open("current_question.wav", "rb") as f:
    current_audio = base64.b64encode(f.read()).decode('utf-8')

completion = client.chat.completions.create(
    model="step-audio-2",
    modalities=["text", "audio"],
    messages=[
        {
            "role": "system",
            "content": "你是一个友好的助手，请用自然的语气回答用户的问题。",
        },
        # 第一轮对话（可以用 ASR 文本表示历史语音）
        {
            "role": "user",
            "content": "你好，请问今天天气怎么样？",
        },
        {
            "role": "assistant",
            "content": "你好！今天天气晴朗，气温适宜，非常适合出门活动。",
        },
        # 当前轮语音输入
        {
            "role": "user",
            "content": [
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": f"data:audio/wav;base64,{current_audio}",
                    }
                }
            ],
        }
    ],
    audio={
        "voice": "wenrounansheng",
        "format": "wav",
    },
    stream=False,
)

print(completion.choices[0].message.audio.transcript)
```

<Info>
  **上下文限制说明**：

  * `step-audio-2` / `step-audio-r1.1` 支持上下文传入 wav 格式音频
  * 请求最大支持 10MB（指 base64 后的总大小，大致能传 7.5MB 的 wav 文件）
  * 最多支持 30 段声音（如果单段声音超过 25s，会被自动分段，每 25s 视为一段）
  * `step-1o-audio` 目前不支持上下文中传入 wav（但支持语音输出）
</Info>

## 结合 Tool Call 使用

`step-audio-2` / `step-1o-audio` 语音模型支持 Tool Call 功能，可以在语音对话中调用外部工具。完整流程包括：检测函数调用、执行函数、返回结果并获取最终语音回复。

```python copy theme={null}
import base64
import json
from openai import OpenAI

client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

# 定义工具函数
def get_weather(city: str) -> str:
    """模拟获取天气信息"""
    # 实际应用中这里调用真实的天气 API
    return f"{city}：晴，气温 25°C，空气质量良好"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取指定城市的天气信息",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，如：北京、上海"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "北京今天天气怎么样？",
    }
]

# 第一次调用：模型可能返回 tool_calls
completion = client.chat.completions.create(
    model="step-audio-2",
    modalities=["text", "audio"],
    messages=messages,
    tools=tools,
    audio={
        "voice": "wenrounansheng",
        "format": "wav",
    },
    stream=False,
)

assistant_message = completion.choices[0].message

# 检查是否有 tool_calls
if assistant_message.tool_calls:
    # 将 assistant 消息加入上下文
    messages.append({
        "role": "assistant",
        "content": assistant_message.audio.transcript if assistant_message.audio else None,
        "tool_calls": [
            {
                "id": tc.id,
                "type": "function",
                "function": {
                    "name": tc.function.name,
                    "arguments": tc.function.arguments
                }
            }
            for tc in assistant_message.tool_calls
        ]
    })

    # 执行每个工具调用并添加结果
    for tool_call in assistant_message.tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        # 执行函数
        if function_name == "get_weather":
            result = get_weather(function_args["city"])
        else:
            result = "未知函数"

        # 将工具执行结果加入上下文
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        })

    # 第二次调用：获取最终的语音回复
    final_completion = client.chat.completions.create(
        model="step-audio-2",
        modalities=["text", "audio"],
        messages=messages,
        tools=tools,
        audio={
            "voice": "wenrounansheng",
            "format": "wav",
        },
        stream=False,
    )

    # 获取最终回复
    final_message = final_completion.choices[0].message
    print("文字回复:", final_message.audio.transcript)

    # 保存音频
    with open("response.wav", "wb") as f:
        f.write(base64.b64decode(final_message.audio.data))
else:
    # 没有 tool_calls，直接输出回复
    print("文字回复:", assistant_message.audio.transcript)
    with open("response.wav", "wb") as f:
        f.write(base64.b64decode(assistant_message.audio.data))
```

### Tool Call 返回示例

第一次调用返回（text+audio 模态，带 tool\_call 字段）：

```json theme={null}
{
  "id": "019b55f32eb27db7a0cc933be0216686",
  "choices": [
    {
      "finish_reason": null,
      "index": 0,
      "message": {
        "role": "assistant",
        "audio": {
          "data": "[base64 wav data]",
          "transcript": "让我帮您查一下北京的天气。"
        },
        "tool_calls": [
          {
            "id": "call-1766673564415832077",
            "function": {
              "arguments": "{\"city\": \"北京\"}",
              "name": "get_weather"
            },
            "type": "function",
            "index": 0
          }
        ]
      }
    }
  ],
  "model": "step-audio-2",
  "usage": {
    "completion_tokens": 106,
    "prompt_tokens": 410,
    "total_tokens": 516
  }
}
```

<Info>
  **注意**：模型可能会在返回 tool\_calls 的同时输出语音（如"让我帮您查一下"），你可以在等待函数执行时播放这段语音，提升用户体验。
</Info>

## 音频格式说明

### 输入音频格式

* 支持 mp3 和 wav 格式
* Base64 编码格式示例：`data:audio/mpeg;base64,${base64_string}` 或 `data:audio/wav;base64,${base64_string}`

### 输出音频格式

| 场景                | 格式  | 规格              |
| ----------------- | --- | --------------- |
| 非流式（stream=false） | wav | 标准 wav 文件格式     |
| 流式（stream=true）   | pcm | 24kHz，单声道，16bit |

## Chat Completions vs Realtime API

阶跃星辰提供两种语音对话方案，适用于不同的场景需求：

| 特性           | Chat Completions API | Realtime API          |
| ------------ | -------------------- | --------------------- |
| 连接方式         | HTTP 请求              | WebSocket 长连接         |
| 语音识别 (ASR)   | 需自行实现或使用第三方服务        | 内置，自动识别用户语音           |
| 上下文管理        | 需自行维护 messages 列表    | 内置，自动管理对话历史           |
| 语音活动检测 (VAD) | 需自行实现                | 内置，自动检测用户说话           |
| 联网搜索         | 需自行实现搜索接口            | 内置 web\_search 工具     |
| 知识库检索        | 需自行实现                | 内置 retrieval 工具       |
| 延迟           | 较低（流式输出）             | 极低（双向流式交互）            |
| 适用场景         | 离线处理、批量任务、简单集成       | 实时对话、语音助手、客服机器人       |
| 音色复刻         | 不支持                  | `step-audio-2` 支持音色复刻 |

### 使用 Realtime API 的优势

如果你需要构建实时语音对话应用，推荐使用 [Realtime API](/zh/guides/developer/realtime)：

* **开箱即用**：内置 ASR、VAD、上下文管理，无需额外集成
* **超低延迟**：基于 WebSocket 的实时双向通信
* **内置工具**：支持 `web_search` 联网搜索和 `retrieval` 知识库检索
* **自定义 Tool Call**：同样支持自定义函数调用
* **音色复刻**：支持使用自定义音色进行语音生成

<Card title="实时语音互动开发指南" href="/zh/guides/developer/realtime" />

## 常见问题

### 流式播放 PCM 音频

在浏览器环境中播放流式 PCM 音频，需要使用 Web Audio API。以下是一个简单的播放器示例：

```javascript theme={null}
class SimplePCMPlayer {
  constructor() {
    this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
    this.bufferedData = [];
    this.isPlaying = false;
    this.nextStartTime = 0;
  }

  // 追加 PCM 数据（16位有符号小端，24kHz，单声道）
  appendPCM(pcmArrayBuffer) {
    const int16Array = new Int16Array(pcmArrayBuffer);
    const float32Array = new Float32Array(int16Array.length);
    for (let i = 0; i < int16Array.length; i++) {
      float32Array[i] = int16Array[i] / 32768;
    }
    this.bufferedData.push(float32Array);
    if (!this.isPlaying) {
      this.playNext();
    }
  }

  playNext() {
    if (this.bufferedData.length === 0) {
      this.isPlaying = false;
      return;
    }
    this.isPlaying = true;
    const data = this.bufferedData.shift();
    const audioBuffer = this.audioContext.createBuffer(1, data.length, 24000);
    audioBuffer.copyToChannel(data, 0);
    const source = this.audioContext.createBufferSource();
    source.buffer = audioBuffer;
    source.connect(this.audioContext.destination);
    const startTime = Math.max(this.audioContext.currentTime, this.nextStartTime);
    this.nextStartTime = startTime + audioBuffer.duration;
    source.start(startTime);
    source.onended = () => this.playNext();
  }

  // 清空缓冲并停止播放
  clear() {
    this.bufferedData = [];
    this.isPlaying = false;
    this.nextStartTime = this.audioContext.currentTime;
  }
}
```

### 优化首字延迟

如果需要更低的首字延迟：

1. 使用 `step-audio-2-mini` 模型，它的响应速度更快
2. 使用流式输出（stream=true），可以边生成边播放
3. 考虑使用 [Realtime API](/zh/guides/developer/realtime) 获得最低延迟体验
