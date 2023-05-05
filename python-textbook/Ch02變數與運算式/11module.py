
#實作自訂模組

'''
1. 載入內建的 sys模組並取得資訊

2. 建立檔案 geometry.py
並且定義平面幾何運算用的函式

3. 載入並使用
使用模組語法:
模組名稱/別名.函式名稱(參數資料)
模組名稱/別名.變數名稱

#最後創建一個資料夾"modules", 來儲存各項模組
#也因為這個新的資料夾會讓路徑增加而改變, 因此進入第4步

4. 調整搜尋模組的路徑:
先載入sys模組, 使用sys.path.append()語法
來操作增加路徑中的位置(modules)

'''
#  1. 載入內建的 sys模組並取得資訊
# import sys as s
# print(s.platform)
# print(s.maxsize)

#  2. 建立檔案 geometry.py並且定義平面幾何運算用的函式

#  3. 載入並使用(呼叫函式)
'''
import geometry

result = geometry.distance(2,4,5,6) #呼叫函式
print(result)  
# print(geometry.distance(2,4,5,6))

result = geometry.slope(3,5,6,7) #呼叫函式
print(result)  
# print(geometry.slope(3,5,6,7))
'''
#  4. 調整搜尋模組的路徑
import sys
sys.path.append("modules")
print(sys.path)

import geometry
print(geometry.distance(2,4,5,6))