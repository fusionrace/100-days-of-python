#higher-lower game
import random
from game_data import data
from art import logo, vs
from replit import clear 

def format_data(account):
  """Format the account data into printable format"""
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
  """Take the users guess and follower counts and return if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == 'b'

# display art

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
  print(logo)
  # Generate a random account from the game data
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  # Start game
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  # Ask user to guess
  guess = input("Who has more followers, 'A' or 'B': '").lower()

  # Check if the user had the correct answer
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']

  is_correct = check_answer(guess, a_follower_count,b_follower_count)

  clear()
  print(logo)

  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}\n")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")
