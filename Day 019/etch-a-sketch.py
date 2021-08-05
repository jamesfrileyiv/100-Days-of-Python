from turtle import Turtle, Screen
import turtle

t = Turtle()
screen = Screen()
turtle.listen()


def forward():
    t.forward(10)


def backward():
    t.backward(10)


# d - rotate right
def rotate_right():
    t.right(10)


def rotate_left():
    t.left(10)


def clear():
    turtle.resetscreen()


screen.onkeypress(fun=forward, key='w')
screen.onkeypress(fun=backward, key='s')
screen.onkeypress(fun=rotate_right, key='d')
screen.onkeypress(fun=rotate_left, key='a')
screen.onkey(fun=clear, key='c')

turtle.mainloop()
