from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 270)
        self.level = 1
        self.current_level()


    def current_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.current_level()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
