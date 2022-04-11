from os import close
from turtle import Turtle,Screen, clone, color
import time,random
from snake import Snake
from food import Food
from scoreboard import Scoreboard
my_screen = Screen()
my_screen.setup(width=620,height=620)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")
flag = True
score = 0
while(flag):
    time.sleep(0.1)
    my_screen.update()
    snake.move()
    snake.segments[len(snake.segments)-1].showturtle()
    if(snake.head.distance(food) < 20):
        scoreboard.score += 1
        scoreboard.refresh_score()
        food.generate_food()
        new_segment = Turtle()
        new_segment.hideturtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("green")
        snake.segments.append(new_segment)
    if(snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300):
        flag = False
        scoreboard.refresh_score()
        scoreboard.game_over()
    innerflag = False
    for seg in snake.segments:
        if(seg == snake.head):
            continue
        else:
            if(snake.head.distance(seg) < 15):
                innerflag = True
                break
    if(innerflag):
        flag = False
        scoreboard.refresh_score()
        scoreboard.game_over()
    
my_screen.exitonclick()