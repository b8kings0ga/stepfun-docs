<!-- title: StepSearch -->
<!-- source: https://platform.stepfun.com/docs/zh/step-plan/integrations/search-mcp.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# StepSearch

StepSearch MCP Server 是基于模型上下文协议（Model Context Protocol）实现的搜索服务，为 Claude Code、Cline、OpenCode 等兼容 MCP 的客户端提供阶跃星辰的专业搜索能力，包括网络搜索、网页内容获取等功能。

## 功能特性

* **实时搜索**：支持全网搜索，获取最新的网络信息和资源
* **编程增强**：在开发过程中检索编程最佳实践、API 文档及论文等
* **远程服务**：基于 HTTP 协议的远程 MCP 服务，无需本地安装

## 支持的工具

该服务实现了模型上下文协议，可与任何兼容 MCP 的客户端一起使用。目前提供以下工具：

| 工具           | 说明                   |
| ------------ | -------------------- |
| `web_search` | 全网信息检索与索引化结果输出       |
| `web_fetch`  | 指定 URL 的网页内容抓取与结构化提取 |

## 快速开始

### 1. 获取访问令牌

前往 [阶跃星辰开放平台](https://platform.stepfun.com/interface-key) 获取您的 API Key。

### 2. 配置 MCP 服务器

根据您使用的客户端，选择对应标签页查看配置方式。

<Tabs>
  <Tab title="Claude Code">
    **一键安装命令：**

    ```bash theme={null}
    claude mcp add -s user -t http web-search https://api.stepfun.com/step_plan/v1/mcp/web_search/mcp --header "Authorization: Bearer your_api_key"
    ```

    **手动配置：**

    编辑 Claude Code 的配置文件（位于用户目录下 `~/.claude.json`）：

    ```json theme={null}
    {
      "mcpServers": {
        "web-search": {
          "type": "http",
          "url": "https://api.stepfun.com/step_plan/v1/mcp/web_search/mcp",
          "headers": {
            "Authorization": "Bearer your_api_key"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="Cline（VS Code）">
    安装 Cline 扩展后，在侧边栏点击右上角 **MCP Servers** → **Configure** → **Configure MCP Servers**，将以下配置粘贴并保存：

    ```json theme={null}
    {
      "mcpServers": {
        "web-search": {
          "type": "streamableHttp",
          "url": "https://api.stepfun.com/step_plan/v1/mcp/web_search/mcp",
          "headers": {
            "Authorization": "Bearer your_api_key"
          }
        }
      }
    }
    ```
  </Tab>

  <Tab title="OpenCode">
    编辑全局配置文件 `~/.config/opencode/opencode.json`，将以下内容粘贴并保存：

    ```json theme={null}
    {
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "web-search": {
          "type": "remote",
          "url": "https://api.stepfun.com/step_plan/v1/mcp/web_search/mcp",
          "headers": {
            "Authorization": "Bearer your_api_key"
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

## 使用示例与最佳实践

将搜索 MCP 服务器安装到客户端后，即可在对话中直接使用搜索能力。以下是几种典型使用场景。

### 预备：创建搜索专用 Agent

Claude Code 通过 `.claude/agents/` 目录下的定义文件来识别可用的 Sub-Agent。创建专用搜索 Agent 后，Claude Code 可以在需要实时信息时自动调用该 Sub-Agent 执行搜索任务，每次处理一个查询并返回结构化结果。

**1. 创建 Agent 定义文件**

在项目根目录下创建 `.claude/agents/search-agent.md`：

```markdown theme={null}
---
name: search-agent
description: 执行网络搜索，获取实时信息（最新版本、CVE 漏洞、定价、社区反馈等）。每次只处理一个查询并返回结构化结果。
tools: mcp__web-search__web_search, mcp__web-search__web_fetch
---

你是专职网络搜索助手，只负责执行搜索任务并返回结构化结果。

## 工作流程

1. 接收主 Agent 传入的搜索关键词
2. 使用可用的 Search MCP 工具执行搜索
3. 过滤并整理结果
4. 返回结构化输出

## 输出格式

每次搜索按以下格式返回：

### 查询：[搜索关键词]

**结果 1**：
- 标题：[文章或页面标题]
- 核心结论：（1-2 句话概括关键发现）
- 代码片段：（如有相关代码，最多 10 行）
- 来源：[URL]

## 规则

- 每次查询最多返回 3 条最相关结果
- 不得返回网页全文
- 只返回与查询直接相关的信息
- 优先返回含代码示例的结果
- 优先返回近期内容（1-2 年内）
- 过滤 SEO 垃圾内容和低质量页面
```

**2. 在 CLAUDE.md 中配置调用规则**

在项目的 `CLAUDE.md` 中添加以下内容，告诉 Claude Code 什么时候使用搜索 Agent：

```markdown theme={null}
## 搜索 Sub-Agent 调用规则

### 可用的搜索 Agent
- **search-agent**: 通过 Search MCP 执行网络搜索，用于获取实时信息（CVE、定价、社区反馈等）

### 什么时候调用
- 涉及最新版本、安全漏洞、定价限额等模型知识无法覆盖的实时信息时，使用 search-agent
- 不要用于模型能直接回答的问题（基础语法、技术选型、Bug 修复等）

### 多查询调用规则
- 当有多个独立搜索需求时，为每个查询单独调用一次 search-agent
- 每个 Agent 实例只处理一个查询，保持结果清晰可追溯
```

### 场景一：多 API 文档查询

项目集成多个第三方服务时，需要获取各服务的最新 API 用法。第三方 API 随时可能更新，模型训练时的文档版本可能已过时。

```text theme={null}
我正在开发一个 SaaS 付费功能：用户付款 → 发送确认邮件 → 文件上传到云存储。

涉及的服务：
- Stripe（支付）
- Resend（邮件）
- Cloudflare R2（存储）

请使用 search-agent 通过 search mcp 依次查询各服务的最新官方文档：
1. Stripe: Checkout Session 创建 + Webhook 验证
2. Resend: 发送邮件 API + 模板功能
3. Cloudflare R2: S3 兼容 API 上传

输出：整合后的 Node.js 实现方案，包含完整代码示例。
```

### 场景二：代码安全审计 + CVE 搜索

审查代码安全性时，模型可以识别漏洞模式，但需要搜索最新的 CVE 信息和安全公告。

```text theme={null}
请审计以下代码的安全性：
[粘贴代码]

第一步：直接分析代码中的漏洞（不需要搜索）。
第二步：使用 search-agent 搜索以下三个方向：
1. "jsonwebtoken npm vulnerability CVE 2024 2025" — 查该依赖的最新已知漏洞
2. "OWASP authentication best practices 2024" — 查最新认证安全指南
3. "bcrypt vs argon2 vs scrypt comparison 2024" — 查当前推荐的密码哈希方案

输出：
- 漏洞清单（分：模型识别 vs 搜索发现）
- 修复后的完整代码
- 依赖安全建议
```

### 场景三：依赖升级影响分析

升级主要依赖版本时，新版本的 breaking changes 和社区反馈往往是模型训练后产生的实时信息。

```text theme={null}
我需要将项目从 Next.js 14 升级到 Next.js 15。

请使用 search-agent 搜索以下方向：
1. "Next.js 15 breaking changes migration issues"
2. "Next.js 15 upgrade problems Reddit GitHub"
3. "Next.js 15 app router changes 2024"

输出：
- 升级检查清单（官方文档 vs 社区踩坑）
- 必须修改的代码示例
- 需要同步升级的依赖列表
- 社区反馈的高频问题
```

### 场景四：开源生态实时调研

评估开源项目时，GitHub stars、最近 commit、维护者动态都是实时数据，模型无法直接回答。

```text theme={null}
我在考虑使用 Drizzle ORM，但想了解它当前的生态状态。

请使用 search-agent 搜索以下方向：
1. "Drizzle ORM GitHub issues bugs 2024" — 最近的 bug 和问题
2. "Drizzle ORM production experience" — 生产环境使用反馈
3. "Drizzle ORM vs Prisma 2024 comparison" — 最新的对比评测
4. "Drizzle ORM roadmap changelog" — 近期发展方向

我不需要你介绍 Drizzle 是什么（我知道），
我需要的是：它现在稳定吗？社区活跃吗？有什么已知的坑？
```

## MCP 使用额度说明

* **计费规则**：`web_search` 按照开放平台网络搜索的计价方式收费，每次调用 0.04 元，与 Step Plan 其他用量一并消耗 Credit 额度；`web_fetch` 不单独计费
* **额度周期**：消耗 Step Plan 月度 Credit，月池月末清零，可用加油包补充
* **限流策略**：以 QPM / QPH / 并发控制为主，并对单用户增加必要限频

如需订阅或升级套餐，请访问：[Step Plan 订阅](https://platform.stepfun.com/step-plan)

## 常见问题

### 访问令牌无效？

* 确认 API Key 已完整复制，没有多余空格
* 验证 Key 已激活且余额充足
* 检查 `Authorization` 头格式是否正确（需包含 `Bearer ` 前缀，注意空格）

### 连接超时？

* 检查网络连接是否正常
* 确认防火墙未拦截对 `api.stepfun.com` 的访问
* 确认服务端点 URL 拼写正确

### 搜索结果为空？

* 尝试调整搜索关键词的表述方式
* 避免过于具体或过于宽泛的查询条件
* 确保网络连接正常

## 参考链接

* [Model Context Protocol 官方文档](https://modelcontextprotocol.io/)
* [Claude Code MCP 配置指南](https://docs.anthropic.com/en/docs/claude-code/mcp)
* [Step Plan 订阅](https://platform.stepfun.com/step-plan)
* [阶跃星辰开放平台](https://platform.stepfun.com)
* [Search API 文档](https://platform.stepfun.com/docs/zh/api-reference/Search/search)
