<!-- title: Hermes Agent 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/hermes-agent.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hermes Agent 接入指南

Hermes Agent 是由 Nous Research 开发的开源 AI Agent 框架，支持在终端环境中通过自然语言完成代码生成、文件编辑、任务自动化等开发任务。Hermes Agent 可以接入 Step 模型，在命令行或消息平台中调用推理能力。

本文档介绍如何在 Hermes Agent 中完成 Step API 的接入配置，并验证模型是否可用。

## 概述

Hermes Agent 适合在服务器或本地终端中运行的 AI 编程助手。完成配置后，你可以通过终端 TUI 或 Telegram 等消息平台与 Agent 对话，让它执行代码生成、文件操作、定时任务等自动化工作。

## 前置条件

### 操作系统

Hermes Agent 支持以下系统：

* Linux（推荐 Ubuntu/Debian）
* macOS
* Windows（需使用 WSL2）

### 安装 Hermes Agent

Hermes Agent 提供一键安装脚本，自动完成依赖安装和配置。

**通过安装脚本（推荐）：**

```bash theme={null}
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装脚本会自动检测并安装以下组件：

* `uv`（Python 包管理器）
* `Python 3.9+`
* `Node.js`（部分技能需要）
* `ripgrep`、`ffmpeg` 等工具

安装完成后，重新加载 shell 配置：

```bash theme={null}
source ~/.bashrc   # Bash 用户
# 或
source ~/.zshrc    # Zsh 用户
```

验证安装：

```bash theme={null}
hermes --version
```

若返回版本号（如 `Hermes Agent v0.6.0`），则说明安装成功。

### 订阅 Step Plan

在开始配置前，请先确认当前账号已完成 Step Plan 订阅。只有在账号具备对应计划或调用权限后，后续模型调用与额度使用才会正常生效。

如需订阅或购买，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

在 [Step 开放平台](https://platform.stepfun.com/interface-key) 获取 API Key，用于身份认证和请求授权。建议通过控制台创建新的 Key，并避免将其硬编码进代码仓库。

推荐做法：

* 使用环境变量保存 Key
* 或通过本地配置文件管理 Key

## 配置步骤

Hermes Agent 通过环境变量或配置文件读取 API 服务地址和认证信息。

### 方式一：通过 Hermes Agent 的配置向导

如果你是首次安装或希望重新运行引导流程：

打开终端，执行以下命令：

```bash theme={null}
hermes setup
```

在引导过程中：

1. 当提示选择模型提供商时，选择 **StepFun Step Plan**后选择**China**。

2. 填入你在第一步获取的 **API Key**。

3. 选择你想要用的 Model ID。

### 方式二：配置文件修改

Hermes Agent 的配置文件位于 `~/.hermes/config.yaml`。

打开配置文件，找到 `model` 相关配置项，添加或修改以下内容：

```yaml theme={null}
model:
  provider: openai
  api_key: "你的Step API Key"
  base_url: "https://api.stepfun.com/step_plan/v1"
  model: "<model_id>"
```

> **说明**：本文示例中的 `<model_id>` 可填写为 `step-3.7-flash`、`step-3.5-flash-2603` 或 `step-3.5-flash`。

### 选择模型

配置完成后，运行以下命令选择模型：

```bash theme={null}
hermes model
```

## 测试接入

完成配置后，启动 Hermes Agent 并发送测试消息：

```bash theme={null}
hermes
```

在对话界面中输入：

```text theme={null}
hello
```

如果返回正常内容，说明 API 调用成功。

### 代码生成测试

输入：

```text theme={null}
Create a hello world script in Python
```

预期返回类似结果：

```python theme={null}
print("Hello, world!")
```

### 文件操作测试

输入：

```text theme={null}
在当前目录创建一个名为 test.txt 的文件，内容为 "Hermes Agent test"
```

如果 Agent 成功创建文件，则说明模型调用链路正常。

## 常见问题

### 模型列表为空或无法加载

如果 `hermes model` 命令中未显示 Step 相关模型，请检查：

1. 当前网络是否能访问 `api.stepfun.com`。
2. Base URL 是否填写为 `https://api.stepfun.com/step_plan/v1`。
3. API Key 是否具有 Step Plan 权限。
4. Hermes Agent 是否为最新版本（`hermes update` 升级）。

### API Key 错误

如果出现以下报错：

```text theme={null}
401 Incorrect API key
```

请检查：

* Key 是否复制完整
* Key 是否属于正确环境（Step Plan 对应 `.com` 域名）
* Base URL 是否指向 Step Plan 端点

### 连接超时或失败

请检查：

* 当前网络环境是否正常（如有代理需配置）
* API 端点是否可访问（`curl https://api.stepfun.com/step_plan/v1` 测试连通性）

### 模型返回错误

请确认 Model ID 是否填写正确，例如：

```text theme={null}
<model_id>
```

推荐模型：

* `step-3.7-flash`（多模态推理旗舰，支持图片和视频理解）
* `step-3.5-flash-2603`（Agent 优化版，推理更强）
* `step-3.5-flash`（标准版，响应更快）

## 高级配置（可选）

### 启用工具调用

Hermes Agent 支持自动工具调用。在 `~/.hermes/config.yaml` 中启用：

```yaml theme={null}
tools:
  enabled:
    - terminal
    - file
    - browser
    - code_execution
```

### 配置记忆系统

Hermes Agent 的持久记忆存储在 `~/.hermes/memories/` 目录。你可以通过自然语言让 Agent 记住重要信息，这些记忆会在后续对话中自动召回。

### 消息网关（Telegram/Discord）

如需在手机上通过 Telegram 与 Hermes Agent 对话，启动网关：

```bash theme={null}
hermes gateway start
```

首次运行会提示配置 `TELEGRAM_BOT_TOKEN` 和 `TELEGRAM_ALLOWED_USERS`，相关信息可在 Telegram 中通过 @BotFather 获取。

## 总结

完成环境变量或配置文件配置后，Hermes Agent 即可通过 Step API 在终端或消息平台中执行代码生成、文件编辑、任务自动化等开发任务。建议先用最小示例（如 hello world）验证连通性，再逐步探索技能创建、记忆管理和定时任务等高级功能。
