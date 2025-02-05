from turtle import Turtle, Screen, colormode
import random

"""
Getting color from image

import colorgram

colors = colorgram.extract("image.jpg", 24)
color_list = []
for color in colors:
    color_list.append(tuple(color.rgb))
print(color_list)

"""

niq = Turtle()
colormode(255)
rgb_colors = [(209, 165, 124), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190), (233, 174, 161), (141, 213, 224), (191, 191, 193), (160, 211, 182)]
y = -197.49

def get_rand_color():
    return random.choice(rgb_colors)

def create_row():
    niq.pendown()
    niq.seth(0)
    niq.showturtle()
    for _ in range(10):
        niq.dot(20, get_rand_color())
        niq.penup()
        niq.fd(50)
        niq.dot(20, get_rand_color())

def set_pos(y):
    niq.hideturtle()    
    niq.penup()
    niq.setpos(-247.49, y)

niq.hideturtle()
niq.penup()
niq.setheading(225)
niq.fd(350)

for _ in range(10):
    create_row()
    set_pos(y)
    y += 50


    



screen = Screen()
screen.exitonclick()
