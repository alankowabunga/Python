#定義類別和屬性(封裝在類別中的函示和變數)
#定義一個類別 IO , 有兩個屬性 supportedsrc and read
class IO:
    supportedsrc=["console","file"] #終端機, 檔案
    def read(src): #參數 src
        print("read from", src)
#使用類別
print(IO.supportedsrc) # ['console', 'file']
IO.read("file") #read函式送入參數file # read from file
