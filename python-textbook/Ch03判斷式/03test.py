'''
設計一款輸入月份, 可判斷季節的程式
1-3: spring
4-6: summer
7-9: autumn
10-12:winter

'''
month = int(input("請輸入月份:"))


if month >= 1 and month <= 3:
    print("現在是春天")

elif month >= 4 and month <= 6:
    print("現在是夏天")

elif month >=7 and month <= 9:
    print("現在是秋天")

elif month >= 10 and month <= 12:
    print("now is winter")

else:
    print("沒有此月份")

