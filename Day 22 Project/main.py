
#creat and move paddle
#creat and move another paddle
#creat ball and make it move
#detect collision with wall and bounce 
#detect collision with paddlw and bounce
#detect when paddle misses
#keep scoreboard
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)



screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()


#screen.exitonclick()
 
