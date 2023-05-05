# FullName 實體物件的設計:分開紀錄姓,名資料的全名
class fullname:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name=fullname("Alan","Chen")
print(name.first,name.last)

name2=fullname("Wen","Chen")
print(name2.first,name2.last)