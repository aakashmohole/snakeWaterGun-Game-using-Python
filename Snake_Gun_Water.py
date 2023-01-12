# import random
# list = [1,2,3,5,4,9]
# a=random.choice(list)
# print(a)

# """Start Here"""

# from cmath import e
# import random
# from ssl import Options
# print("Snake - Water - Gun")

# #variable declaration
# # n=int(input("Enter the number of rounds you want to play:"))
# n=3
# option= ['s','w','g']

# rounds=1

# com_w=0
# ply_w=0

# #main manu
# while rounds <= n:
#     print(f"Round : {rounds} \nSnake- 's' \nWater- 'w' \nGun- 'g'")
#     player = input("Enter Your Choice: ")

#     if player != 's' and player!='w' and player!='g':
#         print("Invalid Choice..!")
#         continue

# #Random Pakage use
# computer= random.choice(Options)

# #Logic devlopment
# if computer=='s':
#     if player=='w':
#         com_w += 1
#     elif player=='g':
#         ply_w += 1

# elif computer=='w':
#     if player=='g':
#         com_w += 1
#     elif player=='s':
#         ply_w += 1

# elif computer=='g':
#     if player=='s':
#         com_w +=1
#     elif player=='w':
#         ply_w +=1

# #winner of Every Round
# if ply_w>com_w:
#     print(f"You Won Round {rounds} \n")
# elif com_w>ply_w:
#     print(f"Computer Won Round {rounds}\n")
# else:
#     print("Match Draw !!\n")
#     rounds += 1

# #final Winner
# if ply_w>com_w:
#     print("Congratulations...! You Won")
# elif com_w>ply_w:
#     print("You Lose..!!")
# else:
#     print("Match Draw...!")




# Snake water gun

import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0
print("------------------------------------\n")
print("_ Snake,Water,Gun Game _ \n")
print("------------------------------------\n")

# print("Snake- 's' \nWater- 'w' \nGun- 'g'\n")

# making the game in while
while no_of_chance < chance:
    print("Snake- 's' \nWater- 'w' \nGun- 'g'\n")
    _input = input('Enter Your Chocie:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")

#
# Snake Water Gun Game in Python
# The snake drinks the water, the gun shoots the snake, and gun has no effect on water.
#