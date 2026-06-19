<!-- title: 手机操作 Agent -->
<!-- source: https://platform.stepfun.com/docs/zh/guides/models/step-3.7-flash-mobile-agent.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 手机操作 Agent

> 通过 GELab-Zero 连接 Android 真机，让 Step 3.7 Flash 基于屏幕截图规划操作

`step-3.7-flash` 的多模态理解能力可以用于手机 GUI Agent 场景：模型读取手机截图、任务描述和历史轨迹，判断下一步动作，再由运行框架把动作执行到 Android 真机上。

当前推荐使用 [GELab-Zero](https://github.com/stepfun-ai/gelab-zero) 跑通这类任务。GELab-Zero 是一个面向 Android 手机上的 GUI Agent 运行框架，负责连接手机、采集截图、调用多模态模型、执行动作并记录过程。

<Info>
  手机操作 Agent 涉及真机、ADB、模型调用和本地运行环境，适合作为进阶场景使用。第一次接入建议先完成 [多模态快速上手](/zh/guides/models/step-3.7-flash-quickstart)，确认 API Key 与模型调用正常。
</Info>

## 工作流程

GELab-Zero 将模型决策和手机执行串成一条完整链路：

1. 你给 Agent 一个自然语言任务。
2. 电脑通过 ADB 连接 Android 手机并获取截图。
3. 框架把当前截图、历史轨迹和任务描述发给多模态模型。
4. 模型输出下一步动作，例如 `AWAKE`、`CLICK`、`TYPE`、`SLIDE`。
5. 框架把动作真正执行到手机上。
6. 每一步截图、动作和模型输出都会被记录。
7. 任务结束后，可以通过可视化页面按 `Session ID` 回看整个过程。

## 前置准备

运行前需要准备：

* 一台 Android 手机，并开启开发者模式和 USB 调试
* ADB / platform-tools
* Python 3.12+
* GELab-Zero 仓库代码与依赖
* 可用的 Step API Key

手机需要先通过 USB 连接电脑，并确认 ADB 可以识别：

```bash theme={null}
adb devices
```

如果设备状态显示为 `unauthorized`，需要在手机上允许 USB 调试授权。

## 安装 GELab-Zero

```bash theme={null}
git clone https://github.com/stepfun-ai/gelab-zero
cd gelab-zero
pip install -r requirements.txt
```

建议从 GELab-Zero 项目根目录执行后续命令。

## 配置模型服务

GELab-Zero 的模型调用会读取 `model_config.yaml`，并通过 OpenAI 兼容接口发起请求。先在 `model_config.yaml` 中配置 Step API：

```yaml theme={null}
stepfun:
  api_base: "https://api.stepfun.com/v1"
  api_key: "YOUR_API_KEY"
```

然后在 `examples/run_single_task_state_compress.py` 中把模型 provider 指向 `stepfun`，并使用 `step-3.7-flash`：

```python theme={null}
local_model_config = {
    "task_type": "parser_0920_summary_adv_state_compress",
    "model_config": {
        "model_name": "step-3.7-flash",
        "model_provider": "stepfun",
        "args": {
            "temperature": 1,
            "top_p": 0.95,
            "frequency_penalty": 0.05,
            "max_tokens": 32768,
        },
    },
    "config": {
        "enable_state_compression": True,
        "state_compression_interval": 10,
        "state_compression_recent_window": 10,
        "state_compression_max_field_items": 10,
    },
    "max_steps": 400,
    "delay_after_capture": 3,
    "debug": False,
}
```

<Note>
  GELab-Zero 的极简运行指南建议 `temperature` 保持为 `1`，不要改成 `0.1` 或 `0.5`。长轨迹任务建议开启 state compression，避免历史上下文持续膨胀。
</Note>

## 运行手机任务

先确认手机仍然在线：

```bash theme={null}
adb devices
```

然后运行单个任务：

```bash theme={null}
python examples/run_single_task_state_compress.py \
  --task "帮我看看微博文娱热搜上有哪些内容，总结一下给我"
```

如果电脑连接了多台设备，建议显式指定设备：

```bash theme={null}
python examples/run_single_task_state_compress.py \
  --device-id AN2CVB4C28000731 \
  --task "帮我看看微博文娱热搜上有哪些内容，总结一下给我"
```

运行后终端会打印 `Session ID`、每一步耗时、当前动作和最终总耗时。任务日志默认写入：

* `running_log/server_log/os-copilot-local-eval-logs/traces`
* `running_log/server_log/os-copilot-local-eval-logs/images`

## 查看执行过程

GELab-Zero 提供本地可视化页面，用于查看每一步截图、模型思考和动作结果：

```bash theme={null}
streamlit run visualization/pages/main_page.py \
  --server.address 127.0.0.1 \
  --server.port 33503
```

启动后打开：

```text theme={null}
http://localhost:33503
```

从任务终端复制 `Session ID`，粘贴到页面输入框后即可回看完整执行轨迹。

## 参考

<Card title="GELab-Zero 极简运行指南" href="https://github.com/stepfun-ai/gelab-zero/blob/main/%E6%9E%81%E7%AE%80%E8%BF%90%E8%A1%8C%E6%8C%87%E5%8D%97_CN.md">
  查看 Android 真机配置、State Compress 入口、推荐参数和可视化页面说明。
</Card>
