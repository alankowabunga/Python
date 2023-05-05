'''

輸入最近幾個月的電費, 輸入ENTER結束 
以內件函示顯示最多&最少的電量, 並將每個月電費由大到小做排列顯示

'''

elist = []
innum = 0
while (innum != -1): #!!!為了讓輸入指令的int()整數函式順利使用, 必須設定結束的時候也是輸入數值!
    #否則會出現invalid literal for int()!!!
    innum = int(input("Enter the electric fee(input -1 to run code):"))
    elist.append(innum)


elist.pop()   #刪除最後一項元素""

print("Max fee={:d}, min fee={:d}".format(max(elist),min(elist)))
print("Final elist fromt most to least is:{}".format(sorted(elist,reverse=True)))