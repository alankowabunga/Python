'''
寫一個程式碼，輸入數值並做操作。並使用try...except捕捉錯誤
若是輸入的內容不是數值，則須重新輸入
'''
#keypoint: 錯誤重點在型態轉換，而重新輸入次數沒有固定，因此使用while迴圈

while True: #建立一個無窮迴圈，以利重新輸入
    n=input("Enter an integer:")
    try:
        number=int(n)
        break        #若型態轉換成功則跳出迴圈 
    except:
        print("Wrong datatype")

number*=2
print("two-fold = ",number)