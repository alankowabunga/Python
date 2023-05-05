'''

函式形式:自訂, 數值 & 字串函式    #內建函式如 print(), int(), str()
模組介紹: 亂數random模組 , 時間模組

'''
# 自訂: 以 def 命令建立函式
# def sayHello():
#     print("alan")
#呼叫
# sayHello()



#建立算面積的函式
def getArea(width,height):
    area=width*height
    return area
#呼叫: (變數 =)函式名稱([參數])
r = getArea(3,4)
#也可以用參數的名稱減少順序錯誤 r = getArea(width=3,length=4)
#使用參數名稱呼叫順序可以調換   r = getArea(length=4,width=3)
print(r)