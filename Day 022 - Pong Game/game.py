from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


class Game():

    BACKGROUND_COLOR = "black"
    SCREEN_TITLE = "Pong"
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    RIGHT_START_X = 350
    LEFT_START_X = (-1) * RIGHT_START_X
    START_Y = 0
    MAX_SCORE = 10

    def __init__(self):
        self.game_screen = self.new_screen()
        self.right_paddle = Paddle(self.RIGHT_START_X, self.START_Y, "right", self.SCREEN_HEIGHT)
        self.left_paddle = Paddle(self.LEFT_START_X, self.START_Y, "left", self.SCREEN_HEIGHT)
        self.ball = Ball()
        self.scoreboard = Scoreboard()
        self.line_drawing_turtle = Turtle()
        self.line_drawing_turtle = self.draw_center_line()
        self.game_is_on = True 
        self.game_screen.listen()

        self.game_screen.onkey(key="Up", fun=self.right_paddle.move_up)
        self.game_screen.onkey(key="Down", fun=self.right_paddle.move_down)
        self.game_screen.onkey(key="w", fun=self.left_paddle.move_up)
        self.game_screen.onkey(key="s", fun=self.left_paddle.move_down)

    def new_screen(self):
        screen = Screen()
        screen.bgcolor(self.BACKGROUND_COLOR)
        screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        screen.title(self.SCREEN_TITLE)
        screen.tracer(0)
        return screen
    
    def draw_center_line(self):
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto((0, (-1 * self.SCREEN_HEIGHT) / 2))
        turtle.pendown()
        turtle.pencolor("white")
        turtle.seth(90)
        turtle.forward(self.SCREEN_HEIGHT)
        return turtle
    
    def play_game(self):
        while self.game_is_on:
          #  print("play_game() while loop")
            self.game_screen.update()
            if (self.detect_boundary_bounce_condition()):
                self.ball.bounce()
            elif (self.detect_paddle_collission()):
                self.ball.bounce()
            if (self.detect_left_score()):
                self.scoreboard = self.score_process(self.left_paddle)
            elif (self.detect_right_score()):
                self.scoreboard = self.score_process(self.right_paddle)
         #   print("moving forward")
            self.ball.move_forward()
            self.game_is_on = self.get_game_status()
            #print(f"game_is_on = {self.game_is_on}")
            if not self.game_is_on:
                self.scoreboard.display_winner()
        #print("exited play_game() while loop")
       # self.ball.reset()
        self.game_screen.exitonclick()

    def detect_boundary_bounce_condition(self):
        max_y = (self.SCREEN_HEIGHT / 2) - 20  # 20 chosen based on trial and error to get it to look right
        min_y = -1 * max_y
        if (self.ball.ycor() >= max_y) or (self.ball.ycor() <= min_y):
            return True 
        else:
            return False
    
    def detect_paddle_collission(self):
        if ((self.ball.distance(self.left_paddle) < 50 or self.ball.distance(self.right_paddle) < 50) and \
            ((self.ball.xcor() > self.RIGHT_START_X - 10) or self.ball.xcor() < self.LEFT_START_X + 10)):
            return True 
        else: 
            return False
    
    def detect_left_score(self):
        if self.ball.xcor() > self.SCREEN_WIDTH / 2:
            return True 
        else: 
            return False
    
    def detect_right_score(self):
        if self.ball.xcor() < ((-1) * self.SCREEN_WIDTH / 2):
            return True 
        else:
            return False 
    
    def score_process(self, paddle):
        self.ball.reset(paddle.get_name())
        self.scoreboard.increment_score(paddle.get_name())
        self.scoreboard.clear()
        self.scoreboard.display_score()
        return self.scoreboard
    
    def get_game_status(self):
        if self.scoreboard.get_l_score() == self.MAX_SCORE or self.scoreboard.get_r_score() == self.MAX_SCORE:
            return False 
        else:
            return True 