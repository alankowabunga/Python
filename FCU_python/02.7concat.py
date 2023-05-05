'''
concat(資料一,資料二):
合併2+個 dataframe字典資料
'''
import pandas as pd
 
 
grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}
 
df1 = pd.DataFrame(grades)
print("原來的df")
print(df1)
 
print("=================================")
 
df2 = pd.DataFrame({
    "name": ["Henry"],
    "math": [60],
    "chinese": [62]
})
 
print("pd.concat()合併後的新資料, 新增資料的索引值維持原狀")
new_df = pd.concat([df1, df2])
print(new_df)
print("=================================")
new_df = pd.concat([df1, df2], ignore_index=True)
print("pd.concat( , ignore_index=True), 索引值順序重新整理")
print(new_df)
