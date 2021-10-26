from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# snake = []
snake = Snake()

food = Food()
print(food.shape())
score = ScoreBoard()

# for i in range(1, 4):
#     turtle = Turtle()
#     turtle.penup()
#     turtle.shape("square")
#     # turtle.shapesize(1, 1)
#     turtle.goto(20*i, 0)
#     turtle.color("white")
#     snake.append(turtle)
# screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.snake[0].distance(food) < 15:
        food.move_next()
        print("Eaten!")
        score.increase_score()
        snake.extend_snake()
    if snake.snake[0].xcor()>290 or snake.snake[0].xcor()<-290 or snake.snake[0].ycor()>290 or snake.snake[0].ycor()<-290:
        score.game_over()
        game_is_on = False

    for segment in snake.snake[1:]:
        if snake.snake[0].distance(segment) < 10:
            game_is_on = False

# print(f"{snake[0].xcor()}, {snake[1].xcor()}, {snake[2].xcor()}")


# screen.exitonclick()