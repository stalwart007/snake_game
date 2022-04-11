from turtle import Turtle,Screen
import time
from food import Food
INITIAL = [(0,0),(-20,0),(-40,0)]
M = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for i in range(1,4):
            tim = Turtle(shape="square")
            tim.color("green")
            tim.penup()
            tim.goto(INITIAL[i-1])
            self.segments.append(tim)
    def move(self):
            for i in range(len(self.segments)-1,0,-1):
                self.segments[i].goto(self.segments[i-1].xcor(),self.segments[i-1].ycor())
            self.segments[0].forward(M)
            
    def up(self):
        if(self.segments[0].heading() != 270):
            self.segments[0].setheading(90)
    def down(self):
        if(self.segments[0].heading() != 90):
            self.segments[0].setheading(270)
    def right(self):
        if(self.segments[0].heading() != 180):
            self.segments[0].setheading(0)
    def left(self):
        if(self.segments[0].heading() != 0):
            self.segments[0].setheading(180)

