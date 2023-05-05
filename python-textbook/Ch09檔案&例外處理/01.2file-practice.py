#建立文件檔案
with open("data.txt", mode = "w" , encoding = "utf-8") as file: #當無指定檔案時會直接新增
    file.write("first line\nsecond line\nthird line")

#利用readlines()函式讀取文件所有內容,　並且將文件的內容加入編號
with open("data.txt" , mode = "r" , encoding = "utf-8") as file:
    content=file.readlines() # 將讀取到的文件內容放到 content 變數裡面

title = 0 # 設定標題初始值為 1
for row in content:
    title += 1
    print("{}:{}".format(title,row))