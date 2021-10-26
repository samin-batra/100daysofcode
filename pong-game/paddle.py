from turtle import Turtle

POSITIONS = [(-380, 0), (-380, 10), (-380, 20), (-380, 30), (-380, 40), (-380, 50)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(350, 0)

    def move_paddle_up(self):
        # self.setheading(90)
        x_pos = 350
        y_pos = self.ycor() + 20
        self.goto(x_pos, y_pos)

    def move_paddle_down(self):
        x_pos = 350
        y_pos = self.ycor() - 20
        self.goto(x_pos, y_pos)
