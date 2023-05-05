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
# 輸入兩個正數並求和，若輸入的非數值資料，用 try...except捕捉錯誤
try:
    a=int(input("Enter a intager:"))
    b=int(input("Enter a intager:"))
    sum=a+b
    print("a+b= ", sum)
except:
    print("The input content isn't integer number!")