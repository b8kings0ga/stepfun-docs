<!-- title: 上传文件 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/files/create.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 上传文件

上传一个文件到文件服务

## 请求地址

`POST https://api.stepfun.com/v1/files`

## 请求体

* `purpose` `string` ***required***<br />文件上传的意图，支持 `file-extract` 、 `retrieval-text` 、`retrieval-image` 和 `storage` 等四种类型；
  * `file-extract`: 用于提取文件内容
  * `retrieval-text` 用于文本知识库
  * `retrieval-image` 用于图片知识库
  * `storage` 用于图片理解、视频理解、音色复刻等功能。

* `url` `string` ***optional***<br /> 远程文件的 URL ，支持 文件格式等同于 file 字段支持的文件格式；同时传 file 和 url 字段，取 file 字段内容。

* `file` `File` ***optional***<br />用于上传的文件。限制单个用户上传文件 1000 个；当传入 url 时，可不传入此字段。<br />
  `file-extract` 和 `retrieval-text` 支持的文件格式,文件大小限制为 64M；

  * 纯文本（.txt,.md）
  * PDF(.pdf)
  * Word（doc,docx）
  * Excel（xls,xlsx）
  * PPT(ppt,pptx)
  * CSV(.csv)
  * HTML/XML(.html,.htm,.xml)

  `storage` 支持的文件格式,文件大小限制为 128M；

  * 视频（mp4）
  * 图片（jpg/jpeg、png、webp、静态 gif）
  * 音频文件（mp3、wav），用于音色复刻时，音频时长为 5\~10 秒。

  `retrieval-image` 支持的文件格式,文件大小限制为 64M；

  * 图片（jpg、png）

## 请求响应

返回单个[File 对象](/zh/api-reference/files/object)

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    client.files.create(
        file=open("salesOverview.pdf", "rb"),
        purpose="file-extract"
    )
    ```
  </Tab>

  <Tab title="js">
    ```js theme={null}
    import OpenAI from "openai";
    import fs from "fs";

    const openai = new OpenAI({
        apiKey: "STEP_API_KEY",
        baseURL: "https://api.stepfun.com/v1"
    });

    async function main() {
        const file = await openai.files.create({
            file: fs.createReadStream("salesOverview.pdf"),
            purpose: "file-extract"
        });

        console.log(file);
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/files \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -F purpose="file-extract" \
      -F file="@salesOverview.pdf"
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
  "status": "processed"
}
```

## 备注

* 原 `purpose` 为 `retrieval`，现已废弃，建议使用 `retrieval-text` 替代。`retrieval` 将于 2025 年 5 月 15 日下线。
