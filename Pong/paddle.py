from turtle import Turtle

STARTING_POSITIONS = (350, 0)
MOVE_DISTANCE = 20
UP = 0
DOWN = 180

class Paddle(Turtle):
    def __init__(self, position = (0,0)):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)