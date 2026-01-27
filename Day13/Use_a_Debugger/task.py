import random
import maths


# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2                   Bugged Code
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)

"""
Debuggers allows us to peek into our code during execution
and pause on chosen lines to figure out what is the inner mechanism
and where it's going wrong.
Options in Debuggers :
Breakpoint
Step Over
Step Into
Step Into My Code
"""

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2                   # Debugged code
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
