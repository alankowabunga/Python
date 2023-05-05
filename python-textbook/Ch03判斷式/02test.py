'''
設計輸入整數後,能判斷奇偶數的程式

'''

#偶數除2...餘0, ( %2 = 0 )
num = int(input("輸入一個整數:"))
if num % 2 == 0:
    print("{}為偶數".format(num))

else:
    print("{}為奇數".format(num))