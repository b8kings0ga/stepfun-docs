<!-- title: 删除知识库 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/delete.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 删除知识库

删除已经创建的知识库

## 请求地址

`DELETE https://api.stepfun.com/v1/vector_stores/{vector_store_id}`

## 路径参数

* `vector_store_id` `string` ***required***
  <br />
  知识库的唯一 ID

## 请求响应

* `id` `string`
  <br />知识库的唯一 ID

* `deleted` `boolean`
  <br /> 删除是否成功

* `object` `string`
  <br />固定为 `vector_store.deleted`

## 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L -X DELETE 'https://api.stepfun.com/v1/vector_stores/160051919799205888' \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "160051919799205888",
  "deleted": true,
  "object": "vector_store.deleted"
}
```
