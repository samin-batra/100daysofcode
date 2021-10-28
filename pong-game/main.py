from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("The Pong Game")
screen.tracer(0)
player_one = Paddle((380,0))
player_two = Paddle((-380,0))
ball = Ball()
score = Scoreboard()
# b = Turtle()
# b.shape("circle")
# b.color("white")
ball.move_ball()

screen.listen()
screen.onkey(player_one.move_paddle_up, "Up")
screen.onkey(player_one.move_paddle_down, "Down")
screen.onkey(player_two.move_paddle_up, "w")
screen.onkey(player_two.move_paddle_down, "s")


# screen.update()
while True:
    time.sleep(0.01)
    screen.update()
    ball.move_ball()
    # time.sleep(0.1)
    if ball.ycor()<-290 or ball.ycor()>290:
        ball.bounce_y()
    elif ball.xcor()>360 and ball.distance(player_one)<50 or ball.xcor()<-360 and ball.distance(player_two)<50:
        ball.bounce_x()
    elif ball.xcor()>380:
        print("Out of bounds!")
        ball.reset_position()
        score.increase_l_score()
    elif ball.xcor()<-380 :
        print("Out of bounds!")
        ball.reset_position()
        score.increase_r_score()

screen.exitonclick()