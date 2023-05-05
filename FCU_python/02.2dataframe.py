import pandas as pd 
 
 #建立字典
grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}


print("使用字典來建立df：")
df = pd.DataFrame(grades)
 
 
print("取得單一欄位資料(型別為Series)")
print(df["name"])
 
print("=================================")
 
print("取得單一欄位資料(型別為DataFrame)")
print(df[["name"]])
 
print("=================================")
 
print("取得多欄位資料(型別為DataFrame)")
print(df[["name", "chinese"]])
 
print("=================================")
 
print("取得索引值0~2的資料")
print(df[0:3])