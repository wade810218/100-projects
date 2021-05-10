import turtle
import pandas as pd

data = pd.read_csv('50_states.csv', index_col = 'state')

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#3. Write correct guesses on to the map
def write_state(name):
    x, y = data.loc[name]
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()  
    pen.goto(x, y)
    pen.write(name)
    

#5. Record the correct guesses in a list
guessed_states = []

#4. Use a loop to allow the user to keep guessing
while True:
    #1. Convert the guess to Title classmethod
    #6. Keep track of the score
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    #2. Check if the guess is among the 50 states
    if answer_state in data.index:
        write_state(answer_state)
        guessed_states.append(answer_state)
        

print(turtle.position())
turtle.goto(25,10)
for name in data.index:
    write_state(name)
print(turtle.position())


