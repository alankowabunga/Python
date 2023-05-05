list1 = []
innum = 0
while (innum != ""):
    innum = input("Enter the electric fee:")
    list1.append(innum)


list1.pop()   #刪除最後一項元素""
M = (max(list1))
m = (min(list1))
print("Max fee={}, min fee={}".format(M,m))  #這裡排序的是字串,而非數值
print(sorted(list1,reverse= True))

list1 = list(map(int,list1))