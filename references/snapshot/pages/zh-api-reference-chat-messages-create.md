<!-- title: Messages API -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/chat/messages-create.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Messages API

调用 Messages API，获取模型生成的响应数据。该接口兼容 Anthropic Messages API 格式，可直接复用 Anthropic SDK 或相同的 JSON 结构接入。

<Note>
  本文仅列出当前已确认支持的字段；未在本文出现的字段请不要传入。
</Note>

## 请求地址

`POST https://api.stepfun.com/v1/messages`

<Note>
  使用 Anthropic SDK 时，base\_url 应设为 `https://api.stepfun.com`，SDK 会自动拼接 `/v1/messages`，无需手动带 `/v1`。
</Note>

<Note>
  Step Plan 场景请求地址为 `POST https://api.stepfun.com/step_plan/v1/messages`，对应 SDK base\_url 为 `https://api.stepfun.com/step_plan`。
</Note>

## 请求参数

* `model` `string` ***required***<br />模型名称，填写当前账号已开通的公开模型名称，例如 `step-3.7-flash` 或 `step-3.5-flash`。`step-router-v1` 仅可通过 [Step Plan](/zh/step-plan/overview) 通道调用，详见本文「Step Plan 通道：DeepSeek 引擎字段差异」。
* `messages` `object array` ***required***<br />对话消息列表，至少一条
  <Expandable>
    * `role` `string`<br />角色名称，常用取值为 `user`、`assistant`
    * `content` `string or object array`<br />纯文本，或 Content Block 数组
        <Expandable>
          * 纯文本消息 `string`
          * Content Block 数组 `object array`
                <Expandable>
                  * 文本块 `object`
                          <Expandable>
                            * `type` `string`<br />总为 `text`
                            * `text` `string`<br />文本内容
                          </Expandable>
                  * 图片块 `object`
                          <Expandable>
                            * `type` `string`<br />总为 `image`
                            * `source` `object`<br />图片来源，支持 URL 或 Base64 两种写法
                                      <Expandable>
                                        * URL 写法：`{ "type": "url", "url": "https://..." }`
                                        * Base64 写法：`{ "type": "base64", "media_type": "image/png", "data": "..." }`
                                      </Expandable>
                          </Expandable>
                  * 工具调用块 `object`（模型发起）
                          <Expandable>
                            * `type` `string`<br />总为 `tool_use`
                            * `id` `string`<br />工具调用的唯一标识
                            * `name` `string`<br />调用的工具名称
                            * `input` `object`<br />传递给工具的参数
                          </Expandable>
                  * 工具结果块 `object`（用户回传）
                          <Expandable>
                            * `type` `string`<br />总为 `tool_result`
                            * `tool_use_id` `string`<br />对应工具调用的 ID
                            * `content` `string or object array`<br />工具执行结果
                            * `is_error` `boolean`<br />是否执行出错
                          </Expandable>
                </Expandable>
        </Expandable>
  </Expandable>
* `max_tokens` `int` ***required***<br />最大生成 token 数，必须大于 0
* `system` `string or array` ***optional***<br />系统提示词；可传字符串，或由文本块组成的数组
* `tools` `object array` ***optional***<br />工具定义列表
  <Expandable>
    * `name` `string`<br />工具名称
    * `description` `string`<br />工具描述，帮助模型理解何时使用该工具
    * `input_schema` `object`<br />JSON Schema，用于描述工具入参
  </Expandable>
* `output_config` `object` ***optional***<br />结构化输出配置
  <Expandable>
    * `effort` `string`<br />控制模型的思考深度。支持三档推理强度的模型可选值为 `low`、`medium`、`high`；`step-3.5-flash-2603` 兼容 `low`、`high` 两档。
  </Expandable>
* `stream` `boolean` ***optional***<br />是否启用流式返回，默认非流式
* `temperature` `float` ***optional***<br />采样温度，取值范围 0 到 2
* `top_p` `float` ***optional***<br />nucleus sampling 参数，取值范围大于 0 且小于等于 1
* `top_k` `int` ***optional***<br />top-k 参数，取值范围 0 到 500
* `stop_sequences` `string array` ***optional***<br />停止序列列表，生成内容中遇到任意一个停止序列时停止生成

## Step Plan 通道：DeepSeek 引擎字段差异

`step-router-v1` 仅可通过 [Step Plan](/zh/step-plan/overview) 通道（`https://api.stepfun.com/step_plan/v1`）调用，系统会自动在 `deepseek-v4-pro` 与 `step-3.5-flash` 之间路由。该模型的字段约束与本文「请求参数」一致，下表列出的字段除外。

| 字段                             | Step Plan 通道下的行为                                              |
| ------------------------------ | ------------------------------------------------------------- |
| `model`                        | 仅接受 `step-router-v1`，其他名称返回 HTTP 400 `request_params_invalid` |
| `max_tokens`                   | 上限为 384K                                                      |
| `messages.content` 中的图像块 / 文档块 | 不支持，使用会返回 `unsupported_content_type`                          |
| `tools` 中的 `web_search`        | 不支持，使用会返回 `unsupported_content_type`                          |
| `output_config.effort`         | 字段会被忽略                                                        |

## 请求响应

### 非流式响应

`Content-Type: application/json`

```json theme={null}
{
    "id": "msg_xxx",
    "type": "message",
    "role": "assistant",
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 20,
        "output_tokens": 12
    },
    "content": [
        {
            "type": "text",
            "text": "我是一个 AI 助手。"
        }
    ]
}
```

**响应字段说明**

* `id` `string`<br />消息的唯一标识
* `type` `string`<br />对象类型，总是为 `message`
* `role` `string`<br />角色名称，总是为 `assistant`
* `content` `object array`<br />返回内容块列表；常见为 `text`，工具调用场景下也可能返回 `tool_use`
* `stop_reason` `string`<br />生成停止原因，可选值为 `end_turn`、`tool_use`、`max_tokens`
* `usage` `object`<br />token 用量统计，至少包含 `input_tokens` 与 `output_tokens`

### 流式响应

`Content-Type: text/event-stream`

流式返回采用标准 SSE 格式，每个事件包含 `event:` 和 `data:` 两部分，`data:` 的内容为 JSON。

常见事件类型：`message_start`、`content_block_start`、`content_block_delta`、`content_block_stop`、`message_delta`、`message_stop`、`ping`

当返回工具调用参数时，`content_block_delta.delta.type` 可能为 `input_json_delta`。

```text theme={null}
event: message_start
data: {"type":"message_start","message":{"id":"msg_xxx","type":"message","role":"assistant","model":"step-3.5-flash"}}

event: content_block_start
data: {"type":"content_block_start","index":0,"content_block":{"type":"text","text":""}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"你"}}

event: message_delta
data: {"type":"message_delta","stop_reason":"end_turn","usage":{"input_tokens":20,"output_tokens":12}}

event: message_stop
data: {"type":"message_stop"}
```

## 示例

<Tabs>
  <Tab title="基础对话">
    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from anthropic import Anthropic

        client = Anthropic(api_key="STEP_API_KEY", base_url="https://api.stepfun.com")

        message = client.messages.create(
            model="step-3.5-flash",
            max_tokens=1024,
            system="你是由阶跃星辰提供的AI聊天助手，你擅长中文、英文及多种语言。在保证用户数据安全的前提下，快速精准地回答用户问题。",
            messages=[
                {
                    "role": "user",
                    "content": "请用一句话介绍你自己。"
                }
            ],
        )

        print(message)
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import Anthropic from "@anthropic-ai/sdk";

        const client = new Anthropic({
            apiKey: "STEP_API_KEY",
            baseURL: "https://api.stepfun.com"
        });

        async function main() {
            const message = await client.messages.create({
                model: "step-3.5-flash",
                max_tokens: 1024,
                system: "你是由阶跃星辰提供的AI聊天助手，你擅长中文、英文及多种语言。在保证用户数据安全的前提下，快速精准地回答用户问题。",
                messages: [
                    {
                        role: "user",
                        content: "请用一句话介绍你自己。"
                    }
                ]
            });

            console.log(JSON.stringify(message));
        }

        main();
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.stepfun.com/v1/messages \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.5-flash",
            "max_tokens": 1024,
            "system": "你是由阶跃星辰提供的AI聊天助手，你擅长中文、英文及多种语言。在保证用户数据安全的前提下，快速精准地回答用户问题。",
            "messages": [
                {
                    "role": "user",
                    "content": "请用一句话介绍你自己。"
                }
            ]
        }'
        ```
      </Tab>
    </Tabs>

    ```json filename="Response" theme={null}
    {
        "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
        "type": "message",
        "role": "assistant",
        "stop_reason": "end_turn",
        "usage": {
            "input_tokens": 35,
            "output_tokens": 20
        },
        "content": [
            {
                "type": "text",
                "text": "我是阶跃星辰提供的AI聊天助手，能够用中文、英文等多种语言快速精准地回答您的问题。"
            }
        ]
    }
    ```
  </Tab>

  <Tab title="流式响应">
    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from anthropic import Anthropic

        client = Anthropic(api_key="STEP_API_KEY", base_url="https://api.stepfun.com")

        with client.messages.stream(
            model="step-3.5-flash",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "请用一句话介绍你自己。"
                }
            ],
        ) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)

        print()
        ```
      </Tab>

      <Tab title="js">
        ```js theme={null}
        import Anthropic from "@anthropic-ai/sdk";

        const client = new Anthropic({
            apiKey: "STEP_API_KEY",
            baseURL: "https://api.stepfun.com"
        });

        async function main() {
            const stream = client.messages.stream({
                model: "step-3.5-flash",
                max_tokens: 1024,
                messages: [
                    {
                        role: "user",
                        content: "请用一句话介绍你自己。"
                    }
                ]
            });

            for await (const event of stream) {
                if (
                    event.type === "content_block_delta" &&
                    event.delta.type === "text_delta"
                ) {
                    process.stdout.write(event.delta.text);
                }
            }

            console.log();
        }

        main();
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.stepfun.com/v1/messages \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEP_API_KEY" \
          -d '{
            "model": "step-3.5-flash",
            "max_tokens": 1024,
            "stream": true,
            "messages": [
                {
                    "role": "user",
                    "content": "请用一句话介绍你自己。"
                }
            ]
        }'
        ```
      </Tab>
    </Tabs>
  </Tab>

  <Tab title="使用 output_config.effort">
    <Tabs>
      <Tab title="python">
        ```python theme={null}
        from anthropic import Anthropic

        client = Anthropic(api_key="STEP_API_KEY", base_url="https://api.stepfun.com")

        message = client.messages.create(
            model="step-3.7-flash",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "请用三句话解释什么是强化学习。"
                }
            ],
            extra_body={
                "output_config": {
                    "effort": "medium"
                }
            }
        )

        print(message)
        ```
      </Tab>

      <Tab title="curl">
        ```bash theme={null}
        curl https://api.stepfun.com/v1/messages \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer $STEPFUN_API_KEY" \
          -d '{
            "model": "step-3.7-flash",
            "max_tokens": 1024,
            "messages": [
                {
                    "role": "user",
                    "content": "请用三句话解释什么是强化学习。"
                }
            ],
            "output_config": {
                "effort": "medium"
            }
        }'
        ```
      </Tab>
    </Tabs>
  </Tab>
</Tabs>
