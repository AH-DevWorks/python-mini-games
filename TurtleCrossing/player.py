from turtle import Turtle

STARTING_POSITION = (0, -282)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.color("#74CC68")
        self.setposition(STARTING_POSITION)
        self.left(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def reach_goal(self):
        return self.ycor() >= FINISH_LINE_Y

    def next_stage(self):
        self.setposition(STARTING_POSITION)
