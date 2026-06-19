<!-- title: 故障排查指南 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/troubleshooting.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 故障排查指南

为了方便用户快速定位问题，阶跃星辰在[异常事件处理建议](/zh/guides/developer/exception)中提供了常见问题的处理建议。如果您在使用过程中遇到无法解决的问题，建议您先查看该页面的内容

但在您无法通过自助排查解决问题的情况下，您可以通过[联系我们](/zh/guides/contact-us)的方式与我们取得联系。请在联系时提供以下信息，以便我们更快地定位问题：

## Chat API

如果你使用的是 [Chat API](/zh/api-reference/chat/chat-completion-create) / [文生图](/zh/api-reference/images/image)/[图生图](/zh/api-reference/images/image2image)/[图片编辑](/zh/api-reference/images/edits)/[音频生成](/zh/api-reference/audio/create-audio)/[复刻音色](/zh/api-reference/audio/create-voice)/[音频转写](/zh/api-reference/audio/transcriptions)，请提供以下信息：

* 返回响应头 Header 中的 `X-Trace-Id` 字段。
* 生成结果中的 ID，即下方示例中的 `b7b56af0-52a6-483f-a589-948182676a1b`

```json theme={null}
{
	"id": "b7b56af0-52a6-483f-a589-948182676a1b",
	"object": "chat.completion",
	"created": 1709893411,
	"model": "step-3.7-flash",
	"choices": [
		{
			"index": 0,
			"message": {
				"role": "assistant",
				"content": "你好！阶跃星辰是一家专注于人工智能技术的公司，致力于开发和提供各种AI解决方案。我们的人工智能技术涵盖了自然语言处理、计算机视觉、机器学习等领域，旨在帮助用户在各个行业和领域中提高效率和创造价值。\n\n我们提供多种AI产品和服务，包括智能客服、虚拟助手、智能推荐、智能审核等。这些产品和服务可以应用于多个行业，如金融、零售、教育、医疗等。通过使用我们的AI技术，用户可以更好地理解和分析数据，提供个性化的服务和体验，提高决策效率和准确性。\n\n我们注重用户数据的安全和隐私保护，严格遵守相关法律法规和行业标准。我们相信，人工智能技术应该为人类创造更多的福祉，而不是带来负面的影响。我们将继续努力，为用户提供更加智能、高效、安全的AI解决方案。"
			},
			"finish_reason": "stop"
		}
	],
	"usage": {
		"prompt_tokens": 83,
		"completion_tokens": 176,
		"total_tokens": 259
	}
}
```

## Realtime API

如果你使用的是 [Realtime API](/zh/api-reference/realtime/chat)，请提供以下信息：

* `session.created` 和 `session.updated` 中的 `session.id` 字段,即下方示例中的 `sess_001`

```json theme={null}
{
	"event_id": "event_def",
	"type": "session.created",
	"session": {
		"id": "sess_001",
		"object": "realtime.session",
		"model": "step-1o-audio",
		"modalities": ["text", "audio"],
		"instructions": "你是由阶跃星辰提供的AI聊天助手，你擅长中文，英文，以及多种其他语言的对话。",
		"voice": "linjiajiejie",
		"input_audio_format": "pcm16",
		"output_audio_format": "pcm16",
		"max_response_output_tokens": "4096"
	}
}
```

## 流式生成音频 api

如果你使用的是 [流式生成音频 API](/zh/api-reference/audio/ws-audio)，请提供以下信息：

* 任一事件中的 `session_id` 字段，即下方示例中的 `01956e7388477cfcbdc3aaabf364bc70`

```json theme={null}
{
	"event_id": "01956e73888c7953896a6e176bf3d760",
	"type": "tts.connection.done",
	"data": {
		"session_id": "01956e7388477cfcbdc3aaabf364bc70"
	}
}
```
