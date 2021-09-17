from turtle import Turtle
import random

MAX_HEIGHT = 250        # recall screen height 600, so 600/2=300. 250 gives 50px wiggle room at both ends
MIN_HEIGHT = -1 * MAX_HEIGHT
MAX_WIDTH = 300
MIN_WIDTH = -1 * MAX_WIDTH
HEADING = 270
CAR_SHAPE = "square"
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    
    def __init__(self):
        super().__init__(shape=CAR_SHAPE)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        random_y = random.randint(MIN_HEIGHT, MAX_HEIGHT + 1)
        self.goto(MAX_WIDTH, random_y)
        # self.seth(HEADING)

    def move_left(self):
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())

    def out_of_bounds(self):
        if self.xcor() < MIN_WIDTH:
            return True
        else:
            return False
