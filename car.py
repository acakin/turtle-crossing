from turtle import Turtle
from random import randint, choice

color = ["red", "blue", "yellow", "orange", "purple", "green"]


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.all_c = []
        self.speed_c = 5
        self.add()

    def add(self):
        self.hideturtle()
        if randint(1, 6) == 1:
            new_c = Turtle("square")
            new_c.shapesize(1, 2)
            new_c.color(choice(color))
            new_c.penup()
            new_c.goto(300, randint(-250, 250))
            self.all_c.append(new_c)

    def move(self):
        for _ in self.all_c:
            _.backward(self.speed_c)







