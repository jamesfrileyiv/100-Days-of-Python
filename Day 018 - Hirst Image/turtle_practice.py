from turtle import Turtle, Screen
import random
from tkinter import simpledialog


# def draw_centered_square(turtle, size):
#     """Draws a size x siz px square centered on current position. After, angle will be right 90 deg and position
#     shifted to the right by size/2 px"""
#     turtle.penup()
#     turtle.forward(size/2)
#     turtle.right(90)
#     turtle.pendown()
#     turtle.forward(size/2)
#     turtle.right(90)
#     turtle.forward(size)
#     turtle.right(90)
#     turtle.forward(size)
#     turtle.right(90)
#     turtle.forward(size)
#     turtle.right(90)
#     turtle.forward(size/2)


# def draw_line(turtle, length):
#     """length is the number of dashes"""
#     for _ in range(length):
#         turtle.forward(10)
#         turtle.penup()
#         turtle.forward(10)
#         turtle.pendown()


# def draw_shape(turtle, sides, color):
#     interior_angle = (sides - 2) * (180 / sides)
#     turtle.pencolor(color)
#     for _ in range(sides):
#         turtle.forward(100)
#         turtle.right(180-interior_angle)


# def random_walk(turtle, steps):
#     angles = [0, 90, 180, 270]
#     for step in range(steps):
#         color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         turtle.pencolor(color)
#         turtle.setheading(angles[random.randint(0, len(angles)-1)])
#         turtle.forward(30)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def spirograph(turtle, angle):
    current_angle = 0
    while current_angle <= 360:
        turtle.pencolor(random_color())
        turtle.circle(radius=100)
        turtle.setheading(current_angle)
        current_angle += angle

turtle = Turtle()
turtle.pensize(5)
turtle.hideturtle()
turtle.speed(0)
screen = Screen()
screen.colormode(255)
# draw_centered_square(turtle, 500)

# length = simpledialog.askinteger(title="length", prompt="Enter length of line:")
# draw_line(turtle, 10)

# for sides in range(3, 11):
#     color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     draw_shape(turtle, sides, color)

# steps = simpledialog.askinteger(title="steps", prompt="Enter steps in random walk:")
# random_walk(turtle, steps)

spirograph(turtle, 20)

screen.exitonclick()
