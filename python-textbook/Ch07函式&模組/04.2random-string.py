'''隨機取得字元或串列元素

choice(字串/串列):      隨機取得一個字元或串列元素
sample(字串/串列, 數量): ......多個...........
'''

# random.choice()
import random
for i in range(5): # 使用迴圈取5個字元/串列元素
    print(random.choice("abcdefg"), end=",")
print()

# random.sample()
import random
print(random.sample("lijkmnop", 3 )) # sample 函式可直接設定取幾個字元/串列元素
print(random.sample([1,2,3,4,5,6], 3 ))