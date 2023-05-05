'''
用串列顯示成績

國英數
'''

c = int(input("國文成績:"))
e = int(input("英文成績:"))
m = int(input("數學成績:"))

score = [ c , e , m ]
print("國文成績為:{}".format(score[0]))
print("英文成績為:{}".format(score[1]))
print("數學成績為:{}".format(score[2]))