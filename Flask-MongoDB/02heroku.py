'''
部屬到雲端
1.建立 Flask 專案描述檔案
2.安裝 Git 工具
3.到 Heroku 註冊帳號，建立應用
4.安裝 Heroku CLI 命令列工具
5.將程式部屬到 Heroku App ， 並測試

首先建立描述檔:
runtime.txt (描述使育的python環境): python_3.6.4
requirements.txt (所需要的套件): Flask，gunicorn #為了在heroku上啟動專案
Procfile (如何執行程式): web gunicorn 檔案名稱:設定的變數名稱

初始化專案:
git init
heroku git:remote _a 專案名稱

更新專案:
git add .
git commit _m "更新的訊息"
git push heroku master
'''
