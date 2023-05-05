#取值, 若key不存在會產生錯誤,導致程式結束
dic_name = {"banana":20, "apple":50, "apple":30} #apple重複
print(dic_name["apple"]) # ["香蕉":50] 被覆蓋

#另外也可以用 get 方法取得字典元素值
#此方法當key不存在時會回傳None或預設值, 不會產生錯誤導致程式結束
# 語法為:
# dic_name.get(key[, 預設值])

print(dic_name.get("banana"))
print(dic_name.get("guava"))
print(dic_name.get("apple", 80))  #有此key對應其value
print(dic_name.get("guava", 484)) #無此key,使用預設值484