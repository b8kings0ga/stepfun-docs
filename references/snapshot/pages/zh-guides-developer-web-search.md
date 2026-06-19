<!-- title: 网络搜索使用建议 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/web-search -->
<!-- extracted: trafilatura -->

### 启用互联网搜索

如需启用互联网搜索，可以通过在调用 API 时，传入 tools 定义来使用，具体定义如下：```
#构建web_search工具
tools = [
{
"type": "web_search",# 固定值
"function": {
"description": "这个web_search用来搜索互联网的信息"# 描述什么样的信息需要大模型进行搜索。
}
}
]
```


`type`

固定为 `web_search`

，并支持通过 `function.description`

来描述需要使用搜索的场景，用于指引大模型判断是否需要调用互联网搜索搜索相关信息。在完成搜索后，会以上下文的方式，插入到对话中，并交给大模型进行推理。互联网搜索工具按实际调用的次数计费，具体计费可见[定价说明](https://platform.stepfun.com/docs/zh/guides/pricing/details)。

### 实现步骤 & 参考代码

实现联网搜索，需要先构建 web_search 工具，这是阶跃星辰大模型为开发者定义好的网络搜索工具。如开发者有搜索渠道也，可以自行通过 tool call 实现调用自定义搜索引擎。- 非流式响应
- 流式响应
- 流式响应并获取引用

```
from openai import OpenAI
# 初始化 阶跃星辰 Client
STEPFUN_KEY = "YourAPIkey"
client = OpenAI(
base_url="https://api.stepfun.com/v1",
api_key=STEPFUN_KEY
) #定义sys扮演的角色和任务
sys_prompt = "每个提问先通过web search，然后通过web search的结果，回答用户问题"
user_prompt = "上海最高的楼上海什么楼？请只回答楼的名称，不要包含其他内容。例如：上海金茂大厦。" #构建信息
message = [
{"role": "system", "content": sys_prompt},
{"role": "user", "content": user_prompt}
] #构建web_search工具
tools = [
{
"type": "web_search",# 固定值
"function": {
"description": "这个web_search用来搜索互联网的信息"# 描述什么样的信息需要大模型进行搜索。
}
}
]
# 调用补全接口进行补全
completion = client.chat.completions.create(
model="step-3.7-flash",
messages=message,
tool_choice="auto",
tools=tools,
stream=False#非流式可以不进行设置使用默认值
) #非流式
print(completion)
```


**返回结果**

- 返回结果中的 tool_calls.function.results 当中包含的是搜索引擎返回的信息，你可以基于此渲染 UI。

```
{
"id": "354dff9f4e8b0d273cf9d4639ba5f183.2618f2a05bbfdd02896c32051994da8c",
"object": "chat.completion",
"created": 1722413870,
"model": "step-3.7-flash",
"choices": [
{
"index": 0,
"message": {
"role": "assistant",
"content": "上海中心大厦",
"tool_calls": [
{
"id": "call__Tg9p9DHRK2JamqimG-IVA",
"type": "web_search",
"function": {
"name": "step_websearch",
"arguments": "{\"keyword\": \"上海 最高的楼\"}",
"results": [
{
"index": 0,
"url": "https://www.tianqi.com/video/3352.html",
"title": "上海最高的楼 上海最高的楼是哪",
"summary": "\n上海中心大厦是上海市的一座超高层地标式摩天大楼，其地上有119层，还有5层裙楼和5层地下室。上海中心大厦分为9个区，每一个都有自己的空中大厅和中庭。其中空中大厅每一层都建有自己的零售店和餐馆，形成了一个垂直商业区。\n相关推荐 更多 >>\n-\n### 何超莲看中国女排比赛快窒息 并且引发了网友的共鸣\n##### 热点07-30\n-\n### 覃海洋张雨霏一天7次尿检 游泳运动员受大干扰和压力\n##### 热点07-29\n-\n"
},
{
"index": 1,
"url": "https://www.maigoo.com/news/481863.html?fromapp=wx",
"title": "上海十大高楼排行榜 上海10大最高的摩天大楼 上海最高建筑盘点→买购网",
"summary": "\n15 | 上海信息港枢纽大楼 | 288.00米 | 已建成 |\n16 | 上海恒基中心 | 285.00米 | 已建成 |\n17 | 上海明天广场 | 284.60米 | 已建成 |\n18 | 上海前滩中心 | 280.00米 | 已建成 |"
},
{
"index": 2,
"url": "http://m.wenda.bendibao.com/sgh/128141.shtm",
"title": "上海最高的楼有多少层- 本地宝",
"summary": "【导语】: 118层.上海最高建筑物是上海中心大厦.上海中心大厦项目面积433954平方米,总高为632米,结构高度为580米,机动车停车位布置在地下,可停放2000辆. 118层.上海最高建筑物是上海中心大厦.上海中心大厦项目面积433954平方米,总高为632米,结构高度为580米,机动车停车位布置在地下,可停放2000辆. 上海三个高楼通常指上海环球金融中心、上海金茂大厦、上海中心大厦.其中,上海环球金融中心是位于中国上海陆家嘴的一栋摩天大楼,楼高492米,地上101层,是世界最高的平顶式大楼. 上海中心大厦是中国第一高楼(截止2018年1月).上海中心大厦项目面积433954平方米,建筑主体为118层,总高为632米,结构高度为580米,机动车停车位布置在地下,可停放2000辆. 金茂大厦又称金茂大楼,曾经是中国大陆最高的大楼,位于上海市浦东新区黄浦江畔的陆家嘴金融贸易区,楼高420.5米. 温馨提示: 微信关注上海本地宝 公众号(shbendibao)输入框回复 社保 ,查看更多上海最新社保卡更换流程、社保卡余额查询,社保卡办理网点等信息. "
},
{
"index": 3,
"url": "https://hf.house365.com/info6666/398606.html",
"title": "上海最高楼叫什么大厦有多少米高-365淘房网-上海最高楼",
"summary": "上海最高楼叫上海中心大厦,总高为632米,共有132层,地上127层,地下5层.它不仅是上海最高的楼,也曾是中国最高的楼,现被739米的H700深圳塔取代.上海中心大厦于2008年11月29日开工,直到2016年3月12日全部完工,2016年4月27日开始运营.上海中心的设计来自美国的Gensler建筑设计事务所设计,其设计的'龙型方案中标后,与同济大学建筑设计研究院完成施工图出图,深化大厦细部设计. 上海中心大厦采用了一种'龙型设计能够延缓风流,随着高度的升高,每层扭曲近1度,将风环绕建筑时的侧力减少24%,提升了大厦的安全.此外,上海中心大厦不单单是一座办公楼,每个区都有自己的空中大厅和中庭,形成了一个垂直区.1号区将是零售区,2号区到6号区将为办公区,酒店和观景台座落于7号区到9号区.空中大厅的每一层都将建有自己的零售店和餐馆,成为一个垂直区. 除了上海中心大厦外,上海环球金融中心也是上海的地标建筑之一,它位于中国上海陆家嘴的一栋摩天大楼,2008年8月29日竣工,楼高492米,地上101层.环球金融中心曾一度成为国内外游客来上海的首选之地,位于100层的观光厅更是成为了上海的一个标志. 总的来说,上海中心大厦和上海环球金融中心都是上海的标志建筑,代表着上海的发展和成就.它们不仅仅是一座建筑,更是上海人民勇于进取、开拓创新的精神象征."
},
{
"index": 4,
"url": "http://m.nongpin88.com/know/1957952.html",
"title": "上海最高的楼是哪个楼_知道问答_醉学网",
"summary": "上海最高的的楼是上海中心大厦 . 上海中心大厦,位于陆家嘴,建筑主体为118层,总高为632米,其设计高度超过附近的上海环球金融中心,被称为中国第一高楼,世界第三高楼. 上海中心大厦项目面积433954平方米,结构高度为580米,机动车停车位布置在地下,可停放2000辆. 美国SOM建筑设计事务所、美国KPF建筑师事务所及上海现代建筑设计集团等多家国内外设计单位提交了设计方案,美国Gensler建筑设计事务所的“龙型”方案及英国福斯特建筑事务所“尖顶型”方案入围.经过评选,“龙型”方案中标,大厦细部深化设计以“龙型”方案作为蓝本,由同济大学建筑设计研究院完成施工图出图."
}
]
}
}
]
},
"finish_reason": "stop"
}
],
"usage": {
"cached_tokens": 64,
"prompt_tokens": 1516,
"completion_tokens": 4,
"total_tokens": 1520
}
}
```


```
from openai import OpenAI
# 初始化 阶跃星辰 Client
STEPFUN_KEY = "YourAPIkey"
client = OpenAI(
base_url="https://api.stepfun.com/v1",
api_key=STEPFUN_KEY
) #定义sys扮演的角色，以及user提出的任务
sys_prompt = "每个提问先通过web search，然后通过web search的结果，回答用户问题" #在调用 Web Search 时，阶跃星辰会将搜索结果作为上下文传入传给大模型，因此如果你需要获取引用内容，可以通过 Prompt Engineering 的方式，#来要求大模型将信息来源反馈给你。具体效果可以参考下方的高亮加粗部分。
#user_prompt = "上海最高的楼上海什么楼？请只回答楼的名称，不要包含其他内容。例如：上海金茂大厦。回答时，你会将所使用的具体信息的 index 一并返回给用户。"
user_prompt = "上海最高的楼上海什么楼？请只回答楼的名称，不要包含其他内容。例如：上海金茂大厦。" #构建信息
message = [
{"role": "system", "content": sys_prompt},
{"role": "user", "content": user_prompt}
] #构建web_search工具
tools = [
{
"type": "web_search",# 固定值
"function": {
"description": "这个web_search用来搜索互联网的信息"# 描述什么样的信息需要大模型进行搜索。
}
}
]
# 调用补全接口进行补全
completion = client.chat.completions.create(
model="step-3.7-flash",
messages=message,
tool_choice="auto",
tools=tools,
stream=True#流式需要设置此参数，非流式可以不进行设置使用默认值
) #非流式
#print(completion) #对流式返回的内容进行打印 / 渲染输出
for chunk in completion:
print(chunk)
#print(chunk.choices[0].delta.content.strip(),end="")
```


**响应**

```
{
"id": "1681409a3e4f09244a0951a67612cdf2.c78632c4a6ec4e2ef404a3222c81a82c",
"object": "chat.completion.chunk",
"created": 1722413589,
"model": "step-3.7-flash",
"choices": [
{
"index": 0,
"delta": {
"role": "assistant",
"tool_calls": [
{
"id": "call_GygttvWbRZu1ympMbC_eEw",
"type": "web_search",
"function": {
"name": "step_websearch",
"arguments": "{\"keyword\": \"上海 最高 楼 名称\"}",
"results": [
{
"index": 0,
"url": "https://www.tianqi.com/toutiao/read/190032.html",
"title": "上海最高的大楼 上海最高的大楼是什么名字 - 天气加",
"summary": "\n当前所在位置 : 天气网\n天气生活\n生活 正文\n# 上海最高的大楼 上海最高的大楼是什么名字\n2022-05-31 来源：天气网 【字体： 大 中 小 】\n上海最高的大楼是上海中心大厦Shanghai Tower，建筑高度632米，位于上海市陆家嘴金融贸易区银城中路501号，是上海市的一座巨型高层地标式摩天大楼，始建于2008年11月29日，于2016年3月12日完成建筑总体的施工工作。上海中心大厦主要用途为办公、酒店、商业、观光等公共设施。\n主楼为地上127层，建筑高度632米，地下室有5层。\n\n上海中心大厦为多功能摩天大楼，主楼沿竖向共分为8个区段和1个观光层，在每个区段的顶部均布置有设备层和避难层。其中1区共5层，主要用于商业和会议。2区共12层、3区共13层、4区共13层、5区共14层、6区共14层均用于办公，办公标准层面积分别为：2区约5000平方米、3区约3900平方米、4区约3200平方米、5区约2700平方米、6区约2000平方米，7区共15层，为酒店。8区共15层，其中10层为酒店，5层用于办公。9区共3层，为观光层。观光层以上为设备层。地下5层用于地下商业和停车。\n"
},
{
"index": 1,
"url": "https://m.renrenshipu.com/diet/article/24119.html",
"title": "上海最高的楼叫什么 - 阅品美食",
"summary": "\n在上海之巅360度全视角观光厅，近看东方明珠、金茂大厦、环球金融中心身居足下，远眺外滩、世博园区、八万人体育场尽收眼底，一览苏州河与黄浦江蜿蜒同奔长江共入东海。"
},
{
"index": 2,
"url": "https://hf.house365.com/info6666/398606.html",
"title": "上海最高楼叫什么大厦有多少米高-365淘房网-上海最高楼",
"summary": "上海最高楼叫上海中心大厦,总高为632米,共有132层,地上127层,地下5层.它不仅是上海最高的楼,也曾是中国最高的楼,现被739米的H700深圳塔取代.上海中心大厦于2008年11月29日开工,直到2016年3月12日全部完工,2016年4月27日开始运营.上海中心的设计来自美国的Gensler建筑设计事务所设计,其设计的'龙型方案中标后,与同济大学建筑设计研究院完成施工图出图,深化大厦细部设计. 上海中心大厦采用了一种'龙型设计能够延缓风流,随着高度的升高,每层扭曲近1度,将风环绕建筑时的侧力减少24%,提升了大厦的安全.此外,上海中心大厦不单单是一座办公楼,每个区都有自己的空中大厅和中庭,形成了一个垂直区.1号区将是零售区,2号区到6号区将为办公区,酒店和观景台座落于7号区到9号区.空中大厅的每一层都将建有自己的零售店和餐馆,成为一个垂直区. 除了上海中心大厦外,上海环球金融中心也是上海的地标建筑之一,它位于中国上海陆家嘴的一栋摩天大楼,2008年8月29日竣工,楼高492米,地上101层.环球金融中心曾一度成为国内外游客来上海的首选之地,位于100层的观光厅更是成为了上海的一个标志. 总的来说,上海中心大厦和上海环球金融中心都是上海的标志建筑,代表着上海的发展和成就.它们不仅仅是一座建筑,更是上海人民勇于进取、开拓创新的精神象征."
},
{
"index": 3,
"url": "http://www.zsuan.com/dq/dqzs/1467226.html",
"title": "上海最高楼,上海市最高的楼宇多少米叫什么名字 - 装算",
"summary": "1,上海市最高的楼宇多少米叫什么名字 上海的最高建筑是上海中心大厦,2014年建成,总高度632米,共125层. 2,上海最高楼叫什么名字 东方明珠不是楼是建筑最高楼不确定 上海中心大厦 东方明珠 3,上海最高的楼多高 上海最高的楼——上海中心大厦(总高为632米)地理位置:中国上海市陆家嘴金融贸易区建筑高度:632米层 数:地上118层、5层裙楼和5层地下室 4,上海最高的建筑是那幢 上海最高的建筑是上海中心大厦,地处上海最繁华的金融中心区陆家嘴.上海中心大厦总高度是632米,总高度125层,是国内第一高楼,在已经投入使用的写字楼里排名世界第三. 5,上海最高的楼是哪一座 九月十四日,上海的第一高度再次刷新,492米高、101层的上海环球金融中心结构封顶,整幢大楼预计明年春天竣工.据悉,在距地面472米的100层处,设计了“观光天阁”,这一高度或将成为当今世界摩天大楼中人可到达的最高高度,上海也因此将出现世界最高的大楼观光厅. 图为建造中的“上海第一高楼”已“鹤”立楼群,屹立在黄浦江畔 环球金融中心额 6,上海最高的楼 环球金融中心 上海中心比它还要高 但是现在还在打地基呢 N0.1 上海中心大厦(在建):632米,地下5层,地上124层,总高度632米,建筑造价:148亿元.位于浦东的陆家嘴功能区,百占地3万多平方米,其建筑设计方案由美国Gensler建筑设计事务所完成,总承包单位为上海建工(集团)总公司,是目前中国国内在建中的第一高楼. 在2010年上海世博会时地下部分封顶,2012年结构封顶且部分投入运营,2014年竣工交付使用.NO.2 上海环球金融中心是位于中国上海陆家嘴的一栋摩天大楼,2008年8月29日竣工.是中国目前第二高楼、世界第三高楼、世界最高的平顶式大楼,楼高492米,地上101层NO.3 东方明珠广播电视塔:468米,又名东方明珠塔,是一座位于中国上海的电视塔.坐落在中国上海浦东新区陆家嘴,毗邻黄浦江,与外滩隔江相望.东方明珠塔是由上海现代建筑设计(集团)有限公司的江欢成设计.建筑动工于1991年,于1994年竣工,投资总额达8.3亿元人民币.高467.9米,亚洲第二,世界第四高塔,仅次于广州新电度视塔(600米)、加拿大的加拿大CN电视塔(553.3米)及俄罗斯的奥斯坦金诺电视塔(540.1米),是上海的地标之一. 目前的东方明珠高468"
},
{
"index": 4,
"url": "https://sgh.51dongshi.com/eggaedfresgbcs.html",
"title": "上海市最高的楼叫什么_懂视",
"summary": "上海市最高的楼叫什么 上海最高的楼叫做上海中心大厦,位于陆家嘴,总高632米,建筑主体为118层,是一座超高层地标式摩天大楼,上海中心大厦项目的面积达到了433954平方米,在2008年开工,直到2016年才竣工,费时八年,是目前中国的第一高楼,世界的第二高楼. 推荐度: 导读 上海最高的楼叫做上海中心大厦,位于陆家嘴,总高632米,建筑主体为118层,是一座超高层地标式摩天大楼,上海中心大厦项目的面积达到了433954平方米,在2008年开工,直到2016年才竣工,费时八年,是目前中国的第一高楼,世界的第二高楼. 上海是我们国家经济最为繁荣的城市之一,上海最高的楼也是上海的地标建筑,那么上海最高的楼叫什么呢?一起来看看吧. 上海最高的楼叫做上海中心大厦,位于陆家嘴,总高632米,建筑主体为118层,是一座超高层地标式摩天大楼. 上海中心大厦项目的面积达到了433954平方米,在2008年开工,知道2016年才竣工,费时八年,是目前中国的第一高楼,世界的第二高楼."
}
]
}
}
]
}
}
],
"usage": {
"prompt_tokens": 0,
"completion_tokens": 0,
"total_tokens": 0
}
}
{
"id": "1681409a3e4f09244a0951a67612cdf2.c78632c4a6ec4e2ef404a3222c81a82c",
"object": "chat.completion.chunk",
"created": 0,
"model": "step-3.7-flash",
"choices": [
{
"index": 0,
"delta": {
"role": "assistant"
}
}
],
"usage": {
"prompt_tokens": 0,
"completion_tokens": 0,
"total_tokens": 0
}
}
{
"id": "1681409a3e4f09244a0951a67612cdf2.c78632c4a6ec4e2ef404a3222c81a82c",
"object": "chat.completion.chunk",
"created": 1722413589,
"model": "step-3.7-flash",
"choices": [
{
"index": 0,
"delta": {
"content": "上海"
}
}
],
"usage": {
"cached_tokens": 96,
"prompt_tokens": 2167,
"completion_tokens": 1,
"total_tokens": 2168
}
}
{
"id": "1681409a3e4f09244a0951a67612cdf2.c78632c4a6ec4e2ef404a3222c81a82c",
"object": "chat.completion.chunk",
"created": 1722413589,
"model": "step-3.7-flash",
"choices": [
{
"index": 0,
"delta": {
"content": "中心"
}
}
],
"usage": {
"cached_tokens": 96,
"prompt_tokens": 2167,
"completion_tokens": 2,
"total_tokens": 2169
}
}
{
"id": "1681409a3e4f09244a0951a67612cdf2.c78632c4a6ec4e2ef404a3222c81a82c",
"object": "chat.completion.chunk",
"created": 1722413589,
"model": "step-3.7-flash",
"choices": [
{
"index": 0,
"delta": {
"content": "大厦"
}
}
],
"usage": {
"cached_tokens": 96,
"prompt_tokens": 2167,
"completion_tokens": 3,
"total_tokens": 2170
}
}
{
"id": "1681409a3e4f09244a0951a67612cdf2.c78632c4a6ec4e2ef404a3222c81a82c",
"object": "chat.completion.chunk",
"created": 1722413589,
"model": "step-3.7-flash",
"choices": [
{
"index": 0,
"delta": {}
}
],
"usage": {
"cached_tokens": 96,
"prompt_tokens": 2167,
"completion_tokens": 4,
"total_tokens": 2171
}
}
{
"id": "1681409a3e4f09244a0951a67612cdf2.c78632c4a6ec4e2ef404a3222c81a82c",
"object": "chat.completion.chunk",
"created": 1722413589,
"model": "step-3.7-flash",
"choices": [
{
"index": 0,
"delta": {},
"finish_reason": "stop"
}
],
"usage": {
"cached_tokens": 96,
"prompt_tokens": 2167,
"completion_tokens": 4,
"total_tokens": 2171
}
}
```


由于 OpenAI 的 SDK 在流式下无法获取到 results 的结果，所以在流式场景下，你需要自行实现调用阶跃星辰模型能力，并解析结果以获得响应。如下是一个基于

`httpx`

的参考代码。```
# 需要先执行 pip install httpx httpx-sse 以安装依赖。
import httpx
from httpx_sse import connect_sse
import json
STEP_API_KEY = ""
def main():
headers = {
"Authorization": f"Bearer {STEP_API_KEY}"
}
body = {
"model": "step-3.7-flash",
"stream": True,
"messages": [
{
"role": "system",
"content": "你是由阶跃星辰提供的AI聊天助手，你擅长中文，英文，以及多种其他语言的对话。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容。"
},
{
"role": "user",
"content": "你好，请介绍一下 OPPO 公司！"
}
],
"tools": [
{
"type": "web_search",
"function": {
"description": "这个函数可以用于搜索不同公司的介绍，比如 特斯拉公司、苹果公司"
}
}
]
}
text = ""
search_result = []
finish_reason = ""
with httpx.Client() as client:
with connect_sse(client, "POST", "https://api.stepfun.com/v1/chat/completions", headers=headers, json=body) as event_source:
for sse in event_source.iter_sse():
# 当返回 "[DONE]"，表示流式结束，可以继续处理后续逻辑
if (sse.data == "[DONE]"):
continue
response_message = json.loads(sse.data)
# 提取内容
text = text + response_message["choices"][0]["delta"]["content"]
if "finish_reason" in response_message["choices"][0]:
finish_reason = response_message["choices"][0]["finish_reason"]
# 处理流式返回中的 Tool Call 逻辑
if "tool_calls" in response_message["choices"][0]["delta"]:
# 可能会命中多个tool
for tool_response in response_message["choices"][0]["delta"]["tool_calls"]:
# 处理 web_search 的 tool
if (tool_response["type"] == "web_search"):
search_result = tool_response["function"]["results"]
print("______result_________")
print(f"完整补全内容：{text}")
print(f"搜索结果: {search_result}")
print(f"结束原因: {finish_reason}")
pass
if __name__ == "__main__":
main()
```


### 常见用法

#### 输出使用到的链接

在展示生成结果时，如果希望展示所使用的 Web 链接，则可以要求大模型在返回时，返回所使用的链接，并通过返回的 tool_calls 的 results 来获取到对应链接的基础信息，并渲染给用户。### 注意事项

- 在使用流式输出时，将会在返回的第一个 chunk 中带上搜索引擎的结果。你可以使用第一个 chunk 来渲染 UI。
- 在使用大模型推理时，你需要写清楚 System Prompt 和 Tool 的 description，以便大模型能够正确理解你的需求，调用互联网搜索。
- 目前在实际调用互联网搜索时，会先进行意图判断，评估是否需要调用互联网搜索，并不会对每一次调用都使用互联网搜索。