#Importing Random Module
import random

game = ["R", "P", "S"]
diction = {"R": "Rock", "P": "Paper", "S": "Scissors"}

computer_choice = random.choice(game)

play_game = True

while play_game:
  user_choice = input("Choose your option R - Rock, P - Paper or S - Scissors: ").capitalize()

  try:
    print("Player({}) : CPU({})".format(diction[user_choice], diction[computer_choice]))

    if user_choice == computer_choice:
      print("Lets go again")
      continue
    elif (user_choice == "P" and computer_choice == "R"):
      print("You Win!!!")
    elif (user_choice == "S" and computer_choice == "P"):
      print("You Win!!!")
    elif (user_choice == "R" and computer_choice == "S"):
      print("You Win!!!")
    else:
      print("You Loose!")
  except:
    print("Wrong Option")
    continue

  play_game = False
