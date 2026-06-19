<!-- title: StepAudio 2.5 TTS -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/stepaudio-2.5-tts.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# StepAudio 2.5 TTS

> Contextual TTS · 具备语境感知能力的语音合成模型

真正具有声音表演能力的语音合成模型，首次将语境理解能力引入语音生成全流程。通过 Global Context（全局语境）+ Inline Context（文中语境）双档控制，搭配 Zero-shot 音色复刻，让 AI 不是念文本，而是演文本。

<Columns cols={3}>
  <Card title="在线 Demo" icon="headphones" href="https://stepaudiollm.github.io/step-audio-2.5-tts/">
    访问官方 demo page，快速感受模型效果。
  </Card>

  <Card title="体验中心" icon="play" href="https://www.stepfun.com/studio/audio">
    在阶跃星辰开放平台直接体验完整产品功能。
  </Card>

  <Card title="API 快速开始" icon="rocket" href="#快速上手">
    查看最小可运行的 curl / WebSocket 调用示例。
  </Card>

  <Card title="Step Plan 接入" icon="link" href="/zh/step-plan/integrations/audio-api">
    Step Plan 订阅用户可直接使用。
  </Card>
</Columns>

## 关键信息

<Columns cols={3}>
  <Card title="模型类型">
    Contextual TTS<br />基于语境理解的文本转语音
  </Card>

  <Card title="单次输入上限">
    1000 字符
  </Card>

  <Card title="instruction 上限">
    200 字符<br />全局语境自然语言指导
  </Card>
</Columns>

## 核心能力

<Columns cols={3}>
  <Card title="🎭 双档语境控制">
    Global Context 定调整段基调，Inline Context 用 `()` 括号逐句精控情绪、停顿、气息。自然语言描述替代标签匹配，支持「克制的悲伤，不哭腔，轻轻发颤」这类复合意图。
  </Card>

  <Card title="🎨 Zero-shot 音色复刻">
    只需 3s 参考音频即可进行音色复刻，且完整继承全局 / 文中语境控制能力，不受固定音库和预设角色的限制。
  </Card>

  <Card title="🎙️ 字字有戏，开口无 AI 味">
    停顿、重音、节奏、语气转折等韵律维度全面提升，底层人声品质升级，告别传统 TTS 的"塑料感"与"AI 味"。
  </Card>
</Columns>

## API 端点

<Columns cols={3}>
  <Card title="非流式语音合成" href="/zh/api-reference/audio/create-audio">
    `POST /v1/audio/speech`<br />一次性合成完整音频文件，音质首选。
  </Card>

  <Card title="流式语音合成" href="/zh/api-reference/audio/ws-audio">
    `WebSocket /v1/realtime/audio`<br />低时延流式返回，适合对话与实时播放场景。
  </Card>

  <Card title="复刻试听" href="/zh/api-reference/audio/voices-preview">
    `POST /v1/audio/voices/preview`<br />快速预览参考音频合成效果，不创建正式音色资产。
  </Card>
</Columns>

## 定价

| 计费项          | 单价                                    |
| :----------- | :------------------------------------ |
| 基于语境理解的文本转语音 | **5.8 元 / 万字符**                       |
| 语音复刻 / 生成    | **9.9 元 / 音色**（试听接口仅收合成费用；正式复刻成功立即收费） |

[查看完整定价详情 →](/zh/guides/pricing/details)

## 快速上手

模型最重要的两个能力入口：`instruction` 参数定义**整段**表达基调（全局语境），`input` / `text` 中用圆括号 `()` 插入**句内**指令定义局部细节（文中语境）。括号内的内容仅作为指令处理，**不会被直接朗读**。

<Tabs>
  <Tab title="非流式 (curl)">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/audio/speech \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "stepaudio-2.5-tts",
        "voice": "cixingnansheng",
        "input": "（压低声音）喂……你看我手机。（短促吸气）是不是我眼花了？（强装镇定）……算了，肯定是诈骗短信。",
        "instruction": "声音极度紧绷，像在拼命压住快要失控的狂喜；语速快而断续，带明显的压抑感"
      }' \
      --output step-tts-contextual.mp3
    ```

    `instruction` 定义整段语境，`input` 中括号内文本作为内联指令；模型会把情绪、停顿、气声和潜台词一起合成出来。
  </Tab>

  <Tab title="流式 (WebSocket)">
    连接地址：

    ```text theme={null}
    wss://api.stepfun.com/v1/realtime/audio?model=stepaudio-2.5-tts
    ```

    建连后发送 `tts.create` 创建会话，并附带全局 `instruction`：

    ```json theme={null}
    {
      "type": "tts.create",
      "data": {
        "session_id": "01956e7388477cfcbdc3aaabf364bc70",
        "voice_id": "cixingnansheng",
        "response_format": "wav",
        "sample_rate": 24000,
        "instruction": "语气冰冷，压迫感强，语速偏慢"
      }
    }
    ```

    随后通过 `tts.text.delta` 发送带内联指令的文本：

    ```json theme={null}
    {
      "type": "tts.text.delta",
      "data": {
        "session_id": "01956e7388477cfcbdc3aaabf364bc70",
        "text": "（激动）今天的天气真不错，我想去学习阶跃星辰的大模型技术！"
      }
    }
    ```
  </Tab>

  <Tab title="复刻试听 (curl)">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/audio/voices/preview \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "stepaudio-2.5-tts",
        "file_id": "file-Ckyl3cV09A",
        "text": "智能阶跃，十倍每一个人的可能",
        "sample_text": "今天天气不错",
        "instruction": "语气温柔，语速偏慢"
      }'
    ```

    该接口仅生成试听音频，不创建正式音色资产。
  </Tab>
</Tabs>

## 相关资源

<Columns cols={2}>
  <Card title="语音大模型总览" icon="arrow-left" href="/zh/guides/models/audio">
    返回语音大模型概览页，查看所有 TTS / ASR 模型。
  </Card>

  <Card title="完整定价详情" icon="receipt" href="/zh/guides/pricing/details">
    查看语音 / 文本 / 图像等全部模型的计费规则。
  </Card>

  <Card title="音色列表" icon="microphone" href="/zh/guides/developer/tts#支持音色">
    查看官方提供的音色及参数说明。
  </Card>

  <Card title="Demo 与体验中心" icon="play" href="https://www.stepfun.com/studio/audio">
    在线快速体验 `stepaudio-2.5-tts` 的完整能力。
  </Card>
</Columns>
