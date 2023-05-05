#定義一個裝飾器， 計算 1+2+3...+50 的總和
def cal(callback):
    def innerFunc():
        #裝飾器內的程式碼
        result=0
        for i in range(0,51):
            result+=i
        print("Sum:",result) 
        callback() #step 2: 呼叫回呼函式，執行show函式的程式碼
    return innerFunc #step 3: 回傳內部函式
#使用裝飾器
@cal
def show():
    print("O Func.'s code")

show() #step1: show()呼叫執行裝飾器內部程式碼