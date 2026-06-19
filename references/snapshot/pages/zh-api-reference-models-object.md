<!-- title: model 对象 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/models/object.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# model 对象

单个 Model 对象的描述信息数据

## 属性

* `id` `string`<br />模型的唯一标识 ID
* `created` `int`<br />模型的创建时间，类型为 Unix 时间戳，单位 s
* `object` `string`<br />对象类型，此处总为 `model`
* `owned_by` `string`<br />模型所属的组织名称

## 示例

```json theme={null}
{
  "id": "step-3.7-flash",
  "object": "model",
  "created": 1713196800,
  "owned_by": "stepai"
}
```
