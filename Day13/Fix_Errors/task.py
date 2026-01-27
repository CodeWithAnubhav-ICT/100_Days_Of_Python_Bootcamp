# age = int(input("How old are you?"))
# if age > 18:                              Bugged and risky code
# print("You can drive at age {age}.")

try:
    age = int(input("How old are you?"))  # Debugged and less
                                          # error prone code
except ValueError:
    print("Please enter a numeric value. eg: 15")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
