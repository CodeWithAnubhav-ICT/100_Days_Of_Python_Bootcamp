# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)
print("Welcome to the Blind auction project.")
players = True
auction_data = {}
highest_bidder = ""
highest_bid = 0
while players :
    bidder = input("What's the name of the bidder? : ")
    bid = int(input("What's the bid? : "))
    auction_data[bidder] = bid
    bidders = input("Are there any other bidders? (yes/no) : ").lower()
    if bidders == "yes" :
        print("\n" * 25)
    else:
        players = False
        for key in auction_data :
            if auction_data[key] > 0 :
                highest_bid = auction_data[key]
                highest_bidder = key
print("\n" * 5)
print(f"The highest bidder is {highest_bidder} with bids ${highest_bid}")