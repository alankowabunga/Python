'''html 轉譯文字問題未解決'''
#抓取ptt八卦版的網頁原始碼
import urllib.request as rq
def getData(url):
    #建立一個 Request 物件，附加 Request Headers 的資訊
    request=rq.Request(url, headers={"cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})

    with rq.urlopen(request) as response:
        data=response.read().decode("utf-8")

    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") #解析 html 格式
    titles=root.find_all("div",class_="title") #尋找所有 class="title" 的 div 標籤
    for title in titles:
        if title.a != None: #如果逼題包含a標籤(沒有被刪除)則印出來
            print(title.a.string)

    import html

    nextLink=root.find("a",string="&lsaquo; 上頁") #尋找內文是 上頁 的a標籤
    nextLink=html.unescape(nextLink)
    return nextLink["href"] #2.程式碼跑完抓到上一頁的連結，並返回return後寫入pageURL

#要抓取多個頁面的標題，利用def函式作包裝
pageURL="https://www.ptt.cc/bbs/Gossiping/index39213.html"

#主程序:利用迴圈抓取多個頁面的標題
count=0
while count<3:
    pageURL="https://www.ptt.cc" + getData(pageURL)
    count+=1


#因為getData(pageURL)只能抓到/Gossiping/index39213.html，所以要自行補上"https://www.ptt.cc"
# pageURL="https://www.ptt.cc" + getData(pageURL) #1.呼叫函式將pageURL帶入程式碼，
# getData(pageURL) #3.最後將已寫入上一頁的連結，印出完整的連結