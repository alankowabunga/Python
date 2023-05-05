#splitting切割: 將多維陣列切隔成多個
'''
np.vsplit(陣列,切割數量) - split vertically
np.hsplit(陣列,切割數量) - split horizontally
'''
import numpy as np

arr=np.array([
    [1,2,3,4],
    [5,6,7,8]
]) # 2x4

result1=np.vsplit(arr,2)
'''
[[1, 2, 3, 4]] #1x4
[[5, 6, 7, 8]] #1x4
'''
result2=np.hsplit(arr,2)
'''
[[1, 2],[5, 6]] #2x2
[[3, 4],[7, 8]] #2x2
'''

arr=np.arange(16).reshape([4,4])
print("原arr", arr)
print("after splitting:", np.vsplit(arr,2))
'''
原arr 
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]

after splitting: 
[array([[0, 1, 2, 3],[4, 5, 6, 7]]), 
array([[ 8,  9, 10, 11],[12, 13, 14, 15]])]
'''