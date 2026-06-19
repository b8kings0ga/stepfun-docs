<!-- title: 推理模型总览 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/reasoning.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 推理模型总览

## 模型概览

推理大模型拥有深度思考的推理能力，擅长处理逻辑推理、数学、代码等任务。

## 模型列表

### Step 3.7 Flash

推荐使用。阶跃星辰的旗舰多模态推理模型。在 `step-3.5-flash` 的高速推理与工具调用能力基础上，新增**原生多模态输入能力**，可直接理解图片和视频内容，无需借助视觉 MCP 或额外模型。基于 198B 总参数 / 11B 激活参数的稀疏 MoE 架构，支持三档推理强度（low/medium/high），是智能体、代码与多模态场景的快且可依赖的模型。上下文长度为 256K。

[查看详细文档 →](/zh/guides/models/step-3.7-flash)

### Step 3.5 Flash

纯文本推理。阶跃星辰的旗舰语言推理模型。该模型具备顶尖推理能力与快速可靠的执行能力。能够完成对复杂任务的分解、计划，可快速可靠地调用工具执行任务，胜任逻辑推理、数学、软件工程、深度研究等各种复杂任务。上下文长度为 256K。

## 模型上下文长度

模型的上下文长度是指在进行一次特定的推理时，模型在生成响应之前可以"回顾"和"理解"的输入内容的长度。这个参数决定了模型能够记住和参考多少先前的信息。较长的上下文长度允许模型在生成响应时利用更多的历史信息，从而提高生成文本的连贯性和准确性。需要注意的是，长度同时限制了模型输入和输出，即输入和输出的总长度不能超过模型上下文限制。

| 模型             | 上下文长度 |
| -------------- | ----- |
| Step 3.7 Flash | 256K  |
| Step 3.5 Flash | 256K  |

## 模型快速入门

<Columns cols={2}>
  <Card title="推理模型开发指南" href="/zh/guides/developer/reasoning">
    了解推理模型在复杂任务、工具调用和长上下文中的推荐用法。
  </Card>

  <Card title="从 OpenAI 迁移至阶跃星辰" href="/zh/guides/developer/openai">
    使用兼容 OpenAI 的调用方式，快速切换到阶跃星辰模型。
  </Card>

  <Card title="实现多轮对话" href="/zh/guides/developer/multiple-round">
    管理消息历史与上下文，构建稳定的多轮对话体验。
  </Card>

  <Card title="实现文档问答" href="/zh/guides/developer/doc-parser">
    解析文档内容并结合文本模型完成问答、抽取和理解任务。
  </Card>

  <Card title="输出 JSON" href="/zh/guides/developer/json-mode">
    让模型输出可解析的结构化 JSON，便于和应用逻辑集成。
  </Card>

  <Card title="流式输出" href="/zh/guides/developer/stream">
    通过流式返回逐步渲染结果，缩短用户感知等待时间。
  </Card>

  <Card title="实现 Tool Call" href="/zh/guides/developer/tool-call">
    让模型调用搜索、数据库或业务函数，扩展应用能力。
  </Card>

  <Card title="实现联网搜索" href="/zh/guides/developer/web-search">
    接入互联网搜索，为模型补充最新信息与外部知识。
  </Card>

  <Card title="Prompt 缓存" href="/zh/guides/developer/prompt-cache">
    复用重复上下文，降低成本并提升长对话场景响应速度。
  </Card>
</Columns>
