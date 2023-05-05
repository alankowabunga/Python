''' 搜尋有兩種: 循序搜尋 & 二分搜尋

設計抽獎程式
將顧客和編號 分別儲存於串列中, 當使用者輸入編號時程式會顯示該編號的姓名, 搜尋無果則顯示'無此編號'
'''
#建立串列
name=["alan","wen","leo","anna","ray","angla","ruru","ron"]
number=[123,321,234,432,345,543,456,654]

no=int(input("Enter the number:"))
Found=False
for i in range(len(name)):
    if no == number[i]:
        Found=True
        break

if Found == False:
    print("Sorry, good luck next time")

else:
    print("Congradulation {}".format(name[i]))
print("Searching repetition:{}".format(i+1))