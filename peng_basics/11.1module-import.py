'''
module: 將程式寫在檔案(模組)中 , 
可重複載入, 使用模組中的函式&變數
#模組有自定和內建兩種

import載入語法:
import 模組名稱 (as 別名)

使用模組語法:
1. 模組名稱/別名.函式名稱(參數資料)
2. 模組名稱/別名.變數名稱

'''

#載入sys內建模組
import sys  # import sys as s 下面就用 s 代替 sys即可
#使用sys模組
print(sys.platform) #作業系統
print(sys.maxsize)  #整數之最大值
print(sys.path)     #搜尋模組的路徑
#sys.path.append("newPath") #在路徑最後新增一個位置newPath