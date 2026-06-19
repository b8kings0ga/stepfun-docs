<!-- title: 获取知识库详情 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/retrieve.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取知识库详情

获取已经创建的知识库详情，可查看知识库中文件数量等详细信息。

## 请求地址

`GET https://api.stepfun.com/v1/vector_stores/{vector_store_id}`

## 路径参数

* `vector_store_id` `string` ***required***
  <br />
  知识库的唯一 ID

## 请求响应

返回单个 [Vector Store 对象](/zh/api-reference/vector-stores/object)

## 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L 'https://api.stepfun.com/v1/vector_stores/167907758199320576' \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "167907758199320576",
  "object": "vector_store",
  "created_at": 1731485617,
  "name": "food_calorie2",
  "type": "text",
  "file_counts": {
    "in_progress": 0,
    "completed": 0,
    "failed": 0,
    "cancelled": 0,
    "total": 0
  }
}
```
