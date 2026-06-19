<!-- title: Prompt 缓存最佳实践 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/prompt-cache.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt 缓存最佳实践

在开发大模型的多轮对话和固定场景人设问答时，会将用户的输入和大模型的回答构建成对话历史传递在整个对话中，而随着对话轮次增加，整个对话过程中的重复内容也会逐渐增多。

阶跃星辰为开发者提供了上下文缓存技术，将每次请求过程中的输入进行缓存，当开发者重复请求时，将会自动命中缓存，帮助开发者提升推理速度（在特定场景，推理首字速度最大可提升90%），降低推理成本。**目前缓存部分的 Token 按照 Cache 部分 Token 在对应模型的费用的 20% 的费用进行计费。**

## 缓存支持模型

目前 `step-3.7-flash`、`step-3.5-flash`、`step-3.5-flash-2603`、`step-1o-turbo-vision` 等模型支持 Prompt 缓存，其他模型暂时不支持 Prompt 缓存。

## Prompt 缓存的基础原理

当请求超过 256 个 Token 时，缓存会自动启用。当你发起一次 API 请求时，会执行如下操作：

1. **缓存查询**：根据你的请求的 Prompt 的前缀，查询当前的 Prompt 是否有系统的缓存。

2. **缓存命中**：如果命中系统的缓存，系统将会使用缓存，并加上本次请求中缓存不包含的内容，进行推理。

3. **缓存未命中**：如果未命中系统的缓存，系统将会进行正常的推理并在处理完成后，将 Prompt 前缀进行缓存，以供下次请求使用。

在包含多 Example、多轮次对话、长上下文或背景信息的场景下，缓存命中率会更高，帮助开发者提升系统整体性能，优化成本。

缓存淘汰采用最近最少使用（LRU）策略，在系统请求高峰期，不使用的缓存会更容易被逐出；在系统请求低峰期，缓存则会拥有更长的生命周期。

## 如何判断自己是否使用了 Prompt 缓存

在调用 Chat API 进行补全时，如果 response.usage 存在 cached\_token 字段，则表明该请求命中缓存，而 cached\_token 的值即为具体命中的 Token 的长度。

```json theme={null}
{
    "id": "22ebae159c8f10c8657253671c8f7f17.6de8d4f65f5ba3dddeb693a1aa83de1e",
    "object": "chat.completion",
    "created": 1730963954,
    "model": "step-1o-turbo-vision",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "xxx"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "cached_tokens": 512,
        "prompt_tokens": 591,
        "completion_tokens": 120,
        "total_tokens": 711
    }
}
```

以上面这个请求结果为例，在未启用缓存的请求下，计费输入 token 为 591 ，而在启用缓存后，计费输入 Token 为 591 - 512 = 79 Token，启用缓存帮助用户直接降低了  88% 的 Input Token 消耗。

## 什么样的内容会进入缓存

在进行缓存时，**会以 256 个 Token 作为最小单元开始进行缓存**，当你的 Prompt 长度少于 256 个 Token 时，将不会命中缓存。

具体可缓存的信息会包含如下内容：

* **对话信息**：完整的对话数组会进入到缓存系统当中，其中包含 System Prompt、User Message 以及 Assistant Message。

* **图片信息**：用户消息中包含的图片信息也会进入缓存当中，但需要保证前后使用的是相同的图片。

* **视频信息**：用户消息中包含的视频信息也会进入缓存当中，但需要保证前后使用的是相同的视频。

* **工具调用信息及其结果**：对话信息中的工具调用信息及其调用结果也会参与到缓存当中。

## Prompt 缓存最佳实践

* 在 Prompt 的开头使用静态或者重复的内容，而在整个 Prompt 结尾防止动态的内容；
* 监控不同 Prompt 的 Cached Token 和 Prompt Token 的比重、延迟、命中率，来优化 Prompt 结构；
* 近期未使用的缓存会被系统逐出，因此，尽可能保持 Prompt 前缀的稳定，以获得更高的缓存命中率。
* 对于较长的 Prompt，可以放在系统流量非高峰期进行，以减少缓存被逐出的次数，获得更高的缓存命中率。

## 如何对缓存进行排查

如果你的请求没有按照你的预期进行缓存，你可以按照如下的思路进行排查：

1. 确保缓存的部分在每次调用过程中都始终保持一致；
2. 检查是否两次请求间隔时间太长，以避免缓存失效；
3. 验证是否提供了至少 256个 Token 作为输入。

## 常见问题

### 缓存是否影响模型的推理的效果？

缓存不会影响模型的推理效果，每次生成都会使用完整的 Prompt 进行推理。

### 我是否需要为 Prompt 缓存额外付费？

Prompt Cache 功能将会对 Cache 到的部分进行减免，按照 Cache 部分 Token 在对应模型的费用的 20% 的费用进行计费。

### 我是否可以手动清除 Prompt 缓存？

目前不提供手动清除缓存的能力。你可以通过修改 Prompt 来使请求不命中缓存；

### 我是否可以让我的请求始终命中缓存？

目前我们不提供保证始终命中的 Prompt 缓存，如果你有相关诉求，可以通过联系我们和我们取得联系，确认你的场景和问题。
