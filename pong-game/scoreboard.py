from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")

        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        # self.write(self.score,False,align = "center",font = ("Ariel",80,"normal"))
        self.penup()
        # self.goto(0, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100,150)
        self.write(self.l_score,align = "center",font = ("Ariel",80,"normal"))
        self.goto(100,150)
        self.write(self.r_score,align = "center",font = ("Ariel",80,"normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()