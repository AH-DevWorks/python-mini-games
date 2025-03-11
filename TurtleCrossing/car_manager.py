from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LANES = [-240, -180, -120, -60, 0, 60, 120, 180, 240]


def get_available_lane(cars, start_x=320, safe_distance=49):
    available = []
    for lane in LANES:
        occupied = any(car.ycor() == lane and car.xcor() > (start_x - safe_distance) for car in cars)
        if not occupied:
            available.append(lane)
    return available


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.level = 0
        self.car_speed = STARTING_MOVE_DISTANCE
        self.max_cars_num = 13

    def create_car(self):
        if len(self.cars) <= self.max_cars_num:
            new_car = Turtle(shape="square")
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.penup()
            new_car.car_speed = STARTING_MOVE_DISTANCE + (self.level * MOVE_INCREMENT)
            if self.cars:
                available = get_available_lane(self.cars)
                if available:
                    lane = random.choice(available)
                    new_car.setposition(x=320, y=lane)
                else:
                    lane = random.choice(LANES)
                    new_car.setposition(x=350, y=lane)
            else:
                lane = random.choice(LANES)
                new_car.setposition(x=320, y=lane)
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def reset_car(self, car):
        available = get_available_lane(self.cars)
        if available:
            lane = random.choice(available)
        else:
            lane = random.choice(LANES)
        car.goto(x=320, y=lane)

    def level_up(self):
        self.level += 1
        self.max_cars_num += 1
        self.car_speed += MOVE_INCREMENT
