'''
裝飾器 decorator: 
特殊設計的函式，可重複利用裝飾器內部的程式碼，以不同方式表達結果
HOW?
利用 參數!!
callback(參數)，執行帶有裝飾器的函式(可設多個)，因此最後印出方式可以輕易多變
'''
#定義裝飾器，並印出0-10中偶數的列表
def myDeco(callback):
    def innerFunc():
        parameter=[]
        for i in range(0,11):
            if i % 2 ==0:
                parameter.append(i)
        callback(parameter) # 呼叫 show函式，將參數parameter放入變數 n 中
    return innerFunc

#使用裝飾器 1st way
@myDeco
def show1(n):
    print("1st. way to show",n)
show1()
#使用裝飾器 2nd way
@myDeco
def show2(n):
    print("2nd way to show",n)
show2()