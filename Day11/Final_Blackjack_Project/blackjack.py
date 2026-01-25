import random
from art import logo

def draw(card_list):
    """appends a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_card = random.choice(cards)
    card_list.append(drawn_card)
    return card_list

def add(card_list):
    """sums the value of all the cards"""
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    value = sum(card_list)
    return value

def hit(game):
    """checks if the player went over or not after Hitting"""
    draw(user_cards)
    print(f"Your final hand : {user_cards}, Current score : {add(user_cards)} ")
    print(f"Computer's first card : {dealer_cards[0]}")
    if add(user_cards) > 21:
        print("You went over, You lose!!!")
        game = True
    return game

def stand():
    """calculates the result of the game"""
    print(f"Your final hand : {user_cards}, Final score : {add(user_cards)} ")
    while add(dealer_cards) < 17:
        draw(dealer_cards)
    print(f"Computer's final hand: {dealer_cards}, Final score : {add(dealer_cards)}")
    if add(dealer_cards) > 21:
        print("Computer went over, You win!!!")
    elif add(dealer_cards) < add(user_cards):
        print("You won!!!")
    elif add(dealer_cards) == add(user_cards):
        print("Push !!! Its a draw...")
    else:
        print("You lose!!!")

#_main_
want = True
while want:
    user_cards = []
    dealer_cards = []
    game_over = False
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if start == 'y':
        print(logo)
        for i in range(2):
            user_cards = draw(user_cards)
            dealer_cards = draw(dealer_cards)
        print(f"Your cards : {user_cards},current score : {add(user_cards)} ")
        print(f"Computer's first card : {dealer_cards[0]}")

        if add(user_cards) == 21:                     # BlackJack
            if add(dealer_cards) == 21:
                print(f"Computer's cards : {dealer_cards}, current score : {add(dealer_cards)}")
                print("Push !!! Its a draw...")
            else :
                print("Blackjack!!! You win!!!")

        else :
            while game_over == False :
                choice = input("Type 'y' to get another card, type 'n' to pass : ")

                if choice == 'n':                     # Stand
                    stand()
                    game_over = True
                elif choice == 'y':                   # Hit
                    game_over = hit(game_over)
                else :
                    print("Please type 'y' or 'n'")
        print("\n" * 5)
    elif start == 'n':
        print("Game Over!!!")
        want = False
    else :
        print("Please type 'y' or 'n'")
