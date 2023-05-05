'''

split() 切割字串成為清單, 可將英文句子的每一個單字切割成參數的清單
語法為: 

字串名稱.split()
字串名稱.split(,) #指定用逗號 , 分割字元來切割字串成為清單

'''

str1 = " this is a pen "
list1 = str1.split()
print(list1)

list2 = str1.split(",")
print(list2)