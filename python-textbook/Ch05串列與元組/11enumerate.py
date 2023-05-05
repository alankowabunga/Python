'''

語法為: enumerate(iterable, start_index)。
前者輸入一個可迭代的對象、比如說 List 資料型態；
後者輸入開始的起點編號，為數字，若不設定時從 0 開始。

list = ['a', 'b', 'c', 'd', 'e']
for value in enumerate(list):
    print(value)

(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
(4, 'e')
#返回的值都是tuple型態 , 可用 print(type(value))確認

'''

# 可利用 enumerate & for 迴圈 , 取得清單的索引 & 值
# 也可以在 for 迴圈當中分開 index 以及 value:
# for index, value in enumerate(List):
#     print(index, value)


lst2 = list(" hello world!") # 再宣告變數 , 更改值 或印出時 括號都使用()
for index , value in enumerate(lst2 , 0):
    print(index , ":" , value , end = " ")
