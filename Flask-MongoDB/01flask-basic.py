'''
先在D槽開起一個資料夾: Flask heroku
'''
#以下為網站的司服器，以下程式若終止則網站無法連線

from flask import Flask
#建立應用程式的物件
app=Flask(__name__) # __name__ 為python內建的變數，代表目前執行的模組

@app.route("/") #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def home():
    return "Hello Flsk 2"

@app.route("/test") # 根目錄: 代表要處理的網站路徑
def test():
    return "This is Test"

if __name__=="__main__": #如果主程式執行
    app.run() #立即啟動司服器