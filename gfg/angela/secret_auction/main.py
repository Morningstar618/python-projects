import subprocess
from art import logo

data_dict = {}
print(logo)
print("Welcome to the Secret Auction!")

while True:
    print("What is your name?: ", end='')
    name = input()
    print("What's your bid?: $", end='')
    bid = int(input())
    data_dict[name] = bid
    print("Are there any other bidders? Type 'yes' or 'no'.")
    other_bidders = input()
    if other_bidders == 'yes':
        subprocess.run('clear', shell=True)
        continue
    else:
        subprocess.run('clear', shell=True)
        break

highest_bidder = None
highest_bid_value = 0
for key in data_dict:
    if data_dict[key] > highest_bid_value:
        highest_bid_value = data_dict[key]
        highest_bidder = key

count = 0
for key in data_dict:
    if highest_bid_value == data_dict[key]:
        count += 1
if count == 2:
    print("Two or more than two people have entered the same highest bid value. Try again!")
else:
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid_value}")

