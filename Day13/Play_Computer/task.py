year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")                  Bugged code
# elif year > 1994:
#     print("You are a Gen Z.")

"""The bug was that year 1994 was not coming
 in any conditional statements"""

if year > 1980 and year <= 1994:
    print("You are a millennial.")                    #Debugged code
elif year > 1994:
    print("You are a Gen Z.")
