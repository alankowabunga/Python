'''
總和

'''

n = int(input("Enter a integer:"))
total = 0

for i in range( 1 , n + 1 ):
    total += i

print("由1到{}的累加值為:{}".format( n , total ))

