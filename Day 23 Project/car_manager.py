import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

        self.shape('square')
        self.shapesize(stretch_len =2, stretch_wid=1 )
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)        
        self.goto(300, random.randrange(-250, 250))

        self.drive()

    def creat_car(self):
        self.CarManager()

    def drive(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def speedup(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    #  return STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    #it's global variable not suggest uset it in local score, try to use return method
