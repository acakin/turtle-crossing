from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.p_score = 0
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.goto(300, 200)
        self.write(self.p_score, align="center", font=("Courier", 24, "normal"))
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def p_counter(self):
        self.p_score += 1
        self.update()

    def level_counter(self):
        self.level += 1
        self.update()
