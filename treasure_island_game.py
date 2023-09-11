print('''

       ________   ________    _________  ____________;_
      - ______ \ - ______ \ / _____   //.  .  ._______/
     / /     / // /     / //_/     / // ___   /
    / /     / // /     / /       .-'//_/|_/,-'
   / /     / // /     / /     .-'.-'
  / /     / // /     / /     / /
 / /     / // /     / /     / /
/ /_____/ // /_____/ /     / /
\________- \________-     /_/
''')

print()
print()

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice = input("You\'re at a cross road. Where do you want to go? Type 'left' or 'right' \n\n")

if choice.lower() == "left":
  choice = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n\n")
  if choice.lower() == "wait":
    choice = input("You arrive at the island unharmed. There is a house with 3 doors. One 'red', one 'yellow' and one 'blue'. Which color do you choose? \n\n")
    if choice.lower() == "red":
      print("Burned by fire. Game Over.")
    elif choice.lower() == "blue":
      print("Eaten by beasts. Game Over.")
    elif choice.lower() == "yellow":
      print("You Win!")
    else:
      print("Game Over.")
  else:
    print("Attacked by trout. Game Over.")
else:
  print("Fall into a hole. Game Over.")
