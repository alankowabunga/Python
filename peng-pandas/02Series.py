#pd.Series(資料列表,index=索引列表)
#data=pd.Series(資料列表)
#data.dtype
#data.size
#data.index
#取值(由0開始): data[索引/順序] 

import pandas as pd
data=pd.Series([3,10,5,-12])

#數學/統計
print(data.sum(),data.max(),data.prod()) #prod()乘法總和
print(data.mean(),data.median(),data.std)
print(data.nlargest(3),data.nsmallest(2))

#字串操作
data=pd.Series(["Hello","pandas","python"])

#各種字串操作都定義在str底下, 記得在data後加str: data.str.xxx
print(data.str.lower(),data.str.upper(),data.str.len())

#用逗號將字串連起來 
print(data.str.cat(sep=",")) #DataFrame 用 concat([資料一,資料二] , ignore_index=True/False)

data.str.contains("P")  # DataFrame用isin尋找欄位中包含xxx的資料集: df[df[欄位名稱].isin["xxx"]]
print(data.str.replace("Hello","hey")) #用hey取代Hello