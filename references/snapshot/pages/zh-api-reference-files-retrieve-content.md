<!-- title: 获取文件内容 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/files/retrieve-content.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取文件内容

获取指定文件的内容（仅支持 purpose 为 file-extract 的文件获取内容）

## 请求地址

`GET https://api.stepfun.com/v1/files/{file_id}/content`

## 路径参数

* `file_id` `string` ***required***
  <br />
  文件的唯一标识 id

## 请求响应

返回文件解析后的纯文本内容。

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    content = client.files.content("file-abc123")
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
        const file = await openai.files.content("file-abc123");

        console.log(file);
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/files/file-abc123/content \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```text filename="返回" theme={null}
文件内容
```
