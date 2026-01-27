from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)                              Bugged code
# print(dice_images[dice_num])

"""The bug was the incorrect randint range
 as it will give out of list index"""

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]         #Debugged code
dice_num = randint(0, 5)
print(dice_images[dice_num])


