from game_data import data
from art import logo, vs
from replit import clear
import random

def select():
    """Get a random account"""
    dic = random.choice(data)
    return dic 


def format_data(account):
    """Takes the account data and returns the printable formate.  """
    return f"{account['name']}, a {account['description']}, from {account['country']}."


def high_lower(a, b):    
    """Ask user to guess  and return if they got it right."""
    comparison = a['follower_count'] > b['follower_count']
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if comparison == True: 
        return guess == 'a'
        
    elif comparison  == False: 
        return guess == 'b'        
      

score = 0
stop = False

dict_A = select()

while not stop:
    clear()

    dict_B = select()
    while dict_B == dict_A:
      dict_B = select()

    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")  
    print(f"compare A: {format_data(dict_A)}")
    print(vs)  
    print(f"Against B: {format_data(dict_B)}")
   
    if high_lower(dict_A, dict_B):
        score += 1
        dict_A = dict_B
    else:
        stop = True
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")     
   





