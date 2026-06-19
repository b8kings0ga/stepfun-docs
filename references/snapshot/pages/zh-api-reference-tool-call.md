<!-- title: 工具调用 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/tool-call.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 工具调用

Toolcall（或叫 Function Calling）是阶跃星辰开放平台提供的一项高级功能，它使模型能够根据用户的需求，智能地选择并调用合适的外部工具或函数来完成特定的任务。通过 Toolcall API，开发者可以扩展模型的能力，使其能够处理更广泛的应用场景，并提供更丰富的功能和服务。下面是一个简单的工具调用的请求 JSON 例子, 在这个对象中，必须包含三个关键参数：

```json theme={null}
{
	"model": "step-3.5-flash",
	"messages": [
		{
			"role": "user",
			"content": "小跃跃，你能为我计算 (80 + 20) / 5 吗？"
		}
	],
	"tools": [
		{
			"type": "function",
			"function": {
				"name": "Calculator",
				"description": "这个阶跃星辰开放平台 API 提供基本的算术运算：加法、减法、乘法和除法。",
				"parameters": {
					"type": "object",
					"properties": {
						"formula": {
							"type": "string",
							"description": "需要计算的公式。仅支持整数。有效的运算符包括 +、-、*、/ 和括号。例如，(1 + 2) * 3。"
						}
					}
				}
			}
		}
	]
}
```

## model，模型名称

以下模型支持工具调用，推荐优先使用第一档：

**推荐**

* `step-3.7-flash`、`step-3.5-flash`、`step-3.5-flash-2603`

**仅 Step Plan 通道**

* `step-router-v1`（详见 [Step Plan 推理模型接入](/zh/step-plan/integrations/reasoning-api)）

**其他兼容**

* `step-1o-turbo-vision`

## 官方工具列表

以下是由阶跃星辰支持的官方工具，仅需配置即可实现相关能力：

* [互联网搜索](/zh/guides/developer/web-search)：调用搜索引擎，获取互联网上的最新信息。
* [知识库搜索](/zh/guides/developer/retrieval)：上传文本到知识库中，并完成对知识库内容的搜索，帮助大模型消除幻觉

## tools，工具函数列表

通过 `tools` 参数告知模型本地支持的函数列表。每个成员对象包含 `type` 和 `function` 两个字段：`type` 当前仅支持 `function`，`function` 对象包含 `name`、`description` 和 `parameters`。函数数量建议控制在合理规模，过多的函数定义会消耗较多 prompt token，并可能降低模型的命中准确率。

* **name**（函数名称）：建议使用英文字母、数字、下划线与连字符，遵循正则 `^[a-zA-Z_][a-zA-Z0-9_-]{0,63}$`，长度不超过 64 字符。使用语义化的英文名更易被模型识别。
* **description**（功能介绍）：支持中英文，用于告诉模型此函数的用途与适用场景，便于模型判断何时调用。描述越清晰，模型命中越准确。
* **parameters**（参数定义）：根节点 `type` 必须为 `object`；`properties` 内每个字段按 [JSON Schema](https://json-schema.org/understanding-json-schema/reference/type) 规范描述其 `type` 和 `description`。若参数必填，请在 `required` 数组中列出。

## messages，上下文消息体

请求消息体结构参考 [Chat Completion 请求参数](/zh/api-reference/chat/chat-completion-create#请求参数)。当模型返回 `tool_calls` 后，开发者在本地执行对应函数，再通过 `role: "tool"` 的消息（携带 `tool_call_id`）将结果回传至下一轮请求，模型据此生成最终回答。

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    completion = client.chat.completions.create(
        model="step-3.5-flash",
        messages=[
            {
                "role": "user",
                "content": "你能为我计算(80 + 20) / 5 吗？"
            }
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "Calculator",
                    "description": "这个阶跃星辰开放平台API提供基本的算术运算：加法、减法、乘法和除法。",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "formula": {
                                "type": "string",
                                "description": "需要计算的公式。仅支持整数。有效的运算符包括+、-、*、/和括号。例如，'(1 + 2) * 3'。"
                            }
                        }
                    }
                }
            }
        ]
    )

    print(completion)
    ```
  </Tab>

  <Tab title="js">
    ```js theme={null}
    import OpenAI from "openai";

    const openai = new OpenAI({
        apiKey: "STEP_API_KEY",
        baseURL: "https://api.stepfun.com/v1"
    });

    async function main() {
        const completion = await openai.chat.completions.create({
            model: "step-3.5-flash",
            messages: [
                {
                    "role": "user",
                    "content": "你能为我计算(80 + 20) / 5 吗？"
                }
            ],
            tools: [
                {
                    "type": "function",
                    "function": {
                        "name": "Calculator",
                        "description": "这个阶跃星辰开放平台API提供基本的算术运算：加法、减法、乘法和除法。",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "formula": {
                                    "type": "string",
                                    "description": "需要计算的公式。仅支持整数。有效的运算符包括+、-、*、/和括号。例如，'(1 + 2) * 3'。"
                                }
                            }
                        }
                    }
                }
            ]
        });

        console.log(JSON.stringify(completion));
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-3.5-flash",
        "messages": [
          {
            "role": "user",
            "content": "你能为我计算(80 + 20) / 5 吗？"
          }
        ],
        "tools": [
          {
            "type": "function",
            "function": {
              "name": "Calculator",
              "description": "这个阶跃星辰开放平台API提供基本的算术运算：加法、减法、乘法和除法。",
              "parameters": {
                "type": "object",
                "properties": {
                  "formula": {
                    "type": "string",
                    "description": "需要计算的公式。仅支持整数。有效的运算符包括+、-、*、/和括号。例如: (1 + 2) * 3。"
                  }
                }
              }
            }
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "b7b56af0-52a6-483f-a589-948182676a1b",
  "object": "chat.completion",
  "created": 1717744611,
  "model": "step-3.5-flash",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "",
        "tool_calls": [
          {
            "id": "call_ybVBO_JASgipgJH8xWbhKg",
            "type": "function",
            "function": {
              "name": "Calculator",
              "arguments": "{\"formula\": \"(80 + 20) / 5\"}"
            }
          }
        ]
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 151,
    "completion_tokens": 25,
    "total_tokens": 176
  }
}
```
