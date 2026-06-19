<!-- title: Goose 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/goose.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Goose 接入指南

Goose 是由 Block（前身为 Square）开发的开源 AI Agent 客户端。它通过自然语言支持代码生成、文件编辑、命令执行和项目分析等开发任务。通过配置 OpenAI Compatible 提供商，Goose 可以连接到 Step 模型，并在常见的开发工作流中使用本地工具。

本文档介绍将 Step API 与 Goose 集成的前置条件、配置步骤和基本验证方法。

## 概述

Goose 支持通过 OpenAI Compatible API 集成第三方大型语言模型。配置提供商后，您可以直接在 Goose 中使用 Step 模型进行对话任务、代码编辑和工具调用。

通过配置自定义提供商，Goose 可以使用 Step 模型实现以下功能：

* 自主任务执行：自动编辑文件并运行 Shell 命令。
* 代码库分析：理解项目结构并回答复杂的编程问题。
* 自动化工作流：结合本地工具链完成端到端的开发任务。

## 前置条件

开始之前，请确保满足以下要求。

### 安装 Goose

确保已安装 Goose 命令行工具或桌面客户端。

* [官方网站](https://block.github.io/goose/)

### 订阅 Step Plan

开始配置之前，请确保您的当前账户已有有效的 Step Plan 订阅。只有具备所需套餐或调用权限的账户才能正常使用模型调用和配额。

如需订阅或购买，请访问 [Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

登录 StepFun 开放平台获取用于身份验证的 API Key，并妥善保管。

### 确认连接信息

提前准备以下连接信息：

* Base URL：`https://api.stepfun.com/step_plan/v1`
* 协议类型：`OpenAI Compatible`

## 配置步骤

### 打开提供商设置

在 Goose 桌面客户端中，点击 `Settings`，选择 `Providers`，然后点击 `Add Provider`。

### 填写配置参数

在配置对话框中，输入以下信息：

* Provider Type：选择 `OpenAI Compatible`
* Display Name：输入 `StepFun`
* API URL：输入 `https://api.stepfun.com/step_plan/v1`
* API Key：粘贴您从 Step 平台获取的密钥
* Available Models：输入以下模型名称

```text theme={null}
<model_id>
```

> 说明：本文示例中的 `<model_id>` 可填写为 `step-3.7-flash`、`step-3.5-flash-2603` 或 `step-3.5-flash`。

配置完成后，Goose 即可通过该提供商调用 Step 模型。

## 测试集成

配置完成后，在 Goose 主聊天窗口切换至 `StepFun` 提供商下的任意模型，并使用以下示例进行验证。

### 基础对话测试

输入：

```text theme={null}
你好，你是谁？
```

预期结果：返回由 StepFun 提供的模型身份回复。

### 工具能力测试

输入：

```text theme={null}
请列出我当前目录下的所有文件。
```

预期结果：Goose 调用本地目录列表工具，并使用 Step 模型对文件列表进行汇总。

### 代码编辑测试

输入：

```text theme={null}
帮我创建一个名为 hello.py 的文件，输出当前时间。
```

预期结果：Goose 生成代码并将文件保存到本地磁盘。

## 常见问题

### 工具识别失败或连接超时

可能原因：当前网络环境可能无法直接访问 API 端点。

请检查以下内容：

* 代理或网络设置是否正确
* API URL 末尾是否误加了斜杠

### 模型列表为空

如果模型下拉列表为空，请确保已在 `Available Models` 中手动输入具体的模型标识符，例如：

```text theme={null}
<model_id>
```

如果未输入任何模型标识符，下拉列表可能无法正确显示可用选项。

## 总结

通过 Goose 的 `OpenAI Compatible` 模式，开发者可以将 Step 模型的推理能力与 Goose 的本地工具链相结合，用于代码生成、文件操作和项目分析等任务。

建议使用 `<model_id>` 进行集成验证和日常开发任务。
