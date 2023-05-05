'''
倒印顯示串列

'''

name = ["alan" , "leo" , "anna"]

#先利用len()找出串列長度 , 再用for...range迴圈讀取串列元素
#range(3) 相當於 list[ 0 , 1 , 2 ]
#串列要從最後一個倒數回來的話可用負數 , list[-1] 即為最後一個數
for i in range(len(name)):
    print("{}".format(name[-i-1] , end = ","))  # -(i) 為 -(0 , 1 , 2) , 但從最但從最後一個開始要為-(1 , 2 , 3)所以要多"-1"  