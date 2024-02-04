# Secret Bidding Auction

from art import logo

# Print Logo
print(logo)
print('Welcome to the secret auction program.')

bidders = {}
no_bidder = False


def add_bidder(bidder_name, bidder_amt):
    bidders[bidder_name] = bidder_amt


def check_highest_bidder(bidders):
    highest = 0
    winner = ""
    for value in bidders:
        if bidders[value] > highest:
            highest = bidders[value]
            winner = value

    print(f"The winner is {winner} with a bid of ${highest}")


while not no_bidder:
    name = input('What is your name?: ')
    amount = int(input("What's your bid?: $"))

    add_bidder(name, amount)

    choice = input("Are there any other bidders? Type 'yes' or 'no'.")
    if choice == "no":
        check_highest_bidder(bidders)
        no_bidder = True