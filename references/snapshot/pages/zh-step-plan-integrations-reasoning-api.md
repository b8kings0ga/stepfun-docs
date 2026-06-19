<!-- title: 推理模型接入 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/reasoning-api.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 推理模型接入

Step Plan 支持通过专属路径接入阶跃星辰推理大模型。所有请求统一使用 `/step_plan/v1/...` 路径前缀，域名固定为 `https://api.stepfun.com`。

## 前置条件

1. 已订阅 [Step Plan](https://platform.stepfun.com/step-plan) 套餐
2. 已获取 [API Key](https://platform.stepfun.com/interface-key)

***

## 支持的模型

| 模型                    | 说明                                                                           |
| --------------------- | ---------------------------------------------------------------------------- |
| `step-3.7-flash`      | 旗舰多模态推理模型，原生支持图片和视频理解，支持三档推理强度（low/medium/high），适合智能体、代码与多模态场景               |
| `step-3.5-flash-2603` | 基于 `step-3.5-flash` 针对高频 Agent 场景优化，Token 效率提升、推理速度更快，可切换至低推理模式大幅降低 Token 消耗 |
| `step-3.5-flash`      | 196B 总参数 / 11B 激活参数的稀疏 MoE 架构，高速推理，专为智能体和代码任务优化                              |
| `step-router-v1`      | 智能路由模型，自动在 `deepseek-v4-pro` 与 `step-3.5-flash` 之间切换                         |

<Note>
  `step-router-v1` 的字段约束（`max_tokens` 上限、不支持的内容类型等）详见 API 文档 [Messages API](/zh/api-reference/chat/messages-create) 与 [Chat Completion API](/zh/api-reference/chat/chat-completion-create) 中「Step Plan 通道：DeepSeek 引擎字段差异」一节。
</Note>

## 接口路径

| 能力                         | 请求方式 | Step Plan 路径                                            |
| -------------------------- | ---- | ------------------------------------------------------- |
| Chat Completion（OpenAI 协议） | POST | `https://api.stepfun.com/step_plan/v1/chat/completions` |
| Messages（Anthropic 协议）     | POST | `https://api.stepfun.com/step_plan/v1/messages`         |

<Info>
  接口参数详见 [Chat Completion API 文档](/zh/api-reference/chat/chat-completion-create) 和 [Messages API 文档](/zh/api-reference/chat/messages-create)。
</Info>

<Warning>
  Anthropic SDK 会自动在 base\_url 后拼接 `/v1/messages`，因此使用 Anthropic SDK 时 base\_url 应设为 `https://api.stepfun.com/step_plan`（不带 `/v1`）。OpenAI SDK 则使用 `https://api.stepfun.com/step_plan/v1`。
</Warning>

## 推理强度

支持三档推理强度的模型可在请求中指定 `low`、`medium`、`high`。Chat Completion（OpenAI 协议）使用 `reasoning_effort`；Messages（Anthropic 协议）使用 `output_config.effort`。

| 推理强度     | 适用场景              |
| -------- | ----------------- |
| `low`    | 简单问答、摘要、改写、信息抽取   |
| `medium` | 默认推荐，适合一般推理和多步骤任务 |
| `high`   | 复杂推理、数学、规划、代码分析   |

## 计费说明

计费逻辑与开放平台一致，最终按开放平台实际计费金额折算为 Step Plan 总额度消耗。具体套餐权益请参考 [Step Plan 概览](/zh/step-plan/overview)。`step-router-v1` 按实际命中模型计费——命中 `deepseek-v4-pro` 按 `deepseek-v4-pro` 计费，命中 `step-3.5-flash` 按 `step-3.5-flash` 计费。

## 接入方式

### 直接调用 API

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -X POST 'https://api.stepfun.com/step_plan/v1/chat/completions' \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $STEP_API_KEY" \
    -d '{
        "model": "step-3.7-flash",
        "messages": [
            {"role": "user", "content": "你好，请介绍一下你自己"}
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
        model="step-3.7-flash",
        messages=[
            {"role": "user", "content": "你好，请介绍一下你自己"}
        ],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    ```python theme={null}
    from anthropic import Anthropic

    # 注意：Anthropic SDK 会自动拼接 /v1/messages，base_url 不带 /v1
    client = Anthropic(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/step_plan",
    )

    message = client.messages.create(
        model="step-3.7-flash",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "你好，请介绍一下你自己"}
        ],
    )

    print(message.content[0].text)
    ```
  </Tab>
</Tabs>

### 切换到 Step Router V1

调用方式与上述完全一致，将 `model` 字段切换为 `step-router-v1` 即可：

<Tabs>
  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/step_plan/v1",
    )

    response = client.chat.completions.create(
        model="step-router-v1",
        messages=[
            {"role": "user", "content": "你好，请介绍一下你自己"}
        ],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="Python (Anthropic SDK)">
    ```python theme={null}
    from anthropic import Anthropic

    client = Anthropic(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/step_plan",
    )

    message = client.messages.create(
        model="step-router-v1",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "你好，请介绍一下你自己"}
        ],
    )

    print(message.content[0].text)
    ```
  </Tab>
</Tabs>

### 通过工具接入

推理模型可通过各类 Agent 工具和编码助手接入，只需将 Base URL 设置为 `https://api.stepfun.com/step_plan/v1`，模型选择 `step-3.7-flash`、`step-3.5-flash-2603`、`step-3.5-flash` 或 `step-router-v1`。

详见 [快速开始](/zh/step-plan/quick-start) 以及各工具的接入指南：

<Columns cols={2}>
  <Card title="OpenClaw" href="/zh/step-plan/integrations/openclaw">
    指令驱动的 Agent 和初始化型工作流
  </Card>

  <Card title="Claude Code" href="/zh/step-plan/integrations/claude-code">
    终端内完成编码、调试和工程协作
  </Card>

  <Card title="Hermes Agent" href="/zh/step-plan/integrations/hermes-agent">
    终端或消息平台中运行的开源 AI Agent 框架
  </Card>

  <Card title="Open Code" href="/zh/step-plan/integrations/open-code">
    终端内用自然语言驱动开发任务
  </Card>
</Columns>
