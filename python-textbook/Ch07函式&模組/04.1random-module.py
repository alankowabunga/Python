'''亂數模組 random :
#p7-24
random模組有 random, uniform, randint, randrange, choice, sample, shuffle 等函式

random():       0-1之間隨機取一個浮點數
uniform(f1,f2):     f1,f2之間隨機取一個浮點數
randint(n1,n2):     n1-n2之間取一個整數
randrange(n1,n2,n3):    n1-n2之間, 每隔n3的數取得一個整數
choice(字串):        在字串中隨機取得一個字元
sample(字串, n):     在字串中隨機取得 n 個字元
shuffle(串列):       將串列洗牌

# 載入模組: Import 模組名稱  eg. import random as r #取別名為 r
# 使用模組中的函式: 模組名稱.函式名稱(參數)  eg. random.randint(參數)
'''

# randint()
import random #載入 random 模組
for i in range(5): # 執行5次, 也就是取5個數
    print(random.randint(1,10), end=",")  #取的值在1-10之間
print() #換行


# randrange : 功能比 randint 多了遞增值
import random
for i in range(5):
    print(random.randrange(0,12,2), end=",")   # 在 0,2,4,6,8,10 中取值
print()


