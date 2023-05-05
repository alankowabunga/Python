'''
年利率2%, 計算6年後之金額
6年後存款 = 本金*(1+年利率)**6

i *= x 即為 i = i*x

'''

deposit = int(input("請輸入本金:"))
rate = (1 + 0.02)**6
deposit *= rate
print("6年後的金額為{0:5.2f}:".format(deposit))