def add(n1,n2,cb):
    cb(n1+n2)

def handle(result):
    print("The result:",result)

def handle2(result):
    print("2nd. Callback function:",result)


add(3,4,handle)
add(5,7,handle2)
'''
add函式計算帶入的參數
handle/handle2函式則提供不同的印出彈性
'''