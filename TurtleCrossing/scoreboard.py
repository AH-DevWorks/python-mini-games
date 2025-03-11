from turtle import Turtle

LEVEL_FONT = ("Kingthings Petrock Light", 29, "normal")
GAME_OVER_FONT = ("Kingthings Petrock", 75, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(x=-275, y=255)
        self.score = 0
        self.color("#7DAEFE")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=LEVEL_FONT)

    def level_up(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.color("#C32223")
        self.setposition(x=0, y=5)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
