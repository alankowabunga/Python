"""
在函式中使用 yield 語法，呼叫時回傳生成器 generator
並搭配for迴圈使用。

基本語法: 
def 函式名稱():
    yield 資料

#呼叫函式，回傳生成器
變數名稱=函式名稱()

eg.
def test():
    yield 3
    yield 5

gen=test()
for data in gen:
    print(data)
#搭配 for 迴圈使用，逐一印出3,5
"""

#建立生成器函式，與一般函式不同 無法用gen=test()呼叫出結果 
def test():
    print("phase 1")
    yield 5
    print("phase 2")
    yield 10
#呼叫並回傳生成器
gen=test()
# print(gen) #印出結果不是 5，而是一個生成器:<generator object test at 0x0000025B77B39A10>

#搭配for迴圈使用
for d in gen:
    print(d) #5