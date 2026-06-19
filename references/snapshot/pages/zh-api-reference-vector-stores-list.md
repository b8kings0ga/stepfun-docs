<!-- title: 查看知识库列表 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/list.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 查看知识库列表

查看当前用户创建的所有知识库。

## 请求地址

`GET https://api.stepfun.com/v1/vector_stores`

## Query 参数

* `limit` `string` ***optional***<br />分页的数量，默认 20，最大 100 ，最小 1。默认值为 20。

* `order` `string` ***optional***<br />基于创建时间的返回顺序，支持参数 `asc` 和 `desc`，默认为 `desc`。

  <br /> `asc`：升序，创建早的知识库先出现
  <br /> `desc` :降序，创建晚的知识库先出现

* `before` `string` ***optional***<br /> 指针 ID（知识库 ID），可与 limit / order 联合使用

* `after` `string` ***optional***<br /> 指针 ID（知识库 ID），可与 limit / order 联合使用。

## 请求响应

返回 [Vector Store 对象](/zh/api-reference/vector-stores/object) 列表

## 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L 'https://api.stepfun.com/v1/vector_stores?limit=1&order=desc&before=137723691273302016' \
    -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
    "object": "list",
    "data": [
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
    ],
    "first_id": "167907758199320576",
    "last_id": "167907758199320576",
    "has_more": true
}
```
