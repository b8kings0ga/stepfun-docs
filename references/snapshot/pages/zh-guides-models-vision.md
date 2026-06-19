<!-- title: 视觉理解大模型 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/vision.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 视觉理解大模型

## 模型概览

视觉理解大模型在文本大模型的基础上，增加了图像和视频输入能力，以实现更全面、更准确的理解和推理。

当前阶跃星辰已推出 Step 系列视觉理解大模型：

## 模型列表

### Step 3.7 Flash

推荐使用。阶跃星辰的旗舰多模态推理模型，**原生支持图片和视频理解**，无需借助视觉 MCP 或额外模型，可直接完成图像 / 视频问答、跨模态分析等任务。支持三档推理强度（low/medium/high），上下文长度为 256K。详见 [Step 3.7 Flash](/zh/guides/models/step-3.7-flash)。

### Step-1o Turbo Vision

该模型拥有强大的图像理解和视频理解能力，暂时只开放文本、图像和视频输入，且仅支持文本生成。输出速度快，上下文长度为 32K。

## 关键术语

1. **图像分辨率**：通常指长宽像素数量，分辨率越高，图像能表达的信息越丰富，模型推理成本越高，如更高的网络传输时间、首字延迟和费用消耗。建议长或宽不要超过4096像素。
2. **图像的 Token 数量**：与图像的分辨率有关，目前自适应缩放到最佳大小。
3. **支持的图像格式**：JPG/JPEG、PNG、静态 GIF、WebP
4. **URL 格式**：
   * **http/https 协议的网络资源**：要求中国大陆互联网可访问，且资源加载时间会影响推理首字延迟。
   * **base64编码**：遵循 RFC2394规范，基本格式为 `data:[<mediatype>][;base64],<data>`。示例 `data:image/jpeg;base64,<base64_data_string>`
   * **参考资源**： [RFC2397](https://www.rfc-editor.org/rfc/rfc2397#section-2)、[Data URL Format](https://developer.mozilla.org/en-US/Web/HTTP/Basics_of_HTTP/Data_URLs)

## 使用限制

1. **单次请求图像数量上限**：单次请求的图像数量受模型上下文长度约束。轮次较多的对话，建议先通过多模态模型对图像进行描述或总结，再放入轮次历史作为文本理解的上下文。
2. **单次请求图像体积大小限制**：多张图片总大小控制在20M 以内。
3. **图像元数据**：模型无法获得图像元数据信息，如文件路径、文件名、文件大小、原始分辨率、作者、相机型号、地理位置信息等。在输入模型前，预处理阶段会将元数据清除，以免泄露隐私。此外，图像也会被缩放到最佳尺寸。
4. **字体过小的文本**：文字过小可能会影响识别效果。
5. **旋转和裁切**：不完整或非正位可能会影响识别效果。
6. **计数**：模型输出的数值可能不是完全精确，而是估算的值。
7. **准确性**：在某些情况下，模型可能会生成不正确的描述或标题。请勿在有严重后果的场景依赖模型推理结果。

## 模型快速入门

<Columns cols={2}>
  <Card title="从 OpenAI 迁移至阶跃星辰" href="/zh/guides/developer/openai">
    使用兼容 OpenAI 的调用方式，快速切换到视觉理解模型。
  </Card>

  <Card title="实现图片理解" href="/zh/guides/developer/image-chat">
    让模型结合图片内容进行问答、描述和多模态理解。
  </Card>

  <Card title="实现视频理解" href="/zh/guides/developer/video-chat">
    传入视频链接，让模型读取并理解视频中的关键信息。
  </Card>

  <Card title="实现多轮对话" href="/zh/guides/developer/multiple-round">
    结合上下文历史，构建连续稳定的视觉对话体验。
  </Card>

  <Card title="实现文档问答" href="/zh/guides/developer/doc-parser">
    解析文档内容并结合视觉模型完成问答、抽取和理解任务。
  </Card>

  <Card title="输出 JSON" href="/zh/guides/developer/json-mode">
    让视觉理解结果按 JSON 结构返回，方便程序处理。
  </Card>

  <Card title="流式输出" href="/zh/guides/developer/stream">
    在模型生成过程中实时返回内容，提升交互体验。
  </Card>

  <Card title="实现 Tool Call" href="/zh/guides/developer/tool-call">
    让多模态模型结合外部工具完成更复杂的任务。
  </Card>

  <Card title="实现 联网搜索" href="/zh/guides/developer/web-search">
    接入互联网搜索，为模型补充最新信息与外部知识。
  </Card>

  <Card title="Prompt 缓存" href="/zh/guides/developer/prompt-cache">
    缓存重复上下文，优化长对话和复杂多模态输入场景。
  </Card>
</Columns>
