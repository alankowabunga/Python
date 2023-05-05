'''
裝飾器工廠:用來生產裝飾器的函式
由於單純一個裝飾器能做的事情沒有彈性，永遠只能固定印出裝飾器內的程式
做的動作都是固定的。
因此利用裝飾器工廠來添加操作性的彈性。

eg.
def 裝飾器工廠名稱(參數名稱,...):
    def 裝飾器名稱(回呼函式名稱):
        def 內部函式名稱():
            #裝飾器內部程式碼
            回呼函式名稱()
        return 內部函式名稱
    return 裝飾器名稱

@裝飾器工廠名稱(參數名稱,...)
def 函式名稱():
        #函式內部程式碼
函式名稱() #呼叫帶有裝飾器的函式
'''
#eg.1
def decFactory(base):
    def myDeco():
        def innerFunc(callback): #?? 為何參數要放callback??

            result=base*3 #step2:將 3 帶入base後進行操作
            callback(result) #step3: 將操作後的結果放進回呼函式的參數，並執行 ln.26 的 decoratedFunc函式

        return innerFunc
    return myDeco #??為何要 return 以上兩個函式??
'''如果函式定義中未出現 return 陳述式，則會在執行所呼叫函式的最後一個陳述式之後，
自動將控制權還給呼叫函式。 在此情況下，所呼叫函式的傳回值會是未定義。
'''
@decFactory(3) # step1: 參數 3 帶入 ln.19 的 base變數
def decoratedFunc(result): #step4:將result設為函式的參數並執行程式碼
    print("Ordinary Function",result)
decoratedFunc() #執行一系列動作