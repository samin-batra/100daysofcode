from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_score()
         # self.color("white")

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score = {self.high_score}", align="center", font=("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align="center", font=("Arial", 10, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt","w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()