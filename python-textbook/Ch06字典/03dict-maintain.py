#修改字典中的元素值: 字典名稱[key] = value
food_price = {"香蕉":10 , "蘋果":20 , "西瓜":30}
food_price["西瓜"] = 20  #將西瓜value覆蓋為20
print(food_price)


#新增字典資料
#如果輸入的 key 不存在,　則做為新增之資料
food_price["New key"] = "value"
print(food_price)


#刪除特定元素值: del 字典名稱[key]
#刪除字典中所有元素: 字典名稱.clear
#刪除字典，不再存在: del 字典名稱