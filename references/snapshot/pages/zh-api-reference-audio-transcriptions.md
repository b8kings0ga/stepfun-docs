<!-- title: 音频转写（逐步废弃） -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/transcriptions.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 音频转写（逐步废弃）

音频转文本，支持开发者上传音频文件，获取音频文件对应的文本内容。

<Warning>
  该接口已逐步废弃，建议优先使用「[音频文件识别](/zh/api-reference/audio/asr)」接口实现相关能力。
</Warning>

### 请求地址

`POST https://api.stepfun.com/v1/audio/transcriptions`

### 请求参数

* `model` `string` ***required***<br /> 需要使用的模型名称，固定为 `step-asr`

* `response_format` `string` ***required*** <br /> 输出的文件格式。 - 支持 `json`、`text`

* `file` `File` ***required*** <br /> 音频文件
  * 支持格式: mp3, pcm, ogg, wav
    <br />- 文件大小限制：小于 100MB

* `hotwords` `string` ***optional*** <br /> 热词列表，JSON String 格式，需要为可解析的 JSON List。如 `["1","2","3","4","abc"]`

### 请求响应

根据 `response_format`，返回对应格式的内容

<Tabs>
  <Tab title="json">
    * `text` `string`
      <br /> 识别所得文字

    ```json theme={null}
    { "text": "测试录制音频" }
    ```
  </Tab>

  <Tab title="text">
    ```text theme={null}
    测试录制音频
    ```
  </Tab>
</Tabs>

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L 'https://api.stepfun.com/v1/audio/transcriptions' \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -F 'model="step-asr"' \
      -F 'response_format="json"' \
      -F 'file=@"sample.mp3"'
    ```
  </Tab>
</Tabs>

### 废弃说明

* 本接口已逐步迭代废弃，平台不再进行功能迭代与问题优化，仅保留基础可用性
* 新增业务场景请统一使用「[音频文件识别](/zh/api-reference/audio/asr)」接口，支持更多音频参数配置、分句时间戳、声道拆分等进阶能力
* 存量业务建议尽快完成迁移，后续该接口将逐步关闭服务
