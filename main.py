from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("<----Snake Game---->")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.clear()
        score.update_score()
        score.new_score += 1

screen.exitonclick()

