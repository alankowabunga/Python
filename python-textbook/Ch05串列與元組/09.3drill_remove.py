'''
此情況次數無固定 , 適合用while迴圈 , 而要讓使用者可以在內層可持續做輸入 , 因此外層建立無限迴圈 while True

'''
#若清單中有1+個相同名稱的元素 , 要如何一口氣刪除?
#利用搜尋索引值index() + 利用索引值刪除的pop()

fruit_list = ['kiwi' , 'apple' , 'watermelon' , 'orange']

while True:
    print(" The fruits listed:" , fruit_list)
    dislike = input("Enter the food you don't like(Press Enter to run ):")

    if dislike == "" :   # Press Enter to run
        break

    n = fruit_list.count(dislike)  # 不喜歡水果的數量
    if n > 0:
        fruit_list.remove(dislike)
        print("The latest list: {}".format(fruit_list)) 

    else:
        print(dislike , "not in the list.")