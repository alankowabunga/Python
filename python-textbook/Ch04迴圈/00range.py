'''

range函式 , 語法為:
數列變數 = range( 起始值 , 結束值 , 間隔值 )
產生的數列為: 起始值到[結束值-1]

!!間隔值也可以為負數 ,且必須 起始值 > 結束值
數列結果為: 起始值遞減到[結束值+1]

'''

#最後將range函數產生的數列轉換成串列list
list1 = range( 18 , 3 , -3 )
print(list(list1))