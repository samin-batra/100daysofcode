from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.position = position
        self.goto(self.position)

    def move_paddle_up(self):
        # self.setheading(90)
        x_pos = self.xcor()
        y_pos = self.ycor() + 20
        self.goto(x_pos, y_pos)

    def move_paddle_down(self):
        x_pos = self.xcor()
        y_pos = self.ycor() - 20
        self.goto(x_pos, y_pos)
