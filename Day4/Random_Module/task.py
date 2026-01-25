import random

import my_module

random_integer = random.randint(1, 10)
random_float = random.random()  # 0 <= Generates random no. < 1
random_floating = random.uniform(1, 10)  # Generates floating point no. with a and b inclusive
print(random_integer)
print(random_float)
print(random_floating)
print(my_module.my_favourite_number)

print("Welcome to coin toss")
# L = ["Heads", "Tails"]
# print(random.choice(L))

randomNumber = random.randint(0,1)
if randomNumber == 0:
    print("Heads")
else:
    print("Tails")
