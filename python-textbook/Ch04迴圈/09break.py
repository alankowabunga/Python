'''
找輸入兩的值的最小公倍數

'''

num1 = int(input("請輸入第一個正整數:"))
num2 = int(input("請輸入第二個正整數:"))


#最小公倍數不會大於兩數相乘( maxno <= num1 * num2)
#公倍數可被兩個值整除(i % num1 == 0 and i % num2 == 0)

maxno = num1 * num2
for i in range( 1 , maxno + 1 ):
    if(i % num1 == 0 and i % num2 == 0):
        break

#[!!!極重要!!!] 若把輸出print放在跟if判斷視同一個程式區塊, 則會在迴圈裡重複輸出結果
print("{}和{}的最小公倍數為:{}".format(num1 , num2 , i))
