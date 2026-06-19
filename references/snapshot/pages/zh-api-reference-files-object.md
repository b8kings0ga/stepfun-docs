<!-- title: File 对象 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/files/object.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# File 对象

单个 File 对象的描述信息

## 属性

* `id` `string`<br />File 的唯一 ID
* `object` `string`<br />对象类型，此处总为 `file`
* `bytes` `int`<br />文件大小
* `created_at` `int`<br />File 的创建时间，类型为 Unix 时间戳，单位 s
* `filename` `string`<br />文件名
* `purpose` `string`<br />上传意图，可选项为  `file-extract` 、 `retrieval-text`  、`retrieval-image`  和 `storage`。
* `status` `string`<br />处理状态，可选项为 `success` 和 `processed`

## 示例

```json theme={null}
{
    "id": "file-abc123",
    "object": "file",
    "bytes": 140,
    "created_at": 1613779121,
    "filename": "salesOverview.pdf",
    "purpose": "file-extract",
}
```
