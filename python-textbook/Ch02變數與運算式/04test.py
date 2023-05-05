'''
1 inch = 2.54 cm  , 1 cm = 1/2.54 inch
1 foot = 12 inch  , 1 inch = 1/12 foot
設計程式輸入身高(cm), 換算為英吋和幾英尺
'''

height = int(input("請輸入身高(公分):"))
inch = height*1/2.54
foot = height*2.54*1/12
print("身高{:3d}公分等於{:5.2f}英寸,{:5.2f}英尺".format(height , inch , foot))