def test(arg):
    arg("paramax") #呼叫回呼函式，並帶入參數

#定義回呼函式
def handle(data):
    print(data)

test(handle) #呼叫 test 函式，帶入handle