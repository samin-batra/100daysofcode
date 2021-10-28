from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.move_x = 3
        self.move_y = 3

    def move_ball(self):
        # self.setheading(0)
        x_pos = self.xcor() + self.move_x
        y_pos = self.ycor() + self.move_y
        self.goto(x_pos, y_pos)
        # self.forward(0.1)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.move_y += 0.4

    def reset_position(self):
        self.goto(0, 0)
        self.move_x *= -1
