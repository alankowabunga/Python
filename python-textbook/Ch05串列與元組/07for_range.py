s1 = int(input("Enter score:"))
s2 = int(input("Enter score:"))
s3 = int(input("Enter score:"))

n1 = str(input("Enter name:"))
n2 = str(input("Enter name:"))
n3 = str(input("Enter name:"))

score = [ s1 , s2 , s3]
name = [ n1 , n2 , n3]

#利用len()取得串列長度 , 再以for..range迴圈讀取串列元素
for i in range(len(name)):
    print("Name:{:6s} Grade:{:3d}".format(name[i] , score[i]))
