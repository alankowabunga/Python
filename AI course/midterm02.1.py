'''
### 題目1.
- 題目會給定一個字串，字串內包含數字、英文字元及特殊字元，請將這些字元拆開成3個list，每個list裡各含一種種類，請依照前面的順序回傳list(數字、英文、特殊字元)

- example 1:
    - input : "k8q&12j9K"
    - output: ['8','1','2','9'],['k','q','j','K'],['&']
- example 2:
    - input : "123qwe"
    - output: ['1','2','3'],['q','w','e'],[]

- hint : 字元大小比較可以參考ascii code表 https://www.wikiwand.com/zh-tw/ASCII
        - 每個字元代表了某個數字值，所以可以拿來做比較判斷，例如 a代表了61,b代表了62，所以當程式輸入 a < b時，會回傳 True。'''

numList = []
letList = []
symList = []
for i in list_1:
    if i.isdigit()==True:
        numList.append(i)
    elif i.isalpha()==True:
        letList.append(i)
    else:
        symList.append(i)
print("Letter:{}, Number:{}, Symbol:{}".format(numList,letList,symList))