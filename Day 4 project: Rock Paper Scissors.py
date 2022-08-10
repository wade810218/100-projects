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

import random

choice = [rock, paper, scissors]

player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if (player >2) or (player <0):
  print("You type invalid number, you lose! ")
else:  
  print(choice[player])

  computer = random.randint(0,2)
  print(f"Computer chose: \n{choice[computer]}")


  if player == computer:
    print("It's a draw")
    
  elif player == 0:
    if computer  == 1:
      print("You Lose")
    else:
    # elif computer == 2:
      print("You Win")  
  elif player == 1:
    if computer  == 0:
      print("You Win")
    # elif computer == 2:
    else:
      print("You Lose")
  elif player == 2:
    if  player == 0:
      print("You Lose")
    else:
      print("You Lose")


 
