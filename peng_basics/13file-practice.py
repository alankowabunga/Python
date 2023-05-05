#儲存檔案: 建立變數file來裝檔案物件, 檔案路徑最簡單的方式就是指定一個檔名data.txt
# file = open("data.txt", mode="w", encoding="utf-8")
# file.write("hello file\nsecond line\n測試中文") #操作
# file.close() #關閉...產生一個新的檔案data.txt
'''最佳關閉的實務語法'''
with open("data.txt", mode="w", encoding="utf-8")as file:
    file.write("中文測試\n黑嗨嗨")


#讀取檔案'r', 線是在終端機
with open("data.txt", mode="r", encoding="utf-8") as file:
    data=file.read()
print(data)

#使用json格式讀取, 複寫檔案