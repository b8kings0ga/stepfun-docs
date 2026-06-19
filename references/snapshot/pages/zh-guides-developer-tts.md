<!-- title: 音频合成最佳实践 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/tts.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 音频合成最佳实践

阶跃星辰为开发者提供了语音互动模型，开发者可以使用阶跃星辰的语音互动模型来完成音频生成、[音色复刻](/zh/api-reference/audio/create-voice)、[语音识别](/zh/api-reference/audio/transcriptions)的能力，帮助开发者可以在自己的应用中除了实现标准的大模型的理解能力，还可以实现语音交互。

## 快速开始

### 快速生成一段音频

复制如下代码，你可以快速生成一段音频文件。

```bash theme={null}
curl --location 'https://api.stepfun.com/v1/audio/speech' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $STEP_API_KEY" \
--data '{
    "model":"step-tts-mini",
    "input":"智能阶跃，十倍每一个人的可能",
    "voice":"cixingnansheng"
}'\
--output "step.mp3"
```

<div id="支持音色" />

## 场景与官方音色推荐

阶跃星辰为开发者提供了七大场景数十种官方推荐音色，你可以在这里试听不同的音色，并在 API 当中调用。
但我们强烈建议您通过 [音色复刻](/zh/api-reference/audio/create-voice) 的能力，定制您的专属音色。`step-tts-2` 具备业界领先的复刻性能，且复刻音色可 0 成本支持全部情绪、风格控制。

### 1. 营销场景

营销场景需要音色具有感染力、说服力和亲和力，能够有效传递产品价值并激发购买欲望。`step-tts-2` 特色在于能够给出饱满的情绪，给用户以信任感和专业度，让营销内容更具吸引力。

| 推荐模型                                                 | 推荐音色 | Voice-id            | 合成示例                                                                                                                                                                                                                                                                                                                                                                            |
| :--------------------------------------------------- | :--- | :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 活力轻快 | livelybreezy-female | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764227859773_6r0lga.wav" target="_blank" rel="noopener noreferrer">我们的在线课程帮助数千人实现了职业突破，下一个成功的就是您！</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764227873237_xbptdq.wav" target="_blank" rel="noopener noreferrer">精致的设计，贴心的细节，让每一件产品都成为您生活中的艺术品。</a>          |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 正派青年 | zhengpaiqingnian    | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764227897199_sz9mse.wav" target="_blank" rel="noopener noreferrer">限时优惠仅剩最后3天！现在购买即可享受买一送一超值福利，错过不再有！</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764227907908_w73z24.wav" target="_blank" rel="noopener noreferrer">想象一下，每天清晨被温暖的阳光唤醒，我们的智能窗帘为您开启美好的一天。</a> |

### 2. 客服场景（电话催收等）

客服场景需要音色亲切、耐心、专业，能够有效安抚用户情绪并提供清晰解决方案。我们提供两种类型的客服音色，`step-tts-2` 音质突出、情绪饱满、真人感强，前四个推荐音色非常适合电话场景。

| 推荐模型                                                 | 推荐音色 | Voice-id             | 合成示例                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :--------------------------------------------------- | :--- | :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stepaudio-2.5-tts` / `step-tts-2`                   | 爽快男声 | shuangkuainansheng   | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232419372_cjweb4.wav" target="_blank" rel="noopener noreferrer">【催收场景】您好，请问是张先生吗？这里是催债公司客服，关于您账户尾号1788的款项，想跟您做个温馨提醒，目前已经逾期5天了。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232431616_d45kct.wav" target="_blank" rel="noopener noreferrer">感谢您的来电，我是客服专员张明，工号2087，请问怎么称呼您？</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232439733_ucrkox.wav" target="_blank" rel="noopener noreferrer">关于您查询的账单问题，我这边可以看到具体明细，现在为您详细说明。</a> |
| `stepaudio-2.5-tts` / `step-tts-2`                   | 干练女声 | ganliannvsheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232450294_e3wqt8.wav" target="_blank" rel="noopener noreferrer">【催收场景】孙女士，这次逾期可能会对您的个人信用记录产生负面影响，我们希望能协助您避免这个问题。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232467535_p2pu4n.wav" target="_blank" rel="noopener noreferrer">您好，欢迎致电客户服务中心，我是您的专属客服李静，很高兴为您服务。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232485079_rarrcy.wav" target="_blank" rel="noopener noreferrer">请您提供一下手机号码和身份证后四位，我来为您核实账户信息。</a>                |
| `stepaudio-2.5-tts` / `step-tts-2`                   | 亲和女声 | qinhenvsheng         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232648658_g46auz.wav" target="_blank" rel="noopener noreferrer">【催收场景】如果目前全额还款有压力，我们可以先安排处理一部分，比如先还3万元，剩余部分我们再协商一个方案，您看可以吗？</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232658059_p1hw59.wav" target="_blank" rel="noopener noreferrer">听到您的情况我很关切，请相信我们会尽全力帮助您。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232666804_uxi2nq.wav" target="_blank" rel="noopener noreferrer">这个情况确实比较特殊，请允许我请示主管后给您回电解答。</a>                |
| `stepaudio-2.5-tts` / `step-tts-2`                   | 活力女声 | huolinvsheng         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232752142_umr3gn.wav" target="_blank" rel="noopener noreferrer">【催收场景】“您说‘马上处理’具体是指今天下午几点前呢？我需要记录一个确切的时间点，以便后续为您跟进服务。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232784129_7y8d7t.wav" target="_blank" rel="noopener noreferrer">很高兴能为您解决问题，祝您有美好的一天，再见！</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232765549_zhtxfv.wav" target="_blank" rel="noopener noreferrer">我们的服务时间是早8点到晚10点，欢迎再次来电。</a>                         |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 气质温婉 | elegantgentle-female | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232963968_2lpzrh.wav" target="_blank" rel="noopener noreferrer">您的满意是我们最大的追求，感谢您选择我们的服务。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764232975950_nb22zj.wav" target="_blank" rel="noopener noreferrer">我完全理解您的情况，让我们一起来看看如何最好地解决这个问题。</a>                                                                                                                                                                                                                                |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 活力轻快 | livelybreezy-female  | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233092953_7uj9hs.wav" target="_blank" rel="noopener noreferrer">您的满意是我们最大的追求，感谢您选择我们的服务。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233081037_2uelez.wav" target="_blank" rel="noopener noreferrer">我完全理解您的情况，让我们一起来看看如何最好地解决这个问题。</a>                                                                                                                                                                                                                                |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔男声 | wenrounansheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233106756_zi400x.wav" target="_blank" rel="noopener noreferrer">非常理解您的心情，我们会尽快为您解决这个问题。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233116023_vvny08.wav" target="_blank" rel="noopener noreferrer">您的订单已经处理完成，预计明天下午就能送达，请您注意查收。</a>                                                                                                                                                                                                                                  |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 经典女声 | jingdiannvsheng      | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233202847_b14wof.wav" target="_blank" rel="noopener noreferrer">您的满意是我们最大的追求，感谢您选择我们的服务。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233185685_fx2jym.wav" target="_blank" rel="noopener noreferrer">我完全理解您的情况，让我们一起来看看如何最好地解决这个问题。</a>                                                                                                                                                                                                                                |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔熟女 | wenroushunv          | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233217617_grbf54.wav" target="_blank" rel="noopener noreferrer">您的满意是我们最大的追求，感谢您选择我们的服务。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233227812_ca92c6.wav" target="_blank" rel="noopener noreferrer">我完全理解您的情况，让我们一起来看看如何最好地解决这个问题。</a>                                                                                                                                                                                                                                |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 甜美女声 | tianmeinvsheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233448772_4id5xn.wav" target="_blank" rel="noopener noreferrer">您的满意是我们最大的追求，感谢您选择我们的服务。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233457923_qdn6vq.wav" target="_blank" rel="noopener noreferrer">我完全理解您的情况，让我们一起来看看如何最好地解决这个问题。</a>                                                                                                                                                                                                                                |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 清纯少女 | qingchunshaonv       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233506642_dd78q1.wav" target="_blank" rel="noopener noreferrer">您的满意是我们最大的追求，感谢您选择我们的服务。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233498003_buc059.wav" target="_blank" rel="noopener noreferrer">我完全理解您的情况，让我们一起来看看如何最好地解决这个问题。</a>                                                                                                                                                                                                                                |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 元气男声 | yuanqinansheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233516928_rpphje.wav" target="_blank" rel="noopener noreferrer">非常理解您的心情，我们会尽快为您解决这个问题。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764233522624_r33ce3.wav" target="_blank" rel="noopener noreferrer">您的订单已经处理完成，预计明天下午就能送达，请您注意查收。</a>                                                                                                                                                                                                                                  |

### 3. 有声书场景

有声书需要音色富有表现力、感染力，能够生动展现不同角色和情节氛围。我们的 TTS 特色在于细腻的情感表达和多变的语音风格，让听众沉浸于故事世界。

| 推荐模型                                                 | 推荐音色 | Voice-id         | 合成示例                                                                                                                                                                                                                                                                                                                                                                      |
| :--------------------------------------------------- | :--- | :--------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 儒雅男士 | ruyananshi       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231706722_cerhao.wav" target="_blank" rel="noopener noreferrer">“老人的眼中闪烁着智慧的光芒，缓缓道出那个埋藏千年的秘密。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231727050_6znwwg.wav" target="_blank" rel="noopener noreferrer">“狂风呼啸，海浪拍打着船舷，水手们紧紧抓住缆绳，与命运抗争。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔女声 | wenrounvsheng    | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231734698_puka7d.wav" target="_blank" rel="noopener noreferrer">“魔法森林中，精灵们跳着轻盈的舞蹈，星光为她们点亮前路。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231740416_syoeyy.wav" target="_blank" rel="noopener noreferrer">她轻轻抚摸着那本旧日记，泪水模糊了字迹，回忆如潮水般涌来。</a>      |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔公子 | wenrougongzi     | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231762453_68oj6b.wav" target="_blank" rel="noopener noreferrer">“月光洒在古老的城堡上，远处传来狼群的嚎叫，令人不寒而栗。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231771111_0r0h3f.wav" target="_blank" rel="noopener noreferrer">“他深吸一口气，推开了那扇尘封已久的大门，命运的齿轮开始转动。”</a>  |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 磁性男声 | cixingnansheng   | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231784986_xvr1ij.wav" target="_blank" rel="noopener noreferrer">月光洒在古老的城堡上，远处传来狼群的嚎叫，令人不寒而栗。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231791652_9d9uy1.wav" target="_blank" rel="noopener noreferrer">“他深吸一口气，推开了那扇尘封已久的大门，命运的齿轮开始转动。”</a>    |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 元气少女 | yuanqishaonv     | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231810865_xiz5jk.wav" target="_blank" rel="noopener noreferrer">“花园里的玫瑰在晨露中绽放，散发着淡淡的香气，宛如少女的脸颊。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231820537_fz8979.wav" target="_blank" rel="noopener noreferrer">“她轻轻抚摸着那本旧日记，泪水模糊了字迹，回忆如潮水般涌来。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 正派青年 | zhengpaiqingnian | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231834824_31a18s.wav" target="_blank" rel="noopener noreferrer">“月光洒在古老的城堡上，远处传来狼群的嚎叫，令人不寒而栗。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231842616_3y3jsx.wav" target="_blank" rel="noopener noreferrer">“他深吸一口气，推开了那扇尘封已久的大门，命运的齿轮开始转动。”</a>  |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 元气男声 | yuanqinansheng   | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231882851_ha2oe6.wav" target="_blank" rel="noopener noreferrer">“老人的眼中闪烁着智慧的光芒，缓缓道出那个埋藏千年的秘密。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231889066_vty0d3.wav" target="_blank" rel="noopener noreferrer">“狂风呼啸，海浪拍打着船舷，水手们紧紧抓住缆绳，与命运抗争。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 播音男声 | boyinnansheng    | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231898586_yvqsfk.wav" target="_blank" rel="noopener noreferrer">“月光洒在古老的城堡上，远处传来狼群的嚎叫，令人不寒而栗。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231903863_n0rq6k.wav" target="_blank" rel="noopener noreferrer">“他深吸一口气，推开了那扇尘封久的大门，命运的齿轮开始转动。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 深沉男音 | shenchennanyin   | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231909638_diuypc.wav" target="_blank" rel="noopener noreferrer">“月光洒在古老的城堡上，远处传来狼群的嚎叫，令人不寒而栗。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764231916499_zk19wv.wav" target="_blank" rel="noopener noreferrer">“他深吸一口气，推开了那扇尘封已久的大门，命运的齿轮开始转动。”</a>  |

### 4. 情感陪伴场景

情感陪伴需要音色温暖、柔和、富有同理心，能够给予用户心理慰藉和支持。我们的 TTS 特色在于细腻的音色温柔动听，情绪感染力强，可为您的用户营造出安全、舒适的交流氛围。

| 推荐模型                                                 | 推荐音色 | Voice-id             | 合成示例                                                                                                                                                                                                                                                                                                                                                             |
| :--------------------------------------------------- | :--- | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 气质温婉 | elegantgentle-female | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230170888_rpysp8.wav" target="_blank" rel="noopener noreferrer">“我在这里陪着你，无论快乐还是忧伤，我们都一起面对。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230185710_01rt1x.wav" target="_blank" rel="noopener noreferrer">“你的坚强让我感动，但也要记得适时地让自己休息一下。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 活力轻快 | livelybreezy-female  | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230220618_qbsx4o.wav" target="_blank" rel="noopener noreferrer">“生活中总会有不如意的时候，但美好的事物永远值得期待。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230236362_tfyy2l.wav" target="_blank" rel="noopener noreferrer">“说出来会好受一些，我永远是你忠实的听众和朋友。”</a>  |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔男声 | wenrounansheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230277656_1jj8at.wav" target="_blank" rel="noopener noreferrer">“今天过得怎么样？如果有什么心事，我很愿意倾听。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230256668_9lhgua.wav" target="_blank" rel="noopener noreferrer">“每个人都会有感到迷茫的时候，这很正常，你并不孤单。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔公子 | wenrougongzi         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230295150_t7wi3h.wav" target="_blank" rel="noopener noreferrer">“深呼吸，放松心情，我相信你有能力面对任何挑战。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230307812_0gi9a8.wav" target="_blank" rel="noopener noreferrer">“你的感受很重要，感谢你愿意与我分享内心的想法。”</a>     |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 经典女声 | jingdiannvsheng      | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230324896_hhowz6.wav" target="_blank" rel="noopener noreferrer">“我在这里陪着你，无论快乐还是忧伤，我们都一起面对。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230343351_k3vj3k.wav" target="_blank" rel="noopener noreferrer">“你的坚强让我感动，但也要记得适时地让自己休息一下。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 亲切女声 | qinqienvsheng        | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230361427_d9rn3n.wav" target="_blank" rel="noopener noreferrer">早上好呀，今天天气真不错，适合出去走走。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764230377953_9uheoc.wav" target="_blank" rel="noopener noreferrer">观众朋友们，大家好！欢迎收看今天的新闻播报。</a>             |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 甜美女声 | tianmeinvsheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229581488_9bjx0x.wav" target="_blank" rel="noopener noreferrer">“生活中总会有不如意的时候，但美好的事物永远值得期待。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229591698_yk6d1a.wav" target="_blank" rel="noopener noreferrer">“说出来会好受一些，我永远是你忠实的听众和朋友。”</a>  |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 磁性男声 | cixingnansheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229600823_8hr2u3.wav" target="_blank" rel="noopener noreferrer">“今天过得怎么样？如果有什么心事，我很愿意倾听。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229613085_i8q5vt.wav" target="_blank" rel="noopener noreferrer">“每个人都会有感到迷茫的时候，这很正常，你并不孤单。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 元气少女 | yuanqishaonv         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229624319_gy96i6.wav" target="_blank" rel="noopener noreferrer">“我在这里陪着你，无论快乐还是忧伤，我们都一起面对。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229636363_rl7puv.wav" target="_blank" rel="noopener noreferrer">“你的坚强让我感动，但也要记得适时地让自己休息一下。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 邻家姐姐 | linjiajiejie         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229893983_biv5nz.wav" target="_blank" rel="noopener noreferrer">“生活中总会有不如意的时候，但美好的事物永远值得期待。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229906559_3bkhy1.wav" target="_blank" rel="noopener noreferrer">“说出来会好受一些，我永远是你忠实的听众和朋友。”</a>  |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 儒雅男士 | ruyananshi           | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229965580_i9iwog.wav" target="_blank" rel="noopener noreferrer">“今天过得怎么样？如果有什么心事，我很愿意倾听。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229990027_178cz8.wav" target="_blank" rel="noopener noreferrer">“每个人都会有感到迷茫的时候，这很正常，你并不孤单。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 深沉男音 | shenchennanyin       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229487791_a43xpe.wav" target="_blank" rel="noopener noreferrer">“深呼吸，放松心情，我相信你有能力面对任何挑战。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229478620_pgi8xr.wav" target="_blank" rel="noopener noreferrer">“你的感受很重要，感谢你愿意与我分享内心的想法。”</a>     |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔女声 | wenrounvsheng        | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229464183_kpaxa8.wav" target="_blank" rel="noopener noreferrer">“我在这里陪着你，无论快乐还是忧伤，我们都一起面对。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229454546_dxzd93.wav" target="_blank" rel="noopener noreferrer">“你的坚强让我感动，但也要记得适时地让自己休息一下。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 软萌女声 | ruanmengnvsheng      | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229441268_p9xrn8.wav" target="_blank" rel="noopener noreferrer">“生活中总会有不如意的时候，但美好的事物永远值得期待。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229433217_mzc9eo.wav" target="_blank" rel="noopener noreferrer">“说出来会好受一些，我永远是你忠实的听众和朋友。”</a>  |

### 5. 语音助手场景

语音助手需要音色清晰、自然、高效，能够准确理解并响应用户指令。我们的 TTS 特色在于韵律自然，情绪饱满，让您的语音助手既专业又亲切。

| 推荐模型                                                 | 推荐音色 | Voice-id             | 合成示例                                                                                                                                                                                                                                                                                                                                                             |
| :--------------------------------------------------- | :--- | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 气质温婉 | elegantgentle-female | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228832095_29ybp3.wav" target="_blank" rel="noopener noreferrer">“您要查询的航班信息已经找到，需要我为您详细说明吗？”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228840760_7lfeif.wav" target="_blank" rel="noopener noreferrer">“已为您设置明天早上7点的闹钟，祝您晚安。”</a>      |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 活力轻快 | livelybreezy-female  | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228850379_g5udri.wav" target="_blank" rel="noopener noreferrer">正在搜索您需要的资料，找到3个相关结果，现在为您展示。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228867575_iogyx5.wav" target="_blank" rel="noopener noreferrer">今天北京天气晴朗，气温25度，适合外出活动。</a>      |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 清纯少女 | qingchunshaonv       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228890474_009vob.wav" target="_blank" rel="noopener noreferrer">“您要查询的航班信息已经找到，需要我为您详细说明吗？”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228880711_uo1s1z.wav" target="_blank" rel="noopener noreferrer">“电量不足，建议连接充电器，以保持最佳使用体验。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 元气少女 | yuanqishaonv         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228956977_jkgzvk.wav" target="_blank" rel="noopener noreferrer">“新消息来自张经理：‘项目方案已通过，辛苦了！’”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228942094_6cgojl.wav" target="_blank" rel="noopener noreferrer">“正在搜索您需要的资料，找到3个相关结果，现在为您展示。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 邻家姐姐 | linjiajiejie         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228982358_2c8eqk.wav" target="_blank" rel="noopener noreferrer">“您要查询的航班信息已经找到，需要我为您详细说明吗？”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228972645_kzl33n.wav" target="_blank" rel="noopener noreferrer">“电量不足，建议连接充电器，以保持最佳使用体验。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 儒雅男士 | ruyananshi           | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229029290_58c9et.wav" target="_blank" rel="noopener noreferrer">“已为您设置明天早上7点的闹钟，祝您晚安。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229015620_qu5naz.wav" target="_blank" rel="noopener noreferrer">“今天北京天气晴朗，气温25度，适合外出活动。”</a>         |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 机灵少女 | jilingshaonv         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229042857_sbtid3.wav" target="_blank" rel="noopener noreferrer">“新消息来自张经理：‘项目方案已通过，辛苦了！’”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229055562_gz7tjs.wav" target="_blank" rel="noopener noreferrer">“正在搜索您需要的资料，找到3个相关结果，现在为您展示。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 软萌女声 | ruanmengnvsheng      | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229191918_0u5rmk.wav" target="_blank" rel="noopener noreferrer">“您要查询的航班信息已经找到，需要我为您详细说明吗？”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229207559_ifljss.wav" target="_blank" rel="noopener noreferrer">“电量不足，建议连接充电器，以保持最佳使用体验。”</a>   |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 邻家妹妹 | linjiameimei         | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229220926_vubdhb.wav" target="_blank" rel="noopener noreferrer">“新消息来自张经理：‘项目方案已通过，辛苦了！’”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229230493_3vr4dl.wav" target="_blank" rel="noopener noreferrer">“正在搜索您需要的资料，找到3个相关结果，现在为您展示。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 知性姐姐 | zhixingjiejie        | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229251134_r2dv2t.wav" target="_blank" rel="noopener noreferrer">“您要查询的航班信息已经找到，需要我为您详细说明吗？”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764229242754_6j194i.wav" target="_blank" rel="noopener noreferrer">“电量不足，建议连接充电器，以保持最佳使用体验。”</a>   |

### 6. 视频配音场景

视频配音需要音色富有表现力、节奏感和画面感，能够与视频内容完美融合。我们的 TTS 特色在于精准的情绪表达和语音节奏控制，增强您视频的感染力。

| 推荐模型                                                 | 推荐音色  | Voice-id           | 合成示例                                                                                                                                                                                                                                                                                                                                                                            |
| :--------------------------------------------------- | :---- | :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 邻家姐姐  | linjiajiejie       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228368225_q6vf14.wav" target="_blank" rel="noopener noreferrer">“细腻的手工，精致的工艺，每一件作品都承载着匠人的心血与智慧。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228358790_54hsjm.wav" target="_blank" rel="noopener noreferrer">“美食是文化的载体，味蕾的记忆，让我们开启这段舌尖上的旅程。”</a>       |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 邻家妹妹  | linjiameimei       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228406946_msnk7y.wav" target="_blank" rel="noopener noreferrer">“在这个快节奏的时代，偶尔慢下来，发现生活中被忽略的美好。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228422631_jv0wae.wav" target="_blank" rel="noopener noreferrer">“爱与温暖，成长与蜕变，这是一个关于家庭和梦想的动人故事。”</a>          |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 青年大学生 | qingniandaxuesheng | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228453152_11xqp7.wav" target="_blank" rel="noopener noreferrer">最近在研究一个新课题，感觉超有挑战性，你要一起来研究吗？</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228437723_owq9wd.wav" target="_blank" rel="noopener noreferrer">从12月1日起，全区将全面应用医保刷脸支付，这一举措将进一步提升医保服务的便捷性。</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 软萌女声  | ruanmengnvsheng    | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228469573_c9d14l.wav" target="_blank" rel="noopener noreferrer">“时尚不仅是外在的装扮，更是内心态度的表达和个性的宣言。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228481762_npxp0m.wav" target="_blank" rel="noopener noreferrer">“在这个快节奏的时代，偶尔慢下来，发现生活中被忽略的美好。”</a>           |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 优雅女声  | youyanvsheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228538767_2lkmyq.wav" target="_blank" rel="noopener noreferrer">“在这个快节奏的时代，偶尔慢下来，发现生活中被忽略的美好。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228548744_a6t35v.wav" target="_blank" rel="noopener noreferrer">“爱与温暖，成长与蜕变，这是一个关于家庭和梦想的动人故事。”</a>          |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 冷艳御姐  | lengyanyujie       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228563074_mkfaxu.wav" target="_blank" rel="noopener noreferrer">“细腻的手工，精致的工艺，每一件作品都承载着匠人的心血与智慧。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228577493_12hmg5.wav" target="_blank" rel="noopener noreferrer">“美食是文化的载体，味蕾的记忆，让我们开启这段舌尖上的旅程。”</a>       |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 知性姐姐  | zhixingjiejie      | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228598185_j5cgak.wav" target="_blank" rel="noopener noreferrer">“从概念到现实，这款产品的诞生经历了数百个日夜的精心打磨。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228588844_rylx9j.wav" target="_blank" rel="noopener noreferrer">“穿越云海，俯瞰大地，这是只属于勇者的视觉盛宴和心灵震撼。”</a>          |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 爽快姐姐  | shuangkuaijiejie   | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228610601_8ca7fa.wav" target="_blank" rel="noopener noreferrer">这个项目我来负责，保证完成得漂漂亮亮！</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228620326_6f4lyx.wav" target="_blank" rel="noopener noreferrer">从12月1日起，全区将全面应用医保刷脸支付，这一举措将进一步提升医保服务的便捷性。</a>          |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 文静学姐  | wenjingxuejie      | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228640932_1hg09k.wav" target="_blank" rel="noopener noreferrer">这本书的见解很独特，值得一读。</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228632403_m8zdxc.wav" target="_blank" rel="noopener noreferrer">近期有报道显示，出租车霸占公交车泊位的现象时有发生，这给乘客上下车带来了安全隐患。</a>              |

### 7. 教育与培训场景

教培场景需要音色清晰、准确、有启发性，能够有效传递知识并激发学习兴趣。我们的 TTS 特色在于能把握教师在不同情绪下的声音特点。

| 推荐模型                                                 | 推荐音色 | Voice-id             | 合成示例                                                                                                                                                                                                                                                                                                                                                                        |
| :--------------------------------------------------- | :--- | :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 气质温婉 | elegantgentle-female | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228058073_102wb4.wav" target="_blank" rel="noopener noreferrer">“英语中的现在完成时表示过去发生但与现在有关联的动作或状态。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228049743_8dc93a.wav" target="_blank" rel="noopener noreferrer">“让我们一起朗读这首古诗，感受诗人笔下的明月和思乡之情。”</a>      |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔男声 | wenrounansheng       | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228096723_naf04h.wav" target="_blank" rel="noopener noreferrer">“今天我们学习勾股定理：直角三角形的两条直角边的平方和等于斜边的平方。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228085782_awotak.wav" target="_blank" rel="noopener noreferrer">“请注意这个发音要点：舌尖要轻抵上齿龈，发出清晰的辅音。”</a> |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 活力轻快 | livelybreezy-female  | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228115572_zfgvsz.wav" target="_blank" rel="noopener noreferrer">“光合作用是植物将光能转化为化学能的重要过程，让我们详细了解。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228129774_s17gwn.wav" target="_blank" rel="noopener noreferrer">“绘画时要注意透视原理，近大远小，让画面更有立体感。”</a>       |
| `stepaudio-2.5-tts` / `step-tts-2` / `step-tts-mini` | 温柔熟女 | wenroushunv          | <a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228171350_vs3v5a.wav" target="_blank" rel="noopener noreferrer">“英语中的现在完成时表示过去发生但与现在有关联的动作或状态。”</a><br /><a href="https://static-openapi.stepfun.com/static/platform-docs/resource/1764228180145_lct34k.wav" target="_blank" rel="noopener noreferrer">“让我们一起朗读这首古诗，感受诗人笔下的明月和思乡之情。”</a>      |

## 官方音色清单

| **中文名**               | **Voice ID**          | **支持模型**                                         | **推荐场景**                     |
| --------------------- | --------------------- | ------------------------------------------------ | ---------------------------- |
| Vibrant Youth         | vibrant-youth         | `stepaudio-2.5-tts`、`step-tts-2`                 | 有声书、视频配音                     |
| Lively Girl           | lively-girl           | `stepaudio-2.5-tts`、`step-tts-2`                 | 有声书、视频配音                     |
| Soft-spoken Gentleman | soft-spoken-gentleman | `stepaudio-2.5-tts`、`step-tts-2`                 | 情感陪伴、有声书                     |
| Magnetic-voiced Male  | magnetic-voiced-male  | `stepaudio-2.5-tts`、`step-tts-2`                 | 有声书、视频配音                     |
| 自信男声                  | zixinnansheng         | `stepaudio-2.5-tts`、`step-tts-2`                 | 有声书、情感陪伴、教育与培训、营销            |
| 气质温婉                  | elegantgentle-female  | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 客服与业务办理、口播（解说、新闻）、教育与培训、情感陪伴 |
| 活力轻快                  | livelybreezy-female   | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 情感陪伴、客服与业务办理、教育与培训、营销        |
| 温柔男声                  | wenrounansheng        | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 口播（解说、新闻）、情感陪伴、客服与业务办理、教育与培训 |
| 温柔公子                  | wenrougongzi          | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 情感陪伴、有声书                     |
| 元气男声                  | yuanqinansheng        | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 有声书、口播（解说、新闻）、客服与业务办理        |
| 经典女声                  | jingdiannvsheng       | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 客服与业务办理、情感陪伴                 |
| 温柔熟女                  | wenroushunv           | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 客服与业务办理、口播（解说、新闻）、教育与培训      |
| 甜美女声                  | tianmeinvsheng        | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 情感陪伴、客服与业务办理                 |
| 清纯少女                  | qingchunshaonv        | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 客服与业务办理、语音助手                 |
| 磁性男声                  | cixingnansheng        | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 有声书、情感陪伴                     |
| 元气少女                  | yuanqishaonv          | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 有声书、情感陪伴、语音助手                |
| 邻家姐姐                  | linjiajiejie          | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 口播（解说、新闻）、情感陪伴、语音助手、视频配音     |
| 正派青年                  | zhengpaiqingnian      | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 营销、有声书                       |
| 青年大学生                 | qingniandaxuesheng    | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 口播（解说、新闻）                    |
| 播音男声                  | boyinnansheng         | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 有声书、口播（解说、新闻）                |
| 儒雅男士                  | ruyananshi            | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 有声书、情感陪伴、口播（解说、新闻）、语音助手      |
| 深沉男音                  | shenchennanyin        | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 情感陪伴、有声书                     |
| 亲切女声                  | qinqienvsheng         | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 口播（解说、新闻）                    |
| 温柔女声                  | wenrounvsheng         | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 有声书、情感陪伴                     |
| 机灵少女                  | jilingshaonv          | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 语音助手、口播（解说、新闻）               |
| 软萌女声                  | ruanmengnvsheng       | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 情感陪伴、语音助手、视频配音               |
| 优雅女声                  | youyanvsheng          | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 视频配音                         |
| 冷艳御姐                  | lengyanyujie          | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 视频配音                         |
| 爽快姐姐                  | shuangkuaijiejie      | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 口播（解说、新闻）                    |
| 文静学姐                  | wenjingxuejie         | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 口播（解说、新闻）                    |
| 邻家妹妹                  | linjiameimei          | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 视频配音、口播（解说、新闻）、语音助手          |
| 知性姐姐                  | zhixingjiejie         | `stepaudio-2.5-tts`、`step-tts-2`、`step-tts-mini` | 视频配音、口播（解说、新闻）、语音助手          |
| 爽快男声                  | shuangkuainansheng    | `stepaudio-2.5-tts`、`step-tts-2`                 | 客服与业务办理、语音助手                 |
| 干练女声                  | ganliannvsheng        | `stepaudio-2.5-tts`、`step-tts-2`                 | 客服与业务办理、语音助手                 |
| 亲和女声                  | qinhenvsheng          | `stepaudio-2.5-tts`、`step-tts-2`                 | 客服与业务办理、语音助手                 |
| 活力女声                  | huolinvsheng          | `stepaudio-2.5-tts`、`step-tts-2`                 | 客服与业务办理、语音助手                 |

## 音色标签

音色标签支持语速演绎风格、情绪和语言三种选项；其中情绪类型的标签需要放置在 `voice_label.emotion` 字段中、语速演绎风格需放置在 `voice_label.style` 字段中。他们具体的支持情况如下表所示：

| **序号** | **标签名称** | **标签类型** | **step-tts-2支持情况** | **step-tts-mini 支持情况** |
| ------ | -------- | -------- | ------------------ | ---------------------- |
| 1      | 高兴       | 情绪       | √                  | √                      |
| 2      | 非常高兴     | 情绪       | √                  | √                      |
| 3      | 悲伤       | 情绪       | √                  | √                      |
| 4      | 生气       | 情绪       | √                  | √                      |
| 5      | 非常生气     | 情绪       | √                  | √                      |
| 6      | 撒娇       | 情绪       | √                  | √                      |
| 7      | 慢速       | 语速风格     | √                  | √                      |
| 8      | 极慢       | 语速风格     | √                  | √                      |
| 9      | 快速       | 语速风格     | √                  | √                      |
| 10     | 极快       | 语速风格     | √                  | √                      |
| 11     | 恐惧       | 情绪       | √                  | √                      |
| 12     | 惊讶       | 情绪       | √                  | √                      |
| 13     | 兴奋       | 情绪       | √                  | √                      |
| 14     | 钦佩       | 情绪       | √                  | √                      |
| 15     | 困惑       | 情绪       | √                  | √                      |
| 16     | 冷漠       | 演绎风格     | √                  | √                      |
| 17     | 尴尬       | 演绎风格     | √                  | √                      |
| 18     | 沮丧       | 演绎风格     | √                  | √                      |
| 19     | 骄傲       | 演绎风格     | √                  |                        |
| 20     | 温柔       | 演绎风格     | √                  |                        |
| 21     | 甜美       | 演绎风格     | √                  |                        |
| 22     | 豪爽       | 演绎风格     | √                  |                        |
| 23     | 严肃       | 演绎风格     | √                  |                        |
| 24     | 傲慢       | 演绎风格     | √                  |                        |
| 25     | 老年       | 演绎风格     | √                  |                        |
| 26     | 吼叫       | 演绎风格     | √                  |                        |
| 27     | 阴阳怪气     | 演绎风格     | √                  |                        |
| 28     | 磕巴       | 演绎风格     | √                  |                        |

## 输出格式

阶跃星辰 TTS 模型 支持 wav、mp3、flac、opus 和 pcm 格式的音频输出，默认为 mp3格式，你可以根据自己的实际情况选择合适的音频格式进行使用。

## 输出语言

阶跃星辰 TTS 模型支持输出中文、英文，中英混合和日语音频。

## FAQ

**我是否拥有创造出来的音频？**

是的，你创造出来的音频归你所有。但建议在产品上向用户说明相关音频由 AI 生成，以便于用户感知相关音频为 AI 生成。

**如何调整生成的音频的音量?**

你可以在调用生成 API 时，传入 volume 参数，可选值为 0.1\~2.0 ，代表着将音量缩小至 10% \~ 增大至 200%（两倍音量）。

**如何调整生成的音频的语速**
你可以在调用生成 API 时，传入 speed 参数，可选值为 0.5-2 ，代表着将语速降速为之前的一半 \~ 提速至两倍。
