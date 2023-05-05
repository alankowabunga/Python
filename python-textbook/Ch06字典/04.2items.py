
food_price = {"香蕉":10 , "蘋果":20 , "西瓜":30}
item1 = food_price.items()  #印出 dict_items([('香蕉', 10), ('蘋果', 20), ('西瓜', 30)])

for k,v in item1:
    print(k,v,end="  dollars  ,")

#要取得個別元素值, 可使用串列list()函式:'字典名稱.items()' 轉換後, print(item2[串列索引值][元素索引值])
item2 = list(item1) # item1 = food_price.items()  , 轉換為串列
print(item2[1])      #('蘋果', 20)
print(item2[1][0])   # 蘋果
print(item2[1][1])   # 20