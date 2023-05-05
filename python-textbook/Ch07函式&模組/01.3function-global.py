'''變數有效範圍

全域變數: 函式外的變數, 在整個檔案都有效
區域變數: 函式中的變數, 只在函式內有效

#若變數相同, 則是看是在函式的內外, 去使用相對應的變數

若想在函式內使用全域變數, 則需在函式內以global宣告: 'global 變數名稱'
'''
#邏輯詳見p7-6
def scope():
    var1=1
    print(var1,var2) # 1 , 20

var1=10
var2=20
scope()
print(var1,var2)  # 10 , 20


# global 宣告變數
def scope():
    global var01 # 將函式內的區域變數 , global為全域變數
    var01=1
    var02=2
    print(var01,var02)

var01=10
var02=20
scope()
print(var01,var02) # var01已被 global全域變數值1覆蓋了