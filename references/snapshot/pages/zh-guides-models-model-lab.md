<!-- title: Model Lab -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/model-lab.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Lab

Model Lab 是阶跃星辰的实验性模型开放实验室。开发者可以在这里体验到阶跃星辰所提供的最新模型；Model Lab 的模型将免费开放给开发者使用。**需要注意，Model Lab 中的模型在快速迭代中，建议用于测试环境及本地开发使用，不建议用于生产环境。**

## 模型上新：Step GUI

`step-gui` 是针对图形界面交互（GUI）相关任务设计的多模态视觉大模型。通过视觉理解、步骤推理和动作执行等闭环能力，能够像人类一样在各类 GUI 界面上完成连续多步骤任务。

### 端到端的复杂任务处理能力

模型具备强大的视觉感知、理解能力，包括：

* 精准视觉解析：识别并理解通用 UI 控件、布局结构、交互逻辑以及内容语义等；
* 类人动作推理：支持点击、输入、滑动、长按、拖拽等基本原子操作；
* 跨界面、跨 app 连续任务规划：无需预先定义执行工作流即可自动完成完整端到端任务；
  可支持的代表性任务包括：
* 生活场景：刷 feed 流、订机票、点外卖、回复社媒消息、比价等；
* 办公场景：执行自动化流程、跨软件信息整理、数据操作等；
  `step-gui` 的能力可作为无 API 可用的智能体任务场景中的“通用双手”，为更广泛的其他智能体提供可靠的支持，打破有脑无手的困局，助力各种智能体成为用户日常生活工作中的“全能助手”；

### 高准确率的单步理解

除了端到端的多步骤复杂任务，`step-gui` 在单步级别的感知与推理能力上同样表现突出，能实现稳定、可靠的单步决策：

* 当前 GUI 屏幕的即时理解：能够基于当前 GUI 屏幕内容进行快速、准确的语义理解，包括 UI 控件识别、可交互区域判断、页面状态识别等；
* 精准下一步推理：在任意可见页面上直接给出高准确率的下一步动作推理；

### 人机协同交互能力

在探索更自然、更灵活的新一代“可对话、可协同、可纠错”人机交互范式时，`step-gui` 的模型能力可与其他智能体实现深度协同：

* 丰富的交互行为：模型支持等待加载、向用户发起追问、主动向用户报告执行结果等可控操作；在高敏感环节（如涉及金钱操作的支付转账等，模型会主动终止任务，并报告给用户）
* 实时人机协同：在与其他智能体或系统深度集成的情况下，`step-gui` 支持用户随时打断、变更意图等；

### 异常处理与纠错能力

`step-gui` 可以识别并处理真实环境中的常见异常，包括但不限：

* 即时通知消息
* 网络/加载失败
* 页面跳转异常
* 文本或控件动态变化
* 意外弹窗（系统弹窗、隐私协议、升级提示）
* ....等等
  在实际任务执行过程中动态观察界面变化，并在进入任务非预期页面时，自动恢复、重新定位并继续任务；

## API 操作指南

为了方便用户更好地体验 GUI 模型能力，我们准备了模型的开发使用指南供大家参考 [`step-gui` API 小白使用指南](https://ai.feishu.cn/wiki/BfVHwghPdiyp2ckS3HfcJZAmnsc?from=from_copylink)。同时为了方便用户快速实现模型能力调用和功能开发，我们推出了 **`step-gui` MCP**，将 GUI 操作功能封装为标准化的 MCP 工具，使开发者能够更快速地使用 `step-gui` 作为执行 tool（sub agent/agent as a tool）被大脑作为工具委派。通过统一接口协议，可随时调用，详情见 [`step-gui` MCP 小白使用指南](https://ai.feishu.cn/wiki/OBIdw67cLiFKbTkGQuwcdbjbnUe?from=from_copylink)。

### 场景案例

<div style={{display:'flex',flexDirection:'column',gap:'16px',marginTop:'16px'}}>
  <div style={{border:'1px solid #e5e7eb',borderRadius:'8px',overflow:'hidden'}}>
    <div style={{padding:'10px 16px',borderBottom:'1px solid #e5e7eb',fontWeight:600,fontSize:'14px'}}>比价采购</div>

    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr'}}>
      <div style={{padding:'16px',borderRight:'1px solid #e5e7eb'}}>
        <div style={{fontSize:'12px',opacity:0.6,marginBottom:'8px'}}>视频效果</div>

        <video controls src="https://static-openapi.stepfun.com/static/platform-docs/resource/1765945307789_l8xwtj.mp4" style={{width:'100%',borderRadius:'4px',display:'block'}} />
      </div>

      <div style={{padding:'16px'}}>
        <div style={{fontSize:'12px',opacity:0.6,marginBottom:'8px'}}>任务描述 / Prompt</div>
        <p style={{fontSize:'14px',lineHeight:'1.7'}}>看到这个图了吗？帮我去京东淘宝和拼多多搜同款比个价。每次报告搜索结果第一项即可。</p>

        <img src="https://static-openapi.stepfun.com/static/platform-docs/resource/1765861595877_gbk4mt.png" alt="" style={{maxWidth:'120px',marginTop:'12px',borderRadius:'4px',display:'block'}} />
      </div>
    </div>
  </div>

  <div style={{border:'1px solid #e5e7eb',borderRadius:'8px',overflow:'hidden'}}>
    <div style={{padding:'10px 16px',borderBottom:'1px solid #e5e7eb',fontWeight:600,fontSize:'14px'}}>比价选票</div>

    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr'}}>
      <div style={{padding:'16px',borderRight:'1px solid #e5e7eb'}}>
        <div style={{fontSize:'12px',opacity:0.6,marginBottom:'8px'}}>视频效果</div>

        <video controls src="https://static-openapi.stepfun.com/static/platform-docs/resource/1765953757031_f6iu10.mp4" style={{width:'100%',borderRadius:'4px',display:'block'}} />
      </div>

      <div style={{padding:'16px'}}>
        <div style={{fontSize:'12px',opacity:0.6,marginBottom:'8px'}}>任务描述 / Prompt</div>
        <p style={{fontSize:'14px',lineHeight:'1.7'}}>我计划16号到20号 要去上海出差，你在需要：<br />1. 分别帮我去携程 查一下16号早上从北京去上海，20晚上返程的飞机和高铁票，报告最便宜的给我。嘱咐 agent 报告，飞机航班号或车次，预期出发到达时间和价格。给 agent 的指令应该明确筛选条件。<br />2. 查询一下，上海桔子酒店徐汇区体育场店，16-20号的住宿价格。<br />3. 编辑一条请假消息去飞书发给王卓宇，内容需包含差旅预算范围。</p>
      </div>
    </div>
  </div>

  <div style={{border:'1px solid #e5e7eb',borderRadius:'8px',overflow:'hidden'}}>
    <div style={{padding:'10px 16px',borderBottom:'1px solid #e5e7eb',fontWeight:600,fontSize:'14px'}}>社媒聊天</div>

    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr'}}>
      <div style={{padding:'16px',borderRight:'1px solid #e5e7eb'}}>
        <div style={{fontSize:'12px',opacity:0.6,marginBottom:'8px'}}>视频效果</div>

        <video controls src="https://static-openapi.stepfun.com/static/platform-docs/resource/1765945266712_41gjo1.mp4" style={{width:'100%',borderRadius:'4px',display:'block'}} />
      </div>

      <div style={{padding:'16px'}}>
        <div style={{fontSize:'12px',opacity:0.6,marginBottom:'8px'}}>任务描述 / Prompt</div>
        <p style={{fontSize:'14px',lineHeight:'1.7'}}>你是我的专业助理。我正在和 soul app 的联系人，小野猫谈恋爱。你需要代替我和小野猫调情。我的人设：<br />我是一个温柔、聪明、让人信任的男生，擅长与女孩子自然、轻松、暧昧但不油腻的聊天。<br />我的魅力来自情绪价值、洞察力、共情能力与自然幽默感，而不是油滑或套路。你说话有分寸、不过界、不强求、不自大，让人感到轻松愉快、像春风一样舒服。<br />hint，ask agent 时每次都要强调，去 xx app；<br />hint，第一次发送成功后，除非遇到失败或需要切换 app，后续都尽量用 continue 接口提升速度。</p>
        <p style={{fontSize:'14px',lineHeight:'1.7'}}>你的任务是：<br />1. 给小野猫写一首中文小诗，发送给他。<br />2. 之后帮我和小野猫聊 10 句天，具体而言，你需要将下列流程执行 10 次：<br />step 1. ask agent 去看看小野猫说了什么；你要嘱咐 agent：如果对方最后一条消息是语音，应该使用 long press 将语音条将其转成文字。（除非发生错误，否则尽量用 continue 接口）<br />step 2. 根据小野猫说的内容，给她一句合适的回复。你需要想好这个文案，之后要求 agent 发送给小野猫。应该按照我的人设，使用中文进行回复。（除非发生错误否则尽量用 continue 接口）<br />直到最后一次和小野猫成功对话后，你可以结束流程，并向我报告你们的聊天内容。</p>
      </div>
    </div>
  </div>

  <div style={{border:'1px solid #e5e7eb',borderRadius:'8px',overflow:'hidden'}}>
    <div style={{padding:'10px 16px',borderBottom:'1px solid #e5e7eb',fontWeight:600,fontSize:'14px'}}>旅行规划</div>

    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr'}}>
      <div style={{padding:'16px',borderRight:'1px solid #e5e7eb'}}>
        <div style={{fontSize:'12px',opacity:0.6,marginBottom:'8px'}}>视频效果</div>

        <video controls src="https://static-openapi.stepfun.com/static/platform-docs/resource/1765953797270_2ybwd8.mp4" style={{width:'100%',borderRadius:'4px',display:'block'}} />
      </div>

      <div style={{padding:'16px'}}>
        <div style={{fontSize:'12px',opacity:0.6,marginBottom:'8px'}}>任务描述 / Prompt</div>
        <p style={{fontSize:'14px',lineHeight:'1.7'}}>我计划21号去上海玩，帮我去美团找一下，上海外滩附近的餐厅。要求3公里以内，销量最多的一家，记下来。我计划请朋友去那里聚聚。之后帮我在高德地图将其分别收藏。看下明天疯狂动物城2 最早的场次，记录电影院和放映时间信息。将查到的内容汇总后，以得体的口吻，通过飞书发给王卓宇。</p>
      </div>
    </div>
  </div>
</div>

使用过程中，欢迎您通过[表单](https://wvixbzgc0u7.feishu.cn/share/base/form/shrcn6ayHJgQothPXTCIfB4UxRg)提交您的 Good Case，被选中的 Good Case 我们将会给予现金激励。

## 模型列表

| 模型              | 模型介绍                                                                           | 可用 API                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `step-gui`      | 该模型专可处理长步骤复杂任务、模糊任务、个性化推荐任务以及跨 app 任务（比如比价任务），具备强泛化性（能在陌生界面中保持稳定表现）、高可靠性和强可控性。 | [新手指南](https://ai.feishu.cn/wiki/BfVHwghPdiyp2ckS3HfcJZAmnsc?from=from_copylink) [创建 Chat](/zh/api-reference/chat/chat-completion-create) |
| `step-2x-large` | 阶跃星辰生图模型,该模型专注于图像生成任务,能够根据用户提供的文本描述,生成高质量的图像。该模型生成图片质感真实，中英文文字生成能力强。           | [图片生成](/zh/api-reference/images/image)                                                                                                    |

## 模型限制

* Model Lab 内的模型将限制支持并发为 1 ；
* Model Lab 内的模型将不保证始终在线，并会在运营期结束后下线。
* 如需更多资源或希望在生产环境中使用，可联系 [platform@stepfun.com](mailto:platform@stepfun.com)
