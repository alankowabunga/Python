# 此方法必須知道特定元素

fruits = ['kiwi' , 'apple' , 'kiwi' , 'orange']

for i in fruits:
    if i =="kiwi":
        n=fruits.index(i)
        fruits.pop(n)
print(fruits)
