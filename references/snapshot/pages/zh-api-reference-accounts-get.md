<!-- title: 获取账户信息 -->
<!-- source: https://platform.stepfun.com/docs/zh/api-reference/accounts/get.md -->

> ## Documentation Index
> Fetch the complete documentation index at: https://platform.stepfun.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 获取账户信息

查询当前账户的信息，支持查询当前账户可用余额.

## 请求地址

`GET https://api.stepfun.com/v1/accounts`

## 请求参数

无

## 请求响应

* `object` `string`<br /> 固定为 `account`

* `type` `string` <br /> 账户类型，可选项为 `prepaid` 预付费 和 `postpaid` 后付费

* `balance` `float` <br /> 当前账户可用余额

* `total_cash_balance` `float`<br /> 当前账户总充值金额

* `total_voucher_balance` `float`<br /> 当前账户总赠送金额

### 示例

<Tabs>
  <Tab title="curl">
    ```bash theme={null}
    curl --location 'https://api.stepfun.com/v1/accounts' \
      --header 'Authorization: Bearer YOUR_STEPFUN_TOKEN'
    ```
  </Tab>

  <Tab title="python">
    ```python theme={null}
    import requests

    url = "https://api.stepfun.com/v1/accounts"

    payload = {}
    headers = {
        "Authorization": "Bearer YOUR_STEPFUN_TOKEN"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    ```
  </Tab>
</Tabs>

**响应**

```json theme={null}
{
  "object": "account",
  "type": "prepaid",
  "balance": 0.00,
  "total_cash_balance": 0.00,
  "total_voucher_balance": 26.00
}
```
