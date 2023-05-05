import pandas as pd
#以字典資料為底, 建立DataFrame
#pd.DataFrame(字典)

#自行設定索引
#pd.DataFrame(字典, index=索引)

'''
data.size
data.shape
data.index

取得橫列row的資料: data.iloc[順序]
print(data.iloc[1]) # 0為第一列,1為第二列
df.iloc['viper'] 取得索引值viper的橫列資料
df.iloc['cobra', 'shield'] 取得索引值cobra中的shield欄位的值


取得一整欄 data[欄位名稱]
print(data[欄位名稱]) #Series型態

建立新的欄位
data["新欄位名稱"]=列表資料/Series資料型態
'''

