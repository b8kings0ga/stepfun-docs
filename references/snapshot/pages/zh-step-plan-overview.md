<!-- title: Step Plan 概述 -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/overview.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Step Plan 概述

Step Plan 是阶跃星辰开放平台推出的订阅制服务，让您在主流编码工具与智能体平台（如 OpenClaw、Claude Code、Trae、Cursor 等）中，以订阅价格调用阶跃星辰的旗舰模型。订阅后通过专用 API Key 接入，按月获得统一的模型调用额度。

<Note>
  Step Plan 已升级为 **Credit 月池** 计费：额度以 Credit 为单位按月发放、月内灵活消耗。若您此前订阅的是旧版按请求次数限额的套餐，请参阅 [Step Plan 升级公告](/zh/step-plan/upgrade-notice) 了解差异与升级方式。
</Note>

## 主要特性

* **统一计费单位**：以 Credit 衡量所有模型的用量，无需分别记忆每个模型的价格。
* **默认高速模型体验**：所有档位均提供统一的高速模型性能，不对速度额外收费。
* **月池额度，灵活消耗**：Credit 按月一次性发放，月内任意时段消耗，不受时段或请求频次限制。
* **超额可加购**：当月额度用尽后，可加购加油包补充额度，无需等待次月。
* **全平台可用**：不限制使用平台，一个订阅覆盖主流编码与智能体工具链。
* **覆盖多类模型**：涵盖文本、推理、语音、图像编辑与智能路由等旗舰模型，并将持续扩展。

## 计费方式

Step Plan 以 **Credit** 作为统一计费单位。调用任意模型时，用量都会换算为 Credit，从当月额度中扣减。

Credit 与支付金额按 **1M Credit = ¥1** 换算（即 100 万 Credit 对应 ¥1 的模型用量）。各档位提供的用量高低，取决于其每月发放的 Credit 数量。

订阅后，Credit 一次性发放至当月「月池」，**月内任意时段消耗，月末清零、不结转至下一周期**。

### 扣费顺序

当账户中同时存在月池 Credit 与加油包 Credit 时，按到期时间先后消耗，**优先扣减先到期的额度**。其中月池 Credit 以当月清零日为到期时间，加油包 Credit 以其各自的 30 天到期日为准。

## 套餐档位

Step Plan 提供四个档位，区别在于每月发放的 Credit 额度与价格；各档位均提供统一的高速模型性能。

| 档位             | 适用人群           | 月度 Credit | 月付   | 季付    | 年付    |
| -------------- | -------------- | --------- | ---- | ----- | ----- |
| **Flash Mini** | 入门体验 AI 的用户    | 400M      | ¥49  | ¥129  | ¥456  |
| **Flash Plus** | 日常使用 AI 提效的用户  | 1600M     | ¥99  | ¥269  | ¥936  |
| **Flash Pro**  | 高频使用 AI 的深度用户  | 8000M     | ¥199 | ¥539  | ¥1860 |
| **Flash Max**  | 高强度使用 AI 的专业用户 | 40000M    | ¥699 | ¥1889 | ¥6666 |

季付 / 年付为对应周期一次性支付，Credit 仍按月发放到账（季付 = 月度 Credit × 3 个月，年付 = 月度 Credit × 12 个月）。表中 M 表示百万（Million）Credit。

各档位均包含：支持全部旗舰模型与智能路由、覆盖多款 MCP 工具、多设备登录，以及在 [Studio](https://studio.stepfun.com) 额外赠送相当于套餐 40% 的专属创作额度。Flash Plus 及以上档位另含优先 API 速率与优先技术支持。

## 加油包

当月月池 Credit 用尽后，可加购加油包补充额度，无需等待次月发放。加油包仅向已订阅 Step Plan 的用户开放，周期单独 30 天，与套餐到期时间相互独立。

| 加油包 | 价格  | Credit |
| --- | --- | ------ |
| 小油包 | ¥49 | 400M   |
| 大油包 | ¥99 | 1600M  |

## 支持的模型

Step Plan 当前支持以下旗舰模型，覆盖文本、推理、语音、图像编辑与智能路由等场景。各模型的能力说明与参数详见[模型列表](/zh/guides/models/overview)。

* [`step-3.7-flash`](/zh/guides/models/step-3.7-flash)：旗舰多模态推理模型
* [`step-3.5-flash`](/zh/guides/models/step-3.5-flash)：面向智能体与代码任务的高速模型
* `step-3.5-flash-2603`：针对高频 Agent 场景优化的版本
* [`stepaudio-2.5-realtime`](/zh/guides/models/stepaudio-2.5-realtime)：端到端实时语音对话模型
* [`stepaudio-2.5-chat`](/zh/guides/models/stepaudio-2.5-chat)：端到端语音对话大模型
* [`stepaudio-2.5-tts`](/zh/guides/models/stepaudio-2.5-tts)：新一代 Contextual TTS 模型
* [`stepaudio-2.5-asr`](/zh/guides/models/stepaudio-2.5-asr)：新一代自动语音识别模型
* [`step-router-v1`](/zh/guides/models/step-router)：智能路由模型，按任务复杂度自动调度
* [`step-image-edit-2`](/zh/guides/models/step-image-edit-2)：轻量级文生图与图像编辑模型

后续将逐步引入更多阶跃旗舰模型。

## 接入与使用

订阅后获取专用 API Key，并在所用工具中将 Base URL 配置为 Step Plan 专用地址 `https://api.stepfun.com/step_plan/v1`（注意区别于普通 API 的 `https://api.stepfun.com/v1`）。Step Plan 可在 OpenClaw、Claude Code 等智能体工具，以及 Cline、Kilo Code、Roo Code 等编码工具中使用，各工具的具体配置方法详见[接入指南](/zh/step-plan/quick-start)。

## 常见问题

<AccordionGroup>
  <Accordion title="Step Plan 与直接调用 API 有什么区别？">
    Step Plan 采用订阅制，以月度 Credit 额度提供相比按量付费更高的用量；额度按月发放、月内任意时段消耗，便于控制成本。两者使用不同的 Base URL，互不影响。
  </Accordion>

  <Accordion title="Credit 是怎么计费的？">
    Credit 是 Step Plan 的统一计费单位，按各模型的用量换算扣减。Credit 与支付金额按 1M Credit = ¥1 换算，订阅后按月发放至月池，月内消耗、月末清零。
  </Accordion>

  <Accordion title="月池 Credit 可以累积到下个月吗？">
    不可以。月池 Credit 月末清零、不结转至下一周期。加油包为独立的 30 天周期，按各自到期时间计算。
  </Accordion>

  <Accordion title="当月 Credit 用完了怎么办？">
    可加购加油包补充额度（小油包 ¥49 / 400M、大油包 ¥99 / 1600M，周期单独 30 天），或等待次月额度重新发放。
  </Accordion>

  <Accordion title="Step Plan 会受到充值阶梯限速（RPM / TPM）的约束吗？">
    不会。Step Plan 不适用开放平台按累计充值金额划分的[阶梯限速](/zh/guides/pricing/details#阶梯限速)，用量由所订阅档位的月度 Credit 额度管理。
  </Accordion>

  <Accordion title="Step Plan 订阅与账户余额是什么关系？">
    两者是相互独立的体系。使用 Step Plan 内功能消耗的是订阅自身的 Credit 额度，不会扣除账户余额。当前已支持用账户余额（充值金额）兑换 Step Plan 订阅。
  </Accordion>

  <Accordion title="支持哪些支付方式？">
    国内支持微信、支付宝，以及用账户余额兑换订阅；海外支持通过 Stripe 支付。
  </Accordion>

  <Accordion title="可以取消订阅吗？">
    可以，随时取消。已支付费用不退还，取消后服务持续至当前计费周期结束。
  </Accordion>

  <Accordion title="Step Plan 使用哪个 Base URL？">
    请使用 Step Plan 专用地址 `https://api.stepfun.com/step_plan/v1`，而非普通 API 的 `https://api.stepfun.com/v1`。使用错误地址会导致请求报错。
  </Accordion>

  <Accordion title="第三方工具接入报错怎么办？">
    请依次排查：确认 Base URL 是否使用了专用地址 `https://api.stepfun.com/step_plan/v1`（常见问题点）；参考[接入指南](/zh/step-plan/quick-start)重新配置；仍有问题可提供报错截图协助排查。
  </Accordion>

  <Accordion title="Step Plan 支持 MCP 吗？">
    支持。首个官方 MCP Server 为 [StepSearch](/zh/step-plan/integrations/search-mcp)，提供 `web_search` 与 `web_fetch`，可在 Claude Code、Cline、OpenCode 等兼容 MCP 的客户端中使用。更多 MCP 将陆续上线。
  </Accordion>

  <Accordion title="未来还会加入更多模型吗？">
    会。Step Plan 将逐步扩展至更多现有和未来的阶跃旗舰模型。
  </Accordion>
</AccordionGroup>
