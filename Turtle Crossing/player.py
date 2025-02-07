from turtle import Turtle

STARTING_POSITION = (0, -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.reset()
        
    def move(self):
        self.fd(10)
    
    def reset(self):
        self.goto(STARTING_POSITION)