'''
guess the number

'''

#無固定次數況使用while loop

target = 44

while True: #外層建立無窮迴圈 , 讓使用者可以持續輸入猜測的數字
    guess = int(input("Enter your number in mind:"))
    if guess == target:
        print("Bingo")
        
    elif guess < target:
        print("too small")
        
    elif guess > target:
        print("too large")