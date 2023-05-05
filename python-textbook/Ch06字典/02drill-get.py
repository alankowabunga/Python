#P6-5
'''血型和其對應的個性
當使用者輸入血型會顯示相對應的個性，若沒有該血型則顯示[無此資料]'''

dic_blood = {"O":"Naughty Wen", "B":"Handsome Alan", "A":"stubborn", "AB":"Rare species"}

name = input("請輸入血型(A,B,O,AB):")
blood = dic_blood.get(name)
if blood == None:  #當key不存在時會回傳None或預設值
    print("沒有{}血型".format(name))

else:
    print("The blood type is :{}".format(name))
