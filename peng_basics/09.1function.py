'''

Function 函式 = 程式區塊 , 包裝一段程式碼
函數參數的設計可讓呼叫有彈性

1. 定義函式: def 函式名稱(參數名稱) #參數名稱
2. 呼叫函式: 函式名稱(參數資料) #參數資料

回傳值 return: 函式的運作結果就是回傳值, 並把函式內的結果帶出來
return #未寫出來的預設 , 結束函式 , 回傳 none
return 資料 # 結束函式, 回傳資料

'''

# #定義可印出任何文字函式
# def sayHello(msg):
#     print(msg)
#呼叫上方定義的函式
# sayHello("hello function")  #印出 hello function



# #定義可作加法的函式
# def add(n1,n2):
#     result=n1+n2
#     print(result)
#呼叫上方定義的函式
# add(3,4) #印出7




# #程式範例, 回傳 n1+n2 的結果
# def add(n1,n2):
#     result=n1+n2
#     return result #return將結果從函式內部帶出來放入add
# #呼叫函式取得回傳值
# value=add(3,4)  
# print(value) # 7




# def multiply(n1,n2):
#     print(n1*n2)
# multiply(3,4)            #12




# def multiply(n1,n2):
#     print(n1*n2)
# # value = multiply(2,5)
# # print(value)           #10 , none




# def multiply(n1,n2):
#     print(n1*n2)
#     return n1-n2
# value = multiply(7,3)
# print(value)              # 21 , 4




#在函式外繼續操作資料的需求, 用回傳值
def multiply(n1,n2):
    return n1*n2
value = multiply(3,3)+multiply(5,3)
print(value)                         #(3*3)+(5*3)=24
