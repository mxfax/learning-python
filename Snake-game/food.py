import random
from turtle import Turtle



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.new_food()
        


    def new_food(self):
        self.clear()
        POS_X = random.randrange(-280, 280, 20)
        POS_Y = random.randrange(-280, 280, 20)
        self.food_coords = (float(POS_X), float(POS_Y))
        self.goto(self.food_coords)
