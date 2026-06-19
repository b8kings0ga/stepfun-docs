<!-- title: 创建知识库 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/create.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 创建知识库

创建一个新的知识库，用于存储文本内容。

## 请求地址

`POST https://api.stepfun.com/v1/vector_stores`

## 请求体

* `name` `string` ***required***<br />知识库的名字，用于区分多个不同的知识库。目前仅支持英文、数字和下划线，且不支持以下划线开头。

* `type` `string` **optional**<br />知识库的类型，支持 text (文本类型知识库）和 image (图片知识库）。

## 请求响应

返回单个 [Vector Store 对象](/zh/api-reference/vector-stores/object)

## 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L "https://api.stepfun.com/v1/vector_stores" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "name": "food_calorie2",
        "type": "text"
      }'
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "167907758199320576",
  "name": "food_calorie"
}
```
