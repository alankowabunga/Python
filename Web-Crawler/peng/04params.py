'''
使用 get 的方式發送 request 給範例的網址，
並會加入 params 參數(dict)，當網址收到資料後，就會回傳指定的文字。

'''

import requests
#設定參數
my_params={
    "name":"Alan",
    "age":"26"
}
#加入參數
web=requests.get("https://script.google.com/macros/s/AKfycbw5PnzwybI_VoZaHz65TpA5DYuLkxIF-HUGjJ6jRTOje0E6bVo/exec",params=my_params)
print(web.text)