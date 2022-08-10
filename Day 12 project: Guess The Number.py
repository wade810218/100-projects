import random
from art import logo 

print(logo)
print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == 'easy':  
  attempt = 10
elif level == 'hard':
  attempt = 5
  
answer=random.randint(1,100)

while  attempt > 0:
  print(f"You have {attempt} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if  answer == guess:
    print(f'You got it! The answer was {answer}.')
    attempt = 0
  elif answer > guess:
    print('Guess again')
    print('Too low.')
    attempt -= 1
  elif answer < guess:
    print('Too high.')
    attempt -= 1

if  answer != guess:
  print("You've run out of guesses, you lose.")
