<!-- title: 获取文件列表 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/files/list.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取文件列表

获取当前用户下所有可用的文件列表

## 请求地址

`GET https://api.stepfun.com/v1/files`

## 请求参数

无

## 请求响应

返回[File 对象](/zh/api-reference/files/object)列表

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    client.files.list()
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
        const list = await openai.files.list();

        for await (const file of list) {
            console.log(file);
        }
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/files \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "data": [
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 175,
      "created_at": 1613677385,
      "filename": "salesOverview.pdf",
      "purpose": "file-extract",
      "status": "success"
    },
    {
      "id": "file-abc123",
      "object": "file",
      "bytes": 140,
      "created_at": 1613779121,
      "filename": "puppy.pdf",
      "purpose": "retrieval",
      "status": "success"
    }
  ],
  "object": "list"
}
```
