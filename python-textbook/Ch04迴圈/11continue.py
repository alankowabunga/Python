'''
輸入總樓層, 命名避開四樓
'''

#跳過第4樓, 所以數字會比實際樓層多1: ( floor + 2)

floor = int(input("請輸入總樓層數:"))

for i in range( 1 , floor + 2):
    if i == 4 : 
        continue
    
    print( i , end = "  ")