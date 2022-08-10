from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

auction = {}
bidding_finished = False

while not bidding_finished:
  name = input("What is your name?: ")
  bid =  int(input("What's your bid?: $"))
  auction[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  clear()
  if should_continue == "no":
    bidding_finished = True

highest = 0
winner = ""

for bidder in auction: 
  if auction[bidder] > highest:
    highest = auction[bidder]
    winner = bidder
    
print(f"The winner is {winner} with a bid of ${highest}.")
