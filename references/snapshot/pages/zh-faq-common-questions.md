<!-- title: 常见问题 -->
<!-- source: https://platform.stepfun.com/docs/zh/faq/common-questions.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 常见问题

## 接口支持

### 是否会开放类似跃问的文件内容提取的接口？

目前阶跃星辰已为开发者提供了文件解析能力，可以参考[文件解析](/zh/guides/developer/doc-parser)文档使用。

### 是否会开放类似跃问的搜索接口？

目前阶跃星辰为开发者提供了两种搜索接入方式，按需选择：

* **Web Search 工具**：在 Chat Completion 中通过 `tools` 调用，适合自建应用集成，详见 [Web Search](/zh/guides/developer/web-search) 文档。
* **StepSearch MCP Server**：基于 Model Context Protocol 的远程搜索服务，面向 Claude Code、Cline、OpenCode 等兼容 MCP 的客户端，无需本地安装，详见 [StepSearch](/zh/step-plan/integrations/search-mcp) 文档。

### 是否兼容 Langchain 或者 OpenAI

兼容，可以直接使用 Langchain 或者 OpenAI 的 SDK 调用。你可以参考 [从 OpenAI 迁移至阶跃星辰](/zh/guides/developer/openai) 完成迁移。

## 账号相关

### 个人充值能否开企业抬头的发票？

个人微信充值的订单，进行企业认证后可以开企业抬头发票。

### 如何进行企业认证？

请前往[官网-用户中心](https://platform.stepfun.com/account-info)进行企业认证，请提前准备企业相关信息（企业名称，企业银行账号，统一社会信用代码），平台会向您公司银行账户打款随机金额，用于企业验证。请联系贵公司财务确认金额，填入来自阶跃星辰科技有限公司的打款金额，金额输入正确后，企业认证通过。

### 企业认证后能否转为个人账号？

目前还未支持该功能，如有强烈诉求请扫描官网首页底部的二维码加入开发者交流群，联系客服处理。

### 企业认证后还能通过个人微信充值么？

认证为企业账户后，仍然可以进行个人微信充值。已进行企业认证的账户，进行个人充值后只能开企业抬头发票。

### 企业认证后可以换绑手机号么？

该功能已在规划进行中，预计近期上线。

### 怎么提高账号的请求限制？

为了整体资源分配的公平性，我们会根据您拥有的账户累计充值金额实施相应的速率限制策略。您可前往文档中心-定价与限速查看您的账号对应的数值。

### 充值金额是否有使用时限？

目前没有使用时限，请放心使用。

## 其他

### 怎样获取大模型或应用相关协议/合同？

请扫描官网首页底部的二维码加入开发者交流群，联系客服获取。
