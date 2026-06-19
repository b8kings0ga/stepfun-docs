<!-- title: 推理模型最佳实践 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/reasoning.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 推理模型最佳实践

阶跃星辰为开发者提供了多款推理模型，覆盖文本推理、多模态理解、Agent 和代码分析等场景。推荐优先使用 `step-3.7-flash`；如需纯文本推理，也可以使用 `step-3.5-flash`。

`step-3.7-flash` 是阶跃星辰的旗舰多模态推理模型。在 `step-3.5-flash` 的高速推理与工具调用能力基础上，新增原生图片和视频理解能力，支持三档推理强度，适合 Agent、代码、多模态分析和复杂规划任务。

`step-3.5-flash` 是阶跃星辰最强大的开源基座模型。它专为极致效率而生，具备前沿的推理能力和卓越的智能体（Agent）性能。该模型基于稀疏混合专家（MoE）架构，尽管拥有 1960 亿参数，但处理每个 Token 时仅需选择性激活 110 亿参数。这种极高的“智能密度”使其推理深度足以媲美顶级闭源模型，同时兼顾了实时交互所需的敏捷响应速度。

## 推理强度控制

支持三档推理强度的模型可通过参数控制思考深度。Chat Completion API 使用 `reasoning_effort`；Messages API 使用 `output_config.effort`。

| 推理强度     | 适用场景              |
| :------- | :---------------- |
| `low`    | 简单问答、摘要、改写、信息抽取   |
| `medium` | 默认推荐，适合一般推理和多步骤任务 |
| `high`   | 复杂推理、数学、规划、代码分析   |

<Info>
  完整调用示例见 [Step 3.7 Flash 快速上手](/zh/guides/models/step-3.7-flash-quickstart#控制推理强度)。参数字段说明见 [Chat Completion API](/zh/api-reference/chat/chat-completion-create#请求参数) 和 [Messages API](/zh/api-reference/chat/messages-create#请求参数)。
</Info>

## 文本推理调用示例

推理模型的文本对话调用方式基本一致。以下以纯文本场景常用的 `step-3.5-flash` 为例，构建一个流式对话。

```python theme={null}
import time
from openai import OpenAI

# Set your API Key and Base URL
BASE_URL = "https://api.stepfun.com/v1"
STEP_API_KEY = "YOUR_STEPFUN_API_KEY"

# Select Model
COMPLETION_MODEL = "step-3.5-flash"

# User Prompt
user_prompt = "How many 'r's are in the word strawberry?"

client = OpenAI(api_key=STEP_API_KEY, base_url=BASE_URL)

time_start = time.time()

try:
    response = client.chat.completions.create(
        model=COMPLETION_MODEL,
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        stream=True
    )
except Exception as e:
    print("Exception occurred when requesting API:", e)
    exit(1)

print("Reasoning Process:")
try:
    for chunk in response:
        # Check for reasoning content
        if hasattr(chunk.choices[0].delta, 'reasoning') and chunk.choices[0].delta.reasoning:
             print(chunk.choices[0].delta.reasoning, end='', flush=True)
        # Check for standard content
        elif chunk.choices[0].delta.content:
             print(chunk.choices[0].delta.content, end='', flush=True)

except Exception as e:
    print("\nError occurred while processing streaming results:", e)

time_end = time.time()
print(f"\n\nTotal generation time: {time_end - time_start:.2f} seconds")
```

## 多模态图片理解示例

以下使用最简单的代码实现 `step-3.7-flash` 对图片进行分析。推理强度（`reasoning_effort`）等参数详见 [Step 3.7 Flash 快速上手](/zh/guides/models/step-3.7-flash-quickstart)。

```python copy theme={null}
import time
import base64
from openai import OpenAI

BASE_URL,STEP_API_KEY = "https://api.stepfun.com/v1", "YOUR_STEPFUN_APIKEY"

# 选择模型
COMPLETION_MODEL = "step-3.7-flash"

# 用户问题提示
user_prompt = "帮我看看这是什么菜，如何制作？"

# 将本地图片转换为 base64 字符串
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string.decode('utf-8')

# 注意提供准确的图片路径
image_path1 = "./宫保鸡丁.png"
bstring1 = image_to_base64(image_path1)

# 构造消息，依靠模型自主深度思考
messages = [
    {"role": "user", "content": [
        {"type": "image_url", "image_url": {"url": f"data:image/jpg;base64,{bstring1}", "detail": "high"}},
        {"type": "text", "text": user_prompt}
    ]}
]

time_start = time.time()

client = OpenAI(api_key=STEP_API_KEY, base_url=BASE_URL)
try:
    response = client.chat.completions.create(
        model=COMPLETION_MODEL,
        messages=messages,
        stream=True
    )
except Exception as e:
    print("请求 API 时发生异常:", e)
    exit(1)

try:
    for chunk in response:
        # 你可以在这里获取到补全的内容，并判断是否是 reaonsing 内容。
        print(chunk)
except Exception as e:
    print("处理流式结果时发生错误:", e)

time_end = time.time()
print(f"\n总生成时间: {time_end - time_start:.2f}秒")
```

输入参数详情可以参考[Chat Completion 文档](/zh/api-reference/chat/chat-completion-create#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0)

**输出示例**

```python theme={null}
ChatCompletionChunk(id='f41b47b291e690d3659f6d8c01a6b0a8.20f353f807a52a5f3252692a22d49568', choices=[Choice(delta=ChoiceDelta(content='', function_call=None, refusal=None, role='assistant', tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1744290861, model='step-3.7-flash', object='chat.completion.chunk', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=0, prompt_tokens=701, total_tokens=701, completion_tokens_details=None, prompt_tokens_details=None), agent='')
ChatCompletionChunk(id='f41b47b291e690d3659f6d8c01a6b0a8.20f353f807a52a5f3252692a22d49568', choices=[Choice(delta=ChoiceDelta(content='', function_call=None, refusal=None, role='assistant', tool_calls=None, reasoning='\n'), finish_reason=None, index=0, logprobs=None)], created=1744290861, model='step-3.7-flash', object='chat.completion.chunk', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=1, prompt_tokens=701, total_tokens=702, completion_tokens_details=None, prompt_tokens_details=None), agent='')
ChatCompletionChunk(id='f41b47b291e690d3659f6d8c01a6b0a8.20f353f807a52a5f3252692a22d49568', choices=[Choice(delta=ChoiceDelta(content='', function_call=None, refusal=None, role='assistant', tool_calls=None, reasoning='好的'), finish_reason=None, index=0, logprobs=None)], created=1744290861, model='step-3.7-flash', object='chat.completion.chunk', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=2, prompt_tokens=701, total_tokens=703, completion_tokens_details=None, prompt_tokens_details=None), agent='')
。。。
ChatCompletionChunk(id='f41b47b291e690d3659f6d8c01a6b0a8.20f353f807a52a5f3252692a22d49568', choices=[Choice(delta=ChoiceDelta(content='！', function_call=None, refusal=None, role='assistant', tool_calls=None), finish_reason=None, index=0, logprobs=None)], created=1744290861, model='step-3.7-flash', object='chat.completion.chunk', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=1031, prompt_tokens=701, total_tokens=1732, completion_tokens_details=None, prompt_tokens_details=None), agent='')
ChatCompletionChunk(id='f41b47b291e690d3659f6d8c01a6b0a8.20f353f807a52a5f3252692a22d49568', choices=[Choice(delta=ChoiceDelta(content='', function_call=None, refusal=None, role='assistant', tool_calls=None), finish_reason='stop', index=0, logprobs=None)], created=1744290861, model='step-3.7-flash', object='chat.completion.chunk', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=1032, prompt_tokens=701, total_tokens=1733, completion_tokens_details=None, prompt_tokens_details=None), agent='')
```

响应体字段说明请参考 [Chat Completions API 的流式响应说明](/zh/api-reference/chat/chat-completion-create#流式响应)。

## 获取 Reasoning 内容

阶跃星辰的推理大模型在处理复杂问题时，会在输出中包含 reasoning 字段，展示模型的思考过程。开发者可以通过判断该字段是否存在来获取模型的思考信息。

```python theme={null}
if chunk.choices[0].delta.reasoning:
    reasoning = chunk.choices[0].delta.reasoning
    print("模型思考过程:", reasoning)
```

对于非流式场景可以直接提取 reasoning 字段，获取模型的思考过程。

```python theme={null}
msg  = completion.choices[0].message.content
reasoning = completion.choices[0].message.reasoning
```

### 通过 `reasoning_content` 字段，获取模型的思考过程。

如果你目前使用的推理模型中已经使用 `reasoning_content` 字段，可以继续使用该字段。阶跃星辰的推理模型也支持这一字段，开发者可以根据自己的需求选择使用。

只需要在请求时传入 `reasoning_format="deepseek-style"` 即可。（如使用 OpenAI SDK，则需要通过 `extra_body` 字段传入）

## 多模态模型使用注意事项

* **深度思考优势**：模型在接收到图片及文字提示后，会首先经过内部思考（reasoning）再输出最终结果。这一过程有助于完成复杂的关联和因果推理，但可能会使响应时间略有延迟，应据此考虑超时设置。
* **图片数据格式**：确保传入的图片数据使用正确的 Base64 编码格式，并按照 API 要求指定图片类型（如 JPG/JPEG、PNG、静态 GIF、WebP 等）和细节参数，保证推理的准确性。详见[文档](/zh/guides/models/vision#关键术语)
* **错误处理与日志记录**：在输出时已加入 Trace ID，若遇到模型推理问题，可将此 ID 反馈给我们。

## 智能路由（Step Plan 专属）

`step-router-v1` 是阶跃星辰为 Step Plan 通道提供的智能路由模型，按请求特征自动在 `deepseek-v4-pro` 与 `step-3.5-flash` 之间切换，让复杂决策走 Pro、高频执行走 Flash。详细使用方式与最佳实践见 [Step Router V1 智能路由开发指南](/zh/guides/developer/step-router)。
