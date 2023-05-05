'''

有一個包含三個字串的串列:name = ["alan" , "leo" , "anna"]
依序在每個名子前面加上編號後顯示

想知道串列中有幾個元素可利用 : len(串列) , 再來即可用range函式讀取串列中所有元素資料
'''
#使用 for...range迴圈讀取串列
#利用len() 計算串列的長度,取得串列的長度後, 以for迴圈循環讀取串列元素

name = ["alan" , "leo" , "anna"]
no = ["1" , "2" , "3"]

#length = len(no) = 3
for i in range(len(no)): #即為 for i in range(3)
    print("No.{}  Name: {}".format(no[i] , name[i]))