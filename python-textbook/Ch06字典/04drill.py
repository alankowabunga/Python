'''建立三筆學生成績資料，若輸入學生名子會顯示對應的成績，否則就再輸入其成績將資料加入字典中'''

dict_score = {"Alan":100,"Wen":101,"Biu":99}

name = input("Please enter the name:")
if name in dict_score:
    print("score =", dict_score[name])

else:
    s = input("please enter the score:")
    dict_score[name]= s
    print(dict_score)