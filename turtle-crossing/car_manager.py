from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.increment = STARTING_MOVE_DISTANCE

    def generate_car(self):
        y_pos = random.randint(-250,250)
        color = random.choice(COLORS)
        c = Turtle()
        c.shape("square")
        c.shapesize(stretch_wid=1,stretch_len=2)
        c.color(color)
        c.penup()
        c.goto(250,y_pos)
        self.cars.append(c)

    def move_cars(self):
        for car in self.cars:
            x_pos = car.xcor() - self.increment
            y_pos = car.ycor()
            car.goto(x_pos,y_pos)

    def reset_cars(self):
        # self.cars.clear()
        self.clear()
        self.increment += MOVE_INCREMENT

