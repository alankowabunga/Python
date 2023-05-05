import urllib.request as rq
url="https://www.ptt.cc/bbs/movie/index.html"

#不像一般使用者, 會無法讀取網頁~~
#建立一個request物件，附加 Request headers 的 User-Agent 資訊
request=rq.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
})
#利用request物件，去urlopen(request物件) 當作 response
with rq.urlopen(request) as response:
    data=response.read().decode("utf-8")
    print(data)

# 解析原始碼 ，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,"html.parser") # 使用 BeautifulSoup 解析 HTML 格式文件
#print(root.title) 整個標籤
#print(root.title.string) 標籤裡的文字
titles=root.find("div", class_="title") #尋找 class = "title" 裡的 div 標籤
print(titles)
print("======================")
print("root.find 只找到一個標題 \n", titles.a.string) # 只要標題的 a 標籤中的字串
print("================= \n 接者利用 find_all & for loop")

# 利用 find_all()去找 , 再利用 for 迴圈去取出並篩選
titles=root.find_all("div", class_="title")
for title in titles:
    if title.a != None: # 篩選出標題中有 a  的標籤 (沒有被刪除的)
        print(title.a.string) # 只要標題的 a 標籤中的字串