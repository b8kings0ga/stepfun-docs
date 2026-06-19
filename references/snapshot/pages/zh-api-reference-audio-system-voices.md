<!-- title: 获取官方音色详情 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/system-voices.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取官方音色详情

## 接口说明

本接口用于通过 API 获取对应模型的系统默认音色，支持查询指定模型下的所有系统音色，并返回每个音色的详细信息（名称、描述、推荐场景）。

如果将该接口提供给 agent，agent 可拿到当前全部官方音色和描述，并根据场景选择最适配的音色。

## 请求说明

### 请求方式

`GET`

### 请求路径

```text theme={null}
/v1/audio/system_voices
```

### Query 参数

| 参数名   | 类型     | 是否必选 | 支持选项         | 说明                              |
| ----- | ------ | ---- | ------------ | ------------------------------- |
| model | string | 是    | `step-tts-2` | 指定要查询系统音色的模型，目前仅支持 `step-tts-2` |

### 请求示例

```bash theme={null}
GET /v1/audio/system_voices?model=step-tts-2
```

## 返回说明

### 返回格式

`JSON`

### 返回参数说明

| 参数名                                   | 类型             | 说明                                  |
| ------------------------------------- | -------------- | ----------------------------------- |
| voices                                | array\[string] | 系统音色 ID 列表，包含该模型下所有系统音色的唯一标识        |
| voices-details                        | object         | 音色详细信息集合，key 为音色 ID，value 为该音色的具体详情 |
| voices-details.xxx.voice-name         | string         | 音色名称，部分音色可能为空字符串                    |
| voices-details.xxx.voice-description  | string         | 音色描述，包含音色性别、音色特点等信息                 |
| voices-details.xxx.recommended\_scene | string         | 音色推荐使用场景，多个场景用顿号分隔                  |

### 返回示例

```json theme={null}
{
    "voices": [
        "boyinnansheng",
        "cixingnansheng",
        "elegantgentle-female",
        "energeticconfident-female",
        "ganliannvsheng",
        "huolinvsheng",
        "jilingshaonv",
        "jingdiannvsheng",
        "lengyanyujie",
        "linjiajiejie",
        "linjiameimei",
        "lively-girl",
        "livelybreezy-female",
        "magnetic-voiced-male",
        "qingchunshaonv",
        "qingniandaxuesheng",
        "qinhenvsheng",
        "qinqienvsheng",
        "ruanmengnvsheng",
        "ruyananshi",
        "shenchennanyin",
        "shuangkuaijiejie",
        "shuangkuainansheng",
        "soft-spoken-gentleman",
        "tianmeinvsheng",
        "vibrant-youth",
        "wenjingxuejie",
        "wenrougongzi",
        "wenrounansheng",
        "wenrounvsheng",
        "wenroushunv",
        "yingwennansheng",
        "yingwennvsheng",
        "youyanvsheng",
        "yuanqinansheng",
        "yuanqishaonv",
        "zhengpaiqingnian",
        "zhixingjiejie",
        "zixinnansheng"
    ],
    "voices-details": {
        "cixingnansheng": {
            "voice-name": "磁性男声",
            "voice-description": "男，深情厚重，有感染力，霸总感",
            "recommended_scene": "有声书、情感陪伴"
        },
        "linjiameimei": {
            "voice-name": "邻家妹妹",
            "voice-description": "女，可爱亲和，稚气感",
            "recommended_scene": "视频配音、口播（解说、新闻）、语音助手"
        },
        "zhengpaiqingnian": {
            "voice-name": "正派青年",
            "voice-description": "男，音色具有感染力、说服力和亲和力，有激情和鼓动性",
            "recommended_scene": "营销"
        },
        "elegantgentle-female": {
            "voice-name": "气质温婉",
            "voice-description": "女，真诚温柔，亲和力强，给人安全感",
            "recommended_scene": "客服与业务办理、口播（解说、新闻）、教育与培训、情感陪伴"
        },
        "ruanmengnvsheng": {
            "voice-name": "软萌女声",
            "voice-description": "女，可爱、甜、嗲",
            "recommended_scene": "情感陪伴、语音助手、视频配音"
        },
        "yuanqinansheng": {
            "voice-name": "元气男声",
            "voice-description": "男，情绪饱满有活力",
            "recommended_scene": "有声书、口播（解说、新闻）"
        },
        "shuangkuaijiejie": {
            "voice-name": "爽快姐姐",
            "voice-description": "女，清澈有活力",
            "recommended_scene": "口播（解说、新闻）、语音助手"
        },
        "zixinnansheng": {
            "voice-name": "自信男声",
            "voice-description": "男，真诚亲和，有活力",
            "recommended_scene": "有声书、情感陪伴、教育与培训、营销"
        },
        "wenjingxuejie": {
            "voice-name": "文静学姐",
            "voice-description": "女，冷静沉稳，吐字清晰稳定",
            "recommended_scene": "口播（解说、新闻）、语音助手"
        },
        "qingchunshaonv": {
            "voice-name": "清纯少女",
            "voice-description": "女，温柔，轻盈有活力，亲和力强",
            "recommended_scene": "客服与业务办理、语音助手"
        },
        "livelybreezy-female": {
            "voice-name": "活力轻快",
            "voice-description": "女，音色具有感染力、说服力和亲和力，有活力",
            "recommended_scene": "情感陪伴、教育与培训、营销"
        },
        "ganliannvsheng": {
            "voice-name": "干练女声",
            "voice-description": "女，音色沉稳冷静、慢条斯理，专业感强",
            "recommended_scene": "客服与业务办理、语音助手"
        },
        "tianmeinvsheng": {
            "voice-name": "甜美女声",
            "voice-description": "女，甜美温柔，亲和力强",
            "recommended_scene": "情感陪伴、客服与业务办理"
        },
        "vibrant-youth": {
            "voice-name": "Vibrant Youth",
            "voice-description": "男，英文音色，温柔亲和",
            "recommended_scene": "有声书、视频配音、语音助手"
        },
        "ruyananshi": {
            "voice-name": "儒雅男士",
            "voice-description": "男，沉稳厚重，叙述感强，有亲和力、陪伴感",
            "recommended_scene": "有声书、情感陪伴、口播（解说、新闻）、语音助手"
        },
        "youyanvsheng": {
            "voice-name": "优雅女声",
            "voice-description": "女，成熟亲和，给人踏实感",
            "recommended_scene": "视频配音"
        },
        "jingdiannvsheng": {
            "voice-name": "经典女声",
            "voice-description": "女，语速较慢，真诚温柔",
            "recommended_scene": "客服与业务办理、情感陪伴"
        },
        "linjiajiejie": {
            "voice-name": "邻家姐姐",
            "voice-description": "女，有亲和力，邻家大姐姐的感觉，给人安全感",
            "recommended_scene": "口播（解说、新闻）、情感陪伴、语音助手、视频配音"
        },
        "energeticconfident-female": {
            "voice-name": "",
            "voice-description": "女，英文音色，有活力且自信",
            "recommended_scene": "客服与业务办理、语音助手"
        },
        "boyinnansheng": {
            "voice-name": "播音男声",
            "voice-description": "男，播音腔，中正平稳",
            "recommended_scene": "有声书、口播（解说、新闻）"
        },
        "yuanqishaonv": {
            "voice-name": "元气少女",
            "voice-description": "女，声线细腻，甜、嗲",
            "recommended_scene": "情感陪伴、语音助手"
        },
        "shuangkuainansheng": {
            "voice-name": "爽快男声",
            "voice-description": "男，音色沉稳冷静、慢条斯理，专业感强",
            "recommended_scene": "客服与业务办理、语音助手"
        },
        "qingniandaxuesheng": {
            "voice-name": "青年大学生",
            "voice-description": "男，沉稳厚实，播音专业感",
            "recommended_scene": "口播（解说、新闻）"
        },
        "zhixingjiejie": {
            "voice-name": "知性姐姐",
            "voice-description": "女，成熟沉稳，叙述有画面感",
            "recommended_scene": "视频配音、口播（解说、新闻）、语音助手"
        },
        "qinqienvsheng": {
            "voice-name": "亲切女声",
            "voice-description": "女，温柔带点甜美，亲和力强，邻家感",
            "recommended_scene": "口播（解说、新闻）、情感陪伴、语音助手"
        },
        "wenroushunv": {
            "voice-name": "温柔熟女",
            "voice-description": "女，成熟稳重，温柔有亲和力",
            "recommended_scene": "客服与业务办理、口播（解说、新闻）、教育与培训"
        },
        "qinhenvsheng": {
            "voice-name": "亲和女声",
            "voice-description": "女，冷静温柔、有亲和力",
            "recommended_scene": "客服与业务办理、语音助手"
        },
        "shenchennanyin": {
            "voice-name": "深沉男音",
            "voice-description": "男，有感情，代入感强，给人信心",
            "recommended_scene": "情感陪伴、有声书"
        },
        "huolinvsheng": {
            "voice-name": "活力女声",
            "voice-description": "女，轻盈有活力，亲和力强",
            "recommended_scene": "客服与业务办理、语音助手"
        },
        "wenrougongzi": {
            "voice-name": "温柔公子",
            "voice-description": "男，沉稳温柔，叙述感强",
            "recommended_scene": "情感陪伴、有声书"
        },
        "soft-spoken-gentleman": {
            "voice-name": "Soft-spoken Gentleman",
            "voice-description": "男，英文音色，沉稳温柔，给人安全感",
            "recommended_scene": "情感陪伴、有声书"
        },
        "lively-girl": {
            "voice-name": "Lively Girl",
            "voice-description": "女，英文音色，亲和感，有活力",
            "recommended_scene": "有声书、视频配音、语音助手"
        },
        "wenrounvsheng": {
            "voice-name": "温柔女声",
            "voice-description": "女，温柔甜美，叙述感强，有关怀感",
            "recommended_scene": "有声书、情感陪伴"
        },
        "wenrounansheng": {
            "voice-name": "温柔男声",
            "voice-description": "男，温柔亲和",
            "recommended_scene": "口播（解说、新闻）、情感陪伴、客服与业务办理、教育与培训"
        },
        "jilingshaonv": {
            "voice-name": "机灵少女",
            "voice-description": "女，声线细腻，有活力",
            "recommended_scene": "语音助手、口播（解说、新闻）"
        },
        "lengyanyujie": {
            "voice-name": "冷艳御姐",
            "voice-description": "女，播音感，专业不失亲和",
            "recommended_scene": "视频配音"
        },
        "magnetic-voiced-male": {
            "voice-name": "Magnetic-voiced Male",
            "voice-description": "男，英文音色，强烈的沉稳厚重感",
            "recommended_scene": "有声书、视频配音"
        }
    }
}
```

## 注意事项

* `voices` 数组中的音色 ID 与 `voices-details` 中的 key 一一对应，可通过音色 ID 查询对应详情。
* 推荐场景仅为参考，用户可根据实际需求选择合适的音色。
