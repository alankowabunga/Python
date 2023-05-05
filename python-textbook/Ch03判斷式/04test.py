"""
200以上稅率為30%
100-199稅率為21%
60-99稅率為13%
30-59稅率為6%
29以下面免稅
設計一個程式, 輸入收入後計算出應繳稅額

"""

income = int(input("請輸入收入金額:"))


if income >= 200:
    print("tax:{:5.2f}".format(income*0.3))

elif income >= 100 and income <= 199:
    print("tax:{:5.2f}".format(income*0.21))

elif income >= 60 and income <= 99:
    print("tax:{:5.2f}".format(income*0.13))

elif income >= 30 and income <= 59:
    print("tax:{:5.2f}".format(income*0.06))

else:
    print("tax:0" )

