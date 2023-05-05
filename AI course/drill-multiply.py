'''

階乘

'''

n = int(input("Enter a integer:"))
result = 1

for i in range( 1 , n + 1 ):
    result *= i
print("到{}的階乘為:{}".format( n , result))  