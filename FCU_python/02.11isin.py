'''
#其欄位中包含xxx的資料集
df[df[欄位名稱].isin["xxx"]] 

'''
import pandas as pd
 
 
grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}
#建立dataframe物件: pd.DataFrame(資料名稱)
df = pd.DataFrame(grades)
 
print("原來的df")
print(df)
 
print("=================================")
 
print("篩選name欄位包含John的資料集")
print(df[df["name"].isin(["John"])])