<!-- title: StepAudio 2.5 Chat -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/stepaudio-2.5-chat.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# StepAudio 2.5 Chat

> 活人感对话大模型 · 文本返回 + 副语言感知 + 千万人设自定义

真正具备"活人感"的对话大模型。仅文本返回，但具备行业顶级副语言感知力——瞬间读懂语气中的迟疑与轻笑，输出契合度拉满的高情商反馈。全维度打造专属人设，连每一次呼吸和轻笑都不掉戏。

<Columns cols={3}>
  <Card title="API 快速开始" icon="rocket" href="#快速上手">
    查看最小可运行的 curl / Python 调用示例。
  </Card>

  <Card title="Step Plan 接入" icon="link" href="/zh/step-plan/integrations/audio-api#语音对话">
    Step Plan 订阅用户可直接使用。
  </Card>

  <Card title="Chat Completion API" icon="file-lines" href="/zh/api-reference/chat/chat-completion-create">
    查看完整请求 / 响应参数。
  </Card>
</Columns>

## 关键信息

<Columns cols={2}>
  <Card title="模型类型">
    端到端对话大模型<br />音频/文本输入，仅文本返回
  </Card>

  <Card title="协议">
    HTTP（Chat Completion）
  </Card>
</Columns>

## 核心能力

<Columns cols={2}>
  <Card title="💗 情绪价值">
    不再是冰冷的 AI，而是有脾气、有态度、懂接梗的鲜活搭子，为你带来最自然、好玩的陪伴体验。
  </Card>

  <Card title="🧠 对话双商领跑">
    实现对话智商与情商的双重跃升。深度理解复杂语意、机智抛梗，输出契合度拉满的高情商反馈。
  </Card>

  <Card title="👂 副语言感知">
    具备行业顶级副语言感知力——瞬间读懂语气中的迟疑与轻笑，无需用户明说就能精准捕捉情绪。
  </Card>

  <Card title="🎭 千万人设完全自定义">
    真正实现"全维灵魂捏脸"，彻底打破预设模板束缚。支持细颗粒度定义性格特征、专属口癖与情绪边界。
  </Card>
</Columns>

## API 端点

<Card title="对话补全（Chat Completion）" icon="comments" href="/zh/api-reference/chat/chat-completion-create">
  `POST /v1/chat/completions`<br />使用 OpenAI 兼容的 Chat Completion 协议调用。
</Card>

## 定价

| 计费项       | 单价                   |
| :-------- | :------------------- |
| 输入（缓存未命中） | **10 元 / 1M tokens** |
| 输入（缓存命中）  | **2 元 / 1M tokens**  |
| 输出        | **25 元 / 1M tokens** |

[查看完整定价详情 →](/zh/guides/pricing/details)

## 快速上手

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/chat/completions \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "stepaudio-2.5-chat",
        "modalities": ["text"],
        "messages": [
          {"role": "system", "content": "你是有耐心的陪伴搭子，回答自然、温暖、有人情味。"},
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
        base_url="https://api.stepfun.com/v1",
    )

    response = client.chat.completions.create(
        model="stepaudio-2.5-chat",
        modalities=["text"],
        messages=[
            {"role": "system", "content": "你是有耐心的陪伴搭子，回答自然、温暖、有人情味。"},
            {"role": "user", "content": "今天心情有点闷，陪我聊聊"},
        ],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>
</Tabs>

## 相关资源

<Columns cols={2}>
  <Card title="语音大模型总览" icon="arrow-left" href="/zh/guides/models/audio">
    返回语音大模型概览页，查看所有 TTS / ASR / 对话 / 实时模型。
  </Card>

  <Card title="Chat Completion API" icon="file-lines" href="/zh/api-reference/chat/chat-completion-create">
    查看完整请求 / 响应参数与字段说明。
  </Card>

  <Card title="StepAudio 2.5 Realtime" icon="bolt" href="/zh/guides/models/stepaudio-2.5-realtime">
    需要语音返回？看实时语音版本。
  </Card>

  <Card title="Step Plan 接入" icon="link" href="/zh/step-plan/integrations/audio-api#语音对话">
    Step Plan 订阅下的语音对话路径。
  </Card>
</Columns>
