from turtle import Turtle
import random

FOOD_SHAPE = "circle"
FOOD_COLOR = "red"
FOOD_LENGTH = FOOD_WIDTH = 0.5

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(FOOD_LENGTH,FOOD_WIDTH)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)