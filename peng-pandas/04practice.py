'''
1. 資料工程實務演練
1.1 收集資料
1.2 清理資料
1.3 分析資料
1.4 基於資料的應用

2. 實務演練
2.1 取得讀取 Google Play 應用程式的 CSV 資料: https://cwpeng.github.io/live-records...
2.2 觀察資料的基本特性
2.3 應用程式評分的資料清理和分析
2.4 應用程式安裝數量的資料清理和分析
2.5 提供關鍵字搜尋的基本應用服務
'''

import pandas as pd
#讀取資料
data=pd.read_csv("googleplaystore.csv") # 把 csv格式的檔案讀取成一個DataFrame

#觀察資料
print("觀察資料:")
print("資料數量 data.shape:", data.shape)
print("資料欄位 data.columns \n:" , data.columns)
print("=====================")

# #分析資料: 項目 Rating 的各種統計數據
# print("平均數", data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("取得前100個'nlargest(100)'應用程式的平均:", data["Rating"].nlargest(100).mean())
# '''
# 此時發現前百平均大於5(最多就是5顆星), 懷疑資料來源有問題
# 因此檢查條件 condition > 5 的資料
# '''
# print("====================")
# condition=data["Rating"]>5
# data1=data[condition]
# print(data1) 
# #發現確實有一個資料異常

# #取<=5的資料
# print("====================")
# condition=data["Rating"]<=5
# data=data[condition]
# print("取得前100個'nlargest(100)'應用程式的平均:", data["Rating"].nlargest(1000).mean()) # 4.823--合理
# print("=========================")


# #分析資料: 項目 Install 的各種統計數據
# print(["Installs"][10472]) # Free
# #將資料轉換成數字: to_numeric() , 因資料中有 , 和 + 符號無法轉換成數字, 因此先利用字串替代方法做處理: str.replace[]
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
# condition=data["Installs"]>100000
# print(data[condition].shape[0])


# 基於資料的應用: 關鍵字搜尋應用程式名稱
keyword=input("enter the keyword:")

#條件為 App 標籤中是否含有 contains() 輸入的關鍵字  
condition=data["App"].str.contains(keyword, case=False) # case = False 忽略大小寫
print(data[condition]["App"]) #印出 App 標籤中符合條件的資料

print("===========")
print("包含關鍵字的城市數量 data[condition].shape[0]:", data[condition].shape[0])
