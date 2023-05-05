'''
計算階乘
'''

n = int(input("請輸入正整數:"))

total = i = 1

while i <= n :
    total *= i
    i += 1

#注意輸出列印所在的程式區塊
print(" {}! = {}".format(n , total))
