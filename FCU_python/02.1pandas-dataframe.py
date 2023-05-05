'''
DataFrame 物件: 二維度以上，類似試算表和關聯式資料庫資料表（table）欄列結構，
每一欄是固定資料型別但不同欄可以儲存不同的資料型別
'''

import pandas as pd

#傳入
data={
    "name":["Alan","Wen","backup","angela"],
    "email":["chenyujen@gmail.com","happy@gmail.com","babyalan0857@gmail.com","angla55ray@gmail.com"],
    "grades":[60,77,82,22]
}
#建立dataframe物件: pd.DataFrame(資料名稱)
student_df=pd.DataFrame(data)
student_df=pd.DataFrame(data,index=["initial","second","third","fourth"]) #自定義 index

#欄位資料型別等資訊: 變數名稱.info()
print(student_df.info())

#列出統計資料: 變數名稱.describe()
print(student_df.describe())

#列出dataframe的 index/columns
print(student_df.index)
print(student_df.columns)

# 印出頭尾指定數量之資料: 變數名稱.head/tail(指定資料數量)
print(student_df.head(2))
print(student_df.tail(2))