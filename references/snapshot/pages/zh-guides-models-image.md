<!-- title: 生图改图模型列表 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/image.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 生图改图模型列表

## 模型概览

文生图模型是一种基于深度学习的模型，能够根据给定的文本描述或其他形式的输入，生成高质量、多样化的图像。生图模型在艺术创作、设计、游戏开发等领域具有广泛的应用前景。

当前阶跃星辰已推出 `step-1x`、`step-2x`、`step-image-edit-2` 系列生图改图模型：

## 模型列表

### Step Image Edit 2

阶跃星辰新一代轻量级图像生成编辑模型，单一模型同时支持**文生图**与**图像编辑**两类任务。模型在 6B 以下的参数规模内实现性能最大化，在同量级模型中展现出极强的编辑能力，并能以更小的体积实现对 12B-20B 级开源大模型的跨量级超越。在通用编辑与参考编辑场景下，其表现已足以对标国内顶尖闭源模型。得益于深度的架构优化，单次编辑任务仅需 1-2 秒，适合实时交互修图等低延迟场景。

### Step 2X Large

阶跃星辰生图模型,该模型专注于图像生成任务,能够根据用户提供的文本描述,生成高质量的图像。该模型生成图片质感真实，中英文文字生成能力强。

### Step 1X Edit

该模型专注于图像编辑任务，能够根据用户提供的图片和文本描述，对图片进行修改和增强。支持多种输入格式，包括文本描述和示例图像。模型能够理解用户的意图，并生成符合要求的图像编辑结果。

## 关键术语

1. **图像分辨率**：指生成图像的长宽像素数量，分辨率越高，图像细节越丰富，但生成时间和计算资源消耗也会增加。
2. **图像风格**：指生成图像所呈现的视觉特征和艺术效果，如写实风格、抽象风格、卡通风格等。
3. **输入描述**：指用户向模型提供的关于所需生成图像的文字描述或示例图像，描述越详细、准确，生成的图像越符合预期。
4. **模型参数量**：一般来说，参数量越大，模型的表达能力越强，能够捕捉到更丰富的图像细节和特征，从而生成更高质量的图像。目前 `step-1x` 提供 2B 参数量模型。

## 使用限制

1. **支持的输入格式**：使用自然语言描述所需生成图像的内容、风格等信息。
2. **单次请求生成图像数量上限**：`step-1x` 系列模型限制了单次请求生成的图像数量，单次最多可请求生成 1 张图像。
3. **生成图像分辨率限制**：正方形：`256x256`, `512x512`, `768x768`, `1024x1024`；长方形（16:9）：`1280x800`, `800x1280`。
4. **生成时间**：根据输入的复杂性和模型的计算能力，生成图像可能需要一些时间。
5. **生成质量**：模型生成的图像质量可能受到多种因素的影响，如输入描述的准确性、模型的训练数据等。在某些情况下，可能需要多次尝试才能获得满意的结果。
6. **版权和使用权**：生成的图像版权和使用权归用户所有，但不得用于非法或侵犯他人权益的目的。
   请注意，生图模型仍处于发展阶段，可能存在一些局限性和不确定性。在使用过程中，建议根据实际需求和场景进行评估和调整。

## API 文档

<Columns cols={3}>
  <Card title="文生图" href="/zh/api-reference/images/image" />

  <Card title="图生图" href="/zh/api-reference/images/image2image" />

  <Card title="图片编辑" href="/zh/api-reference/images/edits" />
</Columns>

## 模型快速入门

<Columns cols={2}>
  <Card title="从 OpenAI 迁移至阶跃星辰" href="/zh/guides/developer/openai">
    使用兼容 OpenAI 的调用方式，快速切换到阶跃星辰模型。
  </Card>

  <Card title="图片生成入门指南" href="/zh/guides/developer/image-generate">
    从文本提示出发生成图片，并处理生成结果与返回数据。
  </Card>

  <Card title="垫图生成指南" href="/zh/guides/developer/image-generate#垫图生成">
    基于参考图片和 Prompt 生成新的图片内容。
  </Card>

  <Card title="风格参考生成指南" href="/zh/guides/developer/image-generate#风格参考生成-sref">
    使用风格参考图控制生成图片的整体视觉风格。
  </Card>
</Columns>
