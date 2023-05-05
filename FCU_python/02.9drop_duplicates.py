'''pd.drop_duplicates() 刪除重複資料'''

import pandas as pd
 
 
grades = {
    "name": ["Mike", "Mike", "Cindy", "John"],
    "city": ["Taipei", "Taipei", "Kaohsiung", "Taichung"],
    "math": [80, 80, 93, 86],
    "chinese": [80, 80, 93, 86]
}
 
df = pd.DataFrame(grades)
print("原來的df")
print(df)
 
print("======================================")
 
new_df = df.drop_duplicates()
print("刪除重複值後的df")
print(new_df)