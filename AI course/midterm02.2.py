'''
### 題目2.
- 給定三個邊長，判斷是否能成為一個三角形，題目會給一個list，list內會含多個list，每個小list內含有三個數字，即三角形的三個邊長，請幫忙檢查每個list內的三邊長能否構成一個三角形，可以的話請回傳True，不行的請回傳False。
- example 1:
    - input : [ [1,2,3], [3,4,5], [5,12,13], [0,2,3] ]
    - output: [ False, True, True, False]
'''

#直角三角形條件: a*a + b*b = c*c

  
list_2 = [ [1,2,3], [6,5,4], [8,7,9], [0,2,3] ]
for i in list_2:
    inlist = sorted(list_2[i])
    if inlist[0]**2 + inlist[1]**2 == inlist[2]**2:
        print("true")
    else:
        print("False")


# inlist[0]**2 + inlist[1]**2 == inlist[2]**2