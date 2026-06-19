<!-- title: 生成图片 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/images/image.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 生成图片

生成图片，请求此 API 可基于用户输入的 Prompt 生成图片

### 请求地址

`POST https://api.stepfun.com/v1/images/generations`

### 请求参数

* `model` `string` ***required***<br /> 需要使用的模型名称，当前支持：
  * `step-image-edit-2`（推荐）
  * `step-2x-large`
  * `step-1x-medium`

* `prompt` `string` ***required***<br />图像的文本描述。
  * `step-image-edit-2`：最大长度为 512 个字符。
  * `step-2x-large`：最大长度为 512 个字符。
  * `step-1x-medium`：最大长度为 512 个字符。

* `size` `string` ***optional***<br />生成的图片的大小，默认为 `1024x1024`。不同模型支持的取值如下：
  * `step-image-edit-2`（格式为 `height x width`，不是 `width x height`）：
    * 正方形：1024x1024
    * 长方形：768x1360, 896x1184, 1360x768, 1184x896
  * `step-2x-large`：
    * 正方形：256x256, 512x512, 768x768, 1024x1024
    * 长方形（16:9）：1280x800, 800x1280
  * `step-1x-medium`：
    * 正方形：256x256, 512x512, 768x768, 1024x1024
    * 长方形（16:9）：1280x800, 800x1280

* `n` `int` ***optional***<br />生成的图片数量，当前仅支持每次生成一张图片。

* `response_format` `string` ***optional***<br />生成的图片返回的格式。支持参数为 `b64_json` 或 `url`。默认为 `url`。

* `seed` `int` ***optional***<br />随机种子。
  * `step-image-edit-2`：取值范围 `[0, 2147483647]`；若不传，服务端会随机生成一个种子。
  * `step-2x-large`：当不传或传入为 0 时，使用系统随机生成的种子。
  * `step-1x-medium`：当不传或传入为 0 时，使用系统随机生成的种子。

* `steps` `int` ***optional***<br />生成步数。
  * `step-image-edit-2`：取值范围 `[1, 50]`。默认为 8。
  * `step-2x-large`：取值范围 `[1, 50]`。默认为 50。
  * `step-1x-medium`：取值范围 `[1, 50]`。默认为 50。

* `cfg_scale` `float` ***optional***<br />classifier-free guidance scale。
  * `step-image-edit-2`：必须 >= 1.0，取值范围 `[1.0, 10.0]`。默认为 1.0。
  * `step-2x-large`：取值范围 `[1, 10]`。默认为 6。
  * `step-1x-medium`：支持 1 ～ 10 之间的数字。默认为 7.5。

* `negative_prompt` `string` ***optional***<br />负面提示词，仅 `step-image-edit-2` 支持。字符数不超过 512，默认 `""`。若 `cfg_scale = 1.0`，当前实现不会把负面提示词传给底层模型。

* `text_mode` `bool` ***optional***<br />针对文字场景的优化策略，仅 `step-image-edit-2` 支持。默认 `False`，按需开启。

* `style_reference` `object` ***optional***<br />
  风格参考参数，仅 `step-1x-medium` 支持。
  <Expandable>
    * `source_url` `string` ***required***<br />风格参考图片的 URL 地址，需要是互联网可访问的；除了 URL 外，还可以是 base64。
      <br /> 1. 支持传入10Mb 以内任意大小的图像进行生成；
      <br /> 2. 支持图片格式为：png、jpeg；
      <br /> 3. base64 格式举例：data:image/jpeg;base64,base64\_string
    * `weight` `float` **optional**
      <br /> 源图片在生成时的权重。数值越大，和参数图片越相似。
      <br /> 范围：（0，2]，默认1
  </Expandable>

### 请求响应

* `created` `int`
  <br />
  创建图片时的时间戳，精确到秒级别
* `data` `object array`
  <br />
  计算 token 返回数据 - `seed` `int`
  <br />
  生成时传入的 Seed 或系统随机生成的 Seed。相同的 Seed 有助于生成类似的图片。
* `finish_reason` `string`
  <br />
  生成停止的原因，如果为 success ，则为成功生成；为 content\_filtered 表示生成成功，但命中检测所以停止。
* `b64_json`
  `string`
  <br />
  生成的图片的 Base64 编码。当 response\_format 设置为 b64\_json 时，返回此字段。
* `url` `string`
  <br />
  生成的图片的下载链接。当 response\_format 设置为 url 时，返回此字段。链接存在有效期限（当前为 30 天），建议下载保存到自己的存储以避免依赖。

```json theme={null}
{
  "created": 1589478378,
  "data": [
    {
      "b64_json": "AAAAIGZ0eXBpc29tAAACAGlzb21pc28yYXZjMW1",
      "finish_reason": "success",
      "seed": 123838
    }
  ]
}
```

### 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    STEPFUN_KEY = "STEP_API_KEY"
    STEPFUN_MODEL = "step-1x-medium"

    def generate_image(prompt, model=STEPFUN_MODEL, n=1, response_format="url",
                       size="1024x1024", steps=50, seed=11879934, cfg_scale=7.5):
        client = OpenAI(api_key=STEPFUN_KEY, base_url="https://api.stepfun.com/v1")
        image = client.images.generate(
            model=model,
            prompt=prompt,
            response_format=response_format,
            extra_body={
                "cfg_scale": cfg_scale,
                "seed": seed,
                "steps": steps
            },
            size=size,
            n=n,
        )
        return image.data

    if __name__ == "__main__":
        prompt = "采菊东篱下，悠然见南山。"
        res = generate_image(prompt)
        print(res)
    ```
  </Tab>

  <Tab title="js">
    ```js theme={null}
    import OpenAI from "openai";

    const STEP_API_KEY = "STEP_API_KEY";
    const STEP_API_MODEL = "step-1x-medium";

    const openai = new OpenAI({
        apiKey: STEP_API_KEY,
        baseURL: "https://api.stepfun.com/v1"
    });

    async function main() {
        const completion = await openai.images.generate({
            model: STEP_API_MODEL,
            prompt: "采菊东篱下，悠然见南山",
            response_format: "url",
            size: "1024x1024",
            n: 1,
            extra_body: {
                steps: 100,
                seed: 0,
                cfg_scale: 7.5
            }
        });

        console.log(JSON.stringify(completion));
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/images/generations \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-1x-medium",
        "prompt": "采菊东篱下，悠然见南山。",
        "seed": 945758,
        "response_format": "b64_json"
      }'
    ```
  </Tab>

  <Tab title="curl (step-image-edit-2)">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/images/generations \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-image-edit-2",
        "prompt": "采菊东篱下，悠然见南山",
        "response_format": "b64_json",
        "cfg_scale": 1.0,
        "steps": 8,
        "seed": 1,
        "text_mode": true
      }'
    ```
  </Tab>

  <Tab title="curl (step-2x-large)">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/images/generations \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-2x-large",
        "prompt": "采菊东篱下，悠然见南山",
        "response_format": "url",
        "size": "1024x1024",
        "cfg_scale": 6,
        "steps": 50
      }'
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "2bc5d605013969a6b79ab05b63934143.efa414e8fd5219a7a28c79d8504a9b81",
  "created": 1723595647,
  "data": [
    {
      "url": "https://res.stepfun.com/images/xxxx.jpg",
      "finish_reason": "success",
      "seed": 1764275706
    }
  ]
}
```
