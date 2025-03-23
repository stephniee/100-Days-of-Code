from art import logo

bidders_dictionary = {}
print(logo)

name = input("What is your name? ")
bid = int(input("What is your bid? "))
choice = input("Are there any other bidders? Type 'yes' or 'no'. ")
bidders_dictionary[name] = bid

while choice == 'yes':
    print('\n' * 20)
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bidders_dictionary[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'. ")

# Get the highest bidder

winner_key = max(bidders_dictionary,key=bidders_dictionary.get)
winner_value = max(bidders_dictionary.values())
print(f'The winner is {winner_key} with a bid of {winner_value}')



