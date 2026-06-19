<!-- title: 场景示例 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/step-3.7-flash-cookbook.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 场景示例

> 使用 Step 3.7 Flash 处理白板、图表、票据、截图和录屏等多模态任务

`step-3.7-flash` 可以把图片、视频和文本放在同一次对话中理解，适合把现实世界里的视觉信息转成计划、表格、代码草稿或问题诊断。本文收集一些常见场景的 prompt 模板，帮助你快速判断任务该怎么组织输入和输出。

<Info>
  这些示例侧重任务设计和输出格式。代码调用方式请先参考 [快速上手](/zh/guides/models/step-3.7-flash-quickstart)；图片、视频的细节参数请参考 [图片理解最佳实践](/zh/guides/developer/image-chat) 和 [视频理解最佳实践](/zh/guides/developer/video-chat)。
</Info>

## 使用建议

* 先明确输出格式：让模型输出 Markdown 表格、JSON、CSV 行或任务清单。
* 对关键字段要求保留证据：例如金额、日期、图表数值、任务 owner，需要让模型说明来源或不确定项。
* 不要让模型猜缺失信息：看不清、无法判断的字段应输出 `null`、空字符串或“无法确认”。
* 涉及财务、报销、合同、医疗等高风险数据时，需要人工复核。

## 白板转计划

适合处理会议白板、便利贴墙、手写流程图、项目讨论照片。目标是把松散信息转成可执行计划，而不是逐字转录。

```text theme={null}
这是一张项目讨论白板照片。请完成：
1. 提取白板中的主要议题和结论
2. 整理成一份项目计划，包含目标、关键里程碑、风险和待确认事项
3. 生成任务清单，字段包括：任务、负责人（如无法判断则为 null）、优先级、依赖项、建议截止时间
4. 单独列出识别不清或需要人工确认的内容
```

推荐输出：

```text theme={null}
## 项目计划
## 任务清单
## 风险与依赖
## 待确认事项
```

## 图表转数据

适合处理报告截图、仪表盘截图、柱状图、折线图、饼图等。目标是把图表内容转成结构化数据，并保留不确定性。

```text theme={null}
请从这张图表中提取数据，并按 JSON 返回：
{
  "chart_type": "",
  "title": "",
  "x_axis": "",
  "y_axis": "",
  "series": [
    {
      "name": "",
      "points": [
        {"label": "", "value": null, "confidence": "high|medium|low"}
      ]
    }
  ],
  "insights": [],
  "uncertain_fields": []
}

要求：
- 如果数值只能估算，请把 confidence 标为 low 或 medium
- 不要编造图中没有的信息
- 如果坐标轴、单位或图例看不清，请写入 uncertain_fields
```

<Note>
  图表截图中的数值可能受分辨率、压缩和坐标轴比例影响。需要精确计算时，应优先使用原始数据源；模型提取结果适合作为初稿或人工录入辅助。
</Note>

## 票据转表格

适合处理收据、发票、报销单、购物小票等。目标是转成可直接写入表格的行数据，便于复制进表格或继续写入系统。

```text theme={null}
请从这张票据图片中提取结构化信息，按 JSON 返回：
{
  "merchant": "",
  "date": "",
  "currency": "",
  "total_amount": null,
  "tax_amount": null,
  "items": [
    {
      "name": "",
      "quantity": null,
      "unit_price": null,
      "amount": null
    }
  ],
  "payment_method": "",
  "uncertain_fields": []
}

要求：
- 金额必须来自票据画面，不要自行推断
- 看不清的字段填 null，并写入 uncertain_fields
- 保留原始币种和日期格式
```

如果你希望直接粘贴到电子表格，可以让模型改成 CSV：

```text theme={null}
请把票据中的明细输出为 CSV，列为：
merchant,date,item_name,quantity,unit_price,amount,currency,confidence
```

## 截图生成代码

适合处理网页、移动端界面、组件截图和设计稿截图。目标是得到可继续修改的 HTML / React / Tailwind 初稿。

```text theme={null}
这是一张网页界面截图。请用 React + Tailwind CSS 复刻这个页面。

要求：
1. 先描述页面结构、布局和主要视觉元素
2. 再给出可运行的 React 组件代码
3. 使用语义化命名，不要依赖截图中的真实品牌资产
4. 对无法确认的图片或图标，用占位元素表示
5. 保持移动端和桌面端都有合理布局
```

<Tip>
  如果截图里包含大量文字，建议先让模型做一次“页面结构分析”，再让它生成代码。这样更容易减少布局遗漏。
</Tip>

## 录屏问题诊断

适合处理软件操作录屏、Bug 复现视频、App 使用路径、客服排障录屏等。目标是让模型还原用户动作、定位异常点并给出排查建议。

```text theme={null}
这是一个软件操作录屏。请分析：
1. 用户按时间顺序做了哪些操作
2. 哪一步开始出现异常
3. 异常表现是什么
4. 可能原因有哪些，请按可能性排序
5. 给出排查步骤和建议修复方向

请按 Markdown 输出，并把无法确认的内容单独列为“需要补充的信息”。
```

推荐输出：

```text theme={null}
## 操作时间线
## 异常点
## 可能原因
## 排查步骤
## 需要补充的信息
```

## 多图对比

适合比较设计改版前后、商品图片差异、截图中的 UI 状态差异、文档扫描页差异等。

```text theme={null}
请比较这几张图片，输出：
1. 相同点
2. 差异点，按视觉布局、文字内容、数据数值、状态变化分类
3. 可能影响
4. 需要人工复核的差异

如果某个差异无法确认，请明确说明原因，不要猜测。
```

## 结构化输出建议

当你需要把结果接入程序或表格时，建议显式要求 JSON 或 CSV，并说明空值策略：

```text theme={null}
请只返回合法 JSON，不要返回 Markdown。
如果字段无法从图片中确认，请填 null。
如果存在识别不确定的字段，请把字段名和原因写入 uncertain_fields。
```

如果下游程序需要稳定解析 JSON，可以配合 `response_format` 开启 JSON Mode。具体用法见 [JSON Mode 使用建议](/zh/guides/developer/json-mode) 和 [Chat Completions API](/zh/api-reference/chat/chat-completion-create#请求参数)。

对于需要人工复核的任务，可以让模型同时给出 `confidence`：

```json theme={null}
{
  "field": "total_amount",
  "value": 128.5,
  "confidence": "medium",
  "evidence": "票据底部 Total 一行"
}
```

## 下一步

<Columns cols={3}>
  <Card title="多模态快速上手" href="/zh/guides/models/step-3.7-flash-quickstart">
    学习图片、视频、Base64 和 Files API 的基础调用方式。
  </Card>

  <Card title="Chat Completions API" href="/zh/api-reference/chat/chat-completion-create">
    查看 `messages`、`image_url`、`video_url`、`reasoning_effort` 等参数。
  </Card>

  <Card title="手机操作 Agent" href="/zh/guides/models/step-3.7-flash-mobile-agent">
    通过 GELab-Zero 连接 Android 真机，让模型规划手机操作。
  </Card>
</Columns>
