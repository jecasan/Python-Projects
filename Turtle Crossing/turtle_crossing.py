from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Turtle Crossing")

screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard() 

screen.listen()
screen.onkeypress(player.move, "Up")
 
count = 0
game_is_on = True
while game_is_on:
    screen.update()  
    time.sleep(0.1)
    car.create_car()   
    car.move()      
    
    # Determine if turtle reaches other side
    if player.ycor() > 280:
        car.increase_speed()
        player.reset()
        scoreboard.level_up()
        
    # Determine if turtle collides with car
    for cars in car.all_cars:
        if player.distance(cars) < 25:
            game_is_on = False
            scoreboard.game_over()
        

screen.exitonclick()