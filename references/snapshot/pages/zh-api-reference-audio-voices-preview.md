<!-- title: 复刻试听 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/voices-preview.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 复刻试听

复刻试听接口，本 API 可以基于用户上传的参考音频（WAV、MP3），生成对应的试听音频，用于快速验证音色效果。该接口**不会创建正式音色资产**，仅用于预览效果。

### 请求地址

`POST https://api.stepfun.com/v1/audio/voices/preview`

<Note>
  Step Plan 场景请使用 `POST https://api.stepfun.com/step_plan/v1/audio/voices/preview`
</Note>

### 请求参数

* `model` `string` ***required*** <br /> 复刻使用的模型，支持 `step-tts-2`、`step-tts-mini` 和 `stepaudio-2.5-tts`。

* `file_id` `string` ***required*** <br /> 参考音频文件 ID。通过 [上传文件](/zh/api-reference/files/create) 接口获取，上传时 purpose 必须为 storage。

* `text` `string` ***optional*** <br /> 参考音频对应文本。不传则自动走 ASR 识别；为保证效果，建议传入。

* `sample_text` `string` ***required*** <br /> 试听文本，长度建议限制在 50 字以内。

* `response_format` `string` ***optional*** <br /> 返回的音频格式，支持 `wav`、`mp3`、`flac`、`opus`、`pcm`，默认为 `mp3` 格式。

* `speed` `float` ***optional*** <br /> 语速，取值范围为 0.5\~2，默认值 1.0。0.5 表示 0.5 倍速。

* `volume` `float` ***optional*** <br /> 音量，取值范围为 0.1\~2.0，默认值 1.0。0.1 表示缩小至 10% 音量；2.0 表示扩大至 200% 音量。

* `voice_label` `object` ***optional*** <br /> 音色标签，使用自定义音色时需要传入。language、emotion 和 style 三个字段同时只能有一个字段有值，暂不支持多个组合。
  * `language` `string` ***optional***<br /> 语言，支持 `粤语`、`四川话`、`日语` 三个选项。
  * `emotion` `string` ***optional***<br /> 情绪，支持 `高兴`、`生气` 等最多 11 个选项，不同模型的支持情况可参考[音色标签](/guides/developer/tts#音色标签)。
  * `style` `string` ***optional***<br /> 支持最多 17 种语速或演绎风格，不同模型的支持情况可参考[音色标签](/guides/developer/tts#音色标签)。

<Warning>
  ⚠️ 注意：`stepaudio-2.5-tts` 模型不支持该字段，若传入 `voice_label` 参数会报错。若使用 `stepaudio-2.5-tts` 模型，请直接使用 `instruction` 字段或文本内的 `()` 提示词来控制情绪与风格。
</Warning>

* `instruction` `string` ***optional*** <br /> 全局自然语言指导。仅在使用 `stepaudio-2.5-tts` 模型时生效，其他模型若传入该参数会报错。用于设定整段音频的全局情绪基调、角色人设等。最大长度限制为 200 个字符。

* `sample_rate` `integer` ***optional*** <br /> 采样率，支持 8000、16000、22050、24000、48000 五个选项。默认值为 24000。采样率越高，音质越好，但文件体积也会更大。

* `pronunciation_map` `object array` ***optional*** <br /> 定义某个文字或符号注音或发音替换规则。在中文文本中，声调用数字表示：一声为 1，二声为 2，三声为 3，四声为 4，轻声为 5。
  * `tone` `string` ***required*** <br /> 具体发音映射规则，以“/”隔开，示例：`["绯闻/fei1闻","扁舟/偏舟","嫉妒/ji2妒"]`。

* `markdown_filter` `bool` ***optional*** <br /> 是否启用 Markdown 过滤。

### 请求响应

* `sample_text` `string` <br /> 试听音频对应的文本。

* `sample_audio` `string` <br /> 试听音频的 base64 格式内容，格式为 WAV，可转换成文件后播放。

* `request_id` `string` <br /> 本次请求的唯一标识。

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl -L 'https://api.stepfun.com/v1/audio/voices/preview' \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $STEP_API_KEY" \
    -d '{
        "file_id": "file-Ckyl3cV09A",
        "model": "stepaudio-2.5-tts",
        "text": "智能阶跃，十倍每一个人的可能",
        "sample_text": "今天天气不错",
        "instruction": "语气温柔，语速偏慢"
    }'
    ```
  </Tab>
</Tabs>
