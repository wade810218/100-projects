import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(300, random.randrange(-300, 300))
        self.drive()
    
    def drive(self):
        self.forward(STARTING_MOVE_DISTANCE)

    # def speedup(self):

    #     return STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    #it's global variable not suggest uset it in local score, try to use return method
