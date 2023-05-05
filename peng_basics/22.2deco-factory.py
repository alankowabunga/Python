'''
由於單純一個裝飾器能做的事情永遠只能印出裝飾器內的程式
做的動作都是固定的沒有彈性。
因此利用裝飾器工廠來添加操作性的彈性。

可參考 21.4中，只有單一的裝飾器
'''
#計算 0+1+2+....+ max 的 total。為了讓 max 參數能自行變更的彈性，因此利用裝飾器工廠
def decoFactory(max):
    def myDeco(callback):
        def innerFunc():
            total=0
            for i in range(0,max+1):
                total+=i

            callback(total)
        return innerFunc
    return myDeco

@decoFactory(10) # 帶入到 ln.9 的 max 參數。單純使用裝飾器時不用加()，使用裝飾器工廠時則需要，有點像呼叫的概念
def test1(result):
    print("test.1 pure result:",result)
test1()

@decoFactory(10) # 帶入到 ln.9 的 max 參數。單純使用裝飾器時不用加()，使用裝飾器工廠時則需要，有點像呼叫的概念
def test2(t):
    result=t*2
    print("test.2 total*2:",result)
test2()