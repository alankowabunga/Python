'''
-在瀏覽器中執行 javascript 程式
driver.execute_script("JavaScript 程式碼")

-捲動視窗到底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#實體物件.execute_script("將window捲動到(高度:0, 文件.本體.捲動的高度);")


無限捲動: 需搭配 time 模組使用。為讀取更多資料，在捲到底部時須等待讀取時間
import time
time.sleep(等待秒數)

實際演練: 爬取 Linkedin 工作搜尋的網頁資料
'''
#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#設定 Chrome Driver 的執行檔路徑
options=Options()
options.chrome_executable_path="E:\PY\Python(USB)\Web-Crawler\chromedriver.exe"
#建立 Driver 實體物件，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options)
#連線到 LinkedIn 工作搜尋網頁
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")

#捲動視窗並等待瀏覽器載入更多內容
#   driver實體物件.execute_script("將window捲動到(高度:0, 文件.本體.捲動的高度);")
n=0
while n<3: # 利用迴圈使其自動往下捲動 3 次(n=0.1.2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3) # 等待 3 秒
    n+=1

# 取得網頁中的標題
titletags=driver.find_elements(By.CLASS_NAME,"base-search-card__title") # 標題的 class 屬性如何找到詳見圖檔 class_finding
for titletag in titletags:
    print(titletag.text)

driver.close()