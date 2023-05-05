'''
np.vstack  - vertical
np.hstack    horizontal
Concatenate 串聯: np.concatenate([x, y])
'''
import numpy as np

result=np.vstack((np.zeros(3),np.ones(3)))
print(result)   #[[0. 0. 0.],[1. 1. 1.]]  2x3

result=np.hstack((np.zeros(3),np.ones(3)))
print(result)   #[0. 0. 0. 1. 1. 1.]  1x6

#準備測試資料
arr1=np.array([
    [1,2,3],
    [4,5,6]
]) # 2x3

arr2=np.array([
    [7,8,9],
    [14,25,34]
]) # 2x3
#合併vertically: vstack 
result1=np.vstack((arr1,arr2))
print(result1)
'''
    4x3
    [[ 1  2  3]
    [ 4  5  6]
    [ 7  8  9]
    [14 25 34]]
'''
#合併horizontally: hstack
result2=np.hstack((arr1,arr2))
print(result2)
'''
2x6
[[ 1  2  3  7  8  9]
 [ 4  5  6 14 25 34]]
'''