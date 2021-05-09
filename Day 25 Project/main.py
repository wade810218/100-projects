import turtle
import pandas as pd

data = pd.read_csv('50_states.csv',index_col = 'state')

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

turtle_pen = turtle.Turtle()
turtle_pen.penup()


#2. Check if the guess is among the 50 states
def check_guess(state):
    if state in data.index:
        return True
    else:
        return False
       

#3. Write correct guesses on to the map
def write_state(name):
    x, y = data.loc[name]
    turtle_pen.goto(x, y)
    turtle_pen.write(name)
    

#5. Record the correct guesses in a list


#6. Keep track of the score
score = 0
correct_guess = []
title = 'Guess the State'

#4. Use a loop to allow the user to keep guessing
# while True:

#     if score > 0:
#         title = f"{score}/50 States Correct"

# #1. Convert the guess to Title classmethod
#     answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
      
#     if check_guess(answer_state):
#         score +=1 
#         write_state(answer_state)
#         correct_guess.append(answer_state)
        

print(turtle.position())
turtle.goto(25,10)
for name in data.index:
    write_state(name)
print(turtle.position())


