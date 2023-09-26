############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
import art
from replit import clear

# print logo
print(art.logo)
print()
print()

# start program
playgame = input("Would you like to play a game of Black Jack? Type 'y' or 'n': ")

if playgame == "y":
  playing = True
else:
  playing = False
  
while playing:
  # create list to hold cards
  player = []
  dealer = []
  
  # deal cards
  def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(card)
  
  #check for blackjack function
  def has_blackjack(score):
    if score == 21:
      return True
  
  # Deal initial cards
  for i in range(2):
    player.append(deal_card()) 
    dealer.append(deal_card())

  def calculate_score(card):
    return sum(card)
    
  # print score function
  def show_score():
    print()
    print(f"Your cards: {player}, current score: {calculate_score(player)}")
    print(f"Dealers first card: {dealer[0]}")
  
  # print final score function
  def show_final_score():
    print()
    print(f"Your final cards: {player}, final score: {calculate_score(player)}")
    print(f"Dealers finals cards: {dealer}, final score: {calculate_score(dealer)}")
  
  show_score()
  
  if has_blackjack(calculate_score(dealer)):
    print("Dealer has Blackjack!  You lose.")
    continue
    
  if has_blackjack(calculate_score(player)):
    print("Player has Blackjack!  You Win.")
    continue
    
  # Player workflow
  play_more = True
  while play_more:
    player_one_more = input("Type 'y' to get another card, type 'n' to pass: ")
    if player_one_more == "y":
      player.append(deal_card())
      if player[-1] == 11 and calculate_score(player) > 21:
        player[-1] = 1
      show_score()
    else:
      play_more = False
  
  # Dealer workflow
  while sum(dealer) < 17:
    dealer.append(deal_card())
    if dealer[-1] == 11 and calculate_score(dealer) > 21:
      dealer[-1] = 1
      show_score()
      
  show_final_score()  
  
  if calculate_score(player) == 21:    
    print("Player has Blackjack! You win.")
  elif calculate_score(dealer) == 21:
    print("Dealer has Blackjack! You lose.")
  elif calculate_score(player) > 21:
    print("Player went over 21 You lose.")  
  elif calculate_score(dealer) > 21:
    print("Dealer went over. Player wins!")
  elif calculate_score(dealer) == calculate_score(player):
    print("The game has ended in a draw.")
  elif calculate_score(dealer) > calculate_score(player):
    print("The Dealer has high score. You lose!")
  else:
    print("Player has high score. You win!")

  playgame = input("\nWould you like to play a game of Black Jack again? Type 'y' or 'n': ")
  if playgame != "y":
    playing = False
