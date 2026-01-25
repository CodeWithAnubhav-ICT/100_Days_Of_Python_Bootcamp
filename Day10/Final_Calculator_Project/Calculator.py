from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2==0:
        return "Error !!! <Cannot divide by zero>"
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

first_number = float(input("Enter the first number : "))
while True:
    operator = input("Enter the operator (+ , - , * , /) : ")
    second_number = float(input("Enter the second number : "))
    result = operation[operator](first_number, second_number)
    print(f"The result of {first_number} {operator} {second_number} = {result}")
    choice = input("Do you want to calculate using result"
                   " or start a new calculation"
                   " or end the calculator? (y/n/any_key): ")
    if choice == "n":
        print("\n" * 25)
        print(logo)
        first_number = float(input("Enter a number: "))
    elif choice == "y":
        first_number = result
    else :
        print("Sayonara !!!")
        break

# you can also do this by recurssion in function  see soln
