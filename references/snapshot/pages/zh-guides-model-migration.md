<!-- title: 模型迁移 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/model-migration -->
<!-- extracted: trafilatura -->

**2026 年 07 月 08 日**正式下线。模型下线后将停止推理服务，继续调用该模型的业务将无法正常返回结果。

## 下线模型与推荐替代

下表列出本次下线的模型及推荐迁移的替代模型。迁移时，只需将请求中的`model`

字段替换为对应的推荐替代模型 ID。
| 下线模型 | 推荐替代模型 |
|---|---|
`step-1-8k` |
`step-1o-turbo-vision` |

`step-1-32k`

`step-1o-turbo-vision`

`step-1v-8k`

`step-1o-turbo-vision`

`step-1v-32k`

`step-1o-turbo-vision`

`step-2-mini`

`step-1o-turbo-vision`

`step-1o-vision-32k`

`step-1o-turbo-vision`

`step-2-16k`

`step-1o-turbo-vision`

`step-3`

`step-3.7-flash`

`step-1x-medium`

`step-2x-large`

`step-1x-medium`

的推荐替代模型 `step-2x-large`

已于 2026 年 06 月 12 日结束限时免费，按实际生成图片张数计费，`0.1 元/张`

。请留意调用量与账户余额。## 如何迁移

- 对照上表，找到您正在使用的下线模型所对应的推荐替代模型。
- 将 API 请求中的
`model`

字段值替换为推荐替代模型的 ID。例如，将`step-3`

替换为`step-3.7-flash`

。 - 替代模型的能力说明见上表中各模型页链接，计费标准见
[定价与限速](https://platform.stepfun.com/docs/zh/guides/pricing/details)；建议完成业务全量验证后再切换线上流量。

[联系我们](https://platform.stepfun.com/docs/zh/guides/contact-us)获取支持。