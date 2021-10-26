import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=1000, height=600)
user_bet = screen.textinput(title="Who do you think will win the race?", prompt="Enter your bet here: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
turtles_race = []
for i in range(1, 7):
    t = Turtle(shape="turtle")
    turtles_race.append(t)
    t.penup()
    t.color(colors[i-1])
    t.goto(-(screen.window_width()/2-10), screen.window_height()/2-i*50)

# t.onkey()

is_race_on = False
if user_bet:
    is_race_on = True
print(screen.window_width())
max_distance = screen.window_width()

while is_race_on:
    for turt in turtles_race:
        if turt.xcor() > (max_distance/2-20):
            winning_color = turt.pencolor()
            if turt.pencolor() == user_bet:
                print(f"You've won! The turtle with color {winning_color} won the race!")
            else:
                print(f"You lost! The turtle with color {winning_color} won the race!")
            is_race_on = False
        turt.forward(random.randint(0, 10))

screen.exitonclick()
