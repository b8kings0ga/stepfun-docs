<!-- title: 模型能力总览 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/overview.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 模型能力总览

export const DocsLink = ({to, children, ...rest}) => {
  const href = typeof window !== "undefined" && window.location.pathname.startsWith("/docs/") ? `/docs${to}` : to;
  return <a href={href} {...rest}>
      {children}
    </a>;
};

<section className="step-overview-board">
  <div className="step-overview-board__controls">
    <p className="step-overview-board__result">
      <span>共 5 个分类入口，便于按能力快速浏览公开模型</span>
    </p>
  </div>

  <div className="step-overview-board__tab-shell">
    <Tabs>
      <Tab title="官方推荐模型">
        <div className="step-overview-board__tab-panel">
          <section className="step-overview-section">
            <div className="step-overview-section__header">
              <p className="step-overview-section__eyebrow">推荐模型</p>
              <h2>官方推荐模型</h2>
            </div>

            <div className="step-overview-board__list">
              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">推理 / 多模态</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 3.7 Flash</p>
                          <p className="step-overview-card__subtitle">多模态推理旗舰</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">256K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">阶跃星辰旗舰多模态推理模型。在 `step-3.5-flash` 的高速推理与工具调用能力基础上，新增**原生多模态输入能力**，可直接理解图片和视频内容，无需借助视觉 MCP 或额外模型。支持三档推理强度（low/medium/high），是智能体、代码与多模态场景的快且可依赖的模型。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">推理</span>
                      <span className="step-overview-card__tag">多模态</span>
                      <span className="step-overview-card__tag">Agent</span>
                      <span className="step-overview-card__tag">图片理解</span>
                      <span className="step-overview-card__tag">视频理解</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/step-3.7-flash">
                        <p className="step-overview-card__link-type">模型页</p>
                        <p className="step-overview-card__link-label">Step 3.7 Flash</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/step-3.7-flash-quickstart">
                        <p className="step-overview-card__link-type">快速上手</p>
                        <p className="step-overview-card__link-label">多模态快速上手</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/reasoning">
                        <p className="step-overview-card__link-type">开发指南</p>
                        <p className="step-overview-card__link-label">推理模型开发指南</p>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">推理 / 文本</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 3.5 Flash 2603</p>
                          <p className="step-overview-card__subtitle">Agent 优化</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">256K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">基于 `step-3.5-flash` 针对高频 Agent 场景优化，在保留旗舰推理与工具调用能力的同时，进一步提升 Token 效率与推理速度，并支持切换低推理模式以降低消耗。对 Coding 与 Agent 框架兼容性也做了专项优化。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">推理</span>
                      <span className="step-overview-card__tag">Agent</span>
                      <span className="step-overview-card__tag">低推理模式</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/reasoning">
                        <p className="step-overview-card__link-type">模型页</p>
                        <p className="step-overview-card__link-label">推理大模型</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/reasoning">
                        <p className="step-overview-card__link-type">开发指南</p>
                        <p className="step-overview-card__link-label">推理模型开发指南</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <p className="step-overview-card__link-type">API 文档</p>
                        <p className="step-overview-card__link-label">Chat Completion API</p>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">实时语音</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 Realtime</p>
                          <p className="step-overview-card__subtitle">活人感实时语音大模型</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">交互模态</p>
                        <p className="step-overview-card__metric-value">语音 ↔ 语音</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">真正具备"活人感"的实时语音大模型。继承 StepAudio 2.5 TTS 表现力，结合行业顶级副语言感知能力——读懂语气中的迟疑与轻笑，输出契合度拉满的高情商反馈。支持千万人设完全自定义，可细颗粒度定义性格、口癖与情绪边界。适合情感陪伴、日常交流、百科问答、任务助手等实时对话场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">实时语音</span>
                      <span className="step-overview-card__tag">副语言感知</span>
                      <span className="step-overview-card__tag">人设自定义</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-realtime">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 Realtime</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/realtime">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">实时双向语音开发</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/realtime/chat">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Realtime Chat API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音对话</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 Chat</p>
                          <p className="step-overview-card__subtitle">活人感对话大模型</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">输出模态</p>
                        <p className="step-overview-card__metric-value">仅文本</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">真正具备"活人感"的对话大模型，仅文本返回。能深度理解复杂语意、机智抛梗，具备行业顶级副语言感知力——读懂语气中的迟疑与轻笑，输出高情商反馈。支持千万人设完全自定义，细颗粒度定义性格特征、专属口癖与情绪边界。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">对话</span>
                      <span className="step-overview-card__tag">副语言感知</span>
                      <span className="step-overview-card__tag">人设自定义</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-chat">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 Chat</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Chat Completion API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音合成</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 TTS</p>
                          <p className="step-overview-card__subtitle">Contextual TTS</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单次输入上限</p>
                        <p className="step-overview-card__metric-value">1000 字符</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">真正具有声音表演能力的语音合成模型，首次将语境理解能力引入语音生成全流程。通过 Global Context（全局语境）+ Inline Context（文中语境）双档控制，配合 Zero-shot Clone，让合成语音有呼吸感、轻重主次和情绪弧线，适合有声书、短剧配音、广告旁白、情感叙事等高表现力场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">Contextual TTS</span>
                      <span className="step-overview-card__tag">双档语境控制</span>
                      <span className="step-overview-card__tag">Zero-shot Clone</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/audio">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">语音大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/tts">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">语音合成开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/create-audio">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">音频合成 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音识别</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 ASR</p>
                          <p className="step-overview-card__subtitle">新一代流式 ASR 旗舰</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">模型规模</p>
                        <p className="step-overview-card__metric-value">4B MTP</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">阶跃新一代语音识别模型，4B 参数 + Multi-Token Prediction（MTP）架构，单步并行预测多个 Token，5 分钟音频 1 秒内完成转写。在保持 SOTA 转写精度的同时大幅降低时延，适合 Voice Agent、大规模批量转写、实时字幕 / 直播等场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">极速推理</span>
                      <span className="step-overview-card__tag">SOTA 精度</span>
                      <span className="step-overview-card__tag">中英双语</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-asr">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 ASR</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/asr-sse">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">语音识别（流式返回文本）</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">推理 / 文本</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 3.5 Flash</p>
                          <p className="step-overview-card__subtitle">旗舰推理</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">256K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">旗舰级推理模型，专为智能体构建而生。推理深度比肩顶尖闭源模型，同时具备极速响应与稳定可靠的工具调用能力。在通用推理能力基础之上，更擅长复杂项目规划与长程任务执行。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">推理</span>
                      <span className="step-overview-card__tag">工具调用</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/reasoning">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">推理大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/reasoning">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">推理模型开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Chat Completion API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音合成</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step TTS Mini</p>
                          <p className="step-overview-card__subtitle">高表现力 TTS</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单次输入上限</p>
                        <p className="step-overview-card__metric-value">1000 字符</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">支持中、英、日语、粤语、四川话，提供19种官方音色，兼具出色的音色复刻能力，支持中、英、日语复刻。适合客服外呼、情感陪伴、智能助手语音交互等对发音真人感要求高的场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">语音生成</span>
                      <span className="step-overview-card__tag">音色复刻</span>
                      <span className="step-overview-card__tag">情绪风格</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/audio">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">语音大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/tts">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">语音合成开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/create-audio">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">音频合成 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">图像生成 / 编辑</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step Image Edit 2</p>
                          <p className="step-overview-card__subtitle">文生图 + 图像编辑一体化</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单次响应</p>
                        <p className="step-overview-card__metric-value">1-2 秒</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">阶跃星辰最新迭代的轻量级编辑模型，单模型同时支持文生图与图像编辑。在 6B 以下参数规模内实现同量级性能标杆，可跨量级对标 12B-20B 级开源大模型，重塑实时交互修图体验。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">文生图</span>
                      <span className="step-overview-card__tag">图像编辑</span>
                      <span className="step-overview-card__tag">极速响应</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <a className="step-overview-card__link" href="/zh/guides/models/step-image-edit-2">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">Step Image Edit 2</span>
                      </a>

                      <a className="step-overview-card__link" href="/zh/guides/developer/image-edit">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">图像编辑开发指南</span>
                      </a>

                      <a className="step-overview-card__link" href="/zh/api-reference/images/edits">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">图像编辑 API</span>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </Tab>

      <Tab title="全部模型">
        <div className="step-overview-board__tab-panel">
          <section className="step-overview-section">
            <div className="step-overview-section__header">
              <p className="step-overview-section__eyebrow">全部模型</p>
              <h2>全部公开模型</h2>
            </div>

            <div className="step-overview-board__list">
              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">推理 / 多模态</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 3.7 Flash</p>
                          <p className="step-overview-card__subtitle">多模态推理旗舰</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">256K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">阶跃星辰旗舰多模态推理模型。在 `step-3.5-flash` 的高速推理与工具调用能力基础上，新增**原生多模态输入能力**，可直接理解图片和视频内容，无需借助视觉 MCP 或额外模型。支持三档推理强度（low/medium/high），是智能体、代码与多模态场景的快且可依赖的模型。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">推理</span>
                      <span className="step-overview-card__tag">多模态</span>
                      <span className="step-overview-card__tag">Agent</span>
                      <span className="step-overview-card__tag">图片理解</span>
                      <span className="step-overview-card__tag">视频理解</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/step-3.7-flash">
                        <p className="step-overview-card__link-type">模型页</p>
                        <p className="step-overview-card__link-label">Step 3.7 Flash</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/step-3.7-flash-quickstart">
                        <p className="step-overview-card__link-type">快速上手</p>
                        <p className="step-overview-card__link-label">多模态快速上手</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/reasoning">
                        <p className="step-overview-card__link-type">开发指南</p>
                        <p className="step-overview-card__link-label">推理模型开发指南</p>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">推理 / 文本</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 3.5 Flash</p>
                          <p className="step-overview-card__subtitle">旗舰推理</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">256K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">旗舰级推理模型，专为智能体构建而生。推理深度比肩顶尖闭源模型，同时具备极速响应与稳定可靠的工具调用能力。在通用推理能力基础之上，更擅长复杂项目规划与长程任务执行。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">推理</span>
                      <span className="step-overview-card__tag">工具调用</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/reasoning">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">推理大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/reasoning">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">推理模型开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Chat Completion API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">视觉</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step-1o Turbo Vision</p>
                          <p className="step-overview-card__subtitle">图像 / 视频理解</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">32K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">典型应用场景有社媒发帖文案创作、AI 问答助手、图片与视频理解等。单次请求限制输入最多60张图片，总大小控制在20M 以内，输入视频为小于128MB 的 MP4文件。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">图片理解</span>
                      <span className="step-overview-card__tag">视频理解</span>
                      <span className="step-overview-card__tag">文本生成</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/vision">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">视觉理解大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/video-chat">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">视频理解开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Chat Completion API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">图像生成 / 编辑</span>
                        <span className="step-overview-card__recommended">新一代</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step Image Edit 2</p>
                          <p className="step-overview-card__subtitle">文生图 / 编辑一体化</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">提示词上限</p>
                        <p className="step-overview-card__metric-value">512 字符</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">轻量级图像生成编辑模型，单模型同时支持文生图与图像编辑任务。6B 以下参数规模实现同量级性能标杆，可跨量级对标 12B-20B 级开源大模型；单次编辑 1-2 秒，适合实时交互修图。输入图片最大支持 4096x4096 分辨率。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">图片生成</span>
                      <span className="step-overview-card__tag">图片编辑</span>
                      <span className="step-overview-card__tag">低延迟</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/image">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">生图改图模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/image-generate">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">图片生成入门指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/images/image">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">图片生成 API</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/images/edits">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">图片编辑 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">图像生成 / 编辑</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 2X Large</p>
                          <p className="step-overview-card__subtitle">文生图</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">提示词上限</p>
                        <p className="step-overview-card__metric-value">512 / 1024 字符</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">该模型生成图片质感真实，中英文文字生成能力强。输入文本最大长度：文生图 512 字符，图生图 1024 字符；输入图片需在10Mb 以内，像素不大于2048x2048，格式为 png 或 jpeg。单次可请求生成1张图像。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">图片生成</span>
                      <span className="step-overview-card__tag">中文提示词</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/image">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">生图改图模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/image-generate">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">图片生成入门指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/images/image">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">图片生成 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">图像生成 / 编辑</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 1X Edit</p>
                          <p className="step-overview-card__subtitle">图像编辑</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">提示词上限</p>
                        <p className="step-overview-card__metric-value">512 字符</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">模型能够理解用户的意图，并生成符合要求的图像编辑结果，适合应用于图像编辑、人像美化、艺术创作等场景。输入文本最大长度为512个字符；输入图片需在10Mb 以内，像素不大于1024x1024，格式为 png 或 jpeg。单次可请求生成1张图像。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">图片编辑</span>
                      <span className="step-overview-card__tag">图像增强</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/image">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">生图改图模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/images/edits">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">图片编辑 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">实时语音</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 Realtime</p>
                          <p className="step-overview-card__subtitle">活人感实时语音大模型</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">交互模态</p>
                        <p className="step-overview-card__metric-value">语音 ↔ 语音</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">真正具备"活人感"的实时语音大模型。继承 StepAudio 2.5 TTS 表现力，结合行业顶级副语言感知能力——读懂语气中的迟疑与轻笑，输出契合度拉满的高情商反馈。支持千万人设完全自定义，可细颗粒度定义性格、口癖与情绪边界。适合情感陪伴、日常交流、百科问答、任务助手等实时对话场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">实时语音</span>
                      <span className="step-overview-card__tag">副语言感知</span>
                      <span className="step-overview-card__tag">人设自定义</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-realtime">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 Realtime</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/realtime">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">实时双向语音开发</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/realtime/chat">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Realtime Chat API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音对话</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 Chat</p>
                          <p className="step-overview-card__subtitle">活人感对话大模型</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">输出模态</p>
                        <p className="step-overview-card__metric-value">仅文本</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">真正具备"活人感"的对话大模型，仅文本返回。能深度理解复杂语意、机智抛梗，具备行业顶级副语言感知力——读懂语气中的迟疑与轻笑，输出高情商反馈。支持千万人设完全自定义，细颗粒度定义性格特征、专属口癖与情绪边界。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">对话</span>
                      <span className="step-overview-card__tag">副语言感知</span>
                      <span className="step-overview-card__tag">人设自定义</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-chat">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 Chat</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Chat Completion API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音合成</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step TTS Mini</p>
                          <p className="step-overview-card__subtitle">高表现力 TTS</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单次输入上限</p>
                        <p className="step-overview-card__metric-value">1000 字符</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">支持中、英、日语、粤语、四川话，提供19种官方音色，兼具出色的音色复刻能力，支持中、英、日语复刻。适合客服外呼、情感陪伴、智能助手语音交互等对发音真人感要求高的场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">语音生成</span>
                      <span className="step-overview-card__tag">音色复刻</span>
                      <span className="step-overview-card__tag">情绪风格</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/audio">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">语音大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/tts">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">语音合成开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/create-audio">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">音频合成 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音识别</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 ASR</p>
                          <p className="step-overview-card__subtitle">新一代流式 ASR 旗舰</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">模型规模</p>
                        <p className="step-overview-card__metric-value">4B MTP</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">阶跃新一代流式语音识别模型，基于 4B MTP 架构，在识别准确率与响应延迟之间取得良好平衡。支持中英文识别与 ITN 文本规范化，适合实时字幕、语音输入、会议记录等对识别速度与准确率均有要求的场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">高准确率</span>
                      <span className="step-overview-card__tag">低延迟</span>
                      <span className="step-overview-card__tag">中英双语</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-asr">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 ASR</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/asr-sse">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">语音识别（流式返回文本）</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音识别</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2 ASR Pro</p>
                          <p className="step-overview-card__subtitle">32B ASR Pro</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">模型规模</p>
                        <p className="step-overview-card__metric-value">32B</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">32B 参数的 ASR Pro 模型。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">大参数</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-asr">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 ASR</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/asr-sse">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">语音识别（流式返回文本）</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音识别</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step ASR</p>
                          <p className="step-overview-card__subtitle">实时 / 离线识别</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单文件上限</p>
                        <p className="step-overview-card__metric-value">100 MB</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">具有强大的中英文语音识别能力的 ASR 模型，能够自动区分语音和噪音，支持中英文混合语音识别和多种重口音普通话识别。可广泛应用于语音输入、语音控制、会议记录等场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">语音识别</span>
                      <span className="step-overview-card__tag">实时</span>
                      <span className="step-overview-card__tag">离线</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/audio">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">语音大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/asr">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">语音识别 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">实时语音</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step-1o Audio</p>
                          <p className="step-overview-card__subtitle">稳定型</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单次互动时长</p>
                        <p className="step-overview-card__metric-value">30 分钟</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">提供超低延迟的双向交互语音对话体验，支持中文、英语、重口音普通话输入，支持中、英、日语、粤语和四川话输出。单次互动时长最长30分钟，可处理音频时长最长70分钟。已在智能座舱、智能终端、社交娱乐、情感陪伴、智能客服、金融调解等行业领域落地。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">实时交互</span>
                      <span className="step-overview-card__tag">工具调用</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/realtime">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">实时语音互动模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/realtime">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">实时双向语音开发</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/realtime/chat">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Realtime Chat API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </Tab>

      <Tab title="推理">
        <div className="step-overview-board__tab-panel">
          <section className="step-overview-section">
            <div className="step-overview-section__header">
              <p className="step-overview-section__eyebrow">推理</p>
              <h2>推理模型</h2>
            </div>

            <div className="step-overview-board__list">
              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">推理 / 多模态</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 3.7 Flash</p>
                          <p className="step-overview-card__subtitle">多模态推理旗舰</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">256K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">阶跃星辰旗舰多模态推理模型。在 `step-3.5-flash` 的高速推理与工具调用能力基础上，新增**原生多模态输入能力**，可直接理解图片和视频内容，无需借助视觉 MCP 或额外模型。支持三档推理强度（low/medium/high），是智能体、代码与多模态场景的快且可依赖的模型。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">推理</span>
                      <span className="step-overview-card__tag">多模态</span>
                      <span className="step-overview-card__tag">Agent</span>
                      <span className="step-overview-card__tag">图片理解</span>
                      <span className="step-overview-card__tag">视频理解</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/step-3.7-flash">
                        <p className="step-overview-card__link-type">模型页</p>
                        <p className="step-overview-card__link-label">Step 3.7 Flash</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/step-3.7-flash-quickstart">
                        <p className="step-overview-card__link-type">快速上手</p>
                        <p className="step-overview-card__link-label">多模态快速上手</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/reasoning">
                        <p className="step-overview-card__link-type">开发指南</p>
                        <p className="step-overview-card__link-label">推理模型开发指南</p>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">推理 / 文本</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 3.5 Flash</p>
                          <p className="step-overview-card__subtitle">旗舰推理</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">256K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">旗舰级推理模型，专为智能体构建而生。推理深度比肩顶尖闭源模型，同时具备极速响应与稳定可靠的工具调用能力。在通用推理能力基础之上，更擅长复杂项目规划与长程任务执行。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">推理</span>
                      <span className="step-overview-card__tag">工具调用</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/reasoning">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">推理大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/reasoning">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">推理模型开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Chat Completion API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </Tab>

      <Tab title="视觉">
        <div className="step-overview-board__tab-panel">
          <section className="step-overview-section">
            <div className="step-overview-section__header">
              <p className="step-overview-section__eyebrow">视觉</p>
              <h2>视觉理解模型</h2>
            </div>

            <div className="step-overview-board__list">
              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">推理 / 多模态</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step 3.7 Flash</p>
                          <p className="step-overview-card__subtitle">多模态推理旗舰</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">256K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">阶跃星辰旗舰多模态推理模型。在 `step-3.5-flash` 的高速推理与工具调用能力基础上，新增**原生多模态输入能力**，可直接理解图片和视频内容，无需借助视觉 MCP 或额外模型。支持三档推理强度（low/medium/high），是智能体、代码与多模态场景的快且可依赖的模型。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">推理</span>
                      <span className="step-overview-card__tag">多模态</span>
                      <span className="step-overview-card__tag">Agent</span>
                      <span className="step-overview-card__tag">图片理解</span>
                      <span className="step-overview-card__tag">视频理解</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/step-3.7-flash">
                        <p className="step-overview-card__link-type">模型页</p>
                        <p className="step-overview-card__link-label">Step 3.7 Flash</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/step-3.7-flash-quickstart">
                        <p className="step-overview-card__link-type">快速上手</p>
                        <p className="step-overview-card__link-label">多模态快速上手</p>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/reasoning">
                        <p className="step-overview-card__link-type">开发指南</p>
                        <p className="step-overview-card__link-label">推理模型开发指南</p>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">视觉</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step-1o Turbo Vision</p>
                          <p className="step-overview-card__subtitle">图像 / 视频理解</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">最大上下文</p>
                        <p className="step-overview-card__metric-value">32K</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">典型应用场景有社媒发帖文案创作、AI 问答助手、图片与视频理解等。单次请求限制输入最多60张图片，总大小控制在20M 以内，输入视频为小于128MB 的 MP4文件。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">图片理解</span>
                      <span className="step-overview-card__tag">视频理解</span>
                      <span className="step-overview-card__tag">文本生成</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/vision">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">视觉理解大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/video-chat">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">视频理解开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Chat Completion API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </Tab>

      <Tab title="语音">
        <div className="step-overview-board__tab-panel">
          <section className="step-overview-section">
            <div className="step-overview-section__header">
              <p className="step-overview-section__eyebrow">语音</p>
              <h2>语音与实时语音模型</h2>
            </div>

            <div className="step-overview-board__list">
              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">实时语音</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 Realtime</p>
                          <p className="step-overview-card__subtitle">活人感实时语音大模型</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">交互模态</p>
                        <p className="step-overview-card__metric-value">语音 ↔ 语音</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">真正具备"活人感"的实时语音大模型。继承 StepAudio 2.5 TTS 表现力，结合行业顶级副语言感知能力——读懂语气中的迟疑与轻笑，输出契合度拉满的高情商反馈。支持千万人设完全自定义，可细颗粒度定义性格、口癖与情绪边界。适合情感陪伴、日常交流、百科问答、任务助手等实时对话场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">实时语音</span>
                      <span className="step-overview-card__tag">副语言感知</span>
                      <span className="step-overview-card__tag">人设自定义</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-realtime">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 Realtime</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/realtime">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">实时双向语音开发</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/realtime/chat">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Realtime Chat API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音对话</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 Chat</p>
                          <p className="step-overview-card__subtitle">活人感对话大模型</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">输出模态</p>
                        <p className="step-overview-card__metric-value">仅文本</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">真正具备"活人感"的对话大模型，仅文本返回。能深度理解复杂语意、机智抛梗，具备行业顶级副语言感知力——读懂语气中的迟疑与轻笑，输出高情商反馈。支持千万人设完全自定义，细颗粒度定义性格特征、专属口癖与情绪边界。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">对话</span>
                      <span className="step-overview-card__tag">副语言感知</span>
                      <span className="step-overview-card__tag">人设自定义</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-chat">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 Chat</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/chat/chat-completion-create">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Chat Completion API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音合成</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 TTS</p>
                          <p className="step-overview-card__subtitle">Contextual TTS</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单次输入上限</p>
                        <p className="step-overview-card__metric-value">1000 字符</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">真正具有声音表演能力的语音合成模型，首次将语境理解能力引入语音生成全流程。通过 Global Context（全局语境）+ Inline Context（文中语境）双档控制，配合 Zero-shot Clone，让合成语音有呼吸感、轻重主次和情绪弧线，适合有声书、短剧配音、广告旁白、情感叙事等高表现力场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">Contextual TTS</span>
                      <span className="step-overview-card__tag">双档语境控制</span>
                      <span className="step-overview-card__tag">Zero-shot Clone</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/audio">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">语音大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/tts">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">语音合成开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/create-audio">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">音频合成 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音合成</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step TTS Mini</p>
                          <p className="step-overview-card__subtitle">高表现力 TTS</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单次输入上限</p>
                        <p className="step-overview-card__metric-value">1000 字符</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">支持中、英、日语、粤语、四川话，提供19种官方音色，兼具出色的音色复刻能力，支持中、英、日语复刻。适合客服外呼、情感陪伴、智能助手语音交互等对发音真人感要求高的场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">语音生成</span>
                      <span className="step-overview-card__tag">音色复刻</span>
                      <span className="step-overview-card__tag">情绪风格</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/audio">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">语音大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/tts">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">语音合成开发指南</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/create-audio">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">音频合成 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音识别</span>
                        <span className="step-overview-card__recommended">推荐</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2.5 ASR</p>
                          <p className="step-overview-card__subtitle">新一代流式 ASR 旗舰</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">模型规模</p>
                        <p className="step-overview-card__metric-value">4B MTP</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">阶跃新一代流式语音识别模型，基于 4B MTP 架构，在识别准确率与响应延迟之间取得良好平衡。支持中英文识别与 ITN 文本规范化，适合实时字幕、语音输入、会议记录等对识别速度与准确率均有要求的场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">高准确率</span>
                      <span className="step-overview-card__tag">低延迟</span>
                      <span className="step-overview-card__tag">中英双语</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-asr">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 ASR</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/asr-sse">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">语音识别（流式返回文本）</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音识别</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">StepAudio 2 ASR Pro</p>
                          <p className="step-overview-card__subtitle">32B ASR Pro</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">模型规模</p>
                        <p className="step-overview-card__metric-value">32B</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">32B 参数的 ASR Pro 模型。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">大参数</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/stepaudio-2.5-asr">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">StepAudio 2.5 ASR</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/asr-sse">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">语音识别（流式返回文本）</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">语音识别</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step ASR</p>
                          <p className="step-overview-card__subtitle">实时 / 离线识别</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单文件上限</p>
                        <p className="step-overview-card__metric-value">100 MB</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">具有强大的中英文语音识别能力的 ASR 模型，能够自动区分语音和噪音，支持中英文混合语音识别和多种重口音普通话识别。可广泛应用于语音输入、语音控制、会议记录等场景。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">语音识别</span>
                      <span className="step-overview-card__tag">实时</span>
                      <span className="step-overview-card__tag">离线</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/audio">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">语音大模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/audio/asr">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">语音识别 API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>

              <div className="step-overview-card">
                <div className="step-overview-card__summary step-overview-card__summary--static">
                  <div className="step-overview-card__summary-top">
                    <div className="step-overview-card__main">
                      <div className="step-overview-card__eyebrow">
                        <span className="step-overview-card__family">实时语音</span>
                      </div>

                      <div className="step-overview-card__heading">
                        <div>
                          <p className="step-overview-card__title">Step-1o Audio</p>
                          <p className="step-overview-card__subtitle">稳定型</p>
                        </div>
                      </div>
                    </div>

                    <div className="step-overview-card__aside">
                      <div className="step-overview-card__metric">
                        <p className="step-overview-card__metric-label">单次互动时长</p>
                        <p className="step-overview-card__metric-value">30 分钟</p>
                      </div>
                    </div>
                  </div>

                  <div className="step-overview-card__summary-body">
                    <p className="step-overview-card__summary-text">提供超低延迟的双向交互语音对话体验，支持中文、英语、重口音普通话输入，支持中、英、日语、粤语和四川话输出。单次互动时长最长30分钟，可处理音频时长最长70分钟。已在智能座舱、智能终端、社交娱乐、情感陪伴、智能客服、金融调解等行业领域落地。</p>

                    <div className="step-overview-card__tags">
                      <span className="step-overview-card__tag">实时交互</span>
                      <span className="step-overview-card__tag">工具调用</span>
                    </div>
                  </div>
                </div>

                <div className="step-overview-card__details step-overview-card__details--static">
                  <div className="step-overview-card__details-block">
                    <p className="step-overview-card__block-title">相关入口</p>

                    <div className="step-overview-card__links">
                      <DocsLink className="step-overview-card__link" to="/zh/guides/models/realtime">
                        <span className="step-overview-card__link-type">模型页</span>
                        <span className="step-overview-card__link-label">实时语音互动模型</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/guides/developer/realtime">
                        <span className="step-overview-card__link-type">开发指南</span>
                        <span className="step-overview-card__link-label">实时双向语音开发</span>
                      </DocsLink>

                      <DocsLink className="step-overview-card__link" to="/zh/api-reference/realtime/chat">
                        <span className="step-overview-card__link-type">API 文档</span>
                        <span className="step-overview-card__link-label">Realtime Chat API</span>
                      </DocsLink>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </Tab>
    </Tabs>
  </div>
</section>
