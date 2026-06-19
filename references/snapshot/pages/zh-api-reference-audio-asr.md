<!-- title: 音频文件识别 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/asr.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 音频文件识别

## 产品简介

本服务提供音频文件中人声对应的语音内容识别为文本的能力，识别过程为异步进行。

核心特性：

* 支持中英文识别，暂不支持中文方言和其他语种
* 暂不支持热词

## 提交任务

用于创建一个新的语音识别任务。

### 请求说明

* **请求方法**：POST
* **请求地址**：`https://api.stepfun.com/v1/audio/asr/file/submit`
* **Content-Type**：`application/json`

### 请求头

| 参数名           | 必填 | 类型     | 说明                             |
| ------------- | -- | ------ | ------------------------------ |
| Authorization | 是  | string | 认证 Token，格式：Bearer \{API\_KEY} |
| X-Trace-Id    | 否  | string | 调用方自定义 trace id；不传则服务端生成       |
| X-Request-Id  | 否  | string | 调用方自定义 request id；不传则服务端生成     |

### 请求参数 (Body)

| 字段                       | 说明                   | 层级 | 类型     | 必填 | 备注                                          |
| ------------------------ | -------------------- | -- | ------ | -- | ------------------------------------------- |
| **audio**                | 音频流配置                | 1  | dict   | 可选 | PCM 格式必填，其他格式使用识别的结果                        |
| └ format                 | 音频容器格式               | 2  | string |    | 音频文件的容器格式。由文件上传服务识别。支持格式：wav, mp3, pcm, ogg |
| └ codec                  | 音频编码格式               | 2  | string |    | 可选：raw / opus，默认为 raw (pcm)。                |
| └ rate                   | 音频采样率                | 2  | int    |    | PCM 必填                                      |
| └ bits                   | 音频采样点位数              | 2  | int    |    | 默认为 16，暂只支持 16bits。                         |
| └ url                    | 访问的公网文件地址            | 2  | string |    | 支持格式: wav、mp3、ogg 和 pcm。文件大小限制：小于 100MB     |
| └ channel                | 音频声道数                | 2  | int    |    | 1 (单声道) / 2 (双声道)，默认为 1。必须准确填写音频文件的实际声道数。   |
| **request**              | 识别请求配置               | 1  | dict   | 是  | 核心层：用于配置模型能力和输出格式。                          |
| └ model\_name            | 模型名称                 | 2  | string | 是  | 例如：step-asr-1.1。                            |
| └ enable\_channel\_split | 启用双声道识别              | 2  | bool   |    | 默认为 false。前提条件：音频声道数 channel 必须为 2。         |
| └ show\_utterances       | 输出语音停顿、分句、分词信息及时间戳信息 | 2  | bool   |    |                                             |

### 请求示例

```http theme={null}
POST https://api.stepfun.com/v1/audio/asr/file/submit
Content-Type: application/json
Authorization: Bearer sk-xxxxxxxxxxxx
```

```json theme={null}
{
    "audio": {
        "format": "wav",
        "codec": "pcm",
        "rate": 16000,
        "bits": 16,
        "channel": 1,
        "url": "https://example.com/audio.wav"
    },
    "request": {
        "model_name": "step-asr-1.1",
        "enable_channel_split": false,
        "show_utterances": false
    }
}
```

### 返回结果

Response Body 包含任务的核心信息：

| 参数名      | 类型     | 描述              |
| -------- | ------ | --------------- |
| task\_id | string | 任务 ID，用于后续查询结果。 |

返回示例：

```json theme={null}
{
    "task_id": "018f2f1a-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

## 查询结果

根据任务 ID 查询识别进度或获取最终结果。

### 请求说明

* **请求方法**：POST
* **请求路径**：`https://api.stepfun.com/v1/audio/asr/file/query`
* **Content-Type**：`application/json`

### 请求参数

| 参数名      | 必选 | 类型     | 描述             |
| -------- | -- | ------ | -------------- |
| task\_id | 是  | string | 提交任务时返回的任务 ID。 |

### 返回参数

| 参数名                 | 层级 | 类型     | 描述               | 状态依赖                            |
| ------------------- | -- | ------ | ---------------- | ------------------------------- |
| duration            | 1  | float  | 音频时长（秒）          | 仅当识别成功时填写                       |
| result              | 1  | list   | 识别结果             | 仅当识别成功时填写                       |
| └ text              | 2  | string | 整个音频的识别结果文本      | 仅当识别成功时填写。                      |
| └ utterances        | 2  | list   | 识别结果语音分句信息       | 仅当识别成功且开启 show\_utterances 时填写。 |
|    └ text           | 3  | string | utterance 级的文本内容 | 仅当识别成功且开启 show\_utterances 时填写。 |
|    └ start\_time    | 3  | int    | 起始时间（毫秒）         | 仅当识别成功且开启 show\_utterances 时填写。 |
|    └ end\_time      | 3  | int    | 结束时间（毫秒）         | 仅当识别成功且开启 show\_utterances 时填写。 |
|    └ words          | 3  | list   | 词/字级别的文本内容       |                                 |
|       └ text        | 4  | string | 识别的文本内容          |                                 |
|       └ start\_time | 3  | int    | 起始时间（毫秒）         |                                 |
|       └ end\_time   | 3  | int    | 结束时间（毫秒）         |                                 |

### 返回示例

**示例 1：处理中**

当任务处于排队/运行中时，服务端返回 200，响应体仅包含 `status` 字段：

```json theme={null}
{"status":"RUNNING"}
```

**示例 2：处理成功**

```json theme={null}
{
    "duration": 5.901375,
    "result": [
        {
            "text": "识别出的完整文本",
            "utterances": [
                {
                    "text": "你好",
                    "start_time": 0,
                    "end_time": 500,
                    "words": [
                        {"text": "你", "start_time": 0, "end_time": 200},
                        {"text": "好", "start_time": 200, "end_time": 500}
                    ]
                }
            ]
        }
    ]
}
```

**声道拆分说明**

当 `enable_channel_split=true` 且输入为立体声时，服务端会拆分为多个声道分别识别，result 数组长度可能为 2，每个元素对应一个声道的输出。

***

## 错误处理

接口会以标准 JSON 错误响应返回失败原因（HTTP 状态码与错误结构以网关/服务端实现为准）。常见错误场景：

* **鉴权失败**：未提供或提供了错误的 `Authorization` 头（`Bearer {API_KEY}`）
* **模型不支持**：`request.model_name` 非 `step-asr-1.1`
* **限流/白名单限制**：请求被限流或不在白名单
* **任务不存在**：`task_id` 不存在或不属于当前 uid
* **任务失败**：后台处理失败（下载失败/转码失败/识别失败等）

## 使用示例

### Curl

#### 提交任务

```bash theme={null}
curl -sS -X POST "https://api.stepfun.com/v1/audio/asr/file/submit" \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer sk-xxxxxxxxxxxx' \
    -d '{
        "audio": {
            "format": "wav",
            "codec": "pcm",
            "rate": 16000,
            "bits": 16,
            "channel": 1,
            "url": "https://example.com/audio.wav"
        },
        "request": {
            "model_name": "step-asr-1.1",
            "enable_channel_split": false,
            "show_utterances": true
        }
    }'
```

返回：

```json theme={null}
{"task_id":"018f2f1a-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}
```

#### 轮询查询

```bash theme={null}
curl -sS -X POST "https://api.stepfun.com/v1/audio/asr/file/query" \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer sk-xxxxxxxxxxxx' \
    -d '{"task_id":"018f2f1a-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}'
```

### 最佳实践

1. **轮询节流**：建议 1s\~3s 轮询一次，避免过于频繁造成限流
2. **超时控制**：客户端设置总体超时，避免无限等待
3. **URL 可达性**：确保 `audio.url` 可被服务端直接下载（建议 HTTPS、可公网访问或在服务网络可访问）
4. **结果粒度**：
   * 只需要整段文本：`show_utterances=false`
   * 需要时间戳/字幕对齐：`show_utterances=true`
5. **声道拆分**：双人对话/左右声道分别录制场景可开启 `enable_channel_split=true`

#### 音频要求（建议）

* 优先使用清晰语音、较少背景噪音的录音
* 若可控制录制格式，建议：16kHz / 16bit / mono
* 立体声场景如需分别识别两路说话人，可启用声道拆分
