'''
Numpy陣列運算速度遠勝列表
Pandas, TensorFlow的基礎

安裝: pip install numpy / conda install numpy
若不行開頭可嘗試:py -3 -m pip 再接 install numpy

np.array([x,y])根據列表建立
np.empty([x,y])建立資料未指定的二維陣列
np.zero([x,y,z])建立資料都是0的三維陣列
np.ones([x,y,z])建立資料都是1的三維陣列
'''


#載入numpy 套件
import numpy as np
'''
#建立一維陣列
data=np.array([3,2,6,4])
print(data)
data=np.empty(4) #創造四個資料的一維陣列, 資料未指定
print(data)
data=np.zeros(3)
print(data)'''
#建立二維陣列: 3x3的二維陣列, 資料未指定
data=np.array([
    [2,3,2],
    [1,5,2],
    [4,2,1]
])
print(data)