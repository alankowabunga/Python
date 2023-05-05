'''

list串列: 元數值和數量可變
n = list1[]

tuple元組: 元數值和數量不可變
n = tuple()

'''

# tuple 與 list 使用上基本相同 , 其優點為速度快且儲存的資料較安全
# 可利用 list() or tuple() 做字串和元組的轉換

# 將元組轉換成串列
tuple1 = ( 1 , 2 , 3 , 4 )
list1 = list(tuple1) 
list1.append(5)      # 可變

# 將串列轉換成元組
list2 = [ 1 , 2 , 3 , 4 ]
tuple2 = tuple(list2)
tuple2.append(5)   # 錯誤 : 不可變