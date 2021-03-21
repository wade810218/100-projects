import colorgram

colors = colorgram.extract('image.jpg', 30)
rgb_colors = []
for color in colors:
    rgb_colors.append(tuple(color.rgb))

print(rgb_colors)

color_list = [  (189, 17, 44), (243, 232, 65), (252, 236, 241), (212, 236, 243), (197, 74, 31), (220, 65, 106), (196, 175, 16), (16, 124, 174), (107, 182, 209), (11, 143, 88), (11, 167, 215), (241, 232, 2), (210, 152, 95), (23, 39, 77), (188, 41, 62), (76, 175, 94), (36, 44, 113), (217, 68, 49), (218, 130, 155), (124, 185, 120), (235, 164, 184), (5, 59, 39), (146, 209, 221), (7, 95, 55), (169, 27, 25), (4, 86, 111), (234, 171, 164), (161, 212, 178)]

import turtle
import random

tim = turtle.Turtle()
screen= turtle.Screen()
turtle.colormode(255)

tim.speed('fastest')
tim.penup()
tim.hideturtle()

def row(dot_number):    
    """Paint dots in one line"""
    for _ in range(dot_number):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)        
        tim.forward(50)        
        

def matrix(m, n):
    """Paint m rows and n columns."""
    tim.setposition(-250, -200) 
    initial = tim.position()
    y = 0
    for _ in range(m):        
        row(n)
        y += 50
        tim.setposition(initial + (0, y) )

matrix(10, 10)
screen.exitonclick()
