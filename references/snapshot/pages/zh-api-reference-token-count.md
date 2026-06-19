<!-- title: Token Count -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/token-count -->
<!-- extracted: trafilatura -->

计算 token 数，支持 Chat Completion 接口与 Messages 接口两种格式。
## 计算 Chat Completion Token 数

### 请求地址

`POST https://api.stepfun.com/v1/token/count`

### 请求参数

-
`model`

`string`

**required**

需要使用的模型名称
-
`messages`

`object array`

**required**

迄今为止用户输入或模型生成的不同类别消息列表

- 系统消息
`object`


`role`

`string`


系统类别名称，总是为 `system`

`content`

`string`


系统消息的文本内容

- 用户消息
`object`


`role`

`string`


用户类别名称，总是 `user`

`content`

`string or object array`


用户消息内容，类型为 `multipart`

消息列表或者普通文本消息字符串

`普通文本消息`

`string`


直接传入字符串作为消息内容
`multipart`

消息列表 `object array`


结构化的图文混合消息

- 文本消息
`object`


`type`

`string`


总为 `text`

`text`

`string`


消息文本内容

- 图片消息
`object`


`type`

`string`


总为 `image_url`

`image_url`

`object`


`url`

`string`


图片地址或 base64编码的图片
图片地址仅支持 http 和 https 协议

base64格式举例：`data:image/jpeg;base64,${base64_string}`

，请更换图片格式(jpeg)及对应的 base64编码后字符串

本接口支持的图片格式：jpg/jpeg、png、webp、静态 gif






- 聊天助手消息
`object`


`role`

`string`


聊天助手类别名称，总是为 `assistant`

`content`

`string | null`


聊天助手消息的文本内容



### 请求响应

`data`

`object`


计算 token 返回数据

`total_tokens`

`int`


输入 token 数


```
curl https://api.stepfun.com/v1/token/count \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $STEP_API_KEY" \
-d '{
"model": "step-3.7-flash",
"messages": [
{
"role": "system",
"content": "你是由阶跃星辰提供的AI聊天助手，你擅长中文，英文，以及多种其他语言的对话。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容。"
},
{
"role": "user",
"content": "你好，请介绍一下阶跃星辰的人工智能！"
}
]
}'
```


```
{
"data": {
"total_tokens": 85
}
}
```


```
curl https://api.stepfun.com/v1/token/count \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $STEP_API_KEY" \
-d '{
"model": "step-3.7-flash",
"messages": [
{
"role": "system",
"content": "你是由阶跃星辰提供的AI聊天助手，你除了擅长中文，英文，以及多种其他语言的对话以外，还能够根据用户提供的图片，对内容进行精准的内容文本描述。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容"
},
{
"role": "user",
"content": [
{
"type": "text",
"text": "用优雅的语言描述这张图片"
},
{
"type": "image_url",
"image_url": {
"url": "https://www.stepfun.com/assets/section-1-CTe4nZiO.webp"
}
}
]
}
]
}'
```


```
{
"data": {
"total_tokens": 497
}
}
```


```
# 加载图片到内存，仅演示。按需改成读文件等
image_base64="data:image/webp;base64,"$(curl -s "https://www.stepfun.com/assets/section-1-CTe4nZiO.webp" | base64)
curl https://api.stepfun.com/v1/token/count \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $STEP_API_KEY" \
-d "{
\"model\": \"step-3.7-flash\",
\"messages\": [
{
\"role\": \"system\",
\"content\": \"你是由阶跃星辰提供的AI聊天助手，你除了擅长中文，英文，以及多种其他语言的对话以外，还能够根据用户提供的图片，对内容进行精准的内容文本描述。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容\"
},
{
\"role\": \"user\",
\"content\": [
{
\"type\": \"text\",
\"text\": \"用优雅的语言描述这张图片\"
},
{
\"type\": \"image_url\",
\"image_url\": {
\"url\": \"${image_base64}\"
}
}
]
}
]
}"
```


```
{
"data": {
"total_tokens": 497
}
}
```



## 估算 Message Token 数

估算 Messages API 输入 token 数量，不生成模型回复。
### 请求地址

`POST https://api.stepfun.com/v1/messages/count_tokens`

使用 Anthropic SDK 时，base_url 应设为 `https://api.stepfun.com`

，SDK 会自动拼接 `/v1/messages/count_tokens`

，无需手动带 `/v1`

。

Step Plan 场景请求地址为 `POST https://api.stepfun.com/step_plan/v1/messages/count_tokens`

，对应 SDK base_url 为 `https://api.stepfun.com/step_plan`

。

### 请求参数

请求体结构与[创建 Message](/docs/zh/api-reference/chat/messages-create) 相同，通常至少需要提供：
`model`

`string`

**required**

模型名称
`messages`

`object array`

**required**

对话消息列表

也可按需携带 `system`

、`tools`

等上下文字段。`max_tokens`

在该接口中可不传。
### 请求响应

`Content-Type: application/json`

`input_tokens`

`int`


估算的输入 token 数量

```
from anthropic import Anthropic
client = Anthropic(api_key="STEP_API_KEY", base_url="https://api.stepfun.com")
response = client.messages.count_tokens(
model="step-3.5-flash",
messages=[
{
"role": "user",
"content": "统计这句话需要多少输入 token？"
}
],
)
print(response.input_tokens)
```


```
curl https://api.stepfun.com/v1/messages/count_tokens \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $STEP_API_KEY" \
-d '{
"model": "step-3.5-flash",
"messages": [
{
"role": "user",
"content": "统计这句话需要多少输入 token？"
}
]
}'
```