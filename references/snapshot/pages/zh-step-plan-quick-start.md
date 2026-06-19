<!-- title: 快速开始 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/quick-start.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

export const stepPlanTools = [{
  title: "Claude Code",
  description: "适合在终端内完成编码、调试和工程协作。",
  href: "/zh/step-plan/integrations/claude-code",
  logo: "/docs/images/stepplan/tools/claudecode-color.svg"
}, {
  title: "Hermes Agent",
  description: "适合在终端或消息平台中运行的开源 AI Agent 框架。",
  href: "/zh/step-plan/integrations/hermes-agent",
  logo: "/docs/images/stepplan/tools/hermes-agent.svg"
}, {
  title: "Open Code",
  description: "适合在终端内用自然语言驱动开发任务。",
  href: "/zh/step-plan/integrations/open-code",
  logo: "/docs/images/stepplan/tools/opencode.svg"
}, {
  title: "OpenClaw",
  description: "适合指令驱动的 Agent 和初始化型工作流。",
  href: "/zh/step-plan/integrations/openclaw",
  logo: "/docs/images/stepplan/tools/openclaw-color.svg"
}, {
  title: "Goose",
  description: "适合在终端中以本地代理方式编排任务与工具调用。",
  href: "/zh/step-plan/integrations/goose",
  logo: "/docs/images/stepplan/tools/goose.svg"
}, {
  title: "Cline",
  description: "适合在 VS Code 或 Cursor 中进行代码协作。",
  href: "/zh/step-plan/integrations/cline",
  logo: "/docs/images/stepplan/tools/cline.svg"
}, {
  title: "Roo Code",
  description: "适合在 IDE 内进行多轮任务协作。",
  href: "/zh/step-plan/integrations/roo-code",
  logo: "/docs/images/stepplan/tools/roocode.svg"
}, {
  title: "Kilo Code",
  description: "适合在 IDE 内完成代码生成与调试。",
  href: "/zh/step-plan/integrations/kilo-code",
  logo: "/docs/images/stepplan/tools/kilocode.svg"
}, {
  title: "Cherry Studio",
  description: "适合在桌面端统一管理多模型工作流。",
  href: "/zh/step-plan/integrations/cherry-studio",
  logo: "/docs/images/stepplan/tools/cherrystudio-color.svg"
}, {
  title: "Zed",
  description: "适合在轻量编辑器中直接使用 AI Assistant。",
  href: "/zh/step-plan/integrations/zed",
  logo: "/docs/images/stepplan/tools/zed-logo-blue.svg"
}];

在你常用的 AI 编程工具里接入 Step 系列模型——挑一个工具，按对应页内说明完成配置即可。

<CardGroup cols={2}>
  <Card title="平台入口" icon="key">
    * [订阅 Step Plan](https://platform.stepfun.com/step-plan)
    * [创建 API Key](https://platform.stepfun.com/interface-key)
  </Card>

  <Card title="接入参数" icon="gear">
    * **Chat Completions API（OpenAI 兼容）Base URL**：`https://api.stepfun.com/step_plan/v1`
    * **Messages API（Anthropic 兼容）Base URL**：`https://api.stepfun.com/step_plan`
    * **推荐验证模型**：`step-3.7-flash`
  </Card>
</CardGroup>

## 选择接入工具

<div className="step-plan-tool-grid">
  {stepPlanTools.map((tool) => (
      <a key={tool.href} className="step-plan-tool-card step-plan-tool-card--link" href={tool.href}>
        <div className="step-plan-tool-card__top">
          <span className="step-plan-tool-card__logo-shell" aria-hidden="true">
            <img className="step-plan-tool-card__logo" src={tool.logo} alt="" loading="lazy" />
          </span>
        </div>
        <div className="step-plan-tool-card__body">
          <h3>{tool.title}</h3>
          <p>{tool.description}</p>
        </div>
      </a>
    ))}
</div>

## 准备账号与 API Key

在开始配置前，请先确认账号已具备可用的 Step Plan，并准备好 Step API Key。它们分别决定您是否可以正常开通调用能力，以及后续请求的身份认证与授权。

> 建议顺序：先确认已订阅或开通 Step Plan，再创建 API Key，最后接入具体工具。

### 订阅 Step Plan

如果您是首次使用开放平台，建议先检查当前账号是否已经完成 Step Plan 订阅或开通。通常情况下，只有在具备可用套餐、计划或对应调用权限后，后续的模型调用、额度消耗和能力使用才会正常生效。

如果您的账号已经由团队统一开通，可直接进入下一步；如果尚未开通，请前往 [Step Plan 订阅](https://platform.stepfun.com/step-plan) 完成对应计划的订阅，再继续创建 API Key 和接入第三方工具。

### 获取 API Key

获取方式：

* [Step 开放平台](https://platform.stepfun.com/interface-key)

建议您在控制台创建一个新的 API Key，并妥善保存，不要直接写入代码仓库。

首次接入时，推荐优先使用以下模型完成验证：

```text theme={null}
step-3.7-flash
```

在不同工具中，您会频繁看到这些配置项：

* `API Provider`：选择接口提供方式，例如 `OpenAI Compatible`
* `Base URL`：按工具使用的协议选择模型服务地址。Chat Completions API（OpenAI 兼容）/ OpenAI Compatible 工具填写 `https://api.stepfun.com/step_plan/v1`；Messages API（Anthropic 兼容）工具填写 `https://api.stepfun.com/step_plan`
* `API Key`：在 Step 平台获取的密钥
* `Model` 或 `Model ID`：填写 `step-3.7-flash`

> 注意：Claude Code 手动编辑配置文件时，`ANTHROPIC_BASE_URL` 应填写 Messages API（Anthropic 兼容）对应的 `https://api.stepfun.com/step_plan`（不带 `/v1`）。Claude Code 会在调用时自动拼接 `/v1/messages`。

## 常见检查项

如果调用失败，优先检查以下几项：

* API Key 是否填写正确且属于正确环境
* `Base URL` 是否与工具协议匹配：Chat Completions API（OpenAI 兼容）/ OpenAI Compatible 使用 `https://api.stepfun.com/step_plan/v1`，Messages API（Anthropic 兼容）/ Claude Code 配置文件使用 `https://api.stepfun.com/step_plan`
* `Model` 或 `Model ID` 是否填写为 `step-3.7-flash`
* 工具是否已经保存配置并完成重启
