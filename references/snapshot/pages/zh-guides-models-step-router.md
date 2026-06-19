<!-- title: Step Router V1 智能路由 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/step-router.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Step Router V1 智能路由

> Pro+Flash 双引擎 · 按任务复杂度自动调度的智能路由模型

`step-router-v1` 是阶跃星辰为 Step Plan 提供的智能路由模型。一行代码切换 `model` 字段，系统会根据任务复杂度自动在 `deepseek-v4-pro` 与 `step-3.5-flash` 之间调度，让复杂决策走 Pro、高频执行走 Flash，在保留高智能产出的同时控制成本。

<Note>
  本模型仅在 [Step Plan](/zh/step-plan/overview) 通道（`https://api.stepfun.com/step_plan/v1`）可用。
</Note>

## 核心能力

<Columns cols={2}>
  <Card title="🧠 双引擎自动调度">
    复杂推理与长链路决策走 `deepseek-v4-pro`，高频与确定性任务走 `step-3.5-flash`，按请求特征自动选择。
  </Card>

  <Card title="💰 成本兼顾智能">
    多数请求走 Flash 控制成本，关键节点由 Pro 兜底质量，无需手动写路由逻辑。
  </Card>
</Columns>

## 路由的两个底层引擎

`step-router-v1` 由以下两个引擎组成，按请求特征自动路由到其一：

<Columns cols={2}>
  <Card title="DeepSeek-V4-Pro" icon="brain">
    **决策引擎**：1M 上下文，384K 最大输出。面向复杂推理与长链路 Agent 决策，支持 `thinking`、`tools` / `tool_choice` 等字段透传。`step-router-v1` 在判定任务复杂或高不确定性时会路由到此模型。
  </Card>

  <Card title="Step 3.5 Flash" icon="bolt">
    **执行引擎**：196B 总参数 / 11B 激活参数 MoE 架构，高速推理。承担多数高频与结构化任务，是 `step-router-v1` 的默认承载模型。
  </Card>
</Columns>

## 路由说明

* 自动根据请求特征（消息轮数、输入 token 量、工具数量等）决定路由

## 计费

按实际命中的底层模型计费：命中 `deepseek-v4-pro` 按 `deepseek-v4-pro` 计费，命中 `step-3.5-flash` 按 `step-3.5-flash` 计费。最终按 [Step Plan](/zh/step-plan/overview) 套餐折算总额度消耗。

## 接入方式

`step-router-v1` 仅在 Step Plan 通道可用，支持 Chat Completion（OpenAI 协议）与 Messages（Anthropic 协议）两类接口：

<Columns cols={3}>
  <Card title="Step Plan 推理模型接入" icon="rocket" href="/zh/step-plan/integrations/reasoning-api">
    完整的 base\_url、SDK 示例与字段差异说明
  </Card>

  <Card title="Chat Completion API" icon="code" href="/zh/api-reference/chat/chat-completion-create">
    OpenAI 协议端点参数与响应说明
  </Card>

  <Card title="Messages API" icon="code" href="/zh/api-reference/chat/messages-create">
    Anthropic 协议端点参数与响应说明
  </Card>
</Columns>
