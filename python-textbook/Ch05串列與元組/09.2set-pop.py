'''若不給特定元素, 清單內有重複元素如何一口氣刪除

在 Python 中，有兩種最流行的方法可以從 List 中刪除重複的元素。
1. 如果你不想在刪除重複元素後還保持列表內元素的順序，那麼你可以使用 Set 函式。
2. 如果你想在刪除重複元素後保持列表內元素的順序，那麼你可以使用名 OrderedDict。

在一個集合set中, 不允許有重複的元素集合, 使用大括號 {}
'''

fruit_list = ['kiwi' ,  'orange' , 'apple' , 'kiwi' , 'apple']
print("Original list is {}".format(fruit_list))

#找出重複的資料
repeated = []
for i in fruit_list:
    rep = fruit_list.count(i)
    if (rep>1) and i not in repeated:
        repeated.append(i)
print("repeated data:{}".format(repeated)) # ['kiwi', 'apple']

# 將原清單轉換成集合函式set(), 利用集合的特性刪除掉重複的字元
convert_set = set(fruit_list)
#再轉換回清單, 每個資料只會出現一次
newList = list(convert_set)
print("Unrepeated list is {}".format(newList))  # ['orange', 'apple', 'kiwi']

#最後將有重複的資料刪除
for j in repeated:
    for k in newList:
        if j == k:
            n=newList.index(k)
            newList.pop(n)
print("Final list is {}".format(newList))
