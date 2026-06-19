<!-- title: Tool Call 使用建议 -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/developer/tool-call.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tool Call 使用建议

大模型虽然掌握了丰富的知识，但在特定领域，例如时效性较高的资讯类和天气预报，或者需要严密科学计算，以及特定行业的知识，当它们匮乏这部分知识时，它们可能会编造看似真实但实则虚假的信息。

为解决这一问题。阶跃大模型提供了 Tool call 工具，Tool call 可以扩展语言模型的功能，使其能够执行额外的操作，如搜索信息、科学计算、访问数据库等。这样模型可以为用户提供更精准的信息，帮助开发者更好地处理业务需求。

除了获取信息以外， Tool Call 还可以帮助开发者生成函数调用签名，开发者通过对调用签名的处理，实现扩展应用能力，让你的应用除了对话，还可以完成各项不同的能力。

### 实现原理 & 参考

在使用 Tool Call 时，我们可以选择两个方向来思考 Tool Call 帮助我们扩展应用能力：

* 使用 Tool Call 获取大模型自身训练不包含的信息，丰富上下文，精确回答内容；
* 使用 Tool Call 操作本地应用程序，执行特定业务操作。

<img src="https://mintcdn.com/stepfun/ivZhb9pOE5X12y-g/images/tool_call.jpeg?fit=max&auto=format&n=ivZhb9pOE5X12y-g&q=85&s=7c8a235c4ace3e198467a444cee565e8" alt="" width="4418" height="2134" data-path="images/tool_call.jpeg" />

前者主要通过 Tool Call 调用预定义好的函数，以获得更加精确的信息，帮助大模型补全上下文，从而生成更加精确的回答。
后者则是通过 Tool Call 调用本地应用程序，执行特定的业务操作，以实现更加丰富的功能。

#### 使用 Tool Call 获取信息

这里我们以助手类应用的常见技能 —— 查询天气为例，我们需要构建一个可以通过自然语言，查询天气的能力。

你需要做以下四步：

* 第一步，需要准备好查询天气接口的地址和密钥，构造查询天气的 Function；
* 第二步，构建 get\_weather 工具定义查询天气 Function 的功能；
* 第三步，阶跃大模型识别用户查询天气的意图时，根据提示语给出查询参数；
* 第四步，使用大模型返回的参数调用查天气接口，获取准确的天气信息。

参考代码：以 Python 为例

```python theme={null}
from openai import OpenAI
import requests
import json

# 初始化 查询天气的接口参数，这里我使用的是高德查询天气接口，各位开发者可以按需自行选择供应商进行实现
get_weather_url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
get_weather_key = "YourGaoDeAPIkey"
COMPLETION_MODEL= "step-3.7-flash"

# 初始化 阶跃星辰 Client
STEPFUN_KEY = "YourAPIkey"
client = OpenAI(base_url="https://api.stepfun.com/v1", api_key=STEPFUN_KEY)

# 初始化查询天气的函数
def get_weather(city):
    params = {
        "city": city,
        "key": get_weather_key,
        "extensions": "base",  # 获取实时天气
    }
    response = requests.get(url=get_weather_url, params=params)  # 实时天气
    if response.status_code == 200:
        data = response.json()
        print(data)
        # weather = data.get ('lives')[0].get ('weather')  # 当前天气现象
        # temperature = data ['lives'][0].get ('temperature')  # 当前温度
        # print ( f"{city} 现在的天气是 {weather} 温度是 {temperature}°C.")
    else:
        print("对不起，我无法获取这个地点的天气。")

# 构建 get_weather 函数说明
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "查询天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "城市名称（必须为汉字）"}
                },
                "required": ["city"],
            },
        },
    }
]

# 调用补全接口进行补全
def query_weather(prompt):
    completion = client.chat.completions.create(
        model=COMPLETION_MODEL,
        messages=[{"role": "user", "content": prompt}],
        ## 自动选择是否调用外部函数
        tool_choice="auto",
        tools=tools,
    )
    # print (completion.choices [0].message.content.strip ())
    print(completion)
    # 判断是否命中查询天气 Function
    if completion.choices[0].message.content.strip() == "":
        if completion.choices[0].message.tool_calls[0].function.name == "get_weather":
            # 获取参数
            city_name = json.loads(
                completion.choices[0].message.tool_calls[0].function.arguments
            )
            # 调用 Function
            get_weather(city_name["city"])
        else:
            print("未命中查询天气 Tool")
    else:
        print("抱歉出错了")
        # print (completion.choices [0].message.content.strip ())

# 查询天气
query_weather("上海现在的天气怎么样？")

```

返回结果：

```jsonc theme={null}
# 返回值结果
# 首先大模型通过意图识别到需要调用 Tool Call，所以在 tool_calls 里给出了需要调用的函数名称，以及参数
{
    "id": "291c59ebf4017a937a2a42a8ed52581f.c2669ebc05a491c70f821b4e568b6433",
    "object": "chat.completion",
    "created": 1722505763,
    "model": "step-3.7-flash",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "",
                "tool_calls": [
                    {
                        "id": "call_brg23SRcTgmpm_V0jfP-iA",
                        "type": "function",
                        "function": {
                            "name": "get_weather",
                            "arguments": "{\"city\": \" 上海 \"}"
                        }
                    }
                ]
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "cached_tokens": 48,
        "prompt_tokens": 94,
        "completion_tokens": 16,
        "total_tokens": 110
    }
}
# 接着使用大模型给出的参数调用查询天气接口，获得准确的天气
{
    "status": "1",
    "count": "1",
    "info": "OK",
    "infocode": "10000",
    "lives": [
        {
            "province": "上海",
            "city": "上海市",
            "adcode": "310000",
            "weather": "晴",
            "temperature": "37",
            "winddirection": "西北",
            "windpower": "≤3",
            "humidity": "42",
            "reporttime": "2024-08-02 10:01:14",
            "temperature_float": "37.0",
            "humidity_float": "42.0"
        }
    ]
}

# 继续拼接作为上下文信息放入 Messages，让大模型进行补全。
```

#### 使用 Tool Call 执行任务

当应用需要扩展其能力，不仅仅是获取数据时，则可以通过 Tool Call 能力，为你的应用增加一些神奇的能力，从而帮助用户更进一步展示不同的能力。

这里我们同样以助手类应用为例，我们可以实现一个通过自然语言发送电子邮件的能力。你需要做以下几步：

* 第一步，在本地构建出一个发送邮件的 Function ，并实现发送邮件相关功能；
* 第二步，构建 send\_email 工具定义发送邮件的功能；
* 第三步，阶跃大模型识别用户发送邮件的意图时，根据提示语给出查询参数；
* 第四步，使用大模型返回的参数调用发送电子邮件。

##### 参考代码：以 Python & Swift 为例

本地的发送邮件的 Function

```swfit theme={null}
func sendEmail (subject:String, body: String, recipient: String) {
    // 调用 MFMailComposeViewController 来发送邮件
}
```

服务端调用阶跃星辰大模型的参考代码

```python theme={null}
from openai import OpenAI

# 初始化 阶跃星辰 Client
STEPFUN_KEY = "YourAPIkey"
client = OpenAI(base_url="https://api.stepfun.com/v1", api_key=STEPFUN_KEY)

# 构建 sendEmail 函数说明
tools = [
    {
        "type": "function",
        "function": {
            "name": "senEmail",
            "description": "这个函数可以用于向特定的用户发送包含特定内容的电子邮件",
            "parameters": {
                "type": "object",
                "properties": {
                    "subject": {
                        "type": "string",
                        "description": "邮件的标题，不可以超过 255 个字",
                    },
                    "body": {
                        "type": "string",
                        "description": "邮件内容，不可以超过 4096 个子",
                    },
                    "recipient": {"type": "string", "description": "收件人"},
                },
                "required": ["subject", "body", "recipient"],
            },
        },
    }
]

# 调用阶跃星辰 API 生成接口调用方法
def get_call_sign(user_input):
    completion = client.chat.completions.create(
        model=COMPLETION_MODEL,
        messages=[{"role": "user", "content": user_input}],
        ## 自动选择是否调用外部函数
        tool_choice="auto",
        tools=tools,
    )
    if completion.choices[0].message.content.strip() == "":
        if completion.choices[0].message.tool_calls[0].function.name == "senEmail":
            # 获取参数
            arguments = json.loads(
                completion.choices[0].message.tool_calls[0].function.arguments
            )
            # 触发本地调用函数
            send_to_client("sendEmail", arguments)

```

#### 注意事项

* 构造 Tool 的时候请注意将 Function 的 description 描述清楚，以便于大模型清晰的知道 Function 的功能，这样能提高命中率；
* Function 入参的 description 也需要备注清楚（建议说明入参是中文还是英文），以便于大模型生成有效的参数供使用。
