from turtle import Turtle, Screen, colormode
import random

niq = Turtle()
niq.speed("fastest")
colormode(255)

def get_rand_color():
    return tuple(random.randint(0, 255) for _ in range(3))

def draw_spirograph(size_of_gap):    
    for _ in range(int(360 / size_of_gap)):
        niq.pencolor(get_rand_color()) 
        niq.circle(100)
        niq.setheading(niq.heading() + size_of_gap)
        
draw_spirograph(5)




    




screen = Screen()
screen.exitonclick()
