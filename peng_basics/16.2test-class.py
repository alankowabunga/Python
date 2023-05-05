class io:
    supportedsrc=["console","file"] #終端機, 檔案
    def read(src): #參數 src
        if src not in io.supportedsrc:
            print("not suported")
        else:
            print("read from", src)

io.read("internet") #internet物在支援範圍中(console, file)