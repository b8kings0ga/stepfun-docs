<!-- title: 查询已复刻音色 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/audio/list-voice.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 查询已复刻音色

本 API 可用于查询当前用户下的复刻音色。官方音色可参看[支持音色](/guides/developer/tts#支持音色)

### 请求地址

`GET https://api.stepfun.com/v1/audio/voices`

### 请求参数

* `limit` `string` ***optional***<br />分页的数量，默认 20，最大 100 ，最小 1。默认值为 20。

* `order` `string` ***optional***<br />基于创建时间的返回顺序，支持参数 `asc` 和 `desc`，默认为 `desc`。<br /> `asc`：升序，创建早的音色先出现<br /> `desc` :降序，创建晚的音色先出现

* `before` `string` ***optional***<br /> 指针 ID（音色 ID），可与 limit / order 联合使用

* `after` `string` ***optional***<br /> 指针 ID（音色 ID），可与 limit / order 联合使用。

### 请求响应

* `object` `string`<br />固定为 `list`

* `data` `array`<br /> 音色 ID 的列表
  * `id` `int` <br /> 音色 ID，可用于后续的音频生成
  * `file_id` `int`<br /> 用于复刻音色的音频源文件的 File ID
  * `created_at` `int`<br /> 音色创建的时间

* `has_more` `boolean`<br /> 是否有下一页

* `first_id` `string`<br /> 第一个音色的 ID

* `last_id` `string`<br /> 最后一个音色的 ID

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl --location 'https://api.stepfun.com/v1/audio/voices' \
      --header 'Authorization: Bearer YOUR_STEPFUN_TOKEN'
    ```
  </Tab>

  <Tab title="python">
    ```python theme={null}
    import requests

    url = "https://api.stepfun.com/v1/audio/voices"

    payload = {}
    headers = {
        "Authorization": "Bearer STEPFUN_API_TOKEN"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    ```
  </Tab>
</Tabs>

**响应**

```json theme={null}
{
  "object": "list",
  "data": [
    {
      "id": "voice-tone-FmBrMBqicC",
      "file_id": "file-FmBrMBqicC",
      "created_at": 1742374363
    }
  ],
  "has_more": false,
  "first_id": "voice-tone-FmBrMBqicC",
  "last_id": "voice-tone-FmBrMBqicC"
}
```
