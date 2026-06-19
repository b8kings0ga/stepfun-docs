<!-- title: 语音合成 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/create-audio.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 语音合成

生成音频，此 API 可以使用 TTS 模型生成音频。

### 请求地址

`POST https://api.stepfun.com/v1/audio/speech`

<Note>
  Step Plan 场景请使用 `POST https://api.stepfun.com/step_plan/v1/audio/speech`
</Note>

### 请求参数

* `model` `string` ***required***<br />需要使用的模型名称，当前支持 `step-tts-2` 、 `step-tts-mini` 和 `stepaudio-2.5-tts`。

  <Note>`step-tts-vivid` 模型名称不再推荐使用，但历史用户请求仍会继续支持。</Note>

* `input` `string` ***required***<br />要生成的文本，最大长度为 1000 个字符。在使用 `stepaudio-2.5-tts` 时，括号 `()` 内的内容将作为指令处理默认不发音，如需发音请勿使用括号包裹。

* `voice` `string` ***required***<br />生成时使用的音色信息，支持[官方音色](/guides/developer/tts#支持音色)和开发者自生成音色。

* `response_format` `string` ***optional***<br />返回的音频格式，支持 `wav`,`mp3`,`flac`,`opus`,`pcm`. 默认为 `mp3` 格式

* `speed` `float` ***optional***<br />语速，取值范围为 0.5\~2，默认值 1.0。0.5 表示 0.5 倍速。

* `volume` `float` ***optional***<br />音频，取值范围为 0.1\~2.0，默认值 1.0。0.1 表示缩小至 10% 音量；2.0 表示扩大至 200% 音量。

* `voice_label` `object` ***optional***<br />音色标签，使用自定义音色时需要传入。language、emotion 和 style 三个自动同时只能有一个字段有值，暂不支持多个组合。
  * `language` `string` ***optional***<br />语言，支持 `粤语`、`四川话`、`日语` 三个选项。
  * `emotion` `string` ***optional***<br />情绪，支持 `高兴`、`生气` 等最多 11 个选项， 不同模型的支持情况可参考[音色标签](/guides/developer/tts#音色标签)
  * `style` `string` ***optional***<br />支持最多17种语速或演绎风格，不同模型的支持情况可参考[音色标签](/guides/developer/tts#音色标签)

<Warning>
  ⚠️ 注意：`stepaudio-2.5-tts` 模型不支持该字段，若传入 voice\_label 参数会报错。 若使用 `stepaudio-2.5-tts` 模型，请直接使用 `instruction` 字段或文本内的 `()` 提示词来控制情绪与风格。其他模型的支持情况可参考[音色标签](/guides/developer/tts#音色标签)。
</Warning>

* `instruction` `string` ***optional***<br />全局自然语言指导。仅在使用 `stepaudio-2.5-tts` 模型时生效，其他模型若传入该参数会报错。用于设定整段音频的全局情绪基调、角色人设等。最大长度限制为 200 个字符。

* `sample_rate` `integer` ***optional*** <br />采样率，支持 8000、16000、22050、24000、48000 五个选项。默认值为 24000。采样率越高，音质越好，但文件体积也会更大。其中 48000 为最近几次迭代新增的采样率。

* `pronunciation_map` `object array` ***optional*** <br /> 定义某个文字或符号注音或发音替换规则，在中文文本中，声调用数字表示：一声为1，二声为2，三声为3，四声为4，轻声为5。
  * `tone`  `string`  ***required*** <br /> 具体发音映射规则，以“/”隔开，示例：`["绯闻/fei1闻","扁舟/偏舟","嫉妒/ji2妒"]`

* `stream_format` `string` ***optional*** <br /> 流式返回，默认为返回语音，支持值 `sse` 和 `audio`,默认为 `audio`。当传入 `sse` 时，音频将会以 SSE 的方式返回，数据包格式如下：

  ```text theme={null}
  data: {"type":"speech.audio.delta","audio":"<BASE64 编码的音频片段>"}

  data: {"type":"speech.audio.delta","audio":"<BASE64 编码的音频片段>"}

  data: {"type":"speech.audio.done","audio":""}

  data: [DONE]
  ```

  事件类型说明：

  * `speech.audio.delta`：音频数据分片，`audio` 字段为该分片的 BASE64 编码二进制，拼接所有分片即为完整音频
  * `speech.audio.done`：生成完成，`audio` 为空字符串
  * `speech.audio.error`：生成过程中出错

* `markdown_filter` `bool` ***optional*** <br /> 是否启用 Markdown 过滤。

* `return_url` `bool` ***optional*** <br /> 仅对非流式生效，是否以 URL 而不是二进制流的形式返回，URL 12 小时内有效。

### 请求响应

音频文件

### 示例

<Tabs>
  <Tab title="python">
    ```python theme={null}
    from pathlib import Path
    from openai import OpenAI

    speech_file_path = Path(__file__).parent / "step-tts.mp3"

    client = OpenAI(
        api_key="STEP_API_KEY",
        base_url="https://api.stepfun.com/v1"
    )
    response = client.audio.speech.create(
        model="step-tts-mini",
        voice="cixingnansheng",
        input="智能阶跃，十倍每个人的可能.",
        extra_body={
            "volume": 1.0,  # volume 在拓展参数里
            "voice_label": {
                "language": "粤语",  # 可选：语言
                "emotion": "高兴",    # 可选：情感
                "style": "慢速"       # 可选：说话语速
            },
            "pronunciation_map": {
                "tone": [
                    "阿胶/e1胶",
                    "扁舟/偏舟",
                    "LOL/laugh out loudly"
                ]
            }
        }
    )
    response.stream_to_file(speech_file_path)
    ```
  </Tab>

  <Tab title="js">
    ```js theme={null}
    import OpenAI from "openai";
    import fs from "fs";
    import path from "path";

    const STEP_API_KEY = "STEP_API_KEY";
    const STEP_API_MODEL = "step-tts-mini";

    const openai = new OpenAI({
        apiKey: STEP_API_KEY,
        baseURL: "https://api.stepfun.com/v1"
    });

    async function main() {
        const speechFile = path.resolve("./speech.mp3");
        const mp3 = await openai.audio.speech.create({
            model: STEP_API_MODEL,
            voice: "cixingnansheng",
            input: "智能阶跃，十倍每个人的可能.",
            extra_body: {
                volume: 2.0, // volume 在拓展参数里
                voice_label: {
                    language: "粤语", // 可选：语言
                    emotion: "高兴",  // 可选：情感
                    style: "慢速"     // 可选：说话语速
                },
                pronunciation_map: {
                    tone: [
                        "阿胶/e1胶",
                        "扁舟/偏舟",
                        "LOL/laugh out loudly"
                    ]
                }
            }
        });
        console.log(speechFile);
        const buffer = Buffer.from(await mp3.arrayBuffer());
        await fs.promises.writeFile(speechFile, buffer);
    }

    main();
    ```
  </Tab>

  <Tab title="curl">
    ```bash theme={null}
    curl --location 'https://api.stepfun.com/v1/audio/speech' \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer $STEP_API_KEY" \
      --data '{
        "model": "step-tts-mini",
        "input": "智能阶跃，十倍每一个人的可能",
        "voice": "cixingnansheng"
      }' \
      --output "step.mp3"
    ```
  </Tab>

  <Tab title="StepAudio 2.5 TTS (python)">
    ```python theme={null}
    from pathlib import Path
    from openai import OpenAI

    speech_file_path = Path(__file__).parent / "step-tts.mp3"

    client = OpenAI(
        api_key="STEP_API_KEY",
        base_url="https://api.stepfun.com/v1"
    )
    response = client.audio.speech.create(
        # 【修改】指定为 stepaudio-2.5-tts 模型
        model="stepaudio-2.5-tts",
        voice="cixingnansheng",
        # 【修改】长度严格 <=1000 字符。括号 () 内作为指令处理不发音；需发音文本直接写（如"北京"）。
        input="（冷笑）你以为我们阶跃星辰北京公司的技术是开玩笑的吗！",
        extra_body={
            "volume": 1.0,  # volume 在拓展参数里
            # 【新增】TTS 2.5 专属全局情绪指令（限制 200 字符以内）
            "instruction": "语气极其愤怒，压迫感强，语速偏快",

            # ⚠️ 注意: stepaudio-2.5-tts 不支持 voice_label 字段，调用时请勿传入
            # "voice_label": {
            #     "language": "粤语",
            #     "emotion": "高兴",
            #     "style": "慢速"
            # },

            "pronunciation_map": {
                "tone": [
                    "阿胶/e1胶",
                    "扁舟/偏舟",
                    "LOL/laugh out loudly"
                ]
            }
        }
    )
    response.stream_to_file(speech_file_path)
    ```
  </Tab>
</Tabs>
