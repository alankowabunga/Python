'''
裝飾器 decorator: 
特殊設計的函式，可重複利用裝飾器內部的程式碼，以不同方式表達結果
HOW?
利用 參數!!
callback(參數)，執行帶有裝飾器的函式(可設多個)，因此最後印出方式可以輕易多變
(詳見12.4)

大方向邏輯~~呼叫帶有裝飾器的函式，會先執行裝飾器內部的程式碼
順序為先跑裝飾器的內部函式，再執行帶有裝飾器的函式

基本裝飾器:
#定義裝飾器
def 裝飾器名稱(回呼函式名稱):
    def 內部函式名稱():
        #裝飾器內部程式碼
        回呼函式()  # 也就是下方帶有裝飾器的函式
    return 內部函式

#使用裝飾器
@裝飾器名稱
def 函式名稱(): #此時變成帶有裝飾器的函式
    #函式內部程式碼
函式名稱() #呼叫帶有裝飾器的函式
'''
#eg.
def testDecorator(callback):
    def innerFunc():
        print("裝飾器")
        callback()
    return innerFunc

@testDecorator
def decoratedFunc():
    print("普通函式")

decoratedFunc() #裝飾器
                #普通函式