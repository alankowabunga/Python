import pandas as pd 
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
print(df)
print("==================================")
print("使用df.iloc['viper'] 取得 索引值viper的橫列資料, 也就是max_speed,shield和其值")
data=df.loc['viper']
data1=df.loc['cobra', 'shield']
print(data)
print("==================================")
print("使用df.iloc['cobra', 'shield'] 取得索引值cobra中的shield欄位的值")
print(data1)