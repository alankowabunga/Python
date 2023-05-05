'''
單維度資料 Series

Series 基本邏輯:

#建立Series資料
import pandas as pd
data=pd.Series(列表)

#建立篩選條件(與資料數量對應的布林值)
condition=[True, False, True] # 要的資料: True, 不要的資料: False
condition=data>5 #產生布林值的列表

#根據條件完成篩選
filteredData=data[condition]
'''

import pandas as pd

data=pd.Series([30,15,20])

print("condition=data>18 , 條件為數值 ~~ 結果為布林值")
condition=data>18
print(condition)

print("==============")
print("condition=[布林值], 條件為布林值 ~~ 結果為取值與否")
condition=[True,False,True] # True:要此資料, False:不用此資料
filteredData=data[condition]
print(filteredData)
'''
condition=data>18 , 條件為數值 ~~ 結果為布林值
0     True
1    False
2     True
==============
condition=[布林值], 條件為布林值 ~~ 結果為取值與否
0    30
2    20
'''
print("===============")
#列表資料為字串, data.str 要加字串的str
data=pd.Series(["您好","python","pandas"])
condition=data.str.contains("p")
print("條件為是資料是否含有p, condition=data.str.contains('p')")
print(condition)
