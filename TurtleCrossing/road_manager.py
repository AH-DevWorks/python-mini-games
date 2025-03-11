from turtle import Turtle

LANE_EDGES = [ -210, -150, -90, -30, 30, 90, 150, 210]

class RoadManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.lanes = LANE_EDGES
        self.hideturtle()
        self.create_lanes_line()
        self.create_start_and_goal_area()


    def create_lanes_line(self):
        for lane in self.lanes:
            line_painter = Turtle(shape="square")
            line_painter.hideturtle()
            line_painter.penup()
            line_painter.color("#FAFBFF")
            line_painter.pensize(4)
            line_painter.setheading(180)
            line_painter.setposition(x=310, y=lane)
            while line_painter.xcor() >= -310:
                line_painter.pendown()
                line_painter.forward(75)
                line_painter.penup()
                line_painter.forward(30)

    def create_start_and_goal_area(self):
        goal_area = Turtle(shape="square")
        goal_area.penup()
        goal_area.setposition(0, 285)
        goal_area.turtlesize(stretch_wid=2.5, stretch_len=13)
        goal_area.color("#22D5E6")
        start_area = Turtle(shape="square")
        start_area.penup()
        start_area.setposition(0, -277)
        start_area.turtlesize(stretch_wid=2, stretch_len=30)
        start_area.color("#A3F7C5")