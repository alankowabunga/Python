'''
AJAX/XHR 網站設計
ex. medium website(現已改版，以下程式碼已失效)

其真正的網址並非是 medium.com ，而是在 Headers 中的 Request URL 才是真正能抓到資料的網址
https://medium.com/_/api/home-feed
'''

import urllib.request as rq
url="https://medium.com/_/api/home-feed"

#建立一個Request物件，附加 Request Headers 的資訊
request =rq.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
})
with rq.urlopen(request) as response:
    data=response.read().decode("utf-8") #觀察到取得的資料為 JSON格式

#解析 json 格式的資料，取得每篇文章的標題
import json
#清理原資料的 json 格式
data=data.replace("])}while(1);</x>" , "")
data=json.loads(data) #解析成字典/列表的形式

'''
取得 JSON 資料中的文章標題
其在 payload-references-Post底下
'''
posts=data["payload"]["references"]["Post"]
for key in posts: #利用迴圈一一取得資料
    post=posts[key]
    print(post["title"])