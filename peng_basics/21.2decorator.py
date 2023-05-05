#定義裝飾器
def myDeco(callback): #裝飾器中的參數為回呼函式
    def innerFunc():
        print("Deorator's code")
    callback()  # 縮排錯誤
    return innerFunc
#使用裝飾器
@myDeco
def test():
    print("Ordinary Func.'s code")

test() # 因使用 @myDeco 使 test函式成為帶有裝飾器的函式，呼叫它會顯跑裝飾器內的程式碼

print("============================")
'''
印出的結果並非預期的以下順序:
Deorator's code
Ordinary Func.'s code

是因為 callback() 呼叫回呼函式的縮排錯誤
當test()呼叫時會先跑myDeco裝飾器內程式碼，此情況為

def innerFunc():
    print("Decorator's code")
callback()
return innerFunc

因此會先執行呼叫 callback() 也就是 test()的程式碼 print("Ordinary Func.'s code")
接著 return innerFunc 執行 print("Decorator's code)
所以結果為:
Ordinary Func.'s code
Deorator's code
'''
def myDeco2(cb):
    def inFunc():
        print("D2's code")
        cb(3) #呼叫被裝飾的函式，若要帶入參數則放這裡，而非一般情況的 oFunc(n)，此參數將帶入n
    return inFunc

@myDeco2
def oFunc(n):
    print("O' func.'s code",n)
oFunc() #一般函式情況帶入參數放這裡，但因為函式已被裝飾，實際上執行oFunc函式的呼叫為 cb()，因此參數要放在 cb(n)