print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at the forgotten crossroads")
print("You hear splashing sound on left and breezing grasses on right")
choice1 = input("Which direction would you like to go?(Left or Right) : ")
if choice1.upper() == "LEFT" or choice1.upper() == "L":
    print("You reach at the seashore and can see an island")
    print("You see no means to go to the island")
    choice2 = input("What would you do?(swim or wait) : ")
    if choice2.upper() == "WAIT" or choice2.upper() == "W":
        print("A boat passed by and they helped you to reach the island")
        print("You see 3 coloured houses on the island.")
        choice3 = input("Which house would you go to?(Red , Blue or Yellow) : ")
        if choice3.upper() == "YELLOW" or choice3.upper() == "Y":
            print("Congratulations! You found the treasure!")
            print(r'''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
            |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
            ''')
            print("You Won !!!")
        elif choice3.upper() == "RED" or choice3.upper() == "R":
            print("You got killed by a man sacrificing cult")
            print("Game Over")
        elif choice3.upper() == "BLUE" or choice3.upper() == "B":
            print("You again teleported to forgotten crossroads and are stuck in the loop forever")
            print("Game Over")
        else :
            print("Please enter a valid choice")
    elif choice2.upper() == "SWIM" or choice2.upper() == "S":
        print("You got eaten by sharks")
        print("Game Over")
    else:
        print("Please enter a valid choice")
elif choice1.upper() == "RIGHT" or choice1.upper() == "R":
    print("You fell into a deep trench")
    print("Game Over")
else :
    print("Please enter a valid direction")