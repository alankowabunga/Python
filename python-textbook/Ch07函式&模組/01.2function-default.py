'''使用預設值可避免未輸入參數值而產生錯誤
如果沒有輸入參數時, 就會使用預設值'''

def getArea(width,length=3):
    area = width*length
    return area

r1=getArea(3)
r2=getArea(3,6)
print("(3):{},  (3,6):{}".format(r1,r2))