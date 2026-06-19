<!-- title: Vector Store File 对象 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/vector-store-file-object.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vector Store File 对象

单个 Vector Store File 对象的描述信息

## 属性

* `id` `string`<br />Vector Store 的唯一 ID

* `object` `string`<br />对象类型，此处总为 `vector_store.file`

* `created_at` `int`<br />Vector Store 的创建时间，类型为 Unix 时间戳，单位 s

* `vector_store_id` `string`<br />知识库 ID

* `metadata` `object`<br />文件的元信息
  * `description` `string`<br />文件的描述信息。

## 示例

```json theme={null}
 {
    "id": "file-CP7v8OT46a",
    "object": "vector_store.file",
    "created_at": 1731491268,
    "vector_store_id": "160042962909147136",
    "metadata":{
         "description":"这是图片描述"
    }
}
```
