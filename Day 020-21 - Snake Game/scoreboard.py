from turtle import Turtle
from os import path

ALIGNMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_TYPE = "normal"
HIGH_SCORE_FILE_PATH = "high_score.txt"
DEFAULT_HIGH_SCORE = 0


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.high_score = self.initialize_high_score()
        self.score = 0
        self.refresh_scoreboard()

    @staticmethod
    def initialize_high_score():
        high_score = DEFAULT_HIGH_SCORE
        if path.exists(HIGH_SCORE_FILE_PATH):
            with open(file=HIGH_SCORE_FILE_PATH, mode="r") as f:
                line = f.readline()
            if line.isdecimal():
                if int(line) > 0:
                    high_score = int(line)
            else:
                with open(file=HIGH_SCORE_FILE_PATH, mode="w") as f:
                    f.write(str(high_score))
        else:
            with open(file=HIGH_SCORE_FILE_PATH, mode="w") as f:
                f.write(str(DEFAULT_HIGH_SCORE))
        return high_score

    def increment_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
        if self.score > self.high_score:
            self.write_high_score()

    def refresh_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}\tHigh Score: {self.high_score}",
                   align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def write_high_score(self):
        with open(file=HIGH_SCORE_FILE_PATH, mode="w") as f:
            f.write(str(self.score))
