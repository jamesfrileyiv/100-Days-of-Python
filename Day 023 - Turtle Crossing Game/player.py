from turtle import Turtle

MAX_HEIGHT = 300        # recall screen height 600, so 600/2=300
MIN_HEIGHT = -1 * MAX_HEIGHT
MAX_WIDTH = MAX_HEIGHT
MIN_WIDTH = -1 * MAX_WIDTH
STARTING_POSITION = (0, MIN_HEIGHT + 20)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setpos(STARTING_POSITION)
        self.seth(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > (MIN_HEIGHT + 20):
            self.backward(MOVE_DISTANCE)

    def move_right(self):
        if self.xcor() < (MAX_WIDTH - 20):
            self.setx(self.xcor() + MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() > (MIN_WIDTH + 20):
            self.setx(self.xcor() - MOVE_DISTANCE)

    def detect_finish_line(self):
        if self.ycor() >= MAX_HEIGHT:
            return True
        else:
            return False

    def refresh(self):
        self.setpos(STARTING_POSITION)
