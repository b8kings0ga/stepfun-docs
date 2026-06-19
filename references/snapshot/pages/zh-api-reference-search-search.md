<!-- title: Search -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/search/search.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search

支持搜索互联网信息，针对重点场景优化站点权威性，更好适配深入研究等对信源要求较高的场景

## 请求地址

`POST https://api.stepfun.com/v1/search`

## 请求参数

* `query` `string` `required` <br />要搜索的关键词
* `n` `int` `optional` <br /> 返回的结果条数，默认为 10 ，可选范围 1\~20.
* `category` `string` `optional` <br />要使用的搜索场景；默认为空，搜索所有场景。<br />
  支持字段
  * `programming`:代码编程场景
  * `research`：学术研究场景
  * `gov`:政务研究场景
  * `business`：商业财经场景

## 请求响应

* `query` `string` <br /> 搜索的关键词
* `n` `int` <br /> 返回的结果条数
* `results` `array`<br />搜索返回的结果
  <Expandable>
    * `url` `string`<br />搜索结果的 URL
    * `position` `int`<br />返回结果的 位置，从 1 开始
    * `title` `string`<br />返回结果的标题
    * `time` `string`<br />返回结果的网页的索引时间
    * `snippet` `string`<br />返回结果的网页的基础内容
    * `content` `string`<br />返回结果的网页的完整内容
  </Expandable>

## 参考代码

```bash theme={null}
curl -X "POST" "https://api.stepfun.com/v1/search" \
     -H 'Authorization: Bearer YOUR_STEPFUN_API_KEY' \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "query": "北京 天气",
  "n": 1,
  "category": "research"
}'
```
