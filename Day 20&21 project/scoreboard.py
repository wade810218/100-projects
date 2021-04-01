from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0    
        #self.shape("square")
        #self.shapesize(stretch_len = 2, stretch_wid=1.5)
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self): 
        self.clear() 
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT )
