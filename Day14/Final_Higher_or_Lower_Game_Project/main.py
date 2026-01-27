#Importing necessary modules and data
import random
from game_data import data
from art import logo,vs

def game():
    """Starts the game"""
    def compare(choice):
        """Checking if the choice was correct or not"""
        if choice == "a":
            result = a_data["follower_count"] > b_data["follower_count"]
        elif choice == "b":
            result = a_data["follower_count"] < b_data["follower_count"]
        else:
            result = None
        return result

    user_score = 0
    a_data = {"follower_count" : 0}
    b_data = {"follower_count" : 0}
    game_over = False
    while a_data["follower_count"] == b_data["follower_count"]:
        #Loops to avoid same values randomly
        a_data = random.choice(data)
        b_data = random.choice(data)

    while not game_over:
        #Loops the game until game over
        print(logo)
        a_list = [a_data["name"] , a_data["description"] , a_data["country"] , a_data["follower_count"]]
        b_list = [b_data["name"] , b_data["description"] , b_data["country"] , b_data["follower_count"]]
        print(f"Compare A: {a_list[0]}, a {a_list[1]}, from {a_list[2]}")
        print(vs)
        print(f"Against B: {b_list[0]}, a {b_list[1]}, from {b_list[2]}")
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        user_result = compare(user_input)
        if user_result:
            user_score += 1
            a_data = b_data
            while a_data["follower_count"]==b_data["follower_count"]:
                b_data = random.choice(data)
            print("\n" *10)
            print("You're right!, Current score: ",user_score)
            print(f"{a_list[0]} has {a_list[3]} million followers vs {b_list[0]} has {b_list[3]} million followers")
        elif not user_result:
            print("Sorry, that's wrong, Final score: ", user_score)
            print(f"{a_list[0]} has {a_list[3]} million followers vs {b_list[0]} has {b_list[3]} million followers")
            game_over = True
            retry = input("Would you like to try again? (Retry: y / Quit: any other key): ").lower()
            if retry == "y":
                print("\n" * 10)
                game()
        else :
            print("Please enter either 'a' or 'b'!!!")
game()