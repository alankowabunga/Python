
food_price = {"香蕉":10 , "蘋果":20 , "西瓜":30}

#len(字典名稱):取得字典元素個數
print(len(food_price))  #3

# 字典名稱.keys() & 字典名稱.values 取得所有字典中的 keys or values
#dict_keys & dict_values若要以索引方式取元素值, 需用list()函式轉換成串列: list(字典名稱.keys())

key1 = food_price.keys()  #印出為 dict_keys(['香蕉', '蘋果', '西瓜'])
'''也可利用for迴圈取出所有keys'''
for k in key1:
    print(k, end=",")   # 香蕉,蘋果,西瓜
key2 = list(food_price.keys())  #用list函示轉換成串列
print(key2[2])  # 西瓜

v1 = food_price.values()
for v in v1:
    print(v, end=",")


'''  in 功能 '''
#看字典中的key是否存在: "key" in 字典名稱
print("蘋果" in food_price)
print("榴槤" in food_price)