import math
from turtle import Turtle
from car import Car
from player import Player
import random

MAX_HEIGHT = 250        # recall screen height 600, so 600/2=300. 250 gives 50px wiggle room at both ends
MIN_HEIGHT = -1 * MAX_HEIGHT
MAX_WIDTH = 300
MIN_WIDTH = -1 * MAX_WIDTH
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RAND_INT_LOW = 1
RAND_INT_HIGH = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.rand_int_high = RAND_INT_HIGH

    def create_car(self):
        if random.randint(RAND_INT_LOW, self.rand_int_high) == RAND_INT_LOW:
            new_car = Car()
            index = 0
            while index < len(self.all_cars):
                if self.all_cars[index].distance(new_car) < 50:
                    new_car.hideturtle()
                    new_car = Car()
                    index = 0
                else:
                    index += 1
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.move_left()

    def increase_difficulty(self, level: int):
        if self.rand_int_high > 2:
            self.rand_int_high -= math.floor(.5 * level)

    def detect_collision(self, player: Player):
        for car in self.all_cars:
            if car.distance(player) < 20:
                return True
        return False
