from turtle import Turtle

ORIGIN = (0,0)
NORMAL = 0.1


class Ball(Turtle):   
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = NORMAL
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        
    def reset(self):
        self.goto(ORIGIN)
        self.bounce_x()
        self.move_speed = NORMAL
    
    

            
        
    