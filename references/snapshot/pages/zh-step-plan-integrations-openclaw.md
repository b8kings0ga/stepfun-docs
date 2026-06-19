<!-- title: OpenClaw 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/openclaw.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenClaw 接入指南

> 在 OpenClaw 中使用阶跃推理模型

## 前置条件

在配置 OpenClaw 之前，确保你已经

* [订阅 Step Plan](https://platform.stepfun.com/step-plan)
* 登录 [platform.stepfun.com](https://platform.stepfun.com)，在控制台创建并获取 API Key。

## 安装 OpenClaw

如果你尚未安装 OpenClaw，请先完成安装。

在终端中运行以下命令：

<Tabs>
  <Tab title="macOS / Linux / WSL2">
    ```bash theme={null}
    curl -fsSL https://openclaw.ai/install.sh | bash
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell theme={null}
    powershell -c "irm https://openclaw.ai/install.ps1 | iex"
    ```
  </Tab>

  <Tab title="npm">
    ```bash theme={null}
    npm i -g openclaw
    ```
  </Tab>
</Tabs>

## 配置阶跃模型

安装后会启动 Onboard 引导。如果已安装过 OpenClaw，可以通过以下命令重新启动 Onboard 引导：

```bash theme={null}
openclaw onboard
```

### 配置模型 API key

使用以下配置：

* 在 Model/auth provider 中选择 StepFun。
* 在 StepFun auth method 中选择 StepFun Step Plan API key。
* 在 Enter StepFun API key 中粘贴你的 API key。
* Model configured 会显示该认证方式下默认模型。
* 在 Default model 列表中，你可以选择保持默认或者选择另外的模型。

### 完成其他配置

接下来您可以根据自己的需求配置 channel、search、skills、hooks。
配置完成后可以选择在终端(TUI) 或者 Web UI 中启动。

### 验证

启动后你可以随便问一个问题，看界面中是否有 OpenClaw 的回应。

### 其他配置方式

<Tabs>
  <Tab title="通过官方脚本快速配置">
    #### macOS / Linux（Bash）

    ```bash theme={null}
    curl -fsSL https://raw.githubusercontent.com/Zgh332358/openclaw-stepfun-installer/main/add_stepfun_smart.sh | bash 
    ```

    #### Windows（PowerShell 管理员模式）

    **注意**：必须在管理员模式的 PowerShell 下运行，否则脚本会提示并退出。

    1. 右键点击 Windows 开始菜单，选择「终端管理员」或「Windows PowerShell (管理员)」

    2. 执行以下命令：

    ```powershell theme={null}
    irm https://raw.githubusercontent.com/Zgh332358/openclaw-stepfun-installer/main/add_stepfun_smart.ps1 | iex
    ```
  </Tab>

  <Tab title="手动编辑配置文件">
    OpenClaw 的配置文件位于 `~/.openclaw/openclaw.json`。

    使用你喜欢的编辑器打开它，在文件中添加或修改以下内容：

    ```jsonc theme={null}
    {
      "agents": {
        "defaults": {
          "model": {
            "primary": "stepfun/<model_id>" // <model_id> 可填写 step-3.5-flash-2603 或 step-3.5-flash
          }
        }
      },
      "models": {
        "mode": "merge",
        "providers": {
          "stepfun": {
            "baseUrl": "https://api.stepfun.com/step_plan/v1",
            "apiKey": "${STEP_API_KEY}",
            "api": "openai-completions",
            "models": [
              {
                "id": "<model_id>",
                "name": "<model_id>",
                "reasoning": true,
                "contextWindow": 256000,
                "maxTokens": 8192
              }
            ]
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

## 常见问题

<AccordionGroup>
  <Accordion title="Q: 配置后提示 'Model is not allowed'">
    如果你设置了 `agents.defaults.models`（模型允许列表），需要确保 `stepfun/<model_id>` 也被加入到该列表中，否则模型会被拦截。解决方法：

    ```jsonc theme={null}
    {
      "agents": {
        "defaults": {
          "models": {
            "stepfun/<model_id>": {
              "alias": "Step Model"
            }
          }
        }
      }
    }
    ```

    或者直接移除 `agents.defaults.models` 配置项以取消白名单限制。
  </Accordion>

  <Accordion title="Q: `api` 字段为什么选 `openai-completions`？">
    StepFun API 完整兼容 OpenAI 的 Chat Completions 请求格式。OpenClaw 在配置自定义 Provider 时支持两种 API 类型：

    * `openai-completions`：适用于兼容 OpenAI 格式的提供商（绝大多数第三方提供商）
    * `anthropic-messages`：适用于兼容 Anthropic Messages 格式的提供商

    StepFun 属于前者。
  </Accordion>

  <Accordion title="Q: Windows 上可以不用 WSL2 吗？">
    不推荐。OpenClaw 依赖 Linux 工具链（`make`、`g++` 等）和 systemd 服务管理，原生 Windows 环境会遇到诸多兼容性问题。WSL2 是官方推荐的 Windows 使用方式。
  </Accordion>
</AccordionGroup>

## 参考链接

* [OpenClaw 官方文档](https://docs.openclaw.ai)
* [OpenClaw 模型配置文档](https://docs.openclaw.ai/concepts/model-providers)
* [OpenClaw Models CLI 文档](https://docs.openclaw.ai/concepts/models)
* [Step Plan 订阅](https://platform.stepfun.com/step-plan)
