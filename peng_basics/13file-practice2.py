'''建立有三行數值的檔案, 讀取並做加總'''
#建立
with open("data2.txt", mode="w") as file:
    file.write("5\n4\n2")

#讀取並將每行數值做加總
sum=0
with open("data2.txt", mode="r") as file:
    for line in file:
        sum+=int(line) #讀進來是看起來像數值的字串
print(sum)