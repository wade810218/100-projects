from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("arial", 40, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        #self.goto(position)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-50 ,240)
        self.write(f'{self.l_score}',align=ALIGNMENT, font = FONT)
        self.goto(50 ,240)
        self.write(f'{self.r_score}',align=ALIGNMENT, font = FONT)  
        


    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()    
