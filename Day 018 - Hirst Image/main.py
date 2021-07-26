import turtle
import colorgram
import random


def get_color_palette():
    rgb_colors = []
    colors = colorgram.extract('image.jpg', 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_rgb = (r, g, b)
        rgb_colors.append(new_rgb)
    rgb_colors.pop(0)  # first two colors were too close to white, so I removed them
    rgb_colors.pop(0)
    return rgb_colors


def draw_dotted_line():
    for _ in range(num_dots_width):
        dot_color = random.choice(color_palette)
        t.dot(spot_size, dot_color)
        t.forward(step_size)


spot_size = 20
step_size = 50
num_dots_width = 10
num_dots_height = 10

# these calculations were derived by trial and error to get dots that fit properly
screen_width = int((num_dots_width - 1) * step_size + (spot_size/2))
screen_height = int((num_dots_height - 1) * step_size + (spot_size/2))

color_palette = get_color_palette()

t = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(screen_width, screen_height)
screen.setworldcoordinates(-1, -1, screen_width-1, screen_height-1)
screen.colormode(255)
t.penup()

for x in range(num_dots_height):
    t.setposition(0, x * step_size)
    draw_dotted_line()

screen.exitonclick()
