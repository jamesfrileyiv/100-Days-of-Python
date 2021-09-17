from turtle import Turtle

FONT = ("Courier", 12, "normal")
POSITION = (-250, 250)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(POSITION)
        self.level = 1
        self.display_score()

    def get_level(self):
        return self.level

    def increment_level(self):
        self.level += 1

    def display_score(self):
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def refresh(self):
        self.clear()
        self.display_score()

    def game_over(self):
        self.clear()
        self.write(arg="Game Over", align="center", font=FONT)
