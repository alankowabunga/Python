'''類別的兩種用法
1. 類別&類別屬性
2. 類別&實體物件, 實體屬性, 實體方法
'''

# 實體屬性: 封裝在實體物件中的變數
# 實體方法: 封裝在實體物件中的函式
'''
class 類別名稱:

    #定初始化函式
    def__init__(self):
        定義實體屬性
    定義實體方法/函式

# 建立實體物件, 放入變數 obj 中
obj=類別名稱()
'''

#更加詳盡的範例如下
'''
class 類別名稱:

    #定初始化函式
    def__init__(self):
        封裝在實體物件中的變數
    def 方法名稱(self,更多自訂參數):
        方法主體, 透過self操作實體物件

# 建立實體物件, 放入變數 obj 中
obj=類別名稱()
'''

# 基本語法: 實體物件.實體方法名稱(參數資料)
class point:
    def __init__(self,x,y): #建立初始函式
        self.x=x            #建立實體屬性x,y
        self.y=y
    def show(self): #建立實體方法self
        print(self.x,self.y)
p=point(1,5) # 建立實體物件
p.show() # 呼叫實體方法