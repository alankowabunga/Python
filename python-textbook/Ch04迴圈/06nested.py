'''
巢狀for迴圈 ,做出高度5層的 [ #字直角三角形 ]
'''

for i in range( 1 , 6 ):
    print(" No.{} outer loop , runnung {} time(s) inner loop:".format(i , i) , end = "")
    for j in range( 1 , i + 1 ): #因為結束值又會再-1 , 因此要加回來
        print("#" , end = "")
    
    print()    
    