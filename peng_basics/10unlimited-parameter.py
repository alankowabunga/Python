'''

函式之 *無限參數

語法為:
def 函式名稱(*無限參數):
    無限參數以Tuple資料形態處理
    函式內部的程式碼

#呼叫函式, 可傳入無限數量的參數
函式名稱(資料1, 資料2, 資料3...)

'''


'''
#函式接受無限參數 *msgs
def say(*msgs):
    #以Tuple的方式處理
    for msg in msgs:
        print(msg)  #用迴圈將Tuple的資料一一拿出並print
    
#呼叫函式, 傳入3個參數資料
say("hello","arbitrary","arguments")

'''


#平均數-*無限參數
def avg(*num):
    #用迴圈來使用Tuple
    sum=0
    for n in num:
        sum+=n
    print(sum/len(num))

avg(2,5)
avg(3,5,7)
avg(3,-5,2)
