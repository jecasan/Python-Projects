from turtle import Turtle, Screen

niq = Turtle()
screen = Screen()


def move_forwards():
    niq.fd(10)
    
def move_backwards():
    niq.bk(10)
    
def clockwise():
    niq.right(10)
    
def counter_clockwise():
    niq.left(10)
    
def clear_screen():
    niq.clear()
    niq.penup()
    niq.home()
    niq.pendown()

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = counter_clockwise)
screen.onkey(key = "d", fun = clockwise)
screen.onkey(key = "c", fun = clear_screen)
screen.exitonclick()