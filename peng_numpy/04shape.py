'''
Shape 多維陣列的形狀

維度:資料的層次
形狀: 同時表達資料的層次和梅層次的資料數量

shape: 觀察資料形狀
T :利用 T 屬性取得多維陣列的轉置
ravel(): 扁平化資料，將多維度的資料打平成一維陣列
reshape(x,y): 重塑資料形狀，資料數量必須一樣
zeros()/ones(): 資料初始化，通常會使用0或1
'''
import numpy as np
data=np.array([
    [2,4,1],
    [1,5,0]
])
#shape: 觀察資料形狀
print(data.shape) #(2,3)

# T :利用 T 屬性取得多維陣列的轉置
print(data.T.shape) #(3,2)

# ravel(): 扁平化資料，將多維度的資料打平成一維陣列
data2=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
]) # 2x2x2=8
print(data2.ravel()) #[1 2 3 4 5 6 7 8]

#reshape(x,y): 重塑資料形狀，資料數量必須一樣
print(data2.reshape(4,2)) # 4x2=8
# data2.reshape(3,3) # 3x3=9 錯誤

#zeros()/ones(): 資料初始化，通常會使用0或1
data3=np.zeros(18).reshape(3,3,2)
print(data3)