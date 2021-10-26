from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        s = Turtle()
        s.penup()
        s.shape("square")
        # turtle.shapesize(1, 1)
        s.goto(position)
        s.color("white")
        self.snake.append(s)

    def move_snake(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            self.snake[seg_num].goto(self.snake[seg_num - 1].xcor(), self.snake[seg_num - 1].ycor())
        self.snake[0].forward(20)

    def up(self):
        if not self.snake[0].heading() == DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if not self.snake[0].heading() == UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if not self.snake[0].heading() == RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if not self.snake[0].heading() == LEFT:
            self.snake[0].setheading(RIGHT)

    def extend_snake(self):
        self.add_segment(self.snake[-1].position())
