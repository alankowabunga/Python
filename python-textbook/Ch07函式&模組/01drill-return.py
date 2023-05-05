'''計算園面積和周長'''

#建立函式
def circle(r):
    length = r*2*3.14
    area = r*r*3.14
    return area,length
    #此時有兩的回傳值, 需用相同數量的變數儲存返回值
l,a = circle(5)
print("length={:5.3f},area={:5.3f}".format(l,a))