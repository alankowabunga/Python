'''
Odd and even number differentiator: Ask user to input an integer.
Tell the user if the number is odd or even.
'''

num = input("Enter an integer:")

if int(num) %2 == 0:
    print("It's even number")
else:
    print("It's odd number")