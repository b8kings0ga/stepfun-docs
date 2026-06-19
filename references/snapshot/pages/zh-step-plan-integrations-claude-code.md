<!-- title: Claude Code 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/claude-code.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Code 接入指南

Claude Code 是一个运行在终端中的 AI 编码助手，可以通过自然语言命令完成代码生成、调试、重构和工程管理等任务。通过配置 API 接口，Claude Code 可以将模型调用请求转发到自定义 AI 服务。

本文档介绍如何在 Claude Code 中完成 Step API 的接入配置，并验证模型是否可用。

## 概述

Claude Code 适合偏终端工作流的开发者。完成配置后，可以直接在本地项目中通过自然语言驱动编码任务。

## 前置条件

### 操作系统

Claude Code 支持以下系统：

* macOS
* Linux
* Windows（建议使用 PowerShell 或 Windows Terminal）

### Node.js 环境

Claude Code 依赖 Node.js 运行，建议安装 `Node.js >= 18`。

不同系统的安装方式示例：

* macOS：使用 Homebrew 或 `nvm`
* Linux：使用系统包管理器或 `nvm`
* Windows：使用 Node 官方安装包或 Chocolatey

示例命令：

```bash theme={null}
brew install node
nvm install 18
sudo apt install nodejs npm
choco install nodejs
```

安装完成后，运行以下命令确认环境：

```bash theme={null}
node -v
npm -v
```

### 订阅 Step Plan

在开始配置前，请先确认当前账号已完成 Step Plan 订阅。只有在账号具备对应计划或调用权限后，后续模型调用与额度使用才会正常生效。

如需订阅或购买，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

在调用模型前，需要先在 [Step 开放平台](https://platform.stepfun.com/interface-key)获取 API Key。建议通过控制台创建新的 Key，并避免将其硬编码进代码仓库。

推荐做法：

* 使用环境变量保存 Key
* 或通过本地配置文件管理 Key

## 配置步骤

### 安装 Claude Code

在终端中执行：

```bash theme={null}
npm install -g @anthropic-ai/claude-code
```

安装完成后，验证版本：

```bash theme={null}
claude --version
```

### 创建配置文件

<Tabs>
  <Tab title="通过官方脚本快速配置">
    macOS / Linux（Bash）

    ```bash theme={null}
    curl -fsSL https://cdn.jsdelivr.net/gh/Zgh332358/claude-key-setup@main/configure_claude.sh -o configure_claude.sh
    chmod +x configure_claude.sh
    bash configure_claude.sh  
    ```

    Windows（PowerShell 管理员模式）

    **注意**：必须在管理员模式的 PowerShell 下运行，否则脚本会提示并退出。

    1. 右键点击 Windows 开始菜单，选择「终端管理员」或「Windows PowerShell (管理员)」。

    2. 执行以下命令：

    ```powershell theme={null}
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; irm https://raw.githubusercontent.com/Zgh332358/claude-key-setup/main/configure_claude.ps1 -OutFile configure_claude.ps1; .\configure_claude.ps1
    ```
  </Tab>

  <Tab title="手动编辑配置文件">
    Claude Code 通过配置文件读取 API 服务地址和认证信息。配置文件位置为：

    ```text theme={null}
    ~/.claude/settings.json
    ```

    如果文件不存在，可以先创建目录和文件：

    ```bash theme={null}
    mkdir -p ~/.claude
    touch ~/.claude/settings.json
    ```

    将以下内容写入配置文件：

    ```jsonc theme={null}
    {
      "env": {
        "ANTHROPIC_AUTH_TOKEN": "YOUR_API_KEY",
        "ANTHROPIC_BASE_URL": "https://api.stepfun.com/step_plan"
      },
      "model": "<model_id>"
    }
    ```

    参数说明：

    * `ANTHROPIC_AUTH_TOKEN`：填写你的 Step API Key
    * `ANTHROPIC_BASE_URL`：填写 Base URL
    * `model`：填写 `<model_id>`

    > 说明：本文示例中的 `<model_id>` 可填写为 `step-3.7-flash`、`step-3.5-flash-2603` 或 `step-3.5-flash`。

    保存后，建议重新打开终端使配置生效。
  </Tab>
</Tabs>

### 启动 Claude Code

进入任意代码项目目录：

```bash theme={null}
cd your-project
```

启动 Claude Code：

```bash theme={null}
claude
```

首次启动时若出现 `Do you want to use this API key?`，选择 `Yes` 即可。

## 测试接入

进入 Claude Code 后，先执行以下命令查看当前配置状态：

```text theme={null}
/status
```

确认以下信息正确：

* API Key 已加载
* Base URL 正确（`https://api.stepfun.com/step_plan`）
* 默认模型名称正确（`<model_id>`）

随后执行测试指令：

```text theme={null}
write a minimal python hello world program into hello.py
```

如果 Claude Code 成功创建文件并写入代码，则说明模型接入成功。

## 常见问题

### 模型不存在

报错示例：

```text theme={null}
model does not exist
```

可能原因：

* 模型名称填写错误（应为 `<model_id>`）
* 当前账号没有该模型权限
* Base URL 指向错误接口（应为 `https://api.stepfun.com/step_plan`）

### API Key 无效

报错示例：

```text theme={null}
401 invalid_api_key
```

可能原因：

* API Key 输入错误
* Key 已过期或被删除
* Key 与当前 API 域名不匹配

### 配额不足

报错示例：

```text theme={null}
402 quota_exceeded
```

这通常表示当前账户调用额度已用完，需要补充余额或升级套餐。

### 修改配置后不生效

建议检查：

1. Claude Code 是否已完全重启。
2. 配置文件 JSON 格式是否正确。
3. 终端环境变量是否已经刷新。

## 总结

完成配置后，Claude Code 即可在终端中通过 Step API 发起模型调用，用于代码生成、调试和开发流程自动化。建议先用 `/status` 和最小任务验证配置，再进入真实项目使用。
