
num = int(input("請輸入一個正整數:"))

#設計累加for迴圈

sum = 0
for i in range( 1 , num + 1 ):
    sum += i

print(" 1 到{}的整數總和為:{}".format( num , sum ))
