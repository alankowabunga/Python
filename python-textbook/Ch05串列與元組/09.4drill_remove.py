# favorite colors = "red" , "blue" , "green"

colors = ["red" , "purple" , "yellow" , "black" , "blue" , "brown" , "green"]

while True:
    print("the ink we have is:", colors)
    dislike = input("Enter the colors you don't like(Press Enter to run):")

    if dislike == "":
        break

    n = colors.count(dislike)
    if n > 0:
        colors.remove(dislike)
        print("Final list is:{}".format(colors))
    
    else:
        print(dislike , "we don't have it.")

