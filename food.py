from turtle import Turtle,Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.75,0.75)
        self.color("blue")
        self.penup()
        self.generate_food()
    def generate_food(self):
        a = random.randint(-280,280)
        b = random.randint(-280,280)
        self.goto(a,b)

