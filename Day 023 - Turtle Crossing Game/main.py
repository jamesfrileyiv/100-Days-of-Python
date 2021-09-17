import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)

car_manager = CarManager()
sb = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    if player.detect_finish_line():
        player.refresh()
        car_manager.increase_difficulty(sb.get_level())
        sb.increment_level()
        sb.refresh()
    elif car_manager.detect_collision(player):
        game_is_on = False
        sb.game_over()

screen.exitonclick()
