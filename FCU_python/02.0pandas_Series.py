'''
Pandas 是 Python 進行資料處理和資料分析一個好用的工具，
其主要資料結構有包含：Series 物件和 DataFrame 物件。其中 DataFrame 就類似我們在使用的 Excel 試算表一樣，由欄列所組成的表格結構。由於 Pandas 本身基於 Numpy 所以在使用大量資料運算時效能表現也優於原生的 Python 資料結構，所以是常用將資料載入進行資料分析的好用工具。

Series 物件: Series 為索引標籤和實際值的陣列組合
'''
import pandas as pd

#建立Series物件並設定index索引
phone = pd.Series(["Apple", "Samsung", "Mi", "Sony"] ,index=["p1","p2","p3","p4"])

print(phone["p3"]) #利用新設定的索引取值
print("==================================")
# data=pd.Series(["alan","Wen"])
# combine=phone.append(data)
# print(combine)

#搜尋特定字串: 布林直
print(phone.str.contains("n"))
