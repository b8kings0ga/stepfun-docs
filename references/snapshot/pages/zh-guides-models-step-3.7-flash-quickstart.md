<!-- title: 快速上手 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/step-3.7-flash-quickstart.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速上手

> 快速学会使用 Step 3.7 Flash 的原生多模态能力：图片理解和视频理解

本指南将帮助你快速上手 `step-3.7-flash` 的核心能力——**原生多模态输入**。你将学会如何让模型同时理解图片和文字、视频和文字。

<Info>所有示例都使用 Chat Completion API，模型原生支持多模态，无需额外配置视觉模型。</Info>

## 前置准备

### 1. 获取 API Key

访问 [开放平台](https://platform.stepfun.com/interface-key) 获取 API 密钥。

### 2. 安装依赖

```bash theme={null}
pip install --upgrade 'openai>=1.0'
```

## 图片理解

`step-3.7-flash` 可以直接理解图片内容，无需额外的视觉模型。

### 最小示例

<Tabs>
  <Tab title="Python">
    ```python copy theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/v1",
    )

    response = client.chat.completions.create(
        model="step-3.7-flash",
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "这张图片里是什么？请详细描述一下。"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://stepfun.com/images/sample.jpg",
                        "detail": "high"
                    }
                }
            ]
        }],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="curl">
    ```bash copy theme={null}
    curl https://api.stepfun.com/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-3.7-flash",
        "messages": [{
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "这张图片里是什么？请详细描述一下。"
            },
            {
              "type": "image_url",
              "image_url": {
                "url": "https://stepfun.com/images/sample.jpg",
                "detail": "high"
              }
            }
          ]
        }]
      }'
    ```
  </Tab>
</Tabs>

### 使用 Base64 图片

如果你的图片是本地文件，可以转换为 Base64 编码：

```python theme={null}
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image("your-image.jpg")

response = client.chat.completions.create(
    model="step-3.7-flash",
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "描述这张图片"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
    }],
)
```

### 使用 Files API 处理图片（推荐）

对于重复使用的图片，上传到阶跃文件存储可以加速访问：

```python theme={null}
# 1. 上传图片
file = client.files.create(
    file=open("sample.jpg", "rb"),
    purpose="storage"
)

# 2. 使用 file ID
response = client.chat.completions.create(
    model="step-3.7-flash",
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "分析这张图片"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"stepfile://{file.id}"
                }
            }
        ]
    }],
)
```

<Tip>
  白板转计划、票据转表格、截图生成代码等 prompt 模板见 [场景示例](/zh/guides/models/step-3.7-flash-cookbook)。
</Tip>

## 视频理解

`step-3.7-flash` 原生支持视频理解，无需额外模型。

<Info>视频建议：128 MB 以内、5 分钟以内的 MP4 格式。</Info>

### 最小示例

<Tabs>
  <Tab title="Python">
    ```python copy theme={null}
    from openai import OpenAI

    client = OpenAI(
        api_key="YOUR_STEP_API_KEY",
        base_url="https://api.stepfun.com/v1",
    )

    response = client.chat.completions.create(
        model="step-3.7-flash",
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "请概括这个视频的主要内容，并提取关键信息点。"
                },
                {
                    "type": "video_url",
                    "video_url": {
                        "url": "https://example.com/demo.mp4"
                    }
                }
            ]
        }],
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="curl">
    ```bash copy theme={null}
    curl https://api.stepfun.com/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-3.7-flash",
        "messages": [{
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "请概括这个视频的主要内容，并提取关键信息点。"
            },
            {
              "type": "video_url",
              "video_url": {
                "url": "https://example.com/demo.mp4"
              }
            }
          ]
        }]
      }'
    ```
  </Tab>
</Tabs>

<Tip>
  录屏问题诊断、操作时间线整理等 prompt 模板见 [场景示例](/zh/guides/models/step-3.7-flash-cookbook)。
</Tip>

## 控制推理强度

`step-3.7-flash` 支持三档推理强度，可根据任务复杂度选择合适档位。Chat Completion API 使用 `reasoning_effort`；Messages API 使用 `output_config.effort`。

| 强度       | 适用场景              |
| -------- | ----------------- |
| `low`    | 简单问答、摘要、改写、信息抽取   |
| `medium` | 默认推荐，适合一般推理和多步骤任务 |
| `high`   | 复杂推理、数学、规划、代码分析   |

<Tabs>
  <Tab title="Chat Completion API">
    ```bash copy theme={null}
    curl https://api.stepfun.com/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEPFUN_API_KEY" \
      -d '{
        "model": "step-3.7-flash",
        "messages": [
          {
            "role": "user",
            "content": "请用三句话解释什么是强化学习。"
          }
        ],
        "reasoning_effort": "medium",
        "max_tokens": 1024
      }'
    ```
  </Tab>

  <Tab title="Messages API">
    ```bash copy theme={null}
    curl https://api.stepfun.com/v1/messages \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEPFUN_API_KEY" \
      -d '{
        "model": "step-3.7-flash",
        "max_tokens": 1024,
        "messages": [
          {
            "role": "user",
            "content": "请用三句话解释什么是强化学习。"
          }
        ],
        "output_config": {
          "effort": "medium"
        }
      }'
    ```
  </Tab>

  <Tab title="Python">
    ```python copy theme={null}
    response = client.chat.completions.create(
        model="step-3.7-flash",
        messages=[{
            "role": "user",
            "content": "分析这个数据图表中的趋势和异常点"
        }],
        reasoning_effort="high",  # 使用高推理强度
        max_tokens=2048,
    )
    ```
  </Tab>
</Tabs>

## 常用字段速查

### image\_url 字段

| 字段       | 类型     | 必填 | 说明                                |
| -------- | ------ | -- | --------------------------------- |
| `type`   | string | 是  | 固定为 `"image_url"`                 |
| `url`    | string | 是  | 图片地址，支持 URL、Base64、`stepfile://`  |
| `detail` | string | 否  | 图片细节级别；`step-3.7-flash` 默认 `high` |

### video\_url 字段

| 字段     | 类型     | 必填 | 说明                               |
| ------ | ------ | -- | -------------------------------- |
| `type` | string | 是  | 固定为 `"video_url"`                |
| `url`  | string | 是  | 视频地址，支持 URL、Base64、`stepfile://` |

## 常见问题

### Q: 视频上传失败怎么办？

**A**: 确保视频满足以下条件：

* 格式：MP4、QuickTime（`.mov`）或 Matroska（`.mkv`）
* 大小：128 MB 以内
* 时长：5 分钟以内

如果视频超出限制，可以使用 ffmpeg 切割：

```bash theme={null}
# 切割为 2 分钟一段
ffmpeg -i input.mp4 -c copy -f segment -segment_time 120 -reset_timestamps 1 output_%d.mp4
```

### Q: 图片/视频返回速度慢？

**A**: 使用 Files API 上传文件到阶跃存储，使用 `stepfile://` 格式可以加速访问。图片任务可先把图片缩放/压缩到合适尺寸（`step-3.7-flash` 的图片 token 随分辨率变化，更小的图更快、更省）；视频任务建议控制文件大小和时长。

### Q: 如何批量处理多张图片？

**A**: 在 `content` 数组中添加多个 `image_url`：

```python theme={null}
"content": [
    {"type": "text", "text": "比较这两张图片的差异"},
    {"type": "image_url", "image_url": {"url": "image1.jpg"}},
    {"type": "image_url", "image_url": {"url": "image2.jpg"}},
]
```

### Q: 支持哪些图片格式？

**A**: 支持 JPG/JPEG、PNG、GIF、WebP 格式。

### Q: 支持哪些视频格式？

**A**: 支持 MP4、QuickTime（`.mov`）、Matroska（`.mkv`）格式。

## 下一步

<Columns cols={3}>
  <Card title="场景示例" href="/zh/guides/models/step-3.7-flash-cookbook">
    查看白板转计划、图表转数据、票据转表格等可复用任务模板。
  </Card>

  <Card title="图片理解最佳实践" href="/zh/guides/developer/image-chat">
    深入了解图片理解的参数设置、detail 模式和性能优化。
  </Card>

  <Card title="视频理解最佳实践" href="/zh/guides/developer/video-chat">
    深入了解视频理解的文件限制、价格预估和 ffmpeg 使用。
  </Card>

  <Card title="推理模型开发指南" href="/zh/guides/developer/reasoning">
    了解推理模型在复杂任务、工具调用和长上下文中的推荐用法。
  </Card>
</Columns>
