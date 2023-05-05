'''
### 題目3.
- 題目會給定一個字串，請幫忙找出重複字元的次數！
- example 1:
    - input : "aabbcccdd"
    - output: "{a:2,b:2,c:3,d:2}"
- example 2:
    - input : "qqddcc"
    - output: "{q:2,d:2,c:2}"

'''

list_3 = "aabbccddeee"
repeat = []
for i in list_3:
    a = list_3.count(i, len(list_3))
    if a > 1 and i not in repeat:
        repeat.appent(i)
import re
for j in repeat:
    print(len(re.findall(j,repeat)))