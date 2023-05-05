'''
1. 指示 Selenium 連線到特定網址
2. 解析網頁 HTML 結構，取得實際想要的標籤
3. 針對取得的標籤進行操作

Driver的搜尋方法:
取得滿足條件的一個標籤WebElement/或所有標籤 WebElement List
一個:driver.find_element(搜尋欄位,"搜尋條件")
所有:driver.find_element(搜尋欄位,"搜尋條件")

-根據標籤的 class 屬性搜尋(By.屬性名稱)
driver.find_element(By.CLASS_NAME,"搜尋條件")
driver.find_elements(By.CLASS_NAME,"搜尋條件")

-根據連結標籤的文字搜尋(By.LINK-TEXT)
driver.find_element(By.LINK-TEXT,"搜尋條件")
driver.find_elements(By.LINK-TEXT,"搜尋條件")

-取得標籤的內部文字:.text
element.text

-取得標籤的某個屬性:get_attribute()
element.get_attribute("屬性名稱")

-模擬使用者點擊標籤:click()
element=driver.find-element(搜尋欄位,"搜尋條件")
element.click()
'''
#載入 Selenium 模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#設定 chrome driver 的執行路徑
options=Options() #先建立option的物件實體，在設定執行檔路徑
#已先將driver檔放在專案資料夾裡
options.chrome_executable_path="E:\PY\Python(USB)\Web-Crawler\chromedriver.exe" 

#載入 Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options) #建立 driver 的物件實體
#連線到 ptt 股票版
driver.get("https://www.cc/bbs/Stock/index.html")
# print(driver.page_source) 取得網頁原始碼
tags=driver.find_elements(By.CLASS_NAME,"title") #記得先載入 By 模組
for tag in tags:
    print(tag.text)

#取得上一頁的文章標題
link=driver.find_element(By.LINK_TEXT,"&lsaquo; 上頁")
link.click() # 點擊連結標籤
tags=driver.find_elements(By.CLASS_NAME,"title") #記得先載入 By 模組
for tag in tags:
    print(tag.text)
    
driver.close()