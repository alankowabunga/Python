'''設計程式, 假設只知道金銀牌和其數量, 銅牌要自己輸入, 並且顯示獎牌名稱和數量'''

medal = {"gold":20,"silver":10}
m = input("Please enter the ranking(gold,silver):")
if m in medal:
    print( m," 的數量為 ",medal[m])

else:
    num = input("Please enter the quantity:")
    medal[m]=num
    print("{}的數量為{}".format(m,num))

print(medal)