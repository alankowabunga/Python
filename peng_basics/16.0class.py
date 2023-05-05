'''基本語法'''
# 定義封裝的變數/函式


# 定義 Test 類別, x和say封裝在Test中, 為其屬性
class Test:
    x=3 # 定義變數 x
    def say(): #定義函式 say
        print("Hello")

"""使用類別"""
#語法: 類別名稱.屬性名稱
Test.x+3 #取得屬性資料x +3
Test.say() # 呼叫屬性say函式