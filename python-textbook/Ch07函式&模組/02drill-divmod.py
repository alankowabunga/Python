'''

input ppl. & apples' number
allocate evenly to each person, and display how many apples for each person and the remained apple.

'''

ppl = int(input("Enter the ppl's number:"))
apple = int(input("Enter the quantity of apple:"))

if ppl > apple:
    print("Not enough apple for each person")
else:
    ret = divmod(apple,ppl) #(商,餘)
    print("Each ppl get {}".format(ret[0]))
    print("And the apple remained is {}".format(ret[1]))