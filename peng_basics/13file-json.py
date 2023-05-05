'''
檔案操作流程
step1: 開啟
step2: 讀取or寫入
step3: 關閉檔案
'''


#開啟檔案基本語法: open
'''檔案物件 = open(檔案路徑, mode=開啟模式)
mode...r , w , r+
'''



#讀取 : read()
'''
No1. 讀取全部文字
檔案物件.read()

No2. 一次讀一行 #使用迴圈
for 變數 in 檔案物件:

No3. 讀取json格式:
import json
讀取到的資料=json.load(檔案物件)
'''



#寫入文字
'''
No.1: 檔案物件.write(字串\n)

No.2:寫入json格式
import json
json.dump(要寫入的資料, 檔案物件)
'''



#關閉檔案: 檔案物件.close()
'''

最佳關閉的實務語法: 會自動且安全的關閉檔案
with open(檔案路徑, mode="?") as 檔案物件:
    讀取or寫入檔案的程式
'''



#使用json格式讀取,複寫檔案
'''
step1: 建立一個新檔config.json, 寫入程式碼
step2: import jason 

'''
import json
#從檔案中讀取json資料, 放入變數data裡面
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) #data是一個字典資料
print("名子:", data["name"])
print("版本:", data["version"])

data["name"]="New name" #修改變數中的資料
print(data) #my name 變成 new name
#把最新的資料複寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data,file) #json.dump(資料,檔案物件)