<!-- title: 查询单个 Model 信息 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/models/retrieve.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 查询单个 Model 信息

查询单个 Model 的信息，包括创建时间，所属组织等。

## 请求地址

`GET https://api.stepfun.com/v1/models/{model}`

## 路径参数

* `model` `string` ***required***
  <br />
  模型唯一标识 ID

## 请求响应

返回单个[Model 对象](/zh/api-reference/models/object)

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    print(client.models.retrieve("step-3.7-flash"))
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
        const model = await openai.models.retrieve("step-3.7-flash");

        console.log(model);
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/models/step-3.7-flash \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "id": "step-3.7-flash",
  "object": "model",
  "created": 1713196800,
  "owned_by": "stepai"
}
```
