num=int(input("Enter an integer"))
sum=0
for i in range(0,num+1):
    if (i%2 == 0):
        print(i,end=" ")
        sum+=i
print("\n=========")
print("The sum of even integer:",sum)