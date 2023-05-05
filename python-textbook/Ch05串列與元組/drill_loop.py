'''

將成績存入串列 , 輸入 -1 表示成績輸入結束 , 並顯示所有成績, 總成績和平均成績

平均成績 = total 所有元素總和 / (len(scores)) 元素數量...即串列長度

'''

scores = []
total = inscore = 0     #總成績和平均成績會需要用到 total 這個變數 , 先將初值也一同設為0

#產生成績字串
while (inscore != -1):
    inscore = int(input("Enter your score:"))
    if (inscore != -1):
        scores.append(inscore)

print("There are {} students. 成績為:{}".format(len(scores) , scores))

#字串已經產生完成, 計算總成績        
for score in scores:  #設定變數 score, 程式會依序將串列中的數, 作為變數 score 的值
    total += score  #串列中所有元素(成績)累加即為總成績

#計算平均成績 : total / (len(scores)) 串列長度(有多少個元素)
average = total / (len(scores))
print("總成績為:{} , 平均成績為:{}".format(total , average))