<!-- title: 图像模型接入 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/image-api.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 图像模型接入

Step Plan 支持图像生成 / 编辑模型通过专属路径接入。所有请求统一使用 `/step_plan/v1/...` 路径前缀，域名固定为 `https://api.stepfun.com`。

## 前置条件

1. 已订阅 [Step Plan](https://platform.stepfun.com/step-plan) 套餐
2. 已获取 [API Key](https://platform.stepfun.com/interface-key)

***

## 图像生成 / 编辑模型

### 支持的模型

| 模型                  | 说明                                                                |
| ------------------- | ----------------------------------------------------------------- |
| `step-image-edit-2` | 轻量级图像生成编辑模型，单模型同时支持文生图与图像编辑；单次编辑任务仅需 1-2 秒，输入图最大支持 4096x4096 分辨率。 |

### 接口路径

| 能力   | 请求方式 | Step Plan 路径                                              |
| ---- | ---- | --------------------------------------------------------- |
| 文生图  | POST | `https://api.stepfun.com/step_plan/v1/images/generations` |
| 图像编辑 | POST | `https://api.stepfun.com/step_plan/v1/images/edits`       |

<Info>
  接口参数与开放平台完全一致，详见各接口的 API 文档：[文生图](/zh/api-reference/images/image)、[图像编辑](/zh/api-reference/images/edits)。
</Info>

### 计费说明

计费逻辑与开放平台一致，最终按开放平台实际计费金额折算为 Step Plan 总额度消耗。具体单价请参考 [定价与限速](/zh/guides/pricing/details)。

### 示例

<Tabs>
  <Tab title="文生图 (curl)">
    ```bash theme={null}
    curl -X POST 'https://api.stepfun.com/step_plan/v1/images/generations' \
    -H 'Content-Type: application/json' \
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

  <Tab title="图像编辑 (curl)">
    ```bash theme={null}
    curl -X POST 'https://api.stepfun.com/step_plan/v1/images/edits' \
    -H "Authorization: Bearer $STEP_API_KEY" \
    -F 'model=step-image-edit-2' \
    -F 'image=@input.webp' \
    -F 'prompt=让图中角色骑自行车，手上举个牌子写着"沙特阿拉伯"' \
    -F 'response_format=b64_json' \
    -F 'cfg_scale=1.0' \
    -F 'steps=8' \
    -F 'seed=1' \
    -F 'text_mode=true'
    ```
  </Tab>

  <Tab title="Python (OpenAI SDK)">
    ```python theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/step_plan/v1",
    )

    image = client.images.generate(
        model="step-image-edit-2",
        prompt="采菊东篱下，悠然见南山",
        response_format="b64_json",
        extra_body={
            "cfg_scale": 1.0,
            "steps": 8,
            "seed": 1,
            "text_mode": True,
        },
    )

    print(image)
    ```
  </Tab>
</Tabs>
