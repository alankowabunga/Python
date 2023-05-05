# 程式的包裝: 同樣的邏輯可重複利用
#定義函式名稱為calculate, 參數名稱為max
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum+=n
    print(sum)

#呼叫
calculate(10)
calculate(20)