<!-- title: 将文件从知识库中移除 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/delete-file.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 将文件从知识库中移除

从知识库中移除某个文件

## 请求地址

`DELETE https://api.stepfun.com/v1/vector_stores/{vector_store_id}/files/{file_id}`

## 路径参数

* `vector_store_id` `string` ***required***<br />知识库的唯一 ID

* `file_ids` `string` ***required***
  <br /> 要添加到知识库中的文件的 File ID，可以通过[查看知识库中的文件](/zh/api-reference/vector-stores/list-file)获取。

## 请求响应

* `id` `string`<br />知识库的唯一 ID

* `deleted` `boolean`<br /> 删除是否成功

* `object` `string` <br />固定为 `vector_store.file.deleted`

## 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L -X DELETE 'https://api.stepfun.com/v1/vector_stores/160042962909147136/files/160050946536124416' \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "160050946536124416",
  "deleted": true,
  "object": "vector_store.file.deleted"
}
```
