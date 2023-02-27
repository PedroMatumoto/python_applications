import random

print("Welcome to Jokempo!")

player = input("Choose your hand: Rock, papers or scissors\n")
random=random.randint(0, 2)

#0=scissor
#1=rock
#2=papers

if (random==0):
    print("Computer choice: Scissors")
elif (random==1):
    print("Computer choice: Rock")
elif (random == 2):
    print("Computer choice: Papers")



if (player=='Rock' and random==0):
    print("You win!")
elif (player == 'Rock' and random == 1):
    print("Tie")
elif (player == 'Rock' and random == 2):
    print("You lose!")

if (player == 'papers' and random == 0):
    print("You lose!")
elif (player == 'papers' and random == 1):
    print("You win!")
elif (player == 'papers' and random == 2):
    print("Tie!")

if (player == 'scissors' and random == 0):
    print("Tie!")
elif (player == 'scissors' and random == 1):
    print("You lose!")
elif (player == 'scissors' and random == 2):
    print("You win!")

    
