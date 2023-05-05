'''循序搜尋

設計抽獎程式
用字典儲存顧客和編號資料, 當使用者輸入編號時程式會顯示該編號的姓名, 搜尋無果則顯示'無此編號'
'''
#建立字典
drawDict={123:"alan",321:"wen",234:"leo",432:"anna",345:"ron",543:"ru",456:"ray",654:"angla"}
no=int(input("Enter the number:"))

#將keys & values 轉換成串列
numList = list(drawDict.keys())
nameList = list(drawDict.values())

found = False
for i in range(len(drawDict)):
    if no == numList[i]:
        found = True
        break

if found == False:
    print("sorry, good luck next time")

else:
    print("Congradulation {}".format(nameList[i]))

print("Searching repetition:{}".format(i+1)) # i 的值從0開始,需+1才正確