#前言
'''要取得串列 list 的特定資料, 必須先知道奇在串列中的位置(索引值) , 再 print(list[索引值])
例如: 
list1 = [10 , 20 , 30 ] #分別為3種水果的價格, 若不知道蘋果的索引值就無法取得價格資料
'''

#字典的優點
'''
字典 dic 的 key-value pair 的特性 , 使我們可以利用key 來取得 value !!
建立字典有3種方式~~

No.1 將元素至於大括號{}中 ,並用雙引號':'連結key&value
語法為  dic_name = {key1:value1, key2:value2, ...}
*for example: 
food_price = {"香蕉":10 , "蘋果":20 , "西瓜":30}


No.2 使用dict()函式 , 將 key-value pair 至於中括號[]中
語法為 dic_name = dict([[key1,value1],[key2,value2],...])
*for example: 
dict2 = dict([["banana":20],["apple":50]])


No.3 也是使用dict()函式, 用等號'='連結 . 此方式相當簡潔但key不能使用數值
其語法為 dic_name = dict(key1=value1, key2=value2, ...)
*for example: 
dic3 = dict(banana=20, apple=40, orange=10)

'''