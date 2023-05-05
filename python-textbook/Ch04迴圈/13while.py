'''
偶數數列
'''

n = int(input("請輸入正整數:"))

i = 1
while i < n : #只能< , 如果 <= 那 (i += 1)這行會變 i 比 n 多 1 
    i += 1
    if i % 2 != 0:
        continue
    
    print( i , end = " ")