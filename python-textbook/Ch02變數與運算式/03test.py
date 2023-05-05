'''
設計程式計算梯形面積
'''

#梯形面積公式 (上底+下底)*高/2

top =  int(input("請輸入上底長度:"))
bottom = int(input("請輸入下底長度:"))
height = int(input("請輸入高的長度:"))
area = (top + bottom)*height/2
print("梯形面積為: {:5.2f}".format(area))