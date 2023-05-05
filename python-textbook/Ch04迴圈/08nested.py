'''
數字遞增三角形(start from 1 )
'''

num = int(input("請輸入一個正整數:"))

for i in range( 1 , num + 2 ):
    for j in range( 1 , i ):
        if j < i : print( j , end = "")

    print()
