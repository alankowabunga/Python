#建立一維隨機數組
d1=np.random.randint(10,size=10)
#建立二維隨機數組
d2=np.random.randint(10,size=(5,5))
#建立三維隨機數組
d3=np.random.randint(10,size=(2,4,6))
print(d1)
print(d2)
print(d3)
'''
[0 7 0 1 2 6 7 3 1 6]

[[5 6 5 3 7]
 [2 4 9 3 7]
 [2 1 5 0 9]
 [1 5 5 5 7]
 [5 6 2 0 3]]
[[[3 9 5 1 8 1]
  [2 6 1 0 0 1]
  [0 5 7 9 5 4]
  [3 5 6 5 6 9]]

 [[3 6 2 1 3 9]
  [9 6 2 3 8 2]
  [0 7 0 1 8 9]
  [8 6 5 3 6 2]]]
'''

# ndim、shape、size、dtype用法
# dim: 數組的維度
# shape: 每個維度的大小
# size: 數組的大小(長度)
# dtype:數據類型
# itemsize:每個數組元素的大小/長度(單位:bytes)
# nbytes: 數組的總大小(單位 bytes)

#印出三維數組的各種屬性:
print ("d3 維度(ndim): ", d3.ndim) 
print ("d3 每個維度的長度/大小(shape): ", d3.shape)
print ("d3 數組的大小長度(size): ", d3.size)
print ("d3 數組類型(dtype): ", d3.dtype)
print ("d3 每個數組元素的大小/長度(bytes): ", d3. itemsize, "bytes")
print ("d3 數組的總大小/長度(bytes): ", d3.nbytes, "bytes")
'''
執行結果:
d3 維度(ndim): 3
d3 每個維度的長度/大小(shape): (2, 4, 6)
d3 數組的大小長度(size): 48
d3 數組類型(dtype): int32
d3 每個數組元素的大小/長度(bytes): 4 bytes
d3 數組的總大小/長度(bytes): 192 bytes'''