#網路連線
# import urllib.request as req
# src="http://ww.ntu.edu.tw/"
# with req.urlopen(src) as response:
#     data=response.read().decode("utf-8") #取得台灣大學網站的原始碼(HTML, CSS)
# print(data)



'''串接, 擷取公開資料'''
import urllib.request as req
import json
src="	https://data.taipei/api/v1/dataset/76398c88-b9e5-4144-ab0f-736e0bc58e0d?scope=resourceAquire"
with req.urlopen(src) as response:
    data=json.load(response) #利用 json 模組處理 json 資料格式
#取得醫院名稱, 整理簡潔資料
hList=data["result"]["results"] #取於 json 格式的層次列表result中的results, 資料會變乾淨

#利用for迴圈，字典取value方式: dic["key-name"]
for hospital in hList:
    print(hospital["動物醫院名稱"]) # 使用取出字典中value的方法: 字典名稱["key"]

#將取出的醫院名稱資料, 放入新檔案中
with open("hospital.txt", "w", encoding="utf-8") as file:
    for hospital in hList:
        file.write(hospital["動物醫院名稱"]+"\n") 