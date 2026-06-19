<!-- title: 流式语音合成 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/ws-audio.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 流式语音合成

流式语音合成

## 请求方式

WebSocket

## 请求地址

`wss://api.stepfun.com/v1/realtime/audio`

<Note>
  Step Plan 场景请使用 `wss://api.stepfun.com/step_plan/v1/realtime/audio`
</Note>

## 请求头

* `Authorization` `string` ***required*** <br /> 鉴权使用的 KEY，其值为 `Bearer STEP_API_KEY`

## 请求参数

* `model` `string` ***required***
  <br />
  需要使用的模型名称，当前仅支持 `step-tts-2`、`step-tts-mini` 和 `stepaudio-2.5-tts`。

<Note>`step-tts-vivid` 模型名称不再推荐使用，但历史用户请求仍会继续支持。</Note>

<Warning>
  注意：`stepaudio-2.5-tts` 模型在 WebSocket 流式语音合成下的效果可能显著低于 HTTP 请求下的非流式语音合成，如果对时延没有要求，建议使用普通的非流式语音合成接口。
</Warning>

## 调用说明

流式生成音频需要在服务链接成功后，发送对应的 Client Event 事件，获取对应的 Server Event ，来完成音频的生成。

### Client Event & Server Event 对应关系

以下为流式调用过程中，客户端发送的 Client Event 事件及服务端返回的 Server Event 事件。

<img src="https://mintcdn.com/stepfun/ivZhb9pOE5X12y-g/images/tts/stream-tts2.png?fit=max&auto=format&n=ivZhb9pOE5X12y-g&q=85&s=4e37ad2b1a2f1f4782be82dfbe37e062" alt="" width="600" height="509" data-path="images/tts/stream-tts2.png" />

详细描述可参考下方的详细说明。

| **消息类型** | **客户端发送**      | **服务端返回**                   | 备注                          |
| -------- | -------------- | --------------------------- | --------------------------- |
| 建联成功     | -              | tts.connection.done         | WebSocket 链接成功后下发的事件        |
| 创建会话     | tts.create     | tts.response.created        | 创建会话及对应响应。收到对应响应后，可进行进一步生成。 |
| 开始生成单句   |                | tts.response.sentence.start | 累计的文本满足生成条件，开始生成            |
| 发送文本     | tts.text.delta | tts.response.audio.delta    | 创建文本及对应的响应，收到响应后即可进行播放。     |
| 结束生成单句   |                | tts.response.sentence.end   | 累计的文本满足生成条件，结束生成            |
| 清空缓冲区    | tts.text.flush | tts.text.flushed            | 可快速清空缓冲区，一次性获得当前尚未返回的音频内容。  |
| 发送文本结束   | tts.text.done  | response.audio.done         | 完成本次生成 ，不再生成，服务端将会释放连接。     |
| 音频生成出错   | -              | tts.response.error          | 在生成过程中出现错误时的事件              |

<Info>
  如果连续 60 秒无动作，则系统会自动断开链接。
</Info>

## Client Event 详细说明

### 创建会话 `tts.create`

创建会话的事件，在完成建联后，收到 `tts.connection.done` Server Event 返回后发送此事件开始生成音频。

* `type` `string` ***required***<br /> 固定为 `tts.create`

* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***
    <br /> 会话 ID，可用于判断具体沟通是哪个会话，由 `tts.connection.done` 事件返回。

  * `voice_id` `string` ***required***
    <br /> 音色 ID，必填，可参考 [音色列表](../../guides/developer/tts#支持音色) 查看支持的音色，试听对应音色。

  * `response_format` `string` ***optional***
    <br /> 音频格式，支持 `wav`、`mp3`、`flac`、`opus`、`pcm`，以及 `mp3_stream`、`opus_stream`、`flac_stream` 三种流式格式。非必填，默认 `mp3`。
    <br /> 说明：不带 `_stream` 后缀的格式，每个 `audio.delta` 返回的数据都是一个独立的完整文件，可直接单独播放或保存；带 `_stream` 后缀的格式则需要将所有 `audio.delta` 的数据按顺序拼接后才能得到一个完整的音频文件，同样支持边收边播，适合最终需要生成单个完整音频文件的场景。

  * `sample_rate` `int` ***optional***
    <br /> 采样率，可选项为 `8000`、`16000`、`22050`、`24000`、`48000`，默认值为 `24000`。其中 `48000` 为最近几次迭代新增的采样率。

  * `pronunciation_map` `object array` ***optional***
    <br /> 定义某个文字或符号注音或发音替换规则，在中文文本中，声调用数字表示：一声为1，二声为2，三声为3，四声为4，轻声为5。
    * `tone`  `string`  **required** <br /> 具体发音映射规则，以"/"隔开，示例：`["绯闻/fei1闻","扁舟/偏舟","嫉妒/ji2妒"]`

  * `speed_ratio` `float` ***optional***
    <br /> 语速，取值范围为 0.5\~2，默认值 1.0。0.5 表示 0.5 倍速。

  * `volume_ratio` `float` ***optional***
    <br /> 音量，取值范围为 0.1\~2.0，默认值 1.0。0.1 表示缩小至 10% 音量；2.0 表示扩大至 200%音量

  * `mode` `string` **optional**
    <br /> 生成模式，可选项为 `sentence`  和 `default`。 `default` 表示按字生成，适合大模型流式生成场景，`sentence` 表示按句生成，适合已经生成好完整句子。默认为 `default`。

  * `markdown_filter` `bool` ***optional***
    <br /> 是否启用 Markdown 过滤。

  * `instruction` `string` ***optional***
    <br /> 全局自然语言指导。仅在连接 `stepaudio-2.5-tts` 模型时生效，用于设定会话全局情绪基调，最大长度限制为 200 个字符。

  * `voice_label` `object` ***optional***
    <br />音色标签，使用自定义音色时需要传入。language、emotion 和 style 三个自动同时只能有一个字段有值，暂不支持多个组合。
    * `language` `string` ***optional***<br />语言，支持 `粤语`、`四川话`、`日语` 三个选项。
    * `emotion` `string` ***optional***<br />情绪，支持 `高兴`、`生气` 等最多 11 个选项， 不同模型的支持情况可参考[音色标签](../../guides/developer/tts#音色标签)
    * `style` `string` ***optional***<br />支持最多17种语速或演绎风格，不同模型的支持情况可参考[音色标签](../../guides/developer/tts#音色标签)

<Warning>
  ⚠️ 注意：`stepaudio-2.5-tts` 模型不支持此字段。若使用 `stepaudio-2.5-tts` 模型，请勿传入 `voice_label`，直接使用 `instruction` 字段控制情绪与风格即可。其他模型的支持情况请参考[音色标签](../../guides/developer/tts#音色标签)。
</Warning>

<Info>
  `default` 模式适用于 TTS 和大语言模型组合使用，该模式会自动进行攒句和切句，因此不会马上返回而内容，而是当用户的输入满足一句话时才会进行生成；如果需要强制返回，则可以发送 `tts.text.flush`，模型则可快速返回内容。

  `sentence` 模式适用于已经有现成的长文本的场景，该模式会自动基于 `。！？!?` 进行切句，并进行生成。
</Info>

**Example**

```json theme={null}
{
  "type": "tts.create",
  "data": {
      "session_id": "01956e7388477cfcbdc3aaabf364bc70",
      "voice_id": "cixingnansheng",
      "response_format": "wav",
      "volume_ratio": 1.0,
      "speed_ratio": 1.0,
      "sample_rate": 16000,
      "pronunciation_map":{
        "tone":[
          "阿胶/e1胶",
          "扁舟/偏舟",
          "LOL/laugh out loudly"
        ]
      }
  }
}
```

**Example（`stepaudio-2.5-tts`）**

```json theme={null}
{
    "type": "tts.create",

    "data": {
        "session_id": "01956e7388477cfcbdc3aaabf364bc70",
        "voice_id": "cixingnansheng",

        "response_format": "wav",
        "volume_ratio": 1.0,

        "speed_ratio": 1.0,

        "sample_rate": 16000,
        "instruction": "语气冰冷，压迫感强，语速偏慢",
        "pronunciation_map":{
            "tone":[
                "阿胶/e1胶",
                "扁舟/偏舟",
                "LOL/laugh out loudly"
            ]
        }
    }
}
```

### 生成音频 `tts.text.delta`

生成音频的 Client Event。

<Info>
  在生成过程中，如果 TTS 引擎认为已经达成了生成的条件，则会返回 `tts.response.sentence.start`
  声明开始推理，并返回1个或多个 `tts.response.audio.delta`，返回音频内容。并在音频内容返回完成后，返回
  `tts.response.sentence.end` 事件声明完成此句完成生成。如 TTS 引擎认为未达成生成的条件，则不会返回任何事件。
</Info>

* `type` `string` ***required***<br /> 固定为 `tts.text.delta`

* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***
    <br /> 会话 ID，可用于判断具体沟通是哪个会话，由 `tts.connection.done` 事件返回。

  * `text` `string` ***required***
    <br /> 要生成的文本内容，最大长度为 1000 个字符。支持使用 `()` 传入不发音的内联指令，若文本本身需发音，请勿带括号。

**Example**

```json theme={null}
{
	"type": "tts.text.delta",
	"data": {
		"session_id": "01956e7388477cfcbdc3aaabf364bc70",
		"text": "今天的天气真不错，我想去学习阶跃星辰的大模型技术"
	}
}
```

**Example（`stepaudio-2.5-tts`）**

```json theme={null}
{
    "type": "tts.text.delta",
    "data": {
        "session_id": "01956e7388477cfcbdc3aaabf364bc70",
        "text": "（激动）今天的天气真不错，我想去学习阶跃星辰的大模型技术！"
    }
}
```

### 清空缓冲区 `tts.text.flush`

清空缓冲区，强制返回模型生成的音频。

* `type` `string` ***required*** <br /> 固定为 `tts.text.flush`

* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***
    <br /> 会话 ID，可用于判断具体沟通是哪个会话，由 `tts.connection.done` 事件返回。

```json theme={null}
{
	"type": "tts.text.flush",
	"data": {
		"session_id": "01956e8dc1d77bb98f9da8d1b642fcf0"
	}
}
```

### 完成音频生成 `tts.text.done`

完成音频生成

* `type` `string` ***required***<br /> 固定为 `tts.text.done`

* `data` `object` ***required***<br /> 事件内容

  * `session_id` `string` ***required***
    <br /> 会话 ID，可用于判断具体沟通是哪个会话，由 `tts.connection.done` 事件返回。

```json theme={null}
{
	"type": "tts.text.done",
	"data": {
		"session_id": "01956e8dc1d77bb98f9da8d1b642fcf0"
	}
}
```

## Server Event 详细说明

### 连接成功 `tts.connection.done`

连接成功

* `event_id` `string` ***required***<br /> 事件 ID，用于标识本次请求，当联系客服获取支持时，可提供此 ID 协助排查问题。

* `type` `string` ***required***<br /> 固定为 `tts.connection.done`

* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***<br /> 会话 ID，后续请求时需要带上使用

**Example**

```json theme={null}
{
	"event_id": "01956e73888c7953896a6e176bf3d760",
	"type": "tts.connection.done",
	"data": {
		"session_id": "01956e7388477cfcbdc3aaabf364bc70"
	}
}
```

### 会话创建成功 `tts.response.created`

会话创建成功

* `event_id` `string` ***required***<br /> 事件 ID，用于标识本次请求，当联系客服获取支持时，可提供此 ID 协助排查问题。

* `type` `string` ***required***<br /> 固定为 `tts.response.created`

* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***<br /> 会话 ID，后续请求时需要带上使用

**Example**

```json theme={null}
{
	"event_id": "01956e73888c7953896a6e176bf3d760",
	"type": "tts.connection.done",
	"data": {
		"session_id": "01956e7388477cfcbdc3aaabf364bc70"
	}
}
```

### 开始生成单句 `tts.response.sentence.start`

开始生成单句

* `event_id` `string` ***required***<br /> 事件 ID，用于标识本次请求，当联系客服获取支持时，可提供此 ID 协助排查问题。
* `type` `string` ***required***<br /> 固定为 `tts.response.sentence.start`
* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***<br /> 会话 ID
  * `text` `string` ***required***<br /> 本次生成的文本内容
  * `started_at` `string` ***required***<br /> 本次生成开始的时间，时间戳

```json theme={null}
{
        "event_id": "01956e73888c7953896a6e176bf3d760",
        "type": "tts.response.sentence.start",
        "data": {
                "session_id": "01956e7388477cfcbdc3aaabf364bc70",
                "text": "blah blah",
                "started_at": 10292929292
        }
}
```

### 接收生成好的音频 `tts.response.audio.delta`

接收生成好的音频

* `event_id` `string` ***required***<br /> 事件 ID，用于标识本次请求，当联系客服获取支持时，可提供此 ID 协助排查问题。

* `type` `string` ***required***<br /> 固定为 `tts.response.audio.delta`

* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***<br /> 会话 ID，后续请求时需要带上使用
  * `status` `string` ***required***<br /> 生成状态，可选项为 `unfinished` 和 `finished`。`unfinished` 表示生成未完成，`finished` 表示生成完成。
  * `audio` `string` ***required***<br /> 音频内容，BASE64 编码的音频内容
  * `duration` `float` ***required***<br /> 音频时长，单位为秒

```json theme={null}
{
	"event_id": "42bd707a-ba16-4ddb-a751-54d84301b474",
	"type": "tts.response.audio.delta",
	"data": {
		"session_id": "01956e8dc1d77bb98f9da8d1b642fcf0",
		"status": "unfinished",
		"audio": "BASE64 的音频内容",
		"duration": 2.043375
	}
}
```

### 结束生成单句 `tts.response.sentence.end`

结束生成单句

* `event_id` `string` ***required***
  <br /> 事件 ID，用于标识本次请求，当联系客服获取支持时，可提供此 ID 协助排查问题。
* `type` `string` ***required***
  <br /> 固定为 `tts.response.sentence.end`
* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***<br /> 会话 ID
    * `text` `string` ***required***
      <br /> 本次生成的文本内容
    * `ended_at` `string` ***required***
      <br /> 本次生成结束的时间，时间戳

```json theme={null}
{
        "event_id": "01956e73888c7953896a6e176bf3d760",
        "type": "tts.response.sentence.end",
        "data": {
                "session_id": "01956e7388477cfcbdc3aaabf364bc70",
                "text": "blah blah",
                "ended_at": 10292929292
        }
}
```

### 开始清空缓存 `tts.text.flushed`

系统收到指令，开始清空缓存。

* `event_id` `string` ***required***<br /> 事件 ID，用于标识本次请求，当联系客服获取支持时，可提供此 ID 协助排查问题。
* `type` `string` ***required***<br /> 固定为 `tts.response.audio.delta`
* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***
    <br /> 会话 ID，后续请求时需要带上使用

```json theme={null}
{
	"event_id": "01956e8ee1b9788c95d5981b1cfdbf12",
	"type": "tts.text.flushed",
	"data": {
		"session_id": "01956e8dc1d77bb98f9da8d1b642fcf0"
	}
}
```

### 完成本次生成 `tts.response.audio.done`

完成本次生成。接收此事件后，将会自动断开链接。此外当 IDLE 时长超过 60 秒，也会自动完成生成。

* `event_id` `string` ***required***<br /> 事件 ID，用于标识本次请求，当联系客服获取支持时，可提供此 ID 协助排查问题。
* `type` `string` ***required***<br /> 固定为 `tts.response.audio.delta`
* `data` `object` ***required***<br /> 事件内容
  * `session_id` `string` ***required***<br /> 会话 ID，后续请求时需要带上使用
  * `audio` `string` ***required***<br /> 音频内容，BASE64 编码的音频内容，包含所有音频的内容。

**Example**

```json theme={null}
{
	"event_id": "01956e8bf5067d6499cdfa0dad34f805",
	"type": "tts.response.audio.done",
	"data": {
		"session_id": "01956e7388477cfcbdc3aaabf364bc70",
		"audio": ""
	}
}
```

### 故障报错 `tts.response.error`

当生成过程中出现问题后，将会返回此事件。

```json theme={null}
{
	"event_id": "01956e8fdb157619a852bdf38028db45",
	"type": "tts.response.error",
	"data": {
		"session_id": "01956e8dc1d77bb98f9da8d1b642fcf0",
		"code": "503",
		"message": "The engine is currently overloaded, please try again later",
		"details": {
			"error": "The engine is currently overloaded, please try again later"
		}
	}
}
```

## 调用代码参考

<Tabs>
  <Tab title="python">
    先执行 `pip install  websocket rel` 后执行如下代码。

    ```python theme={null}
    import websocket
    import rel
    import json

    headers = {
        "Authorization": ""  # 更新为你的 STEPFUN API KEY
    }

    def get_start_event(sid):
        return json.dumps(
            {
                "type": "tts.create",
                "data": {
                    "session_id": sid,
                    "voice_id": "cixingnansheng",
                    "response_format": "wav",
                    "volume_ratio": 1.0,
                    "speed_ratio": 1.0,
                    "sample_rate": 16000
                },
            }
        )

    def on_message(ws, message):
        data = json.loads(message)
        session_id = data["data"]["session_id"]
        event_type = data["type"]

        if event_type == "tts.connection.done":
            start_event = get_start_event(session_id)
            ws.send(start_event)

        # 继续添加其他事件处理逻辑
        print(message)

    def on_error(ws, error):
        print(error)

    if __name__ == "__main__":
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            "wss://api.stepfun.com/v1/realtime/audio?model=step-tts-mini",
            header=headers,
            on_message=on_message,
            on_error=on_error,
        )

        ws.run_forever(
            dispatcher=rel,
            reconnect=5
        )
        rel.signal(2, rel.abort)
        rel.dispatch()
    ```
  </Tab>

  <Tab title="node">
    ```javascript theme={null}
    const WebSocket = require('ws');

    const url = 'wss://api.stepfun.com/v1/realtime/audio?model=step-tts-mini'; // 替换为你的 WebSocket URL
    const headers = {
      'Authorization': 'STEPFUN_API_KEY', // 替换为你的 API 令牌
      'Content-Type': 'application/json',
    };

    const ws = new WebSocket(url, {
      headers: headers
    });

    ws.on('open', () => {
      console.log('连接已建立');

      // 可选：在连接建立后发送消息
      // const message = JSON.stringify({ type: 'subscribe', channels: ['ticker.BTC-USD'] });
      // ws.send(message);
    });

    ws.on('message', (message) => {
      console.log(`收到消息: ${message}`);
      event = JSON.parse(message)
      session_id = event["data"]["session_id"]
      event_type = event["type"]

      if (event_type == "tts.connection.done"){
          ws.send(JSON.stringify({
              "type": "tts.create",
            "data": {
              "session_id": session_id,
              "voice_id": "cixingnansheng",
              "response_format": "wav",
              "volume_ratio": 1.0,
              "speed_ratio": 1.0,
              "sample_rate": 16000
            }
          }))
      }
      // 添加其他处理逻辑
    });

    ws.on('error', (error) => {
      console.error(`发生错误: ${error}`);
    });

    ws.on('close', (code, reason) => {
      console.log(`连接关闭, 状态码: ${code}, 原因: ${reason}`);
    });
    ```
  </Tab>

  <Tab title="StepAudio 2.5 TTS (python)">
    先执行 `pip install websocket rel` 后执行如下代码。

    ```python theme={null}
    import websocket
    import rel
    import json

    headers = {
        "Authorization": "Bearer STEP_API_KEY"  # 更新为你的 STEPFUN API KEY
    }

    def get_start_event(sid):
        return json.dumps(
            {
                "type": "tts.create",
                "data": {
                    "session_id": sid,
                    "voice_id": "cixingnansheng",
                    "response_format": "wav",
                    "volume_ratio": 1.0,
                    "speed_ratio": 1.0,
                    "sample_rate": 16000,
                    # 【修改点 1】新增 TTS 2.5 专属全局指令
                    "instruction": "语气极其愤怒，压迫感极强，语速偏快"
                },
            }
        )

    def on_message(ws, message):
        data = json.loads(message)
        session_id = data["data"]["session_id"]
        event_type = data["type"]

        if event_type == "tts.connection.done":
            # 1. 发送建联与全局指令
            start_event = get_start_event(session_id)
            ws.send(start_event)

            # 【修改点 2】补充文本发送逻辑。展示内联括号指令，并注意文本需 <= 1000字符
            text_event = json.dumps({
                "type": "tts.text.delta",
                "data": {
                    "session_id": session_id,
                    "text": "（拍桌子）你以为我们阶跃星辰北京公司的技术是开玩笑的吗！"
                }
            })
            ws.send(text_event)

            # 3. 发送 flush 强制返回当前音频
            flush_event = json.dumps({
                "type": "tts.text.flush",
                "data": {"session_id": session_id}
            })
            ws.send(flush_event)

        # 打印服务端返回的事件（包含生成的音频数据等）
        print(message)

    def on_error(ws, error):
        print(error)

    if __name__ == "__main__":
        websocket.enableTrace(True)
        # 【修改点 3】将连接 URL 中的 model 指定为 stepaudio-2.5-tts
        ws = websocket.WebSocketApp(
            "wss://api.stepfun.com/v1/realtime/audio?model=stepaudio-2.5-tts",
            header=headers,
            on_message=on_message,
            on_error=on_error,
        )

        ws.run_forever(
            dispatcher=rel,
            reconnect=5
        )
        rel.signal(2, rel.abort)
        rel.dispatch()
    ```
  </Tab>
</Tabs>
