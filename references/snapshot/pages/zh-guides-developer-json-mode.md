<!-- title: JSON Mode 使用建议 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/json-mode.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON Mode 使用建议

除了应用在用户的日常对话外， 阶跃星辰大模型还可以用于和应用自身的逻辑代码进行一些操作，来实现自然语言到应用逻辑的转化。
比如，你可以使用大模型来实现用户评论内容的情绪判断、使用大模型来实现内容评分等功能。你可以通过 Prompt Engineering 的方式，来让大模型返回特定格式的内容并进行解析。阶跃星辰为开发者提供了 JSON Mode 的支持，帮助开发者获取到可以解析的 JSON 数据，更加容易与系统进行集成。

### 使用方法

在使用 JSON Mode 时，你需要做三件事：

1. 在 System Prompt 中，放置你预期大模型给出的输出的 JSON 的结构和说明（推荐使用 JSON Schema 的结构描述，帮助大模型理解）。
2. 请求时，设置 response\_format 为 `{ "type": "json_object" }`，从而来让大模型返回可解析的 JSON 结果。
3. 解析大模型返回的结果，并验证是否符合预期。符合预期后即可使用在业务系统中对接。

### 参考代码

以使用大模型进行评论的情感分析为例子，你可以通过参考如下代码，让大模型返回 JSON 结果。

```python theme={null}
from openai import OpenAI

# 初始化 阶跃星辰 Client
STEPFUN_KEY = ""

client = OpenAI(
    base_url="https://api.stepfun.com/v1",
    api_key=STEPFUN_KEY
)

# 在 System Prompt 中定义返回结果
system_prompt = """
你是一个评论分析师，会根据用户的输入，分析用户输入的情感，并给出评论的情感分析结果
## 分析规则
1. 如果用户的评论中包含了负面情感词汇，那么情感分析结果为 negative
2. 如果用户的评论中包含了正面情感词汇，那么情感分析结果为 positive
3. 如果用户的评论中没有包含正面或者负面情感词汇，那么情感分析结果为 neutral
## 正面情感词汇
- 好
- 棒
- 优秀
## 负面情感词汇
- 差
- 糟糕
- 糟
## 例子
### 例子 1
#### 输入内容
"这个产品真的很好，我很喜欢"
####  输出内容
{  
    "emotion": "positive",
    "score": 0.9.
    "reason": "用户评论中包含了正面情感词汇"
}
### 例子 2
#### 输入内容
"这个产品好垃圾，我很讨厌"
####  输出内容
{  
    "emotion": "negative",
    "score": 0.9,
    "reason": "用户评论中包含了负面情感词汇"
}
## 输入内容
用户的评论文本
## 输出内容
按照如下结构输出 JSON 结果

class Response:
    emotion: str # 用户评论的情感分析结果，可选项为 positive, negative, neutral
    score: float # 用户评论的情感分析得分，范围为 0 到 1 之间
    reason: str # 用户评论的情感分析结果的原因

"""

response = client.chat.completions.create(
  model="step-3.7-flash",
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "这个产品还行？"}
  ],
  response_format={ "type": "json_object" },
)

print(response)
```

### 引入 JSON Schema 帮助模型返回预期的 JSON 结构

在使用 JSON Mode 时，有些时候模型会返回一些不符合我们预期的内容，为了帮助模型更好的理解我们的预期，我们可以使用 JSON Schema 来帮助模型理解我们的预期。

> JSON Schema 是用于验证 JSON 数据结构的强大工具，可以帮助我们定义 JSON 数据的结构，从而帮助模型更好的理解我们的预期。

你可以通过使用 JSON Schema 定义返回体结构需要哪些字段、每个字段的含义、取值范围等，比如如下一段 Schema 定义了一个用户输入解析的 Object 结构，这个结构当中包含两个属性 url 和 notes，并声明了 url 和 notes 都是模型必返回的选项。

```json theme={null}
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "用户输入解析",
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
     "description":"用户输入的 URL"
    },
    "notes": {
      "type": "string",
 "description":"用户对于输入的 URL 的评价"
    }
  },
  "required": [
    "url",
    "notes"
  ]
}
```

在你的 Prompt 当中加入 JSON Schema，并开启 JSON Mode 返回，可以让大模型更加精准的以你想要的 JSON 结构返回内容：

```markdown theme={null}
你是一个专业的文本处理工程师，会根据用户的输入，从中提取 URL 和 用户的评价内容，并以 JSON 的方式返回。

## 约束

- 你会以下方的 JSON Schema 的格式返回给用户

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "用户输入解析",
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
     "description":"用户输入的 URL"
    },
    "notes": {
      "type": "string",
 "description":"用户对于输入的 URL 的评价"
    }
  },
  "required": [
    "url",
    "notes"
  ]
}
```

### 注意事项

* 在使用 JSON Mode 时，你需要检查返回结果的 finish\_reason 是否为 stop。如 finish\_reason 为 length，则是大模型因为受到 max\_token 的限制导致无法完整返回内容，所返回的 Message 可能无法被正常解析。
* 在使用 JSON Mode 时，可以通过在 Prompt 中加入输入和输出的范例，来帮助大模型理解你的场景和需求，给出更加符合预期的输出。
