<!-- title: Step Router V1 智能路由开发指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/step-router.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Step Router V1 智能路由开发指南

`step-router-v1` 是阶跃星辰为 [Step Plan](/zh/step-plan/overview) 通道提供的智能路由模型。开发者只需在 `model` 字段填 `step-router-v1`，请求会被自动路由到 `deepseek-v4-pro` 或 `step-3.5-flash` 中更合适的一个：复杂推理走 Pro、高频执行走 Flash。

<Note>
  仅 [Step Plan](/zh/step-plan/overview) 通道（`https://api.stepfun.com/step_plan/v1`）可用。
</Note>

## 适用场景

* **任务复杂度差异大的混合工作流**：同一个 Agent 既要做格式整理、信息抽取等高频小任务，也要做架构规划、错误诊断等关键决策——交给 router 比手写路由逻辑更省心
* **Agent 长链路任务**：多轮对话、含工具调用的请求，router 会在判定为复杂场景时调度 Pro 兜底质量
* **成本敏感但又需要高质量决策的场景**：默认让多数请求走 Flash 控制成本，复杂请求自动升级到 Pro 保留智能产出

## 调用方式

### 非流式

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
            {"role": "user", "content": "请帮我把这段需求拆解成开发任务列表"}
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
            {"role": "user", "content": "请帮我把这段需求拆解成开发任务列表"}
        ],
    )

    print(message.content[0].text)
    ```
  </Tab>
</Tabs>

### 流式

```python theme={null}
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_STEP_API_KEY",
    base_url="https://api.stepfun.com/step_plan/v1",
)

stream = client.chat.completions.create(
    model="step-router-v1",
    messages=[{"role": "user", "content": "你好"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

## 计费机制

按实际命中模型计费——命中 `deepseek-v4-pro` 时按 `deepseek-v4-pro` 单价收费，命中 `step-3.5-flash` 时按 `step-3.5-flash` 单价收费。计费金额最终折算为 Step Plan 总额度消耗，详见 [Step Plan 概览](/zh/step-plan/overview)。

## 相关链接

<Columns cols={2}>
  <Card title="产品介绍" href="/zh/guides/models/step-router">
    `step-router-v1` 智能路由的产品定位、底层模型组成与定价。
  </Card>

  <Card title="接入文档" href="/zh/step-plan/integrations/reasoning-api">
    Step Plan 推理模型接入：base\_url、SDK、字段差异。
  </Card>
</Columns>
