<!-- title: 从 OpenAI 迁移至阶跃星辰 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/openai.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 从 OpenAI 迁移至阶跃星辰

## 前提条件

阶跃星辰大模型支持个人和企业调用，你可以在开放平台后台创建 API Key，并使用 API Key 调用。在测试模型能力时，除了通过 API 调用，你也可以通过体验中心快速体验阶跃星辰大模型。

> 在测试完成后， 你可以通过[联系我们](/zh/guides/contact-us)联系阶跃星辰客服，我们将会为你提供和 OpenAI 对标的 TPM / RPM 限制，帮助你无缝迁移调用。

## 模型选择

阶跃星辰为开发者提供多种模型能力，你可以根据自己当前使用的模型，切换至阶跃星辰大模型。

### 推理与多模态模型

* `step-3.7-flash`：旗舰多模态推理模型，原生支持图片和视频理解，支持三档推理强度（low/medium/high），适合智能体、代码与多模态场景。
* `step-3.5-flash`：旗舰语言推理模型，顶尖推理能力与快速可靠的执行能力，适合逻辑推理、数学、软件工程、深度研究等复杂任务。

### 文生图模型

* `step-image-edit-2`：文生图与图像编辑一体化模型，单次编辑任务仅需 1-2 秒。

## API 兼容

目前，阶跃星辰大模型兼容 OpenAI 的 API 规范，你可以直接使用 OpenAI 的 SDK 进行调用，如果你的应用已经在使用 OpenAI SDK 开发，那么可以以极低的成本进行迁移。

目前我们与 OpenAI 兼容的 API 如下：

* [Chat Completion](/zh/api-reference/chat/chat-completion-create)
* [上传文件](/zh/api-reference/files/create)
* [获取文件列表](/zh/api-reference/files/list)
* [获取文件信息](/zh/api-reference/files/retrieve)
* [获取文件内容](/zh/api-reference/files/retrieve-content)
* [删除文件](/zh/api-reference/files/delete)
* [获取模型列表](/zh/api-reference/models/list)
* [查询单个模型信息](/zh/api-reference/models/retrieve)
* [生成图片](/zh/api-reference/images/image)

## SDK 迁移指南

### OpenAI Python SDK

从 OpenAI Python SDK 迁移时，你只需要将原本的 Client 初始化中的参数 `api_key` 替换为阶跃星辰的 API Key ，并新增 `base_url` 设置为 `https://api.stepfun.com/v1`，并在具体的模型设置中，设置为阶跃星辰大模型即可完成调用。

```python copy theme={null}
# 修改前
client = OpenAI(
    api_key="OPENAI_KEY"
)

# 修改后
client = OpenAI(
    api_key="STEP_API_KEY",
    base_url="https://api.stepfun.com/v1"
)
```

### OpenAI TypeScript SDK

从 OpenAI TypeScript SDK 迁移时，你只需要将原本的 Client 初始化中的参数 `api_key` 替换为阶跃星辰的 API Key ，并新增 `base_url` 设置为 `https://api.stepfun.com/v1`，并在具体的模型设置中，设置为阶跃星辰大模型即可完成调用。

```typescript copy theme={null}
// 修改前
const openai = new OpenAI({
	apiKey: 'OPENAI_KEY',
})

// 修改后
const openai = new OpenAI({
	apiKey: 'STEP_API_KEY',
	baseURL: 'https://api.stepfun.com/v1',
})
```

### LangChain

在使用 Langchain 开发应用时，你只需要修改 ChatOpenAI 初始化时的 `openai_api_key`、`openai_api_base` 和 `model_name` ，即可切换至阶跃星辰大模型。

```python copy theme={null}
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from os import getenv
from dotenv import load_dotenv

load_dotenv()

template = """你是阶跃星辰大模型开发的智能助手，你会根据用户的问题，一步一步的思考并回答。用户的问题是：问题：{question}"""

prompt = PromptTemplate(template=template, input_variables=["question"])

# 修改前
# llm = ChatOpenAI(
#   openai_api_key=getenv("OPENAI_KEY"),
#   model_name="gpt-4o"
# )

# 修改后
llm = ChatOpenAI(
  openai_api_key=getenv("STEP_API_KEY"),
  openai_api_base="https://api.stepfun.com/v1",
  model_name="step-3.7-flash"
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "阶跃星辰大模型如何帮助企业员工提升效率"

print(llm_chain.run(question))
```

### LangChain.js

在使用 Langchain.js 开发应用时，你只需要修改 ChatOpenAI 初始化时的 modelName、openAIApiKey 和 basePath ，即可切换至阶跃星辰大模型。

```typescript theme={null}
// 修改前
const chat = new ChatOpenAI({
	modelName: 'gpt-4o',
	openAIApiKey: $OPENAI_KEY,
})

// 修改后

const chat = new ChatOpenAI(
	{
		modelName: 'step-3.7-flash',
		openAIApiKey: $STEP_API_KEY,
	},
	{
		basePath: 'https://api.stepfun.com/v1',
	},
)
```
