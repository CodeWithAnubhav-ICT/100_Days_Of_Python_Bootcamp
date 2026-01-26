import random
from art import logo

print(logo)
print("\nWelcome to The Number Guessing Game")
print("I am thinking of a number between 1 to 100")
game_over = False

def guess(chances):
    random_number = random.randint(1, 100)
    while chances > 0:
        print(f"You have {chances} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))
        if user_guess == random_number:
            print(f"You got it! The answer was {random_number}")
            return None
        elif user_guess > random_number:
            print("Too high")
            print("Guess again")
            chances -= 1
        else:
            print("Too low")
            print("Guess again")
            chances -= 1
    print("You ran out of guesses")
    print(f"The number I was thinking of was: {random_number}")
    return None

while not game_over:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        guess(10)
    elif difficulty == "hard":
        guess(5)
    else:
        print("Enter a valid difficulty")
    retry = input("Do you want to try again? Type 'yes' or 'any other key to end': ").lower()
    if retry != "yes":
        game_over = True

print("Game Over !!!")
