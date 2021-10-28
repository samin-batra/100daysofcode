from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.shape("turtle")
        self.seth(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        x_pos = self.xcor()
        y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(x_pos, y_pos)

    def has_reached_edge(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        return False

    def reset_turtle(self):
        self.goto(STARTING_POSITION)