"""This is data for the program"""
from art import logo,title
print(title)
print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# __Functions__
# TODO 4 : Checks the resources to find if the order can be made
def check_resource(entry):
    """Check if resource is available or not"""
    if resources["water"] >= MENU[entry]["ingredients"]["water"] :
        if resources["milk"] >= MENU[entry]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[entry]["ingredients"]["coffee"]:
                return True
            else:
                return "Sorry, you don't have enough coffee🌱"
        else:
            return "Sorry, you don't have enough milk🥛"
    else:
        return "Sorry, you are not enough water💧"
# TODO 5 : Ask the user for coins and calculate it
def process_coins():
    """Process coins and calculates user_money"""
    print("Please insert coins🪙")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
# TODO 6 : Check if the transaction is possible and complete it if possible and update resources
def check_transaction(entry , money):
    """Process transactions if user_money is greater than cost and refunds the change"""
    if money >= MENU[entry]["cost"]:
        refund = money - MENU[entry]["cost"]
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        return True,refund
    else:
        return False,money

# __main__
machine_on = True
profit = 0
# TODO 1 : Make the machine running asking user_input again and again until off
while machine_on:
    user_input = input("What would you like? (espresso - $1.5/latte - $2.5/cappuccino - $3.0): ").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        availability = check_resource(user_input)
        if availability == True:
            user_money = process_coins()
            enough = check_transaction(user_input, user_money)
            # TODO 7 : Give the user his order if transaction is complete
            if enough[0] :
                profit += user_money - enough[1]
                print("\n"*4)
                print(title)
                print(logo)
                if enough[1] > 0:
                    print(f"Here is ${round(enough[1],2)} dollars💵 in change")
                print(f"Here is your {user_input}☕. Enjoy!😁")
            else :
                print("Sorry that's not enough money. Money refunded:$",round(enough[1],2),"💵")
        else :
            print(availability)
    # TODO 3 : Give the report of all the resources and profit of the machine
    elif user_input == "report" :
        for key in resources:
            print(f"{key}: {resources[key]}")
        print("Profit:$",profit)
    # TODO 2 : Make the machine off by user input
    elif user_input == "off" :
        machine_on = False
        print("Machine off")
    elif user_input == "refill" :
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        print("Coffee Machine fully refilled💯")
    elif user_input == "clear" :
        profit = 0
        print("Transactions cleared0️⃣")
    else:
        print("❌Please enter a valid input")
