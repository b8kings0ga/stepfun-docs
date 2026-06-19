<!-- title: 知识库使用指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/retrieval.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 知识库使用指南

RAG（检索增强生成）技术结合了大模型与知识库，通过实时检索相关信息来生成更准确、详实的回答，主要解决大模型在知识更新和特定领域专业性上的不足，确保回答内容与最新数据一致，减少“幻觉”现象。
使用 RAG 可以提升信息检索的效率和准确性，增强模型在复杂查询和专业应用中的表现，如智能客服、内容生成和决策辅助等。此外，RAG 有助于扩展模型的知识覆盖范围，提升用户体验，确保提供可靠且有针对性的解决方案，是提升大模型实用性的重要技术手段。

## 达成效果

基于自有文档创建知识库，并将其与大模型结合使用，实现检索与生成一体化的智能应用。

## 具体的步骤 & 参考代码

### 获取并整理本地知识

1. **知识选取**: 识别并提取与工作相关的非结构化知识源，包括但不限于在线网站、PDF 文档及各类问题清单。<br />
   实际操作：收集有用的需求文档，QA 等，以及打印出官网的相关信息。

2. **信息剔除**: 对所选知识源中的无关信息进行系统化剔除，确保保留下来的内容具有高度的相关性和实用性。<br />
   实际操作：剔除代码，私人信息，未经处理的口语描述等信息

3. **内容精简**: 针对重复性内容进行精简与整合，去除冗余信息，以提高知识库的有效性和可用性。 <br />
   实际操作：将相似内容教给大模型，剔除重复信息，保留精练的信息

4. **文档处理**: 对于 Excel 格式的问题清单，将内容转换为问答形式，确保信息结构化清晰；其他文档则按段落进行整理，形成描述性文字，便于后续查询与引用。<br />
   实际操作：统一将各种文档交给大模型进行优化。

### 一、上传文件

参考[文件管理接口](/zh/api-reference/files/create) API 上传文件，后续将用于录入知识库，注意： **purpose 字段的值为 retrieval**

### 二、创建知识库

创建知识库，用于后续的文件管理，你可以将一个方向的内容录入到同一个知识库中，方便后续的管理。

```python copy theme={null}
import requests

STEP_API_KEY="YOU_STEP_API_KEY"
BASE_URL = "https://api.stepfun.com/v1"
url = BASE_URL+"/vector_stores"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {STEP_API_KEY}"  # 确保 STEP_API_KEY 是定义好的变量
}
data = {
    "name": "food_calorie"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)

```

返回结果如下:

> 注意保存好知识库 ID，后续知识库关联文件，以及使用知识库，都是直接使用此 ID

```json theme={null}
{
	"id": "171215831957549056",
	"name": "food_calorie"
}
```

### 三，知识库关联文件

将文件关联到知识库中，后续就可以使用知识库 ID 进行检索，从而确保多个文件可以同时参与检索。

```python copy theme={null}
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

STEP_API_KEY="YOU_STEP_API_KEY"
BASE_URL = "https://api.stepfun.com/v1"
# 使用创建知识库时获取的ID
vector_store_id = "171215831957549056"
url = BASE_URL+"/vector_stores/"+vector_store_id+"/files"

headers = {
    "Authorization": f"Bearer {STEP_API_KEY}"  # 确保 STEP_API_KEY 是定义好的变量
}

# 准备 multipart 数据
# 使用 上传文件后获取的文件id
multipart_data = MultipartEncoder(
    fields={
        "file_ids": "file-CeAyPYz5Bg"
    }
)
# 添加 multipart content-type 到头部
headers["Content-Type"] = multipart_data.content_type

response = requests.post(url, headers=headers, data=multipart_data)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)
```

返回的报文

```json theme={null}
{
  "id": "file-CeAyPYz5Bg",
  "usage_bytes": 1405210,
  "vector_store_id": "171215831957549056"
}
```

### 四，使用知识库进行对话补全

以下是一个基于食品热量的知识库检索的案例，你可以根据自己的需求，调整问题和答案，以及知识库的内容。

```python copy theme={null}
from openai import OpenAI

STEP_API_KEY = "YOU_STEP_API_KEY"
BASE_URL = "https://api.stepfun.com/v1"

# 初始化
client = OpenAI(api_key=STEP_API_KEY, base_url=BASE_URL)
# 选择模型
COMPLETION_MODEL = "step-3.7-flash"

sys_prompt = """
你是一名食物营养成分专家。
你的任务是识别文本中的每一份食物，并根据以下分类规则预估它们的重量和热量、营养成本（碳水化合物、蛋白质、脂肪），并按「输出格式」进行最后结果的输出。
## 理解食物
1.我会给你一段文字，请识别文字中的食物
2.根据食物的名称，去检索食物的营养成分
4.如果检索后，上下文没有对应食物的营养成分，则直接在食物名称后加上「营养成分未知」，然后输出结果
## 输出格式（请仅输出以下内容，不要说任何多余的话）
1.如果检索出了食物的营养成分，则直接输出以下内容
食物名称：预计每100g的热量（大卡）,碳水化合物（g）,蛋白质（g）,脂肪（g）
2.如果没有检索出了食物的营养成分，则直接输出以下内容
食物名称：营养成分未知
"""
user_prompt = "西红柿鸡炒番茄,西冷牛排"

messages = [
    {
        "role": "system",
        "content": sys_prompt
    },
    {
        "role": "user",
        "content": user_prompt
    }
]
tools = [
    {
        "type": "retrieval",
        "function": {
            "name": "food_nutrition",
            "description": "本文档存储了食物的营养成分，包含：食物名称,预估重量（g）,热量（大卡）,碳水化合物（g）,蛋白质（g）,脂肪（g）等信息",  # 知识库的描述
            "options": {
                "vector_store_id": "171215831957549056",  # 知识库 ID
                "prompt_template": "从文档 {{knowledge}} 中找到问题 {{query}} 的答案。根据文档内容中的语句找到答案，如果文档中没用答案则告诉用户找不到相关信息；"
            }
        }
    }
]
response = client.chat.completions.create(
    messages=messages,
    model=COMPLETION_MODEL,
    tool_choice="auto",
    tools=tools,
    stream=True,
)
for chunk in response:
    print(chunk)
```

返回的报文

```json theme={null}
{
  "id": "e45108181a377f91ae197bcbf5273667.2935815498cc45d238f63de5d0eb5c9e",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "西红柿鸡炒番茄：营养成分未知\n西冷牛排：食物名称：预计每100g的热量（大卡）131,碳水化合物（g）11,蛋白质（g）10,脂肪（g）6\n",
        "role": "assistant",
        "function_call": null,
        "tool_calls": null
      }
    }
  ],
  "created": 1732516765,
  "model": "step-3.7-flash",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": null,
  "usage": {
    "completion_tokens": 80,
    "prompt_tokens": 219,
    "total_tokens": 299
  }
}
```

可以看到命中知识库后，会直接基于知识库的内容进行回复，未命中的知识库则直接说明情况（可以后续补充完善知识库）

<img src="https://mintcdn.com/stepfun/ivZhb9pOE5X12y-g/images/guide/retrieval.png?fit=max&auto=format&n=ivZhb9pOE5X12y-g&q=85&s=e9bea0f926b9213a5fa623905aa9e155" alt="" width="1844" height="338" data-path="images/guide/retrieval.png" />

## 注意事项

1. 上传文件时，`purpose` 字段必须填写为 `retrieval`。有关文件上传及管理的详细信息，请参阅[文档解析开发指南](/zh/guides/developer/doc-parser)。
2. 添加文件到知识库时，确保文件状态为 success 后，才能将其添加到知识库中。
3. 在使用知识库进行对话补全时，确保在 description 中**清晰描述知识库的内容**；并在提示语（prompt）中，将任务描述与 description 紧密结合，以提高知识库命中的概率。
