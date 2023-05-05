'''
df=pd.DataFrame(字典)

新增欄位資料: df.insert(欄位索引值, column="欄位名稱", values=[值,值...])
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
 
df.insert(2, column="engilsh", value=[88, 72, 74, 98])
print("在第三欄的地方新增一個欄位資料")
print(df)