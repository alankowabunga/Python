'''
os module:
1. remove() 刪除指定的檔案
2. mkdir() 建立指定的目錄
3. rmdir() 刪除指定的目錄

os 模組中常與 os.path模組的 exists() 判斷檔案/資料夾是某存在的方法搭配使用
先判斷目標是否存在，接著進行操作指令
'''
import os
file="myFile.txt"                   

if os.path.exists(file):
    os.remove(file)
else:
    print(file+"    is not yet created")