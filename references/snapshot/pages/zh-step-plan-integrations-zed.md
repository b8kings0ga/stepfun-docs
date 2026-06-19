<!-- title: Zed 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/zed.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Zed 接入指南

Zed 是一款高性能代码编辑器，内置 AI Assistant 能力，并支持通过 OpenAI Compatible API 调用第三方大模型。通过配置自定义 API Endpoint，Zed 可以接入 Step 模型，在编辑器内完成对话、代码生成、代码解释和代码修改等任务。

## 概述

Zed 适合在轻量编辑器中直接使用 AI Assistant。完成接口配置后，即可在编辑器内调用 Step 模型完成常见编程辅助任务。

## 前置条件

### 安装 Zed

下载并安装 Zed 编辑器：[https://zed.dev](https://zed.dev)

安装完成后启动 Zed。

### 订阅 Step Plan

在开始配置前，请先确认当前账号已完成 Step Plan 订阅。只有在账号具备对应计划或调用权限后，后续模型调用与额度使用才会正常生效。

如需订阅或购买，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

在 [Step 开放平台](https://platform.stepfun.com) 获取 API Key，用于身份认证和请求授权。

## 配置步骤

### 打开 Agent Panel 设置

使用命令面板（`Cmd+Shift+P`），输入并执行：

```text theme={null}
agent: open settings
```

### 添加 LLM Provider

在打开的界面中，找到 **LLM Providers** 区域，点击右侧的 **+ Add Provider** 按钮，在弹出的表单中填写以下信息：

* **Provider Name**：`Stepfun`（自定义名称，可任意填写）
* **API URL**：`https://api.stepfun.com/step_plan/v1`
* **API Key**：填写在 Step 平台获取的 API Key
* **Model Name**：`<model_id>`

> 说明：本文示例中的 `<model_id>` 可填写为 `step-3.5-flash-2603` 或 `step-3.5-flash`。

填写完成后，点击 **Save Provider** 保存。

## 测试接入

### 基础对话测试

在 Agent Panel 中输入：

```text theme={null}
hello
```

如果返回正常内容，说明 API 调用成功。

### 代码生成测试

输入：

```text theme={null}
Write a python hello world program
```

预期返回类似结果：

```python theme={null}
print("Hello, world!")
```

### 代码解释测试

在代码文件中选中一段代码后输入：

```text theme={null}
Explain this code
```

如果能收到解释结果，说明模型调用链路正常。

## 常见问题

### 无法连接 API

请检查：

* API URL 是否填写为 `https://api.stepfun.com/step_plan/v1`
* API Key 是否有效
* 当前网络是否可访问 API Endpoint

### 模型返回错误

请确认 Model Name 是否填写正确，例如：

```text theme={null}
<model_id>
```

### AI 无响应

建议重新检查以下配置并重启 Zed：

* API URL
* API Key
* Model Name（`<model_id>`）

## 总结

完成 LLM Provider 配置后，Zed 即可通过 Step API 提供对话、代码生成和代码解释等辅助能力。建议先完成基础对话和最小代码示例测试，再投入实际开发使用。
