'''
設計1到輸入值中, 排除5之倍數的數列
'''

num = int(input("數入一個正整數:"))

for i in range( 1 , num + 1 ):
    if i % 5 == 0 :
        continue

    print(i , end = "  ")