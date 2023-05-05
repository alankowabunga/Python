# point實體物件的設計: 平面座標上的點
class point: #類別名稱point
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #定義實體方法show
    def show(self): #self一定要寫
        print(self.x,self.y)

    def distance(self, targetx, targety):
        return ((self.x-targetx)**2+(self.y-targety)*2)**0.5

p = point(3,4) #使用類別...建立一個實體物件: 給類別名稱point一個變數p
p.show() #呼叫實體方法/函式: 實體屬性.實體方法名稱()
result=p.distance(0,0) #計算座標3,4和座標0,0之見的距離
print(result)