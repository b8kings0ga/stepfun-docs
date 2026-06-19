<!-- title: Cline 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/cline.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cline 接入指南

Cline 是一款运行在 IDE 中的 AI Coding Agent，常见于 VS Code、Cursor 等编辑器环境。通过配置 OpenAI Compatible API，Cline 可以接入 Step 模型，在 IDE 内完成代码生成、文件修改和项目分析等任务。

本文档介绍 Cline 接入 Step API 的准备条件、配置步骤与基础测试流程。

## 概述

Cline 适合在编辑器内直接完成多轮代码协作。配置完成后，你可以在 IDE 面板中直接调用 Step 模型执行开发任务。

## 前置条件

### 开发环境

支持以下 IDE：

* Cursor
* VS Code

建议使用最新版本 IDE。

### 安装 Cline 插件

在 IDE Marketplace 中搜索并安装：

```text theme={null}
Cline
```

安装完成后，IDE 左侧将出现 Cline 面板。

### 订阅 Step Plan

在开始配置前，请先确认当前账号已完成 Step Plan 订阅。只有在账号具备对应计划或调用权限后，后续模型调用与额度使用才会正常生效。

如需订阅或购买，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

访问 [Step 平台控制台](https://platform.stepfun.com/interface-key)创建 API Key，并妥善保存：

## 配置步骤

打开 Cline 设置页面，按以下方式配置 API Provider。

### Connection 配置

填写以下参数：

* `API Provider`：`OpenAI Compatible`
* `Base URL`：`https://api.stepfun.com/step_plan/v1`
* `API Key`：填写 Step API Key
* `Model ID`：`<model_id>`

> 说明：本文示例中的 `<model_id>` 可填写为 `step-3.7-flash`、`step-3.5-flash-2603` 或 `step-3.5-flash`。

## 测试接入

完成配置后，可以输入一个简单任务进行验证：

```text theme={null}
Create a hello world script in Python
```

若接入成功，模型通常会返回类似内容：

```python theme={null}
print("Hello, world!")
```

## 常见问题

### Connection error

若出现连接错误，请检查：

1. `Base URL` 是否填写为 `https://api.stepfun.com/step_plan/v1`。
2. API Key 是否有效。
3. `Model ID` 是否存在。

推荐模型：

```text theme={null}
<model_id>
```

### API Key 错误

若出现以下报错：

```text theme={null}
401 Incorrect API key
```

请检查：

* Key 是否复制完整
* Key 是否属于当前中文站账号环境（`.com`）

## 总结

通过 OpenAI Compatible 接口完成配置后，Cline 就可以在 IDE 中直接调用 Step 模型，执行代码生成、文件编辑和项目分析等任务。建议先用最小示例验证，再逐步加入自己的开发场景。
