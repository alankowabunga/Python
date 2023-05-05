'''

串列搜尋: index() 搜尋索引值 ,  count() 計次
增加串列元素: append(元素資料) 加在最後 , insert(n, 元素資料) 在索引值n位置增加元素資料
刪除串列元素: remove(元素名稱) , pop(索引值) , del()

'''

# index() 可搜尋指定元素的索引值, 語法為: 索引值 = 串列名稱.index(元素名稱)
list1 = ["alan" , "wen" , "baby"]
print(list1.index("wen"))   # 1   (直接搜尋列印)
print(list1.index("baby"))  # 2

n = list1.index("alan")
print(n)  # n = 0   (先宣告變數 , 再列印變數)



# count() 可計算指定元素在字串中出現的次數 , 語法為: 次數 = 串列名稱.count(元素名稱)
# list1 = ["alan" , "wen" , "baby"]
print(list1.count("alan"))  # 1 (次)
list1 += ["darling" , "wen"] # 即為 list1 = list1 + [...]
print(list1) #['alan', 'wen', 'baby', 'darling', 'wen']
print(list1.count("wen")) # 2 (次)

n = list1.count("wen") #宣告變數, 再列印變數
print(n)               # n = ['alan', 'wen', 'baby', 'darling', 'wen']



# append()可將元素加在串列最後面, 語法為: 串列名稱.append(元素值)
print(len(list1)) # 5 即串列長度(有幾個元素)
list1.append("Last one")  # 增加此元素到字串最後一位, 索引值為 5
print(list1)
print(list1[5])
print(len(list1)) # 串列長度變為 6 , ['alan', 'wen', 'baby', 'darling', 'wen', 'Last one']



# insert()可將元素加在指定索引位置, 語法為: 串列名稱.insert(索引值 , 元素名稱)
list1.insert( 3 , "middle")
list1.insert( -1 , "倒數第二")  #索引值若為負數 , 由串列的最後向前推算
print(list1)  #['alan', 'wen', 'baby', 'middle', 'darling', 'wen', '倒數第二', 'Last one']



# remove()可刪除串列中出現的第一個元素, 語法為: 串列名稱.remove(元素名稱)
list1.remove("wen")
print(list1)  #['alan', 'baby', 'middle', 'darling', 'wen', '倒數第二', 'Last one']



# pop()可刪除索引值的元素 , 如果沒有給索引值則會刪除最後一個元素 , 語法為: 串列名稱.pop(索引值)
list1.pop()   #['alan', 'baby', 'middle', 'darling', 'wen', '倒數第二' ]
list1.pop(2)  #['alan', 'baby', 'darling', 'wen', '倒數第二' ]



# del 可刪除變數 , 元素和串列
#刪除單一元素語法為: del 串列名稱索引值]
#刪除指定範圍語法為: del 串列名稱[起始值 : 終止值 : 間隔值]
del list1[1]
print(list1)   #['alan' , 'darling', 'wen', '倒數第二' ]

del list1[0 : 3 : 2]   
print(list1)   #[ 'darling' , '倒數第二' ]