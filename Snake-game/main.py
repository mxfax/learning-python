from turtle import Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_on = True
screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
speed = 0.1
snake = Snake()
food = Food()
score = Scoreboard()

def play_game(speed_adjustment=0):
    global speed
    while game_on:
        screen.update()
        time.sleep(speed)
        snake.move()
        # Detect collision with food
        if snake.head.distance(food) < 15:
            snake.extend()
            score.add_score()
            food.new_food()
            speed = max(0.05, speed + speed_adjustment)  # Adjust speed
        # Detect collision with walls
        if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
            score.game_over()
            break
        # Detect collision with self
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 7:
                score.game_over()
                break

game_variant = screen.textinput(title="Snake Game", prompt="Do you want to play simple version (1) or advanced with speed up (2)?")

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

if game_variant == "1":
    play_game(speed_adjustment=0)
elif game_variant == "2":
    play_game(speed_adjustment=-0.002)


screen.exitonclick()