<!-- title: 复刻音色 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/create-voice.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 复刻音色

复刻音色，本 API 可以基于之前上传的 WAV、MP3文件，复制一个新的音色，用于 [TTS 生成音频](/zh/api-reference/audio/create-audio)，或者用于 [Realtime 实时语音对话](/zh/guides/developer/realtime)。

### 请求地址

`POST https://api.stepfun.com/v1/audio/voices`

<Note>
  Step Plan 场景请使用 `POST https://api.stepfun.com/step_plan/v1/audio/voices`
</Note>

### 请求参数

* `model` `string` ***required***<br /> 需要使用的模型名称，可选项有 `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini`。

* `text` `string` **optional**<br />音频源文件对应的文本内容，如不传递，则调用系统 ASR 进行解析；为保证效果，建议传入。

* `file_id` `string` ***required*** <br /> 用于复刻音色的音频源文件的 File ID。File ID 可以通过 [上传文件](/zh/api-reference/files/create)
  获取，上传时，purpose 必须为 storage，支持文件格式为 mp3, wav。音频的时长范围应在 5 \~ 10 秒内;

### 请求响应

* `id` `string`<br /> 音色 ID，可用于后续的音频生成。

* `object` `string`<br /> 文件类型，固定为 audio.voice

* `duplicated` `boolean`<br /> 是否重复请求。如果用户二次消费，则新增此字段，告诉用户已经创建过了。

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L 'https://api.stepfun.com/v1/audio/voices' \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $STEP_API_KEY" \
    -d '{
        "file_id":"file-Ckyl3cV09A",
        "model":"step-tts-mini",
        "text":"智能阶跃，十倍每一个人的可能"
    }'
    ```
  </Tab>
</Tabs>
