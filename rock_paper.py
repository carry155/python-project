import random

item_list = ["paper", "sciersor", "rock"]

com_choice = random.choice(item_list)

user_choice=input("enter your move (paper sciersor rock) = ")

print(f" user choice = {user_choice} \n computer choice = {com_choice}")

if com_choice == user_choice:
    print("match was = tie")

elif user_choice == "paper":
    if com_choice == "rock":
        print("paper cover = you win")
    else:
        print("sciersor cut paper = computer win")

elif user_choice == "rock":
    if com_choice == "paper":
        print("paper cover = computer win")
    else:
        print("rock smash sciersor = you win")

elif user_choice == "sciersor":
    if com_choice == "rock":
        print("rock samsh sciersor = computer win")
    else:
        print("sciersor cut the paper = you win")
 
    


