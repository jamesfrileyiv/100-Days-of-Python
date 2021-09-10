from turtle import Turtle 
from paddle import Paddle
import constants as const
import random


class Ball(Turtle):

    INITIAL_HEADINGS = [45, 315, 135, 225]
    # MAX_HEIGHT = const.SCREEN_HEIGHT / 2
    # MIN_HEIGHT = (-1) * MAX_HEIGHT
    STEP_SIZE = .6        # This number was arrived at through trial and error of what felt like the right speed, previous .25

    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.setpos((0,0))
        self.setheading(random.choice(self.INITIAL_HEADINGS))
        self.speed("slowest")
    
    def move_forward(self):
        self.forward(self.STEP_SIZE)
    
    def detect_paddle_collission(self, paddle):
        flag = (self.xcor() in range(paddle.xcor() + 5, paddle.xcor() - 5)) and (self.ycor() in range(paddle.ycor()-10, paddle.ycor()+10))
        if (flag):
            return True
        else:
            return False

    def bounce(self):
        self.setheading(self.heading() + 90)
    
    def reset(self, scorer):
        self.setpos((0, 0))
        if scorer.lower() == "right":
            self.setheading(random.choice(self.INITIAL_HEADINGS[2:]))
        elif scorer.lower() == "left":
            self.setheading(random.choice(self.INITIAL_HEADINGS[:2]))
        else:
            print("ERROR: Ball.reset() method requires a string input 'left' or 'right'.")
            exit(1)