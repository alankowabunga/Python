'''
所有奇數之加總

'''

num = int(input("請輸入一個正整數:"))

sum = 0
for i in range( 1 , num + 1):
    if i % 2 != 0:
        sum += i
print(" 1 到{}的奇數和為{}:".format( num , sum ))