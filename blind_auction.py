from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
print()
# welcome statement
print("Welcome to the secret auction program.")

more_bids = True

# dictionary to capture bids
bids = {}

while more_bids:
  # ask for for the name of the bidder
  name = input("What is your name?:  ")
  print()
  
  # ask what there bid amount is
  bid = input("What's your bid?:  ")
  bids[name] = {"bid": bid}
  
  # ask if there are any bids
  ask_more_bids = input("Are there any other bidders? Type 'yes' or 'no':  ").lower()
  if ask_more_bids == "no":
    more_bids = False
  else:
    clear()
  
# start logic

winner = (max(bids))
winning_bid = bids[winner]["bid"]
print()
print(f"The winner is {winner} with a bid of {winning_bid}")
