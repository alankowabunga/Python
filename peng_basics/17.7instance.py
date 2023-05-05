#file 實體物件的設計: 包裝檔案讀取的程式
#利用類別來建立實體物件
class file:
    #初始化函式
    def __init__(self,name):
        self.name=name # 將檔案名稱放在實體屬性裡面
        self.file=None # 建立檔案物件, 尚未開啟檔案: 初期是 None
    
    #將開啟檔案的動作定義在實體物件的實體方法中
    def open(self): 
        self.file=open(self.name,mode="r",encoding="utf-8") #用內建函式open()開啟檔案後放入實體屬性file中

    #讀取
    def read(self):
        return self.file.read() #利用剛剛得到的檔案物件read讀取出來, 做return回傳

#包裝完成後, 要開啟檔案就可以簡化
#讀取第一個已建立的檔案
f1=file("data1.txt") #將實體物件放入變數f1
f1.open()            #開啟
data=f1.read()       #將讀取的資料放入變數data
print(data)

#讀取第二個檔案
f2=file("data2.txt")
f2.open()
data=f2.read()
print(data)