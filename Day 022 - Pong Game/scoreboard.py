from turtle import Turtle


class Scoreboard(Turtle):

    ALIGNMENT = "center"
    FONT_STYLE = "courier"
    LARGE_TEXT_SIZE = 80
    SMALL_TEXT_SIZE = 40
    FONT_TYPE = "normal"
    LARGE_DEFAULT_FONT = (FONT_STYLE, LARGE_TEXT_SIZE, FONT_TYPE)
    SMALL_DEFAULT_FONT = (FONT_STYLE, SMALL_TEXT_SIZE, FONT_TYPE)

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.display_score()
    
    def display_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=self.ALIGNMENT, font=self.LARGE_DEFAULT_FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=self.ALIGNMENT, font=self.LARGE_DEFAULT_FONT)
    
    def increment_score(self, scorer):
        if scorer.lower() == "right":
            self.r_score += 1
        elif scorer.lower() == "left":
            self.l_score += 1
        else:
            print("ERROR: increment_score() requires scorer to be 'left' or 'right'")
            exit(1)
    
    def get_l_score(self):
        return self.l_score
    
    def get_r_score(self):
        return self.r_score
    
    def display_winner(self):
        self.goto((0, 0))
        if self.l_score > self.r_score:
            winner = "Left Player"
        else:
            winner = "Right Player"
        message = f"{winner} Wins!"
        self.write(arg=message, align=self.ALIGNMENT, font=self.SMALL_DEFAULT_FONT)