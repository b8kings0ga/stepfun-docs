<!-- title: 将文件添加到知识库 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/vector-stores/create-file.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 将文件添加到知识库

将一个已经上传的 purpose 为 `retrieval` 文件添加到知识库中。

## 请求地址

`POST https://api.stepfun.com/v1/vector_stores/{vector_store_id}/files`

## 路径参数

* `vector_store_id` `string` ***required***
  <br />
  知识库的唯一 ID

## 请求体

* `files` `array` ***required***<br />要添加到知识库中的文件列表。
  * `file_id` `string` ***required***<br />要添加到知识库中的文件的 File ID，可以通过[文件上传 API](/zh/api-reference/files/create) 获取。上传时，purpose 必须为 retrieval-text 或 retrieval-image。
  * `description` `string` ***optional***<br />图片文件的描述信息。支持中文、英文、空格字符等常见内容。最大长度为 255 字；在使用图片知识库的时候，此字段必填。

## 请求响应

* `files` `array`<br /> 上传的文件的数组
  * `file_id` `string`<br /> 文件的 File ID
  * `metadata` `object`<br /> 文件对应的元信息
    * `description` `string`<br /> 文件的描述信息

## 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
      curl -X "POST" "https://api.stepfun.com/v1/vector_stores/160042962909147136/files" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -H 'Content-Type: application/json; charset=utf-8' \
      -d $'{
        "files": [
          {
            "file_id": "abc",
            "description": "这是一个测试文档"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "files":[
      {
          "file_id":"123",
           "metadata":{
              "description":"这是一个测试文档"
          }
      }
  ]
}
```

## 备注

* 原 form 方式提交方式已标记为 `deprecated`，将于 2025 年 5 月 15 日下线 ，新用户可使用 JSON 方式上传。
