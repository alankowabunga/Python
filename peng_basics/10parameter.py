'''預設資料:
def 函式名稱(參數名稱=預設資料):
    print(參數名稱)
'''
# def say(msg="hello"):
#     print(msg)
# say("hello function")  #印出字串
# say()                  #印出預設資料 hello


'''
#參數名稱對應

def 函式名稱(名稱1,名稱2):
    函式內部程式碼
    
#以參數名稱對應資料
函式名稱(名稱2=3,名稱1=5)
'''

def power(base,exp=0): #若沒給次方的資料, 則預設為0
    print(base**exp)
power(3,2)
power(4) #沒有給第二個參數, 則使用預設資料
