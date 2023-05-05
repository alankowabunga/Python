import urllib.request as rq

url="https://www.ptt.cc/bbs/Bank_Service/index.html"

#建立一個request物件，附加 Request headers 的 User-Agent 資訊
request=rq.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
})

#利用request物件，去urlopen(request物件) 當作 response
with rq.urlopen(request) as response:
    data=response.read().decode("utf-8")

#解析原始碼, 載入Beautiful Soup模組
import bs4
root=bs4.BeautifulSoup(data, "html.parser")

titles=root.find_all("div",class_="title")

'''
接著要將擷取的資料，儲存至 csv 檔案中，首先要匯入 csv 模組，
然後透過 with open 建立檔案名稱，最後 newline=" " 是確保寫入的每行最後面不會有多餘的換行，
然後建立 writer 物件，就可以使用 writerow 的方法寫入檔案，先寫入欄位標題後，再透過 for 迴圈一筆筆將每部電影的資料寫入檔案中
'''
import csv

with open("Bank_Service.csv","w",encoding="utf-8",newline="") as csvFile:
    write =  csv.writer(csvFile,delimiter=" ")
    write.writerow(["ptt Bank Service版 爬蟲結果"])

    for title in titles:
        if title.a != None:
            write.writerow(title.a.string)
            

with open("Bank_Service.csv","r",encoding="utf-8",newline="")  as csvFile:
    reader=csv.reader(csvFile)
    
    for info in reader:    
        print(info)