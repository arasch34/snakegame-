from turtle import Screen
from snake_c import Snake
from scoreboard import Scoreboard
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 315 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
