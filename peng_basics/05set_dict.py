'''
set & dic 使用{}括號 , 但在宣告變數 , 變更參數 or 印出結果時則使用[]括號

集合 set = {}

字典 dic{}  : key-value pair 鍵值對 , key 對應 value
字典[key] = value
印出字典的語法: print(dic["key"])

用列表建立字典! 語法為: dic = { key : value for key in [列表]}  # 列表 list = []
'''

s1 = { 2 , 3 , 4 }
print( 2 in s1)  #True
print( 8 in s1)  #False
print( 8 not in s1) #True

s2 = { 3 , 4 , 9 }
# s3 = s1 & s2  # 交集 { 3 , 4 }
# s3 = s1 | s2  # 聯集 { 2 , 3 , 4 , 9 }
# s3 = s1 - s2  # 差集 從s1中減去和s2重疊的部分 { 2 }
# s3 = s1 ^ s2  # 反集合 , 取{ 2 , 9 }



#若要將字串中的文字拆成 set集合, 使用set()使字串成為集合,再宣告一個變數再將其印出
s = set("hello")
print(s)  # { h , e , l , o }


dic = {"apple" : "蘋果" , "banana" : "香蕉"} # key 為 apple & banana , value 為蘋果&香蕉
print(dic["apple"])  #蘋果



#更改 value
dic["apple"] = "小蘋果"
print(dic["apple"])  #小蘋果



#刪除字典中的key-value pair
del dic["apple"]
print(dic)  #  { "banana : 香蕉" }



#用列表建立字典! 語法為: dic = { key : value for key in [列表]}
dic = { x : x*2 for x in [3,4,5]}
print(dic) # {3:6 ,  4:8 , 5:10}