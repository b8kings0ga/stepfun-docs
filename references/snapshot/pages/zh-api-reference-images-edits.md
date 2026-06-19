<!-- title: 图片编辑 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/images/edits.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 图片编辑

图片编辑 API 可基于用户输入的图片和 Prompt 对图片进行修改。

### 请求地址

`POST https://api.stepfun.com/v1/images/edits`

### 请求参数

* `model` `string` ***required*** <br />需要使用的模型名称，当前支持 `step-image-edit-2`。

* `image` `file` ***required*** <br />传入的图片文件，当前仅支持传入一个图片。最大支持 4096x4096 分辨率的输入图；支持传入图片的 Base64。

* `prompt` `string` ***required*** <br />图像的文本描述，最大长度为 512 个字符。

* `seed` `int` ***optional*** <br />随机种子，取值范围 `[0, 2147483647]`；若不传，服务端会随机生成一个种子。

* `steps` `int` ***optional*** <br />生成步数，取值范围 `[1, 50]`。默认为 8。

* `cfg_scale` `float` ***optional*** <br />classifier-free guidance scale。必须 >= 1.0，取值范围 `[1.0, 10.0]`。默认为 1.0。

* `size` `string` ***optional*** <br />编辑场景下该参数不生效，会返回和输入图一样大小的结果图。

* `negative_prompt` `string` ***optional*** <br />负面提示词。字符数不超过 512，默认 `""`。若 `cfg_scale = 1.0`，当前实现不会把负面提示词传给底层模型。

* `text_mode` `bool` ***optional*** <br />针对文字场景的优化策略。默认 `False`，按需开启。

* `response_format` `string` ***optional*** <br />
  生成的图片返回的格式。支持参数为 `b64_json` 或 `url`。默认为 `url`。

### 请求响应

* `created` `int`
  <br />
  创建图片时的时间戳，精确到秒级别
* `data` `object array`
  <br />
  计算 token 返回数据 - `seed` `int`
  <br />
  生成时传入的 Seed 或系统随机生成的 Seed。相同的 Seed 有助于生成类似的图片。 - `finish_reason` `string`
  <br />
  生成停止的原因，如果为 success ，则为成功生成；为 content\_filtered 表示生成成功，但命中检测所以停止。 - `b64_json`
  `string`
  <br />
  生成的图片的 Base64 编码。当 response\_format 设置为 b64\_json 时，返回此字段。 - `url` `string`
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
    import base64
    from openai import OpenAI

    client = OpenAI(api_key=STEP_API_KEY, base_url="https://api.stepfun.com/v1")

    prompt = """
    变成一只英短猫
    """

    result = client.images.edit(
        model="step-image-edit-2",
        image=open("cat.jpg", "rb"),
        prompt=prompt,
        response_format="b64_json",
        extra_body={
            "cfg_scale": 1.0,
            "steps": 8,
            "seed": 1
        },
    )

    print(result)
    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    # Save the image to a file
    with open("cat-on-rooftop.png", "wb") as f:
        f.write(image_bytes)
    ```
  </Tab>

  <Tab title="js">
    ```js theme={null}
    import fs from "fs";
    import OpenAI, { toFile } from "openai";

    const client = new OpenAI({
        apiKey: STEP_API_KEY,
        baseURL: "https://api.stepfun.com/v1"
    });

    const file = await toFile(fs.createReadStream("cat.jpg"), null, {
        type: "image/jpeg"
    });

    const rsp = await client.images.edit({
        model: "step-image-edit-2",
        image: file,
        prompt: "变成一只英短猫",
        // @ts-expect-error this is not yet public
        cfg_scale: 1.0,
        steps: 8,
        seed: 1,
        response_format: "b64_json"
    });

    console.log(rsp);

    // Save the image to a file
    const image_base64 = rsp.data[0].b64_json;
    const image_bytes = Buffer.from(image_base64, "base64");
    fs.writeFileSync("cat2.jpg", image_bytes);
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl -X POST "https://api.stepfun.com/v1/images/edits" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -F 'model=step-image-edit-2' \
      -F 'image=@test_cref_input02_resized.webp' \
      -F 'prompt=让图中角色骑自行车，手上举个牌子写着"沙特阿拉伯"' \
      -F 'response_format=b64_json' \
      -F 'cfg_scale=1.0' \
      -F 'steps=8' \
      -F 'seed=1' \
      -F 'text_mode=true'
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "745f66ca7f11cd5424f06b106e2e5bed.5c51cd6a807226cbd4a88c4bffe8aa38",
  "created": 1752565891,
  "data": [
    {
      "url": "https://res.stepfun.com/image_gen/20250715/sample.png",
      "finish_reason": "success",
      "seed": 1
    }
  ]
}
```
