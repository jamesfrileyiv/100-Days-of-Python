from turtle import Turtle 
import constants as const


class Paddle(Turtle):

    # MAX_HEIGHT = const.SCREEN_HEIGHT / 2
    # MIN_HEIGHT = (-1) * MAX_HEIGHT
    STEP_SIZE = 20

    def __init__(self, start_x, start_y, name, screen_height):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(1, 5)
        self.setpos(x=start_x, y=start_y)
        self.name = name
        self.max_height = screen_height / 2
        self.min_height = -1 * self.max_height
    
    def get_name(self):
        return self.name

    def move_up(self):
        y_position = self.ycor()
        if y_position < self.max_height:
            y_position += self.STEP_SIZE
            self.setpos(x=self.xcor(), y=y_position)
    
    def move_down(self):
        y_position = self.ycor()
        if y_position > self.min_height:
            y_position -= self.STEP_SIZE
            self.setpos(x=self.xcor(), y=y_position)