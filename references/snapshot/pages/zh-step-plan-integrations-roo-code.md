<!-- title: Roo Code 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/roo-code.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Roo Code 接入指南

Roo Code 是一款运行在 IDE 中的 Coding Agent 插件，可以通过自然语言完成代码生成、调试和文件修改等开发任务。通过配置 OpenAI Compatible API，Roo Code 可以接入 Step 模型，并在 IDE 内直接调用推理能力。

本文档介绍 Roo Code 接入 Step API 的准备条件、配置方法、参数建议与常见问题。

## 概述

Roo Code 适合在编辑器中进行多轮代码协作。完成配置后，你可以直接在插件面板中调用 Step 模型完成编码任务。

## 前置条件

### 开发环境

支持以下 IDE：

* Cursor
* VS Code

### 安装 Roo Code 插件

在 IDE Marketplace 中搜索并安装：

```text theme={null}
Roo Code
```

安装完成后，IDE 中通常会出现以下入口：

```text theme={null}
Roo: Open Chat
Roo: New Task
Roo: Settings
```

### 订阅 Step Plan

在开始配置前，请先确认当前账号已完成 Step Plan 订阅。只有在账号具备对应计划或调用权限后，后续模型调用与额度使用才会正常生效。

如需订阅或购买，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

访问 [Step 平台控制台](https://platform.stepfun.com/interface-key)创建 API Key，并妥善保存：

## 配置步骤

打开 Roo Code 设置页面，配置 API Provider。

### Connection 配置

设置如下参数：

* `API Provider`：`OpenAI Compatible`
* `Base URL`：`https://api.stepfun.com/step_plan/v1`
* `API Key`：填写 Step API Key
* `Model ID`：填写 `<model_id>`

> 说明：本文示例中的 `<model_id>` 可填写为 `step-3.5-flash-2603` 或 `step-3.5-flash`。

### 参数建议

推荐配置如下：

```text theme={null}
Stream: Enabled
Context Window: 256000
Include max output tokens: Off
Max Output Tokens: -1
```

### 兼容性说明

在部分插件版本中，如果开启 `Include max output tokens`，请求中可能会自动附带以下字段：

```text theme={null}
max_tokens
max_output_tokens
```

不同 OpenAI Compatible API 对这些字段的兼容性可能存在差异，可能导致请求失败并显示：

```text theme={null}
OpenAI completion error: Connection error
```

如果遇到该问题，可以尝试：

* 关闭 `Include max output tokens`
* 或保持 `Max Output Tokens = -1`

## 测试接入

原始材料未单列测试步骤，但可在完成配置后发起一个最小任务来验证模型调用是否成功，例如新建对话并尝试生成简单代码。

## 常见问题

### Connection error

若出现以下错误：

```text theme={null}
OpenAI completion error: Connection error
```

请检查：

1. `Base URL` 是否填写为 `https://api.stepfun.com/step_plan/v1`。
2. API Key 是否有效。
3. `Model ID` 是否填写为 `<model_id>`。
4. `Context Window` 是否设置为足够大的值（推荐 `256000`）。

### API Key 错误

若出现以下报错：

```text theme={null}
401 Incorrect API key
```

请检查：

* Key 是否复制完整
* 是否属于正确的 Step 环境

## 总结

完成 OpenAI Compatible 配置后，Roo Code 即可在 IDE 中调用 Step 模型，用于代码生成、文件编辑和任务协作。建议优先使用推荐参数，并先完成一次最小任务验证。
