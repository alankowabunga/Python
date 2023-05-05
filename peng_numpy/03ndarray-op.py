import numpy as np
#elementwise逐元運算
# data1=np.array([3,2,10])
# data2=np.array([1,3,6])
# result=data1+data2
# print("加法", result)

# result=data1*data2
# print("乘法",result)

# result=data1>data2
# print("大於",result)

# result=(data1==data2)
# print("是否相等",result)

#matrix矩陣運算
# data1=np.array([
#     [1,4]
# ]) # 1x2
# data2=np.array([
#     [2,-1,3],
#     [-2,5,1]
# ]) # 2X3

#內積:第一個陣列里的元素數量要等於第二個陣列的陣列數才能內積
# result=data1.dot(data2)
# print("內積",result)
# result=data1@data2
# print("內積",result)
# #外積
# result=np.outer(data1,data2)
# print("外積",result)


#statistics統計運算:針對單一陣列運算, axis=0 直行, axis=1 橫列
data=np.array([
    [2,1,7],
    [-5,3,8]
]) #2x3
result=data.sum(axis=0)
print(result)

result=data.sum(axis=1)
print(result)

result=data.max(axis=0)
print(result)

result=data.mean(axis=1)
print(result)

result=data.cumsum()
print(result)       #[ 2  3 10  5  8 16]