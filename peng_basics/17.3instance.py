# point實體物件的設計: 平面座標上的點
class point:
    #定義初始化函式 __init__(), 和固定參數self
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #此實體物件包含 X , Y 兩個實體屬性
    #定義此類別是為了產生實體物件

#建立第一個實體物件
p = point(3,4) # point()產生點的實體物件放入變數 p
print(p.x,p.y) #實體物件.屬性名稱

#建立第二個實體物件
p2=point(5,6)  #5對應到x , 6對應到y
print(p2.x,p2.y) #p2.x對應到上方self.x=x的x