<!-- title: 视频理解最佳实践 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/video-chat.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 视频理解最佳实践

阶跃星辰的 `step-3.7-flash` 和 `step-1o-turbo-vision` 模型支持视频理解能力，开发者可以在对话上下文中传入一个视频链接，模型将会自动读取视频中的内容，并基于视频中的内容进行理解，回答用户提出的问题或参与整个上下文的生成。

> 视频上传支持三种方式：可直接访问的视频 URL、Base64 内联（`data:video/mp4;base64,...`）、或通过 [Files API](/zh/api-reference/files/create) 上传后的 `stepfile://` 引用；容器格式支持 MP4、QuickTime、Matroska。

## 使用 step-3.7-flash

`step-3.7-flash` 原生支持多模态输入，通过 [Chat API](/zh/api-reference/chat/chat-completion-create) 在 `user message` 中传入 `video_url` 和你希望模型做的事情，即可让模型理解视频内容并基于其完成生成。

```bash theme={null}
curl --location 'https://api.stepfun.com/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $STEP_API_KEY" \
--data '{
    "model": "step-3.7-flash",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "video_url",
                    "video_url": {
                        "url": "https://static-openapi.stepfun.com/static/platform-web/vipcase/case1.mp4"
                    }
                },
                {
                    "type": "text",
                    "text": "请概括这个视频的主要内容，并提取关键信息点。"
                }
            ]
        }
    ]
}'
```

完整字段说明、Base64 / Files API 用法、推理强度控制见 [Step 3.7 Flash 快速上手](/zh/guides/models/step-3.7-flash-quickstart)。

## 使用 step-1o-turbo-vision

通过 [Chat API](/zh/api-reference/chat/chat-completion-create)，在 `user message` 中传入 `video_url` 格式的视频链接，并写入你希望模型做的事情，即可让大模型理解视频内容，并基于视频内容来完成生成。

比如，如下是一个简单的基于视频写游记的例子：

```bash theme={null}
curl --location 'https://api.stepfun.com/v1/chat/completions' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $STEP_API_KEY" \
--data '{
    "model": "step-1o-turbo-vision",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "video_url",
                    "video_url": {
                        "url": "https://static-openapi.stepfun.com/static/platform-web/vipcase/case1.mp4"
                    }
                },
                {
                    "type": "text",
                    "text": "你是一个文案专家，你善于通过视频分析内容里面的风景和拍摄者的风格，然后以此为基础创作文案，请根据上传的视频写一段文案，要求充满诗意和浪漫，要求文字极简。"
                }
            ]
        }
    ],
    "max_tokens": 1024
}'
```

大模型会生成如下文字返回给你：

> 在夕阳的余晖中，他们相依相偎，静享这一刻的宁静与美好。酒杯中的液体在微风中轻轻摇曳，仿佛在诉说着他们甜蜜的时光。这一刻，世界仿佛静止，只有他们的心跳声在回响。

你可以参考上述 cURL 的用法，修改 Prompt 并改成你自己想要实现的目标，来让大模型帮助你完成任务。

## 视频理解价格预估

`step-1o-turbo-vision` 的价格会受到 Prompt 长度和视频长度的影响，视频越长，价格越高。这里有一些不同长度的视频在 `step-1o-turbo-vision` 下的价格预估供你参考。

| 视频分辨率     | 视频长度  | 输入 token | 预估输入价格     |
| --------- | ----- | -------- | ---------- |
| 3840x2160 | 00:14 | 5238     | 0.013095 元 |
| 4096x2160 | 01:02 | 24064    | 0.06016元   |

`step-3.7-flash` 的定价详见 [定价详情](/zh/guides/pricing/details)。

<Card title="引入 Prompt 缓存降低费用" href="/zh/guides/developer/prompt-cache" />

## 注意事项

* 在使用时，强烈建议将视频放在指令前，这样可以让大模型获得更好的效果。
* 视频存在下载和审核的过程，耗时较长，因此在设计产品时，可设计相应的等待交互，帮助用户降低焦虑。
* `step-3.7-flash` 与 `step-1o-turbo-vision` 当前均支持单个小于 128MB 的 MP4 视频文件 URL，如果你需要上传更大的视频或其他格式，可以使用 [ffmpeg](https://www.ffmpeg.org/) 将视频切割为多个小于 128MB 的 MP4 视频，具体操作方式可参考下方说明。
* 由于视频文件需要从你的服务器下载到阶跃星辰的服务器，所以下载速度将会直接影响最终返回的速度，你可以将视频文件放在可被高速访问的地址（如对象存储），以便于阶跃星辰服务器下载视频用于视频理解。

## 常见问题

### 使用 Files API 加速视频理解

在使用视频理解时，如果传入的是外部的 URL，阶跃星辰的服务器将会请求外部 URL，获取视频内容并进行生成。生成的速度将会受到视频下载速度的影响，因此，我们推荐将视频放置在 CDN 或具有较大下载带宽的对象存储上，以便于对视频进行更快的下载。但如果你的视频需要重复使用，比如用来做 Few-shot,则可以考虑将视频使用阶跃星辰 Files API 上传至阶跃星辰文件存储服务上，以避免重复下载，产生持续的流量消耗。

<img src="https://mintcdn.com/stepfun/ivZhb9pOE5X12y-g/images/guide/video_url.png?fit=max&auto=format&n=ivZhb9pOE5X12y-g&q=85&s=7847cea6458d835d7d383e1634560e5f" alt="" width="1200" height="292" data-path="images/guide/video_url.png" />

你可以调用[上传文件](/zh/api-reference/files/create) API，并传入文件，选择 **purpose 为 storage**，上传完成后所获取的 File ID 则可以在对话过程中使用。在拿到 File ID 后，你需要在 File ID 前拼上 `stepfile://`，用于标注这个视频从阶跃星辰文件服务中获取，后续模型在推进推理时，将会从阶跃星辰文件存储服务上获取文件，从而降低下载文件所需的时间，提升整体推理的时延。

## ffmpeg 视频切割操作指南

### 切分视频文件

当你要处理的适配文件大于 128MB 时，你可以使用 ffmpeg 将视频切割为多个视频，并**通过模型将视频内容总结后，作为上下文传递在对话中**，以便于使用完整的视频进行对话。如：将 sample.mp4 切分成若干个 120 秒的视频文件。

```bash theme={null}
ffmpeg -i sample.mp4 -acodec copy -f segment -segment_time 120 -vcodec copy -reset_timestamps 1 -map 0 output_time_%d.mp4
```

### 将其他格式转换为 MP4 格式

当你需要将视频从其他格式转换为 MP4 格式时，可以通过 ffmpeg 命令进行转换。如：将 sample.mkv 转换为 sample.mp4 格式可用如下命令：

```bash theme={null}
ffmpeg -i sample.mkv -codec copy sample.mp4
```
