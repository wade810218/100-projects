import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=300, height=300)
screen.tracer(0)

player = Player()
car_manager = []
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.crawl, "Up")


game_is_on = True
n=0
while game_is_on:
    time.sleep(0.1)
    n += 1
    if n % 6:
        
        car_manager.append(CarManager())
    screen.update()
    car_manager[0].drive()

    if player.finish_check():
        scoreboard.next_level()
        car_manager.speedup()
    
    if player.distance(car_manager) < 20:
        print('Gameover')
        scoreboard.gameover()
        game_is_on = False
        
