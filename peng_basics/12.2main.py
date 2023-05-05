#實作
#此為主程式
'''
step1: 建立一個資料夾為geometry
step2: 放入一個檔案為__init__.py, 使geometry成為封包
step3: 在封包裝建立模組point.py & line.py , 並寫分別的程式碼
step4: 回到主程式 import package_name.module_name
'''

import geometry.point #模組的完整名稱包含所屬的封包 
result=geometry.point.distance(3,4)
print("distance:", result)

import geometry.line as line
result=line.slope(1,1,3,3)
print("斜率:", result)