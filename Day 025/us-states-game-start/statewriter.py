from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 6, "normal")


class StateWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self, state: str, x_cor: int, y_cor: int):
        self.goto(x=x_cor, y=y_cor)
        self.write(arg=state, align=ALIGNMENT, font=FONT)
