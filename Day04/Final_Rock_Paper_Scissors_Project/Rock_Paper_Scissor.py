import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choice = [rock, paper, scissors]
bot_choice = random.randint(0, 2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
if 0<= user_choice <3 :
    print("User Choice : \n" , game_choice[user_choice])
    print("Bot Choice : \n" , game_choice[bot_choice])

if user_choice <0 or user_choice >= 3 :
    print("Invalid choice entered")
elif user_choice == bot_choice :
    print("Match Draw")
elif user_choice == 0 :
    if bot_choice == 1 :
        print("You Lose")
    else :
        print("You Win")
elif user_choice == 1 :
    if bot_choice == 0 :
        print("You Win")
    else :
        print("You Lose")
else:
    if bot_choice == 0 :
        print("You Lose")
    else :
        print("You Win")

# if user_choice == "r":
#     print("Your choice : \n" , rock)
# elif user_choice == "p":
#     print("Your choice : \n" , paper)
# else :
#     print("Your choice : \n" , scissors)
#
# if bot_choice == "r":
#     print("Bot choice : \n" , rock)
# elif bot_choice == "p":
#     print("Bot choice : \n" , paper)
# else :
#     print("Bot choice : \n" , scissors)
#
# if user_choice == "r":
#     if bot_choice == "r":
#         print("Match Draw")
#     elif bot_choice == "p":
#         print("You Lose :(")
#     else :
#         print("You Win !!! :)")
#
# elif user_choice == "p":
#     if bot_choice == "r":
#         print("You Win !!! :)")
#     elif bot_choice == "p":
#         print("Match Draw")
#     else:
#         print("You Lose :(")
#
# elif user_choice == "s":
#     if bot_choice == "r":
#         print("You Lose :(")
#     elif bot_choice == "p":
#         print("You Win !!! :)")
#     else :
#         print("Match draw")
#
# else :
#     print("Invalid Choice entered")
