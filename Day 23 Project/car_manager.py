import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:            
            new_car = Turtle('square')
            new_car.shapesize( stretch_len =2, stretch_wid=1 )
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randrange(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
            

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    # def drive(self):
    #     self.forward(STARTING_MOVE_DISTANCE)

    def speedup(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    #  return STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    #it's global variable not suggest uset it in local score, try to use return method
