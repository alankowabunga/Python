'''
P5-21
'''

# 空串列 , while , append , break , sort + reverse

score = []

while True:
    inscore = (input("Enter the grade:"))  # 使用int()會出現問題,因為input裡面不只有數字的字串不能被 Python 的 compiler 所識別，也就是int()中不能接受這些數據，就會出現異常。
    score.append(inscore)

    if inscore == "":
        break

    score2 = sorted(score , reverse = True)
    print(score2)

'''
原先這樣也可以
    score.sort()
    score.reverse()
    print(score)

'''