<!-- title: Responses API -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/responses/responses-create.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Responses API

调用 Responses API，获取模型生成的响应数据。该接口兼容 OpenAI Responses API 的请求与响应格式。

## 请求地址

`POST https://api.stepfun.com/v1/responses`

## 请求参数

* `model` `string` ***required***<br />需要使用的模型名称。当前仅支持 `step-3.7-flash`。
* `input` `string or object array` ***required***<br />输入内容，可以是纯文本字符串，也可以是按时序排列的消息/事件数组。

  <Expandable>
    * 纯文本输入 `string`<br />等价于一条 `role=user` 的纯文本消息。
    * 消息/事件数组 `object array`<br />数组元素可以是以下几种类型：
        <Expandable>
          * 文本消息 `object`
                <Expandable>
                  * `role` `string`<br />消息角色，可选取值：`user`、`assistant`、`system`。
                  * `content` `string or object array`<br />消息内容。可以是纯文本字符串，也可以是用于多模态输入的内容块数组。
                          <Expandable>
                            * 纯文本内容 `string`
                            * 内容块数组 `object array`
                                      <Expandable>
                                        * 文本块 `object`
                                                    <Expandable>
                                                      * `type` `string`<br />总为 `input_text`
                                                      * `text` `string`<br />文本内容
                                                    </Expandable>
                                        * 图片块 `object`
                                                    <Expandable>
                                                      * `type` `string`<br />总为 `input_image`
                                                      * `image_url` `string or object`<br />图片地址。可直接传入字符串，或传入对象 `{ "url": "...", "detail": "high" }`。推荐使用 base64 data URL（格式 `data:image/jpeg;base64,${base64_string}`），或保证外部 URL 可被服务端公网访问。
                                                    </Expandable>
                                        * 视频块 `object`
                                                    <Expandable>
                                                      * `type` `string`<br />总为 `input_video`
                                                      * `video_url` `string or object`<br />视频地址。可直接传入字符串，或传入对象 `{ "url": "...", "detail": "low" }`。视频 URL 需保证可被服务端公网访问。
                                                    </Expandable>
                                      </Expandable>
                          </Expandable>
                </Expandable>
          * 函数调用 `object`（由模型在上一轮返回，需在多轮对话中按原样回传）
                <Expandable>
                  * `type` `string`<br />总为 `function_call`
                  * `id` `string`<br />函数调用唯一 ID，由服务端生成
                  * `call_id` `string`<br />调用关联 ID，用于配对后续的 `function_call_output`
                  * `name` `string`<br />工具名称
                  * `arguments` `string`<br />JSON 字符串格式的参数
                </Expandable>
          * 函数调用结果 `object`（由客户端在执行完工具后回传）
                <Expandable>
                  * `type` `string`<br />总为 `function_call_output`
                  * `call_id` `string`<br />对应 `function_call` 的 `call_id`
                  * `output` `string`<br />工具执行结果（建议使用 JSON 字符串）
                </Expandable>
        </Expandable>
  </Expandable>

<Note>
  图片和视频 URL 必须能被服务端公网访问；如果服务端无法抓取 URL，会返回参数错误。图片输入推荐使用 base64 data URL，以避免外部 URL 鉴权、防盗链或网络访问失败。
</Note>

* `instructions` `string` ***optional***<br />顶层系统级指令。
* `stream` `bool` ***optional***<br />是否启用 SSE 流式输出，默认 `false`。
* `temperature` `float` ***optional***<br />采样温度，介于 0.0 和 2.0 之间。
* `top_p` `float` ***optional***<br />核采样参数。
* `max_output_tokens` `int` ***optional***<br />限制本次响应的最大输出 token 数。

<Note>
  `max_output_tokens` 会同时限制推理过程和最终输出。使用 `medium` / `high` 推理强度、JSON Schema、视频等复杂输入时，建议预留更大的输出预算；预算不足时响应可能返回 `status="incomplete"`，`output` 中可能只有 `reasoning` 项而没有最终 `message`。
</Note>

* `reasoning` `object` ***optional***<br />推理配置。

  <Expandable>
    * `effort` `string` ***optional***<br />推理强度档位，可选值 `low` / `medium` / `high`。
  </Expandable>

* `tools` `object array` ***optional***<br />工具定义列表。当前仅支持 `function` 类型工具。

  <Expandable>
    * `type` `string`<br />总为 `function`
    * `name` `string`<br />函数名称，建议使用纯英文、数字和 `_-` 字符
    * `description` `string` ***optional***<br />函数功能描述，用于辅助模型判断是否调用
    * `parameters` `object`<br />JSON Schema，描述函数入参
    * `strict` `boolean` ***optional***<br />是否启用严格模式，开启后模型输出参数将严格匹配 `parameters` 中的 schema
  </Expandable>

* `tool_choice` `string or object` ***optional***<br />工具调用策略。当前仅支持字符串 `"auto"`（由模型自行决定是否调用工具）。

* `text` `object` ***optional***<br />文本输出格式配置。

  <Expandable>
    * `format` `object`
        <Expandable>
          * `type` `string`<br />取值为 `text`、`json_object` 或 `json_schema`。
          * `name` `string` ***optional***<br />当 `type=json_schema` 时必填，schema 的标识名称。
          * `strict` `boolean` ***optional***<br />当 `type=json_schema` 时可用，开启后模型输出将严格匹配 schema。
          * `schema` `object` ***optional***<br />当 `type=json_schema` 时必填，遵循 [JSON Schema](https://json-schema.org/) 规范的对象。
        </Expandable>
  </Expandable>

## 响应格式

### 非流式响应

当 `stream=false`（默认）时，返回单个 Response 对象。

#### 属性

* `id` `string`<br />响应唯一 ID，格式形如 `resp_xxx`。

* `object` `string`<br />固定为 `response`。

* `created_at` `int`<br />创建时间的 Unix 时间戳（秒）。

* `completed_at` `int or null`<br />完成时间的 Unix 时间戳（秒）。

* `status` `string`<br />响应状态，取值为 `completed`、`incomplete` 或 `failed`。

* `error` `object or null`<br />错误信息，仅在 `status=failed` 时非空。

* `incomplete_details` `object or null`<br />未完成详情，仅在 `status=incomplete` 时非空，常见为 `{ "reason": "max_output_tokens" }`。

* `model` `string`<br />实际使用的模型 ID。

* `output` `object array`<br />输出项数组。元素可能为以下类型：

  <Expandable>
    * 推理项 `object`
        <Expandable>
          * `type` `string`<br />总为 `reasoning`
          * `id` `string`<br />推理项 ID
          * `status` `string or null`<br />推理项状态，流式完成时可为 `completed`
          * `summary` `object array`<br />推理摘要列表，通常为空数组
          * `content` `object or null`<br />推理内容，通常为 `null`
          * `encrypted_content` `string or null`<br />加密推理内容，通常为 `null`
        </Expandable>
    * 文本消息 `object`
        <Expandable>
          * `type` `string`<br />总为 `message`
          * `id` `string`<br />消息 ID
          * `role` `string`<br />总为 `assistant`
          * `status` `string`<br />总为 `completed`
          * `content` `object array`
                <Expandable>
                  * `type` `string`<br />总为 `output_text`
                  * `text` `string`<br />模型生成的文本内容
                  * `annotations` `object array`<br />注释列表，无注释时为空数组
                </Expandable>
        </Expandable>
    * 函数调用 `object`
        <Expandable>
          * `type` `string`<br />总为 `function_call`
          * `id` `string`<br />函数调用唯一 ID
          * `call_id` `string`<br />调用关联 ID，回传 `function_call_output` 时需带上
          * `name` `string`<br />被调用的工具名称
          * `arguments` `string`<br />JSON 字符串格式的参数
          * `status` `string`<br />总为 `completed`
        </Expandable>
  </Expandable>

* `usage` `object`<br />token 使用统计。

  <Expandable>
    * `input_tokens` `int`<br />输入 token 数
    * `input_tokens_details` `object`
        <Expandable>
          * `cached_tokens` `int`<br />命中缓存的输入 token 数
        </Expandable>
    * `output_tokens` `int`<br />输出 token 数
    * `output_tokens_details` `object`
        <Expandable>
          * `reasoning_tokens` `int`<br />其中用于推理的 token 数
          * `tool_output_tokens` `int`<br />其中用于工具输出的 token 数
        </Expandable>
    * `total_tokens` `int`<br />总 token 数
  </Expandable>

* `instructions` `string or null`<br />回显请求中的顶层指令。

* `max_output_tokens` `int or null`<br />回显请求参数。

* `reasoning` `object or null`<br />回显推理配置。

* `temperature` `float or null`<br />回显采样温度。

* `top_p` `float or null`<br />回显核采样参数。

* `text` `object`<br />回显文本输出格式配置。

  <Expandable>
    * `format` `object`
        <Expandable>
          * `type` `string`<br />取值为 `text`、`json_object` 或 `json_schema`。
          * `name` `string`<br />当 `type=json_schema` 时存在，schema 的标识名称。
          * `strict` `boolean`<br />当 `type=json_schema` 时存在。
          * `schema` `object`<br />当 `type=json_schema` 时存在，遵循 [JSON Schema](https://json-schema.org/) 规范的对象。
        </Expandable>
  </Expandable>

* `tool_choice` `string or object`<br />回显工具调用策略。

* `tools` `object array`<br />回显工具定义列表。

#### 示例

```json theme={null}
{
  "id": "resp_xxxxxxxxxxxxxxxx",
  "object": "response",
  "created_at": 1772624997,
  "completed_at": 1772624998,
  "model": "step-3.7-flash",
  "status": "completed",
  "error": null,
  "incomplete_details": null,
  "output": [
    {
      "type": "reasoning",
      "id": "rs_xxxxxxxxxxxxxxxx",
      "summary": [],
      "content": null,
      "encrypted_content": null,
      "status": null
    },
    {
      "type": "message",
      "id": "msg_xxxxxxxxxxxxxxxx",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "量子计算是一种利用量子力学原理（如叠加和纠缠）来处理信息的新型计算范式。",
          "annotations": []
        }
      ]
    }
  ],
  "usage": {
    "input_tokens": 14,
    "input_tokens_details": { "cached_tokens": 0 },
    "output_tokens": 52,
    "output_tokens_details": { "reasoning_tokens": 0, "tool_output_tokens": 0 },
    "total_tokens": 66
  },
  "instructions": null,
  "max_output_tokens": null,
  "reasoning": { "effort": "medium", "summary": null },
  "temperature": 1.0,
  "top_p": 1.0,
  "text": { "format": { "type": "text" } },
  "tool_choice": "auto",
  "tools": []
}
```

### 流式响应

当 `stream=true` 时，返回 Server-Sent Events (SSE) 流式数据。每条事件由 `event:` 行和 `data:` 行组成。

每个事件的 `data` 对象都包含 `type` 和 `sequence_number`。`type` 与 `event` 名称保持一致；`sequence_number` 从 0 开始递增，可用于客户端按顺序处理事件。

#### 事件类型

| 事件名                                      | 触发时机    |
| ---------------------------------------- | ------- |
| `response.created`                       | 响应创建    |
| `response.in_progress`                   | 开始生成    |
| `response.output_item.added`             | 新输出项创建  |
| `response.reasoning_part.added`          | 推理内容块开始 |
| `response.reasoning_text.delta`          | 推理文本增量  |
| `response.reasoning_text.done`           | 推理文本完成  |
| `response.reasoning_part.done`           | 推理内容块完成 |
| `response.content_part.added`            | 文本内容块开始 |
| `response.output_text.delta`             | 文本增量    |
| `response.output_text.done`              | 文本完成    |
| `response.content_part.done`             | 内容块完成   |
| `response.function_call_arguments.delta` | 工具参数增量  |
| `response.function_call_arguments.done`  | 工具参数完成  |
| `response.output_item.done`              | 输出项完成   |
| `response.completed`                     | 响应完成    |
| `response.incomplete`                    | 因输出截断结束 |
| `response.failed`                        | 生成失败    |
| `error`                                  | 传输层错误   |

#### 示例

文本流式输出：

```text theme={null}
event: response.created
data: {"type":"response.created","sequence_number":0,"response":{"id":"resp_xxx","object":"response","created_at":1772624997,"model":"step-3.7-flash","status":"in_progress","output":[]}}

event: response.in_progress
data: {"type":"response.in_progress","sequence_number":1,"response":{"id":"resp_xxx","status":"in_progress"}}

event: response.output_item.added
data: {"type":"response.output_item.added","sequence_number":2,"output_index":0,"item":{"id":"rs_xxx","type":"reasoning","summary":[],"content":null,"encrypted_content":null,"status":"in_progress"}}

event: response.reasoning_part.added
data: {"type":"response.reasoning_part.added","sequence_number":3,"output_index":0,"item_id":"rs_xxx","content_index":0,"part":{"type":"reasoning_text","text":""}}

event: response.reasoning_text.delta
data: {"type":"response.reasoning_text.delta","sequence_number":4,"output_index":0,"item_id":"rs_xxx","content_index":0,"delta":"用户要求问候。"}

event: response.reasoning_text.done
data: {"type":"response.reasoning_text.done","sequence_number":5,"output_index":0,"item_id":"rs_xxx","content_index":0,"text":"用户要求问候。"}

event: response.reasoning_part.done
data: {"type":"response.reasoning_part.done","sequence_number":6,"output_index":0,"item_id":"rs_xxx","content_index":0,"part":{"type":"reasoning_text","text":"用户要求问候。"}}

event: response.output_item.done
data: {"type":"response.output_item.done","sequence_number":7,"output_index":0,"item":{"id":"rs_xxx","type":"reasoning","summary":[],"content":null,"encrypted_content":null,"status":"completed"}}

event: response.output_item.added
data: {"type":"response.output_item.added","sequence_number":8,"output_index":1,"item":{"id":"msg_xxx","type":"message","role":"assistant","status":"in_progress","content":[]}}

event: response.content_part.added
data: {"type":"response.content_part.added","sequence_number":9,"item_id":"msg_xxx","output_index":1,"content_index":0,"part":{"type":"output_text","text":"","annotations":[]}}

event: response.output_text.delta
data: {"type":"response.output_text.delta","sequence_number":10,"item_id":"msg_xxx","output_index":1,"content_index":0,"delta":"你好"}

event: response.output_text.done
data: {"type":"response.output_text.done","sequence_number":11,"item_id":"msg_xxx","output_index":1,"content_index":0,"text":"你好"}

event: response.content_part.done
data: {"type":"response.content_part.done","sequence_number":12,"item_id":"msg_xxx","output_index":1,"content_index":0,"part":{"type":"output_text","text":"你好","annotations":[]}}

event: response.output_item.done
data: {"type":"response.output_item.done","sequence_number":13,"output_index":1,"item":{"id":"msg_xxx","type":"message","role":"assistant","status":"completed","content":[{"type":"output_text","text":"你好","annotations":[]}]}}

event: response.completed
data: {"type":"response.completed","sequence_number":14,"response":{"id":"resp_xxx","object":"response","status":"completed","output":[{"id":"rs_xxx","type":"reasoning","summary":[],"content":null,"encrypted_content":null,"status":"completed"},{"id":"msg_xxx","type":"message","role":"assistant","status":"completed","content":[{"type":"output_text","text":"你好","annotations":[]}]}],"usage":{"input_tokens":10,"output_tokens":2,"total_tokens":12}}}
```

工具调用流式输出（节选）：

```text theme={null}
event: response.output_item.added
data: {"type":"response.output_item.added","sequence_number":0,"output_index":0,"item":{"id":"fc_xxx","type":"function_call","call_id":"call_xxx","name":"get_weather","arguments":"","status":"in_progress"}}

event: response.function_call_arguments.delta
data: {"type":"response.function_call_arguments.delta","sequence_number":1,"item_id":"fc_xxx","output_index":0,"delta":"{\"city\":\"北京\"}"}

event: response.function_call_arguments.done
data: {"type":"response.function_call_arguments.done","sequence_number":2,"item_id":"fc_xxx","output_index":0,"arguments":"{\"city\":\"北京\"}","name":"get_weather"}

event: response.output_item.done
data: {"type":"response.output_item.done","sequence_number":3,"output_index":0,"item":{"id":"fc_xxx","type":"function_call","call_id":"call_xxx","name":"get_weather","arguments":"{\"city\":\"北京\"}","status":"completed"}}

event: response.completed
data: {"type":"response.completed","sequence_number":4,"response":{"id":"resp_xxx","object":"response","status":"completed","output":[{"id":"fc_xxx","type":"function_call","call_id":"call_xxx","name":"get_weather","arguments":"{\"city\":\"北京\"}","status":"completed"}]}}
```

## 示例

<Tabs>
  <Tab title="基础文字">
    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from openai import OpenAI

        client = OpenAI(api_key="YOUR_STEP_API_KEY", base_url="https://api.stepfun.com/v1")

        response = client.responses.create(
            model="step-3.7-flash",
            input="用一句话介绍量子计算",
        )

        print(response.output_text)
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import OpenAI from "openai";

        const openai = new OpenAI({
            apiKey: "YOUR_STEP_API_KEY",
            baseURL: "https://api.stepfun.com/v1"
        });

        const response = await openai.responses.create({
            model: "step-3.7-flash",
            input: "用一句话介绍量子计算",
        });

        console.log(response.output_text);
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.stepfun.com/v1/responses \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.7-flash",
            "input": "用一句话介绍量子计算"
          }'
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="多轮对话 + 函数调用">
    第一轮：模型根据工具定义发起 `function_call`；第二轮：客户端将上一轮的 `function_call` 与本地执行得到的 `function_call_output` 一并回传，模型基于工具结果综合回复。

    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from openai import OpenAI

        client = OpenAI(api_key="YOUR_STEP_API_KEY", base_url="https://api.stepfun.com/v1")

        tools = [{
            "type": "function",
            "name": "get_weather",
            "description": "获取指定城市的当前天气",
            "parameters": {
                "type": "object",
                "properties": {"city": {"type": "string", "description": "城市名称"}},
                "required": ["city"],
            },
            "strict": True,
        }]

        # 第一轮：模型发起 function_call
        r1 = client.responses.create(
            model="step-3.7-flash",
            input=[{"role": "user", "content": "北京今天天气怎么样？"}],
            tools=tools,
            tool_choice="auto",
        )
        fc = next(o for o in r1.output if o.type == "function_call")

        # 客户端执行工具（此处用 mock 数据演示）
        tool_result = '{"temperature":22,"weather":"晴","humidity":45}'

        # 第二轮：回传 function_call 与 function_call_output
        r2 = client.responses.create(
            model="step-3.7-flash",
            input=[
                {"role": "user", "content": "北京今天天气怎么样？"},
                {
                    "type": "function_call",
                    "id": fc.id,
                    "call_id": fc.call_id,
                    "name": fc.name,
                    "arguments": fc.arguments,
                },
                {
                    "type": "function_call_output",
                    "call_id": fc.call_id,
                    "output": tool_result,
                },
            ],
            tools=tools,
        )
        print(r2.output_text)
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import OpenAI from "openai";

        const openai = new OpenAI({
            apiKey: "YOUR_STEP_API_KEY",
            baseURL: "https://api.stepfun.com/v1"
        });

        const tools = [{
            type: "function",
            name: "get_weather",
            description: "获取指定城市的当前天气",
            parameters: {
                type: "object",
                properties: { city: { type: "string", description: "城市名称" } },
                required: ["city"]
            },
            strict: true
        }];

        // 第一轮：模型发起 function_call
        const r1 = await openai.responses.create({
            model: "step-3.7-flash",
            input: [{ role: "user", content: "北京今天天气怎么样？" }],
            tools,
            tool_choice: "auto"
        });
        const fc = r1.output.find(o => o.type === "function_call");

        // 客户端执行工具（此处用 mock 数据演示）
        const toolResult = '{"temperature":22,"weather":"晴","humidity":45}';

        // 第二轮：回传 function_call 与 function_call_output
        const r2 = await openai.responses.create({
            model: "step-3.7-flash",
            input: [
                { role: "user", content: "北京今天天气怎么样？" },
                {
                    type: "function_call",
                    id: fc.id,
                    call_id: fc.call_id,
                    name: fc.name,
                    arguments: fc.arguments
                },
                {
                    type: "function_call_output",
                    call_id: fc.call_id,
                    output: toolResult
                }
            ],
            tools
        });
        console.log(r2.output_text);
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        # 第一轮：模型发起 function_call
        curl https://api.stepfun.com/v1/responses \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.7-flash",
            "input": [{ "role": "user", "content": "北京今天天气怎么样？" }],
            "tools": [{
              "type": "function",
              "name": "get_weather",
              "description": "获取指定城市的当前天气",
              "parameters": {
                "type": "object",
                "properties": { "city": { "type": "string", "description": "城市名称" } },
                "required": ["city"]
              },
              "strict": true
            }],
            "tool_choice": "auto"
          }'

        # 第二轮：回传 function_call 与 function_call_output（call_id 用上一轮返回的值）
        curl https://api.stepfun.com/v1/responses \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.7-flash",
            "input": [
              { "role": "user", "content": "北京今天天气怎么样？" },
              {
                "type": "function_call",
                "id": "fc_xxxxxxxxxxxxxxxx",
                "call_id": "call_xxxxxxxxxxxxxxxx",
                "name": "get_weather",
                "arguments": "{\"city\":\"北京\"}"
              },
              {
                "type": "function_call_output",
                "call_id": "call_xxxxxxxxxxxxxxxx",
                "output": "{\"temperature\":22,\"weather\":\"晴\",\"humidity\":45}"
              }
            ],
            "tools": [{
              "type": "function",
              "name": "get_weather",
              "parameters": {
                "type": "object",
                "properties": { "city": { "type": "string" } },
                "required": ["city"]
              },
              "strict": true
            }]
          }'
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="多模态图片">
    推荐使用 base64 data URL：

    <Tabs>
      <Tab title="python">
        ```python theme={null}
        import base64, requests
        from openai import OpenAI

        client = OpenAI(api_key="YOUR_STEP_API_KEY", base_url="https://api.stepfun.com/v1")

        # 加载图片到内存，仅演示。按需改成读文件等
        r = requests.get("https://www.stepfun.com/assets/section-1-CTe4nZiO.webp")
        r.raise_for_status()
        image_data_url = "data:image/webp;base64," + base64.b64encode(r.content).decode("ascii")

        response = client.responses.create(
            model="step-3.7-flash",
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "描述这张图片的内容"},
                    {"type": "input_image", "image_url": image_data_url},
                ],
            }],
        )
        print(response.output_text)
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import OpenAI from "openai";

        const openai = new OpenAI({
            apiKey: "YOUR_STEP_API_KEY",
            baseURL: "https://api.stepfun.com/v1"
        });

        // 加载图片到内存，仅演示。按需改成读文件等
        async function loadImage(url) {
            const res = await fetch(url);
            const blob = await res.blob();
            const buffer = Buffer.from(await blob.arrayBuffer());
            return "data:" + blob.type + ";base64," + buffer.toString("base64");
        }

        const imageDataUrl = await loadImage("https://www.stepfun.com/assets/section-1-CTe4nZiO.webp");

        const response = await openai.responses.create({
            model: "step-3.7-flash",
            input: [{
                role: "user",
                content: [
                    { type: "input_text", text: "描述这张图片的内容" },
                    { type: "input_image", image_url: imageDataUrl }
                ]
            }]
        });
        console.log(response.output_text);
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        # 加载图片到内存，仅演示。按需改成读文件等
        image_base64="data:image/webp;base64,"$(curl -s "https://www.stepfun.com/assets/section-1-CTe4nZiO.webp" | base64)

        curl https://api.stepfun.com/v1/responses \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d "{
            \"model\": \"step-3.7-flash\",
            \"input\": [
              {
                \"role\": \"user\",
                \"content\": [
                  { \"type\": \"input_text\", \"text\": \"描述这张图片的内容\" },
                  { \"type\": \"input_image\", \"image_url\": \"${image_base64}\" }
                ]
              }
            ]
          }"
        ```
      </Tab>
    </Tabs>

    也可使用对象形态指定 `detail`：

    ```json theme={null}
    {
      "type": "input_image",
      "image_url": { "url": "data:image/jpeg;base64,...", "detail": "high" }
    }
    ```
  </Tab>

  <Tab title="多模态视频">
    视频通过 URL 传入，URL 需可被服务端公网访问：

    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from openai import OpenAI

        client = OpenAI(api_key="YOUR_STEP_API_KEY", base_url="https://api.stepfun.com/v1")

        response = client.responses.create(
            model="step-3.7-flash",
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "请概括这个视频里的主要内容"},
                    {"type": "input_video", "video_url": {"url": "https://example.com/demo.mp4", "detail": "low"}},
                ],
            }],
        )
        print(response.output_text)
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import OpenAI from "openai";

        const openai = new OpenAI({
            apiKey: "YOUR_STEP_API_KEY",
            baseURL: "https://api.stepfun.com/v1"
        });

        const response = await openai.responses.create({
            model: "step-3.7-flash",
            input: [{
                role: "user",
                content: [
                    { type: "input_text", text: "请概括这个视频里的主要内容" },
                    { type: "input_video", video_url: { url: "https://example.com/demo.mp4", detail: "low" } }
                ]
            }]
        });
        console.log(response.output_text);
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.stepfun.com/v1/responses \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.7-flash",
            "input": [
              {
                "role": "user",
                "content": [
                  { "type": "input_text", "text": "请概括这个视频里的主要内容" },
                  { "type": "input_video", "video_url": {"url": "https://example.com/demo.mp4", "detail": "low"} }
                ]
              }
            ]
          }'
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="结构化输出">
    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from openai import OpenAI

        client = OpenAI(api_key="YOUR_STEP_API_KEY", base_url="https://api.stepfun.com/v1")

        response = client.responses.create(
            model="step-3.7-flash",
            input="分析句子情感：这部电影太精彩了，强烈推荐！",
            text={
                "format": {
                    "type": "json_schema",
                    "name": "sentiment_analysis",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "sentiment": {"type": "string", "enum": ["positive", "negative", "neutral"]},
                            "confidence": {"type": "number"},
                            "keywords": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": ["sentiment", "confidence", "keywords"],
                        "additionalProperties": False,
                    },
                }
            },
        )
        print(response.output_text)
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import OpenAI from "openai";

        const openai = new OpenAI({
            apiKey: "YOUR_STEP_API_KEY",
            baseURL: "https://api.stepfun.com/v1"
        });

        const response = await openai.responses.create({
            model: "step-3.7-flash",
            input: "分析句子情感：这部电影太精彩了，强烈推荐！",
            text: {
                format: {
                    type: "json_schema",
                    name: "sentiment_analysis",
                    strict: true,
                    schema: {
                        type: "object",
                        properties: {
                            sentiment: { type: "string", enum: ["positive", "negative", "neutral"] },
                            confidence: { type: "number" },
                            keywords: { type: "array", items: { type: "string" } }
                        },
                        required: ["sentiment", "confidence", "keywords"],
                        additionalProperties: false
                    }
                }
            }
        });
        console.log(response.output_text);
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.stepfun.com/v1/responses \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.7-flash",
            "input": "分析句子情感：这部电影太精彩了，强烈推荐！",
            "text": {
              "format": {
                "type": "json_schema",
                "name": "sentiment_analysis",
                "strict": true,
                "schema": {
                  "type": "object",
                  "properties": {
                    "sentiment": { "type": "string", "enum": ["positive", "negative", "neutral"] },
                    "confidence": { "type": "number" },
                    "keywords": { "type": "array", "items": { "type": "string" } }
                  },
                  "required": ["sentiment", "confidence", "keywords"],
                  "additionalProperties": false
                }
              }
            }
          }'
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="流式输出">
    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from openai import OpenAI

        client = OpenAI(api_key="YOUR_STEP_API_KEY", base_url="https://api.stepfun.com/v1")

        stream = client.responses.create(
            model="step-3.7-flash",
            input="写一首关于春天的五言绝句",
            stream=True,
        )

        for event in stream:
            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)
        print()
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import OpenAI from "openai";

        const openai = new OpenAI({
            apiKey: "YOUR_STEP_API_KEY",
            baseURL: "https://api.stepfun.com/v1"
        });

        const stream = await openai.responses.create({
            model: "step-3.7-flash",
            input: "写一首关于春天的五言绝句",
            stream: true
        });

        for await (const event of stream) {
            if (event.type === "response.output_text.delta") {
                process.stdout.write(event.delta);
            }
        }
        process.stdout.write("\n");
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.stepfun.com/v1/responses \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.7-flash",
            "input": "写一首关于春天的五言绝句",
            "stream": true
          }'
        ```
      </Tab>
    </Tabs>

    流式响应格式参见上文「流式响应」章节。
  </Tab>

  <Tab title="推理强度">
    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from openai import OpenAI

        client = OpenAI(api_key="YOUR_STEP_API_KEY", base_url="https://api.stepfun.com/v1")

        response = client.responses.create(
            model="step-3.7-flash",
            input="证明：任何完全平方数模 4 的余数只能是 0 或 1",
            reasoning={"effort": "high"},
        )
        print(response.output_text)
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import OpenAI from "openai";

        const openai = new OpenAI({
            apiKey: "YOUR_STEP_API_KEY",
            baseURL: "https://api.stepfun.com/v1"
        });

        const response = await openai.responses.create({
            model: "step-3.7-flash",
            input: "证明：任何完全平方数模 4 的余数只能是 0 或 1",
            reasoning: { effort: "high" }
        });
        console.log(response.output_text);
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.stepfun.com/v1/responses \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.7-flash",
            "input": "证明：任何完全平方数模 4 的余数只能是 0 或 1",
            "reasoning": { "effort": "high" }
          }'
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
