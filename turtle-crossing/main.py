import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

##Player turtle which listens for up keystrokes and moves
player = Player()
screen.listen()
screen.onkey(player.move_turtle, "Up")

cars = CarManager()
cars.generate_car()
times_since_last_car = 0

game_is_on = True
current_level = 1
score = Scoreboard(current_level)

def detect_collision(player, cars):
    for car in cars:
        if car.distance(player) < 30:
            return True
    return False


while game_is_on:
    time.sleep(0.1)
    if times_since_last_car % 8 == 0:
        cars.generate_car()
    cars.move_cars()
    screen.update()
    times_since_last_car += 1
    if detect_collision(player, cars.cars):
        game_is_on = False
        score.game_over()
    if player.has_reached_edge():
        # player.clear()
        current_level += 1
        player.reset_turtle()
        cars.clear()
        cars.reset_cars()
        cars.generate_car()
        score.increase_score(current_level)


screen.exitonclick()