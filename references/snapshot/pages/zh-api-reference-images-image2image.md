<!-- title: 图生图 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/images/image2image.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 图生图

生成图片，请求此 API 可基于用户输入的 Prompt 和图片生成图片。

### 请求地址

`POST https://api.stepfun.com/v1/images/image2image`

### 请求参数

* `model` `string` ***required***<br />需要使用的模型名称，当前支持：
  * `step-2x-large`
  * `step-1x-medium`

* `prompt` `string` ***required***<br />图像的文本描述，最大长度为 1024 个字符

* `source_url` `string` ***required***<br />图片的 URL，需要是互联网可访问的；除了 URL 外，还可以是 base64 。
  1. 支持传入10Mb 以内任意大小的图像进行生成；
  2. 支持传图图片像素不可超过 2048x2048
  3. 支持图片格式为：png；jpeg；
  4. base64 格式举例：data:image/jpeg;base64,base64\_string

* `source_weight` `float` ***required***<br />源图片在生成时的权重。数值越小，和参数图片越相似。
  范围：（0，1]

* `size` `string` ***optional***<br />生成的图片的大小，默认为 `1024x1024`。两个模型支持的取值相同：
  <br />正方形：256x256, 512x512, 768x768, 1024x1024
  <br />长方形（16:9）：1280x800, 800x1280

* `n` `int` ***optional***<br />生成的图片数量，当前仅支持每次生成一张图片。

* `response_format` `string` ***optional***<br />生成的图片返回的格式。支持参数为 `b64_json` 或 `url`。默认为 `url`。

* `seed` `int` ***optional***<br />随机种子，当不传或传入为 0 时，使用系统随机生成的种子。

* `steps` `int` ***optional***<br />生成步数。
  * `step-2x-large`：取值范围 `[1, 100]`。默认为 50。
  * `step-1x-medium`：当前支持 1 ～ 100 之间整数。默认为 50。

* `cfg_scale` `float` ***optional***<br />classifier-free guidance scale。
  * `step-2x-large`：取值范围 `[1, 10]`。默认为 6。
  * `step-1x-medium`：当前支持 1 ～10 之间的数字。默认为 7.5。

### 请求响应

* `created` `int`<br />创建图片时的时间戳，精确到秒级别
* `data` `object array`<br />计算 token 返回数据
  * `seed` `int`<br />生成时传入的 Seed 或系统随机生成的 Seed。相同的 Seed 有助于生成类似的图片。
  * `finish_reason` `string`<br />生成停止的原因，如果为 success ，则为成功生成；为   content\_filtered 表示生成成功，但命中检测所以停止。
  * `b64_json` `string`<br />生成的图片的 Base64 编码。当 response\_format 设置为 b64\_json 时，返回此字段。
  * `url` `string`<br />生成的图片的下载链接。当 response\_format 设置为 url 时，返回此字段。链接存在有效期限（当前为 30 天），建议下载保存到自己的存储以避免依赖。

```json theme={null}
{
    "created":1589478378,
    "data":[
        {
            "b64_json":"AAAAIGZ0eXBpc29tAAACAGlzb21pc28yYXZjMW1",
            "finish_reason":"success",
            "seed":123838
        }
    ]
}
```

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
     curl https://api.stepfun.com/v1/images/image2image \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $STEP_API_KEY" \
    -d '{
    "model": "step-1x-medium",
    "prompt": "采菊东篱下，悠然见南山。",
    "source_url":"https://example.com/sample.jpg",
    "source_weight":0.5,
    "seed":945758,
    "response_format":"b64_json"
    }'
    ```

    ```json filename="返回" theme={null}
    {
        "data":[
            {
                "finish_reason":"success",
                "seed":945758,
                "b64_json":"AAAAIGZ0eXBpc29tAA..."
            }
        ]
    }
    ```
  </Tab>

  <Tab title="curl (step-2x-large)">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/images/image2image \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-2x-large",
        "prompt": "换成宫崎骏风格",
        "source_url": "https://example.com/sample.jpg",
        "source_weight": 0.5,
        "size": "1024x1024",
        "cfg_scale": 6,
        "steps": 50,
        "response_format": "url"
      }'
    ```
  </Tab>
</Tabs>
