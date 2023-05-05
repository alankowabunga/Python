'''
設計程式計算BMI
公式為 BMI = 體重(kg) / 身高(m)**2
'''

height = int(input("請輸入身高(公分):"))
weight = int(input("請輸入體重(公斤):"))
bmi = weight / (height/100)**2
print("身高:{:3d} , 體重:{:3d} , BMI:{:5.2f}".format(height , weight , bmi))