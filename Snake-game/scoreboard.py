from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.setpos(0,280)    
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)


    def add_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setpos(0,0)
        self.write(f"Game Over! Your score: {self.score}",align=ALIGNMENT, font=FONT)
        

