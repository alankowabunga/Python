'''
use nested 'for' loop to make a 9*9 chart
'''

for i in range( 1 , 10 ):
    for j in range( 1 , 10):
        result = i * j
        print("{} * {} = {}".format( i , j , result))

    print()