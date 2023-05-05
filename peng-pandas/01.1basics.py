'''
Pandas:類似試算表的資料分析套件
單維度資料-Series: 像是一個列表，或是試算表中直向的欄位
雙維度資料-DataFrame:秀完整的試算表，有欄和列的表格
'''
import pandas as pd
#以列表資料為底，建立　Series
#pd.Series(列表)
#data.max() 
#data.median()
#data=data*2

#以字典資料為底, 建立DataFrame
#pd.DataFrame(字典)
#data=pd.DataFrame(字典)
#data["特定欄位"]

#取得特定列(橫向)
#data.iloc[列編號]  #列編號按順序由0開始累加