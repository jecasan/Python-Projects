from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 1
        self.update()     
    
    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align = ALIGNMENT, font = FONT)   
        
    def level_up(self):
       self.score += 1
       self.update()
       
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)
       
