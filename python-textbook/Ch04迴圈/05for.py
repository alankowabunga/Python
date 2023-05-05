'''
顯示奇數
'''

num = int(input("請輸入一個正整數:"))

for i in range( 1 , num + 1):
    if i % 2 != 0: print( i , end = "  ")
