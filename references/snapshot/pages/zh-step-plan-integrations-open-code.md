<!-- title: Open Code 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/open-code.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Open Code 接入指南

Open Code 是一款运行在终端中的 AI Coding Agent，适合通过自然语言完成代码生成、代码修改和项目分析等开发任务。完成配置后，可以直接在终端中调用 Step 模型完成开发流程。本文档介绍 Open Code 接入 Step Plan 的准备条件、配置步骤与基础验证方法。

## 概述

Open Code 适合偏终端交互的开发工作流。Open Code 内置了 StepFun Provider，但默认 Base URL 指向普通付费 API（`/v1`）。要用上 Step Plan 订阅额度，**必须通过 `opencode.json` 将 Base URL 覆盖为 `step_plan/v1`**——这是本指南的核心配置点。

## 前置条件

### 开发环境

支持以下系统：

* macOS
* Linux
* Windows（推荐使用 WSL）

### 安装 Open Code

推荐使用 Open Code 官方安装脚本（macOS / Linux / WSL）：

```bash theme={null}
curl -fsSL https://opencode.ai/install | bash
```

<Tip>
  如果上述脚本下载较慢（脚本会从 GitHub release 资产拉取，国内网络偶尔会中断），或不希望使用 WSL，可改用以下方式：

  ```bash theme={null}
  # Homebrew（macOS / Linux）
  brew install anomalyco/tap/opencode

  # Chocolatey（Windows）
  choco install opencode

  # Scoop（Windows）
  scoop install opencode

  # npm 全局安装（跨平台）
  npm install -g opencode-ai
  ```
</Tip>

安装完成后，确认安装成功：

```bash theme={null}
opencode --version
```

### 订阅 Step Plan

在开始配置前，请先确认当前账号已完成 Step Plan 订阅。只有在账号具备对应计划或调用权限后，后续模型调用与额度使用才会正常生效。如需订阅或购买，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

访问 [Step 平台控制台](https://platform.stepfun.com/interface-key) 创建 API Key，复制并妥善保存。

## 配置步骤

Open Code 通过 `opencode.json` 配置文件管理 Provider，无需写入 `~/.zshrc`。

### 创建 opencode.json

创建 `~/.config/opencode/opencode.json`（全局配置，对所有项目生效）：

```bash theme={null}
mkdir -p ~/.config/opencode
```

写入以下内容：

```json theme={null}
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "stepfun": {
      "api": "https://api.stepfun.com/step_plan/v1",
      "models": {
        "step-3.7-flash": { "name": "Step 3.7 Flash" }
      }
    }
  }
}
```

<Warning>
  `provider.stepfun.api` 这一行**必须填写**。Open Code 内置的 StepFun Provider 默认指向 `https://api.stepfun.com/v1`（普通付费 API），不覆盖会导致请求走错端点、用不上 Step Plan 订阅额度。
</Warning>

### 设置环境变量

Open Code 通过 `STEPFUN_API_KEY` 环境变量读取 Step API Key。打开终端运行：

```bash theme={null}
echo 'export STEPFUN_API_KEY="xxxxxx"' >> ~/.zshrc
source ~/.zshrc
```

将 `xxxxxx` 替换为你在控制台创建的 Step API Key。

验证：

```bash theme={null}
echo $STEPFUN_API_KEY
```

若输出你的 API Key，则说明配置成功。

### 选择模型

在终端任意目录启动 Open Code：

```bash theme={null}
opencode
```

按下 `/` 输入 `/models` 调出模型列表，选择：

* `stepfun/step-3.7-flash`

选择后终端底部会显示当前模型，例如：

```text theme={null}
> build · step-3.7-flash
```

这表示当前会话已在使用 Step 模型。

## 测试接入

启动 `opencode` 后，输入简单任务进行验证：

```text theme={null}
Create a hello world script in Python
```

若接入成功，模型会返回类似内容：

```python theme={null}
print("Hello, world!")
```

## 常见问题

### 401 Incorrect API key

如果出现：

```text theme={null}
401 Incorrect API key
```

请按顺序排查：

1. `STEPFUN_API_KEY` 是否已写入并 `source ~/.zshrc`，`echo $STEPFUN_API_KEY` 是否有输出。
2. Key 是否复制完整、首尾是否带空格或换行。
3. 控制台对应账号是否已订阅 Step Plan。

### 400 you have no active step plan subscription

如果出现：

```text theme={null}
400 you have no active step plan subscription
```

当前账号尚未订阅 Step Plan。请到 [Step Plan 订阅](https://platform.stepfun.com/step-plan) 开通后重试。

### 请求很久没响应 / 没用上订阅额度

如果调用能成功返回内容，但发现：

* 响应时间异常长、或者
* Step Plan 订阅的 Credit 额度没有消耗、走的是按 token 付费

请确认 `~/.config/opencode/opencode.json` 中的 `provider.stepfun.api` 已正确指向 `https://api.stepfun.com/step_plan/v1`。Open Code 内置的 StepFun Provider 默认指向 `https://api.stepfun.com/v1`，不覆盖会走错端点。

### Provider 未显示 / 模型列表里找不到 StepFun

StepFun 只有在配置了凭证后才会出现在 `/models` 列表中。请检查：

1. 是否已配置 StepFun 凭证（设置 `STEPFUN_API_KEY` 环境变量、`opencode auth login`、或在 `opencode.json` 中配置 `provider.stepfun.options.apiKey`）。
2. `opencode.json` 文件路径与 JSON 格式是否正确（`opencode providers list` 可查看当前识别到的 Provider）。
3. 如果以上都没问题，Open Code 版本可能过低，运行 `opencode upgrade` 升级到最新版本后重试。

### 调用名（模型 ID）

在 Open Code 里指定模型时使用 `<provider>/<model>` 格式：

```text theme={null}
stepfun/step-3.7-flash
stepfun/step-3.5-flash
stepfun/step-3.5-flash-2603
```

## 总结

完成 `opencode.json`、`STEPFUN_API_KEY` 配置后，Open Code 即可通过 Step Plan 在终端中执行代码生成、文件编辑和项目分析等任务。建议先按「测试接入」一节在 TUI 中跑一次范例验证连通性，再继续补充你自己的终端开发工作流。
