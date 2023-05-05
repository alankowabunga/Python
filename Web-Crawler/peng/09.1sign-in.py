'''
取得標籤的方法
1.根據標籤的 ID 搜尋: 
driver.find_element(By.ID,"搜尋條件")

2.標籤的任意屬性-透過 CSS 選擇器: 
driver.find_element(By.CSS_SELECTOR,"[屬性名稱=屬性的值]")

鍵盤操作
1.模擬使用者輸入文字: 
element.send_keys("輸入的文字)

2.模擬使用者按下特定功能按鈕:
element.send_keys(Keys.ENTER)
'''
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#設定 Chrome 的執行檔路徑
options=Options()
options.chrome_executable_path="E:\Python\Web-Crawler\peng\chromedriver.exe"
#建立 Driver 物件實體，用程式操作瀏覽器
driver=webdriver.Chrome(options=options)

#連線到 Leetcode 登入介面
driver.get("https://leetcode.com/accounts/login/")
#輸入帳密並按下登入按鈕
username=driver.find_element(By.ID,"id_login")
password=driver.find_element(By.ID,"id_password")
btn=driver.find_element(By.ID,"signin_btn")

username.send_keys("chenyujen0218@gmail.com")
password.send_keys("alan4645")
btn.send_keys(Keys.ENTER)
#等待登入完成
#連線到登入後才能取得的頁面