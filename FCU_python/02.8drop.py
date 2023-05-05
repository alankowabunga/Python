'''
刪除資料 pd.drop([索引值,索引值..] , axis=0/1)
'''

import pandas as pd
 

grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}
 
df = pd.DataFrame(grades)
print("原來的df")
print(df)
 
print("=================================")
 
new_df = df.drop([0, 2], axis=0)  # 刪除第一筆及第三筆資料
print("刪除第一筆及第三筆資料, 索引值維持原狀")
print(new_df)
print("=================================")

#使用 df.sort_index(ascending=True/False)重新整理索引值
print("使用df.index=[索引值,索引值...]重新整理索引值")
new_df.index=["1","2"]
print(new_df)