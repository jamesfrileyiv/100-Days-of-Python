from turtle import Turtle, Screen
import tkinter.messagebox
import random


screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "green", "blue", "yellow", "purple"]
turtles = []
user_bet = ""
need_bet = True
while need_bet:
    user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color: ")
    if user_bet.lower() in colors:
        need_bet = False
    else:
        tkinter.messagebox.showerror(title="Input Error", message="Enter a color of the rainbow.")

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color)
    turtle.goto(x=-230, y=(-150+len(turtles)*60))       # y-coordinate is more or less calculated by trial and error
    turtles.append(turtle)

race_is_on = True
while race_is_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 11))
        if turtle.xcor() >= 230:
            race_is_on = False
            if user_bet == turtle.color()[0]:
                tkinter.messagebox.showinfo(title="Winner", message=f"{turtle.color()[1].title()} won the race. "
                                                                    f"You won the bet!")
            else:
                tkinter.messagebox.showinfo(title="Winner", message=f"{turtle.color()[1].title()} won the race. "
                                                                    f"You lost the bet!")

screen.exitonclick()
