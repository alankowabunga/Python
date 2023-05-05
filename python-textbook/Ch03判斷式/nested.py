'''
a , b, c 為正整數, 輸入值後用巢狀判斷式, 找出數字中最大的數

'''

a = int(input("請輸入正整數:"))
b = int(input("請輸入正整數:"))
c = int(input("請輸入正整數:"))

if a > b and a > c: 
    if a > b and a > c:
        print("最大的數是:" + str( a ))

    elif b > a and b > c:
        print("最大的數為:" + str(b))

else:
    print("最大的數為:" + str(c))