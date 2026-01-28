# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name" , ["Pikachu" , "Squirtle" , "Charmander"])
table.add_column("Type" , ["Electric" , "Water" , "Fire"])
table.align = "l"
table.border = True
table.vertical_char = "$"
table.horizontal_char = "+"
print(table)