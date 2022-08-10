import turtle
import pandas as pd

data = pd.read_csv('50_states.csv', index_col = 'state')

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Write correct guesses on to the map
def write_state(name):
    x, y = data.loc[name]
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()  
    pen.goto(x, y)
    pen.write(name)    

# Record the correct guesses in a list
guessed_states = []

# Use a loop to allow the user to keep guessing
while True:
    # Convert the guess to Title classmethod
    # Keep track of the score
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == 'Exit':
#         missing_states = []
#         for state in data.index:
#             if state not in guessed_states:
#                 missing_states.append(state)
        missing_states = [state for state in data.index if state not in guessed_states ]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")        
        break

    # Check if the guess is among the 50 states
    if answer_state in data.index:
        write_state(answer_state)
        guessed_states.append(answer_state)


