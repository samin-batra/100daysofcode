from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("The Pong Game")
screen.tracer(0)
player = Paddle()
screen.listen()
screen.onkey(player.move_paddle_up, "Up")
screen.onkey(player.move_paddle_down, "Down")
# screen.update()
while True:
    screen.update()

screen.exitonclick()