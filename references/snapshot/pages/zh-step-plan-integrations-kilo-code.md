<!-- title: Kilo Code 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/kilo-code -->
<!-- extracted: trafilatura -->

## 概述

Kilo Code 适合在编辑器内进行自然语言编程协作。完成 API 配置后，即可在 IDE 面板中直接调用 Step 模型。## 前置条件

### 开发环境

支持以下 IDE：- Cursor（推荐）
- VS Code

### 安装 Kilo Code 插件

在 IDE Marketplace 中搜索并安装：### 订阅 Step Plan

在开始配置前，请先确认当前账号已完成 Step Plan 订阅。只有在账号具备对应计划或调用权限后，后续模型调用与额度使用才会正常生效。 如需订阅或购买，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

访问[Step 平台控制台](https://platform.stepfun.com/interface-key)创建 API Key，并妥善保存：

## 配置步骤

打开 Kilo Code 设置页面，配置 API Provider。### Connection 配置

填写以下参数：`API Provider`

：`OpenAI Compatible`

`Base URL`

：`https://api.stepfun.com/step_plan/v1`

`API Key`

：填写 Step API Key`Model ID`

：填写`<model_id>`


说明：本文示例中的`<model_id>`

可填写为`step-3.7-flash`

、`step-3.5-flash-2603`

或`step-3.5-flash`

。

### 参数建议

推荐参数如下：### 兼容性说明

在部分插件版本中，如果开启`Include max output tokens`

，请求里可能会自动附带以下字段：
- 关闭
`Include max output tokens`

- 或保持
`Max Output Tokens = -1`

，由服务端决定输出长度

## 测试接入

完成配置后，可以输入一个简单任务进行验证：## 常见问题

### Connection error

若出现以下错误：`Base URL`

是否填写为`https://api.stepfun.com/step_plan/v1`

。- API Key 是否有效。
`Model ID`

是否填写为`<model_id>`

。- 是否已关闭
`Include max output tokens`

。

### API Key 错误

若出现以下报错：- Key 是否复制完整
- Key 是否属于正确环境