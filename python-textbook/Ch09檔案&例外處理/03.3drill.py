'''
例外處理:
可參考以下連結
https://blog.gtwang.org/programming/python-howto-check-whether-file-folder-exists/

寫例外程式碼必須由小範圍到大範圍~~
語法(try...except...else...finally)
try:
    測試的程式碼
except:
    若有錯誤發生，會執行此區程式碼
else:
    沒有錯誤時，執行此區程式碼
finally:
    最後必執行的程式碼(通常用來關閉或刪除檔案)
'''
# 開啟指定檔案並顯示內容，若檔案不存在等錯誤時用 try...except 捕捉錯誤
try:
    with open("data.txt",mode="r",encoding="utf-8") as file:
        content=file.read()
        print(content)
except:
    print("No such file !!")