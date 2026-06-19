<!-- title: 计费介绍 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/pricing/intro.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 计费介绍

## 计费概念

### 计费单元

Token：代表常见的字符序列，是模型表示自然语言文本的基本单位，单个 Token 可以是1个中文词语、1个中文短语或者是1个英文单词。
一般来说，对于一段通用的中文文本，Token 和字数的换算比例大约为1:1.6，实际处理 Token 数量以模型调用返回为准，可从返回结果的 `usage` 中的 `prompt_tokens`、`completion_tokens` 和 `total_tokens` 分别获取相应的 Token 统计。

## 计费策略

### 计费逻辑

我们会根据模型的输入和输出的总 Token 数实行按量计费，如果使用了多模态大模型，我们会按照图片的数量进行按每个图片400Token 消耗进行核算，最终按 Token 的总用量进行计费。
费用扣减的方式是通过 Token 使用量 x 模型单价 计算扣减费用，按顺序从赠送账户和充值账户进行扣减。赠送金额会存在过期时间，建议用户按需尽快使用。

### 限速逻辑

速率限制是 API 的常见做法，实施速率限制有以下几个不同考量：

* 有助于防止 API 被滥用或误用。例如，恶意行为者可能会向 API 发送大量请求，以尝试使 API 服务过载或导致服务中断。通过设置速率限制，可以一定程度防范这种行为。
* 速率限制有助于确保每个人都能公平地访问 API。如果一个人或组织发出过多请求，可能会使 API 对其他人的使用变得缓慢。通过限制单个用户可以发出的请求数量，我们可以确保大多数人有机会使用 API，而不会遇到响应过慢问题。
* 速率限制可以帮助我们管理基础设施的总体负载。如果对 API 的请求数量急剧增加，可能会使服务器负担过载并导致性能问题。通过设置速率限制，我们可以帮助为所有用户保持平稳和一致的体验。
