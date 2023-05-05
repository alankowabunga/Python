class point:
    def __init__(self, x,y):
        self.x=x
        self.y=y
#建立實體物件(self.x)
#可直接傳入參數資料
obj=point(1,5)
print(obj.x + obj.y) #實體物件.屬性名稱
'''obj.x就是剛帶入__init__()得1'''