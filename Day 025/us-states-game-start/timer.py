from turtle import Turtle
import datetime

POSITION = (350, 350)


class Timer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.time = datetime.time(minute=10, second=0)
        self.write(arg=self.time.)
