<!-- title: 查询 Model 列表 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/models/list.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 查询 Model 列表

显示当前所有可用的模型，模型信息包括创建时间，所属组织等。

## 请求地址

`GET https://api.stepfun.com/v1/models`

## 请求参数

无

## 请求响应

返回[Model 对象](/zh/api-reference/models/object)列表

## 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    print(client.models.list())
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
        const list = await openai.models.list();

        for await (const model of list) {
            console.log(model);
        }
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl https://api.stepfun.com/v1/models \
      -H "Authorization: Bearer $STEP_API_KEY"
    ```
  </Tab>
</Tabs>

```json filename="返回" theme={null}
{
  "object": "list",
  "data": [
    {
      "id": "step-3.7-flash",
      "object": "model",
      "created": 1713196800,
      "owned_by": "stepai"
    },
    {
      "id": "step-3.5-flash",
      "object": "model",
      "created": 1713974400,
      "owned_by": "stepai"
    },
    {
      "id": "step-3.5-flash-2603",
      "object": "model",
      "created": 1711015200,
      "owned_by": "stepai"
    },
    {
      "id": "step-1o-turbo-vision",
      "object": "model",
      "created": 1711015200,
      "owned_by": "stepai"
    }
  ]
}
```
