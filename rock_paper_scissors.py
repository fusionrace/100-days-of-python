rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

print("Welcome to Rock, Paper Scissors!!")
print("")
print("")
print("Ready...")

# capture player1 choice
player1 = (input("Input you choice: 'Rock', 'Paper' or 'Scissors'\n->")).lower()
print("")

if player1 == "rock":
  print(rock)
elif player1 == "scissors":
  print(scissors)
elif player1 == "paper":
  print(paper)
else:
  print("You selected and invlaid choice")
  
print("")
print("Computer chose:")
print("")

# choices
hands = ['rock', 'paper', 'scissors']

# computer randomly selects its choice
computer = random.choice(hands)

if computer == "rock":
  print(rock)
elif computer == "scissors":
  print(scissors)
else:
  print(paper)


# shorcut to draw
if player1 == computer:
  print("The game is a draw.")
# check if player 1 won
elif (player1 == "rock" and computer == "scissors") or (player1 == "scissors" and computer == "paper") or (player1 == "paper" and computer == "rock"):
  print("Player 1 wins!!!")
# if player one did not win, then the computer must have
else:
  print("The computer wins!!!")
