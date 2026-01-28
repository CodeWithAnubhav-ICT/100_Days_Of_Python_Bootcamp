from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo,title

# Object of Menu
drinks = Menu()
# Object of CoffeeMaker
machine = CoffeeMaker()
# Object of MoneyMachine
transaction = MoneyMachine()
print(title)
print(logo)
machine_on = True
while machine_on:

    user_drink = input(f"What would you like? ({drinks.get_items()}) : ").lower()

    if user_drink == "report":
        machine.report()
        transaction.report()

    elif user_drink == "refill":
        machine = CoffeeMaker()
        print("Coffee Machine fully refilled!")

    elif user_drink == "off":
        machine_on = False
        print("Thank you for using our Coffee Machine")

    else:
        drink = drinks.find_drink(user_drink)
        sufficient = machine.is_resource_sufficient(drink)

        if sufficient:
            success = transaction.make_payment(drink.cost)

            if success:
                machine.make_coffee(drink)
                print(title)
                print(logo)
