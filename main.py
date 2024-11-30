import art
print(art.logo)

# TODO-1: Ask the user for input

continue_bid = True
bid_dict = {}

while continue_bid:
    name = input("What is your name? ")
    price = float(input("What is your bid? $"))

# TODO-2: Save data into dictionary {name: price}
    bid_dict[name] = price

# TODO-3: Whether if new bids need to be added
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    if other_bidders == 'yes':
        continue_bid = True
        print("\n" * 20)
    else:
        continue_bid = False

# TODO-4: Compare bids in dictionary

print(bid_dict)
winner = max(bid_dict)
win_price = bid_dict[winner]

print(f"The winner is {winner} with a bid of ${win_price}")