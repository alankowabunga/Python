'''先建立實體物件才能使用

class 類別名稱:
    #定義初始化函式, 固定參數self
    def __init__(self):
        透過操作self來定義實體屬性
#建立實體物件, 放入變數 obj中
obj=類別名稱() #呼叫初始化函式

'''
#
class point:
    #定義初始化函式 __init__, 固定參數self
    def __init__(self): # 實體屬性名稱 x,y
        self.x=3
        self.y=4
#建立實體物件
#此實體物件包含 X , Y 兩個實體屬性
obj=point() 