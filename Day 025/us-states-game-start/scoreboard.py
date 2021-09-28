from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
MAX_WRONG = 10
NUM_STATES = 50


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.score = 0
        self.wrong = 0
        self.write_score()

    def write_score(self):
        message = f"Score: {self.score}\tWrong Answers: {self.wrong}/{MAX_WRONG}"
        self.write(arg=message, align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.write_score()

    def increment_score(self):
        self.score += 1

    def increment_wrong(self):
        self.wrong += 1

    def confirm_game_over(self):
        if self.wrong == MAX_WRONG or self.score == NUM_STATES:
            return True
        else:
            return False

    def game_over(self):
        self.clear()
        if self.wrong == MAX_WRONG:
            self.write(arg="Game Over!", align=ALIGNMENT, font=FONT)
        elif self.score == NUM_STATES:
            self.write(arg=f"You Win! You know all {NUM_STATES} states!", align=ALIGNMENT, font=FONT)
