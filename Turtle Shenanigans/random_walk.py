from turtle import Turtle, Screen, colormode
import random

niq = Turtle()
niq.shape("turtle")
niq.color("red")
niq.pensize(10)


def niq_move(angle):
    niq.setheading(angle)
    niq.fd(30)

def get_rand_color():
    return tuple(random.randint(0, 255) for _ in range(3))

colormode(255)
 
direction = [0, 90, 180, 270]
for _ in range(200):
    niq.pencolor(get_rand_color())
    niq_move(random.choice(direction))





screen = Screen()
screen.exitonclick()
