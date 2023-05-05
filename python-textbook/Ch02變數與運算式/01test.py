'''
只有兩同學, 用以下格式輸出其名子和成績
姓名    成績
任任    60
雯雯    100
班級平均    80
'''

s1 = str(input("請輸入一號名子:"))
g1 = int(input("請輸入一號成績:"))
s2 = str(input("請輸入二號名子:"))
g2 = int(input("請輸入二號成績:"))
ag = (g1 + g2)/2

print("姓名" , "成績" , sep = "    ")
print("%-3s    %3d" % (s1 , g1))
print("%-3s    %3d" % (s2 , g2))
print("班級平均    %3.2f" % ag)

#嘗試用.format格式化寫
print("姓名" , "成績" , sep = "    ")
print("{0:3s}   {1:3d}".format(s1 , g1))
print("{0:3s}   {1:3d}".format(s2 , g2))
print("班級平均    {:3.2f}".format(ag))