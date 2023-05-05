'''

設計輸入該周每天的存款 , 顯示每天對應的存款金額, 和該週存款總合: 

1. 此情況有固定次數(7天) , 比較適合 for loop
2. 第幾天用迴圈去由1-7遞增
3. 建立字串
4. 建立迴圈, 相加所有的元素()

'''

deposit = []
inMoney = total = 0  # 將串列 deposit 的元素取名為 inMoney , 並且宣告變數 total來做相加總合 ,並都將初值設為0

for i in range(1 , 8):  # 設計迴圈來顯示輸入指令
    inMoney = int(input("請輸入第{}天的存款:".format(i)))  
    deposit.append(inMoney)

for money in deposit:  #在設計一個迴圈來累計總合 , 另外宣告一個變數 money
    total += money

print(" 總額為:{}".format(total))





'''
for i in range(1 , 8):
    money = int(input("請輸入第{}天的存款:".format(i)))  #顯示輸入指令
    for j in range( 1 , i + 1 ):  #使用巢狀迴圈 
        deposit.append(money)
        total += money
print("第{}天的存款金額為{} , 總存款額為{}".format(j , i , total) , end = "")

'''