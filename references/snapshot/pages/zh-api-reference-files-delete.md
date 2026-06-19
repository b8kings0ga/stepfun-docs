<!-- title: 删除单个文件 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/files/delete.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 删除单个文件

删除单个已经上传的文件

## 请求地址

`DELETE https://api.stepfun.com/v1/files/{file_id}`

## 路径参数

* `file_id` `string` ***required***
  <br />
  文件的唯一标识 id

## 请求响应

返回单个[文件对象](/zh/api-reference/files/object)

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    print(client.files.delete("file-stepabc"))
    ```
  </Tab>

  <Tab title="js">
    ```js theme={null}
    import OpenAI from "openai";

    const openai = new OpenAI({
        apiKey: "STEP_API_KEY",
        baseURL: "https://api.stepfun.com/v1"
    });

    async function main() {
        const file = await openai.files.del("file-stepabc");
        console.log(file);
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/files/file-abc123 \
      -X DELETE \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "file-stepabc",
  "object": "file",
  "deleted": true
}
```
