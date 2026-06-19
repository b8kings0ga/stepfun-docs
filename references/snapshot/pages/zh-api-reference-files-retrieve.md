<!-- title: 查询单个文件的信息 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/files/retrieve.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 查询单个文件的信息

查询单个 File 的信息，包括创建时间，所属组织等。

## 请求地址

`GET https://api.stepfun.com/v1/files/{file_id}`

## 路径参数

* `file_id` `string` ***required***
  <br />
  文件唯一标识 ID

## 请求响应

返回单个[File 对象](/zh/api-reference/files/object)

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    print(client.files.retrieve("file-stepab"))
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
        const file = await openai.files.retrieve("file-stepab");

        console.log(file);
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/files/file-abc \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "file-abc123",
  "object": "file",
  "bytes": 140,
  "created_at": 1613779121,
  "filename": "salesOverview.pdf",
  "purpose": "file-extract",
  "status": "success"
}
```
