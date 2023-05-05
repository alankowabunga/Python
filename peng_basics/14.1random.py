'''學習random & statistics 模組'''

#載入 (所有操作前都要先載入模組)
import random

#隨機選取 choice([列表]) & sample([列表],n 取出數量)
random.choice([0,2,4,5]) #從列表中隨機選取1個資料
for i in range(2):
    print(random.choice([0,2,4,5]))
random.sample([2,4,6,1],2) #從列表中隨機選取2個資料


# shuffle()可就地隨機調換順序
data=[2,5,7]
random.shuffle(data)
print(data)


'''random(), uniform() 0.0~1.0之間的隨機亂數'''
# random.random()
# random.uniform(0.0 ,1.0)


'''常態分配亂數 normalvariate'''
#取得平均數100 , 標準差10的常態分配亂數
n = random.normalvariate(100,10)
print(n)