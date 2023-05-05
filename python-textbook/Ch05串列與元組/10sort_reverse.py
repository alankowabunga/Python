'''

串列排序 sort() 由小到大, reverse() 反轉, sorted() 排序

搭配sort() + reverse() 可以使排序由大到小

'''

# 串列名稱.sort()  使串列排序由小到大
list1 = [ 4 , 6 , 2 , 7 ]
list1.sort()
print(list1)  # [ 2 , 4 , 6 , 7]


# 串列名稱.reverse()  使串列排序反轉
list2 = [ 3 , 8 , 2 , 5 ]
list2.reverse()
print(list2)  # [ 5 , 2 , 8 , 3 ]
# 搭配sort() + reverse() 可以使排序由大到小
list2.sort()     # [ 2 , 3 , 5 , 8 ]
list2.reverse()  # [ 8 , 5 , 3 , 2 ]


# sorted() 可在不改變原串列的情況下 , 建立一個新的串列加以排序 , 語法為: 新串列 = sorted( 原串列, reverse = True/False)
#  新串列 = sorted( 原串列, reverse = True/False) , True 由大到小 , False 由小到大 , 省略時預設為False
list3 = [ 6 , 2 , 9 , 4 ]
list4 = sorted( list3 , reverse = True)
print(list4)  # [ 9 , 6 , 4 , 2 ]