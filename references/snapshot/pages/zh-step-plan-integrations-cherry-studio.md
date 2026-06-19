<!-- title: Cherry Studio 接入指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/cherry-studio.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cherry Studio 接入指南

Cherry Studio 是一款桌面 AI 客户端，支持多模型 Provider，并提供对话、代码生成和文本生成等能力。通过配置 Step API Key，Cherry Studio 可以直接接入 Step 模型，在桌面客户端中调用推理能力。

本文档介绍 Cherry Studio 接入 Step API 的准备条件、配置步骤与基础测试流程。

## 概述

Cherry Studio 适合在统一桌面工作台中完成多模型对话和开发辅助任务。完成 Provider 配置后，即可在客户端内直接调用 Step 模型。

## 前置条件

### 客户端环境

支持以下系统：

* macOS
* Windows
* Linux

建议使用最新版本 Cherry Studio。

### 安装 Cherry Studio

访问 [Cherry Studio 官网](https://cherry-ai.com)下载安装包。

安装完成后启动 Cherry Studio。

### 订阅 Step Plan

在开始配置前，请先确认当前账号已完成 Step Plan 订阅。只有在账号具备对应计划或调用权限后，后续模型调用与额度使用才会正常生效。

如需订阅或购买，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

### 获取 Step API Key

访问 [Step 平台控制台](https://platform.stepfun.com/interface-key)创建 API Key，并妥善保存。

## 配置步骤

### 添加 Provider

打开 Cherry Studio，进入模型配置界面：

1. 在模型服务列表中选择**阶跃星辰**。
2. 输入 `Step API Key`。
3. 在 API 地址栏输入：

```text theme={null}
https://api.stepfun.com/step_plan/v1
```

4. 保存配置。

5. 添加 `step-3.7-flash`、`step-3.5-flash-2603` 或 `step-3.5-flash` 模型。

点击<strong>+添加</strong>，在打开的窗口中输入以下选项：

* 模型 ID：`<model_id>`
* 模型名称：可填写便于识别的名称
* 分组名称：可填写便于归类的名称

> 说明：本文示例中的 `<model_id>` 可填写为 `step-3.7-flash`、`step-3.5-flash-2603` 或 `step-3.5-flash`。

点击**添加模型**保存设置。

## 测试接入

点击 API 密钥右侧的**检测**。如果提示成功，则表明设置成功。如果出现错误，则需要检查 API key 和 base url 是否设置正确。
