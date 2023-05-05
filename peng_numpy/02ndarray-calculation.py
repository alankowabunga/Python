'''
逐元運算 elementwise :+-x/,>,==,<=
矩陣運算 matrix: data1.dot(data2) = data1@data2 內積 , np.outer(data1,data2) 外積
統計運算 statistics: 針對單一陣列進行統計運算
'''
#逐元運算
import numpy as np
#建立兩個多維陣列
# data1=np.array([3,4,1])
# data2=np.array([-2,5,8])
# #逐一元素運算
# print(data1+data2)


#矩陣運算
data1=np.array([
    [2,1]
]) # 1x2

data2=np.array([
    [3,2,0],[3,1,-1]
]) # 2x3

print(data1.dot(data2)) # 內積 1x3
print(data1@data2) # 內積 1x3
print(np.outer(data1,data2)) # 外積 2x6



#統計運算
data=np.array([
    [2,1,7],
    [3,-5,8]
])
data.sum() #16
data.sum(axis=0) #加總 column [ 5 -4 15]
data.sum(axis=1) # 加總 row [10  6]
data.min()
data.cumsum() # 逐值壘加 [ 2  3 10 13  8 16]
data.mean() #平均數
data.std() #標準差