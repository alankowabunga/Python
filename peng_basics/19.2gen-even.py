#利用生成器，印出偶數值
def generateEven(maxNumber):
    number=0
    while number<=maxNumber:
        yield number
        number+=2

evenGen=generateEven(10) #變更這個數字就可以改變印出結果的最大值
for data in evenGen:
    print(data)

'''
一般情形要利用input去設定maxNumber
num=input("Enter an integer:)
sum=0
for i in range(0,num+1):
    if i%2 =0:
        sum+=i
print(sum)
'''