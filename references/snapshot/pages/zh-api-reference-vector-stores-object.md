<!-- title: Vector Store 对象 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/object.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vector Store 对象

单个 Vector Store 对象的描述信息

## 属性

* `id` `string`<br />Vector Store 的唯一 ID
* `object` `string`<br />对象类型，此处总为 `vector_store`
* `created_at` `int`<br />Vector Store 的创建时间，类型为 Unix 时间戳，单位 s
* `name` `string`<br />知识库名称
* `type` `string`<br />知识库类型，可选项为 `text` 和 `image`，对应文本知识库 & 多模态知识库（图片）
* `file_counts` `object`<br />知识库的各项统计信息
  * `in_progress` `int` 仍在处理中的文件数量
  * `completed` `int` 已处理完成的文件数量
  * `failed` `int` 处理失败的文件数量
  * `cancelled` `int` 已取消的文件数量
  * `total` `int` 总文件数量

## 示例

```json theme={null}
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
