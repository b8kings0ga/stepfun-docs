<!-- title: 快速开始 -->
<!-- source: https://platform.stepfun.com/docs/zh/quickstart/overview.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 快速开始

## 申请 API 密钥

你可以在开放平台 `账号管理` 子菜单<a href="https://platform.stepfun.com/interface-key" target="\_blank" style={{ color: "rgb(0, 107, 230)", textDecoration: "underline" }}>接口密钥</a>中获取 API 密钥

## 环境准备

### Python 依赖安装

对 python 用户，可以复用 openai 的 sdk

```bash theme={null}
pip install --upgrade 'openai>=1.0'
```

### cURL 环境安装

在不同的操作系统上安装 `curl` 命令，会使用不同的包管理器。以下是在 Debian、CentOS 和 macOS 上安装 `curl` 的命令：

1. **Debian/Ubuntu** (使用 `apt` 包管理器):

   ```bash theme={null}
   sudo apt-get update
   sudo apt-get install curl
   ```

2. **CentOS** (使用 `yum` 或 `dnf` 包管理器, CentOS 8 或更高版本使用 `dnf`):

   * 使用 yum:

   ```bash theme={null}
   sudo yum install curl
   ```

   * 使用 dnf(CentOS 8):

   ```bash theme={null}
   sudo dnf install curl
   ```

3. **macOS** (使用 `brew` 包管理器, 如果尚未安装 Homebrew，可以参考[Homebrew 官网](https://brew.sh/)进行安装):

   ```bash theme={null}
   brew install curl
   ```

## 发送请求

在安装好环境依赖并申请了 API 密钥之后，可以使用 python 库或者 curl 发送请求。下列是简单的 python 以及 curl 示例：<br />

<Tabs>
  <Tab title="python">
    ```python copy theme={null}
    from openai import OpenAI

    client = OpenAI(api_key="STEP_API_KEY", base_url="https://api.stepfun.com/v1")

    completion = client.chat.completions.create(
        model="step-3.7-flash",
        messages=[
            {
                "role": "system",
                "content": "你是由阶跃星辰提供的AI聊天助手，你擅长中文，英文，以及多种其他语言的对话。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容",
            },
            {
                "role": "user",
                "content": "你好，请介绍一下阶跃星辰的人工智能!"
            },
        ],
    )

    print(completion)
    ```
  </Tab>

  <Tab title="curl">
    ```bash copy theme={null}
    curl https://api.stepfun.com/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $STEP_API_KEY" \
      -d '{
        "model": "step-3.7-flash",
        "messages": [
          {
            "role": "system",
            "content": "你是由阶跃星辰提供的AI聊天助手，你擅长中文，英文，以及多种其他语言的对话。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容。"
          },
          {
            "role": "user",
            "content": "你好，请介绍一下阶跃星辰的人工智能！"
          }
        ]
      }'
    ```
  </Tab>
</Tabs>

## 响应请求

**stream 和非 stream 返回类似如下：**

<Tabs>
  <Tab title="非stream">
    ```json filename="返回" copy theme={null}
    {
      "id": "4e38135e3515f98a03d51e852cc55003.1e6b4aa12e23140c302a217c50085b77",
      "object": "chat.completion",
      "created": 1772613689,
      "model": "step-3.7-flash",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "阶跃星辰是一家专注于多模态人工智能技术研发的科技公司，致力于提供安全、可靠且具有国际视野的AI助手服务。"
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 85,
        "completion_tokens": 340,
        "total_tokens": 425
      }
    }
    ```
  </Tab>

  <Tab title="stream">
    ```text filename="返回" copy theme={null}
    data: {"id":"e43fc072dff79dd9ada6104f80c34d6c.25f5f6e94c19f48b6f334ab0c6a6f2e6","object":"chat.completion.chunk","created":1772615012,"model":"step-3.7-flash","choices":[{"index":0,"delta":{"role":"assistant","content":""}}],"usage":{"prompt_tokens":85,"completion_tokens":0,"total_tokens":85},"agent":""}

    data: {"id":"e43fc072dff79dd9ada6104f80c34d6c.25f5f6e94c19f48b6f334ab0c6a6f2e6","object":"chat.completion.chunk","created":1772615012,"model":"step-3.7-flash","choices":[{"index":0,"delta":{"role":"assistant","content":"","reasoning":"用户"}}],"usage":{"prompt_tokens":85,"completion_tokens":1,"total_tokens":86},"agent":""}

    data: {"id":"e43fc072dff79dd9ada6104f80c34d6c.25f5f6e94c19f48b6f334ab0c6a6f2e6","object":"chat.completion.chunk","created":1772615012,"model":"step-3.7-flash","choices":[{"index":0,"delta":{"role":"assistant","content":"","reasoning":"想"}}],"usage":{"prompt_tokens":85,"completion_tokens":2,"total_tokens":87},"agent":""}

    ...

    data: {"id":"e43fc072dff79dd9ada6104f80c34d6c.25f5f6e94c19f48b6f334ab0c6a6f2e6","object":"chat.completion.chunk","created":1772615012,"model":"step-3.7-flash","choices":[{"index":0,"delta":{"role":"assistant","content":"阶跃星辰是一家专注于"}}],"usage":{"prompt_tokens":85,"completion_tokens":607,"total_tokens":692},"agent":""}

    data: {"id":"e43fc072dff79dd9ada6104f80c34d6c.25f5f6e94c19f48b6f334ab0c6a6f2e6","object":"chat.completion.chunk","created":1772615012,"model":"step-3.7-flash","choices":[{"index":0,"delta":{"role":"assistant","content":"人工智能技术研发与应用的公司。"}}],"usage":{"prompt_tokens":85,"completion_tokens":614,"total_tokens":699},"agent":""}

    data: {"id":"e43fc072dff79dd9ada6104f80c34d6c.25f5f6e94c19f48b6f334ab0c6a6f2e6","object":"chat.completion.chunk","created":1772615012,"model":"step-3.7-flash","choices":[{"index":0,"delta":{"role":"assistant","content":" 😊"},"finish_reason":"stop"}],"usage":{"prompt_tokens":85,"completion_tokens":616,"total_tokens":701},"agent":""}

    data: [DONE]
    ```
  </Tab>
</Tabs>

**部分异常响应如下(详细错误信息可以参考[错误码](/zh/api-reference/error-codes)文档)：**

* **请求超时机制**：我们为每个请求设定了一个时间限制，即10分钟。如果在这个时间限制内请求没有完成，系统将不会继续等待，而是立即终止该请求，并返回一个状态码为503的错误响应。
* **速率限制**：系统还设置了速率限制来控制请求的频率。如果用户的请求频率超过了这个限制，系统将不会处理超出限制的请求，而是直接返回一个状态码为429的错误响应。这个错误表示“太多请求”，意味着用户在给定的时间窗口内发送了太多的请求。
