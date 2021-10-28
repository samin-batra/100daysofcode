from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self,level):
        super().__init__()
        self.write_score(level)
        # self.goto(-230, 230)

    def increase_score(self,level):
        self.clear()
        self.write_score(level)
        # self.goto(-230,230)

    def write_score(self,level):
        self.write(f"Level: {level}", align="center", font=FONT)
        self.color("black")
        self.penup()
        # self.goto(-250, 270)
        self.hideturtle()

    def game_over(self):
        self.clear()
        self.write("Game Over!", align="center", font = FONT)
        self.color("black")
