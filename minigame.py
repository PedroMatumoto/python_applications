print("Welcome to Treasure Island!")
print("Yous mission is to find treasure.")
path=input("Your're at a cross road. Where to you want to go? Type 'left' or 'right'\n")
if (path == 'right'):
    print("You found a orc. GAME OVER!")
elif(path=='left'):
    swin=input("You come to a lake. There is a island in te middle of the lake. Wait or Swin across? \n")
    if (swin=='swin'):
        print("Your breath runs out before you achieve the island. GAME OVER")
    elif(swin=='wait'):
        color=input("Your arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if (color=='red'):
            print("Shadows consume everthing. GAME OVER!")
        elif(color=='yellow'):
            print(" You found a chest. Congrats!")
        elif(color=='blue'):
            print("You fall to your death . GAME OVER!")
        
