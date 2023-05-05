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
#eg. 不存在的 n 變數
try:
    print(n)
except:
    print("若錯誤出現則執行 except 程式碼:變數 n 不存在")
else:
    print("若無錯誤執行else")
finally:
    print("finally是最後必執行的程式碼")