import pandas as pd
 

grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}
 
df = pd.DataFrame(grades)
df.index = ["s3", "s1", "s4", "s2"]  # 自訂資料索引值
 
print("原來的df")
print(df)
 
print("============================")
 
new_df = df.sort_index(ascending=True)
print("遞增排序")
print(new_df)
 
print("============================")
 
new_df = df.sort_index(ascending=False)
print("遞減排序")
print(new_df)
