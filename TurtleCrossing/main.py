#  1. Create a turtle player that starts at the bottom of the screen and listen for
#  the "Up" keypress to move the turtle north.
#  2. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
#  and move to the left edge of the screen. No cars should be generated in the top and bottom 50px
#  of the screen (think of it as a safe zone for our little turtle).
#  Hint: generate a new car only every 6th time the game loop runs.
#  3. Detect when the turtle player collides with a car and stop the game if this happens.
#  4. Detect when the turtle player has reached the top edge of the screen
#  (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position
#  and increase the speed of the cars.
#  Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.
#  5. Create a scoreboard that keeps track of which level the user is on.
#  Every time the turtle player does a successful crossing, the level should increase.
#  When the turtle hits a car, GAME OVER should be displayed in the centre.

import time
from turtle import Screen
from player import Player
from road_manager import RoadManager
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("#2C2C2C")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

scoreboard = Scoreboard()

road_manager = RoadManager()

player = Player()

screen.listen()
screen.onkey(player.up, "Up")

car_manager = CarManager()


count = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if count % 6 == 0 and len(car_manager.cars) < car_manager.max_cars_num:
        car_manager.create_car()

    if player.reach_goal():
        time.sleep(0.3)
        scoreboard.level_up()
        player.next_stage()
        car_manager.level_up()
        car_manager.create_car()

    car_manager.move_cars()
    for car in car_manager.cars:
        if abs(player.ycor() - car.ycor()) < 15.0 and abs(car.xcor() - player.xcor()) < 28.0:
            game_is_on = False
            scoreboard.game_over()
            break
        elif car.xcor() <= -315:
            car_manager.reset_car(car)

    count += 1


screen.exitonclick()
