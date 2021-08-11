from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_position()

    def new_position(self):
        rand_x = random.randint(-280, 250)  # y=250 because this keeps food below scoreboard
        rand_y = random.randint(-280, 250)
        self.goto(rand_x, rand_y)
