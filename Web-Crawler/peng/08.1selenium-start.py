'''
selenium需要配瀏覽器的驅動程式driver
因此我們要先去下載 chrome driver & pip install selenium
driver.get(要連線的網址)
'''
#載入 Selenium 模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#設定 chrome driver 的執行路徑
options=Options() #先建立option的物件實體，在設定執行檔路徑
#已先將driver檔放在專案資料夾裡
options.chrome_executable_path="E:\PY\Python(USB)\Web-Crawler\chromedriver.exe" 

#載入 Driver 物件實體，用程式操作瀏覽器運作
driver=webdriver.Chrome(options=options) #建立 driver 的物件實體
driver.maximize_window() #視窗最大化
driver.get("https://www.google.com/") # 取得網址連線
driver.save_screenshot("screenshot-google.png") # 使用save-screenshot儲存截圖並設檔名為()內的文字
driver.get("https://www.ntu.edu.tw/")
driver.save_screenshot("screenshot-ntu.png")
driver.close #關閉瀏覽器