'''
單向判斷式(if)
語法為:
if 條件式:
    程式區塊

若程式區塊只有一列程式碼, 也可以將兩列合併成一列:
if 條件式:  程式碼


設計一個密碼程式, 輸入"1234"才能登入並顯示[歡迎光臨~!]
若輸入密碼錯誤則不會有任何訊息
'''

pw = input("請輸入密碼:")
if pw == "1234":   #用兩個等號, 判斷等號兩邊是否相等
    print("歡迎光臨!")
