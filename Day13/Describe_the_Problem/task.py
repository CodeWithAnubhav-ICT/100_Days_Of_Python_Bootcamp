# def my_function():
#     for i in range(1, 20):                    Bugged code
#         if i == 20:
#             print("You got it")

"""The bug was it assumes that 'i' will be equal to 20
 when 'i' never equals to 20 because the end of range
  function is never counted"""

def my_function():
    for i in range(1, 21):                     #Debugged code
        if i == 20:
            print("You got it")

my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?
