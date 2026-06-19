<!-- title: 查看知识库中文件列表 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/list-file.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 查看知识库中文件列表

查看对应知识库中的文件列表

## 请求地址

`GET https://api.stepfun.com/v1/vector_stores/{vector_store_id}/files`

## 路径参数

* `vector_store_id` `string` ***required***
  <br />
  知识库的唯一 ID

## Query 参数

* `limit` `string` ***optional***<br />分页的数量，默认 20，最大 100 ，最小 1。默认值为 20。

* `order` `string` ***optional*** <br />基于创建时间的返回顺序，支持参数 `asc` 和 `desc`，默认为 `desc`。

  <br /> `asc`：升序，创建早的知识库先出现
  <br /> `desc` :降序，创建晚的知识库先出现

* `before` `string` ***optional***<br /> 指针 ID（知识库 ID），可与 limit / order 联合使用

* `after` `string` ***optional***<br /> 指针 ID（知识库 ID），可与 limit / order 联合使用。

## 请求响应

返回 [Vector Store File 对象](/zh/api-reference/vector-stores/vector-store-file-object) 列表

## 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L 'https://api.stepfun.com/v1/vector_stores/160042962909147136/files' \
    -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
    "object": "list",
    "first_id": "file-CP7v8OT46a",
    "last_id": "160045144211468288",
    "has_more": false,
    "data": [
        {
            "id": "file-CP7v8OT46a",
            "object": "vector_store.file",
            "created_at": 1731491268,
            "vector_store_id": "160042962909147136"
        },
        {
            "id": "file-CP4GQjASki",
            "object": "vector_store.file",
            "created_at": 1731488576,
            "vector_store_id": "160042962909147136"
        }
    ]
}
```
