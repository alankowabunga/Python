import numpy as np

data=np.array([
    [2,1,7],
    [3,-5,8]
])
print(data.sum()) # 16
print(data.sum(axis=0)) #加總 column [ 5 -4 15]
print(data.sum(axis=1)) # 加總 row [10  6]
data.min()
print(data.cumsum()) # 逐值壘加 [ 2  3 10 13  8 16]
print(data.mean()) #平均數
print(data.std()) #標準差