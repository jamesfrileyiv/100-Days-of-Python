from turtle import Turtle

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_TYPE = "normal"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.score = 0
        self.refresh_scoreboard()

    def increment_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
