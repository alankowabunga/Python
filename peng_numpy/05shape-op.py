import numpy as np
#多維陣列維度/形狀操作

#觀察資料形狀
data=np.ones(10)
print(data)
print(data.shape)

data1=np.array([
    [3,5,1],
    [1,2,3]
])  # 2x3
print(data1.shape) # (2, 3)
#資料轉置(然後看形狀):資料名稱.T.shape
print(data1.T.shape) # (3, 2)

#扁平化資料: 資料名稱.ravel()
data2=np.array([
    [
        [2,1,4],[2,3,6]
    ],
    [
        [0,2,1],[4,1,6]    ]
])
print(data2.shape) #(2, 2, 3)
newData=data2.ravel() #[2 1 4 2 3 6 0 2 1 4 1 6]
print(newData)
print(newData.shape) #(12,)

#reshape() : 重塑資料
reshapeData=data2.reshape(3,4) # 3x4=12資料數量要相同
print(reshapeData)

data3=np.zeros(18).reshape(3,2,3)
print(data3)

data4=np.arange(9).reshape(3,3)
print(data4)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]'''
print(data4.T) # T 轉置矩陣
'''
[[0 3 6]
 [1 4 7]
 [2 5 8]]'''