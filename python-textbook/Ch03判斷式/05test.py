'''
設計一個程式判斷所輸入之年分, 是否為平年
平年條件:
1. 可以被100和400同時整除
2. 不能被100整除, 但能被4整除

'''

year = int(input("請輸入年分:"))

if year % 100 == 0 and year % 400 == 0:
    print("yes , it's 平年")

elif year % 100 != 0 and year % 4 == 0:
    print("yes , it's 平年")

else:
    print("no , it's not 平年")