'''
回呼函式-程式範例

#建立第一個函式
def test(arg):
    arg() # 呼叫'回呼函式'

#建立第二個函式
def handle():
    print(100)

test(handle)

邏輯
step 1: test(handle) 將handle 函式放入 test函式里跑程式碼
step 2: test(arg)函式的程式碼 arg() 也就變成 handle()...呼叫handle函式的意思
step 3: 呼叫 handle 函式開始跑其程式碼 print(100)，最後印出100
'''

def test(arg):
    print(50)

def handle(data):
    print(data) #50

test(handle) # 用 test函式呼叫handle函式(帶入參數)

'''
邏輯
step 1: test(handle)將 handle放入test函式中跑程式碼
step 2: print(50)帶入handle後變成handle(50)，並呼叫了handle函式+參數是50
step 3: 將參數50 handle函數的變數data，最後 print(data) = 50
'''