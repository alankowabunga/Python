import pandas as pd

#建立 Series:pd.Series(列表)
data=pd.Series([20,10,15])
#基本 Series操作
#print(data)
'''
0    20
1    10
2    15
'''
# print("Max",data.max()) #20
# print("Meidan", data.median()) #15
# data=data*2
# print(data)

data=data==20 #拿data裡的資料跟20做比較, 得出True or False
print(data)
'''
0     True
1    False
2    False
'''




#建立 DataFrame
data=pd.DataFrame({
    "name":["alan","leo","anna"],
    "salary":[111,222,333]
})
#基本 DataFrame 操作
#print(data)
'''
   name  salary
0  alan     111
1   leo     222
2  anna     333
'''

#取得特定欄位
print(data["name"])
print(data["salary"])
print("===================")
#取得特定列:iloc[]
print(data.iloc[0]) #印出第一列
print("===============")
print(data.iloc[1])