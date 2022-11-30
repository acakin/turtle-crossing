from turtle import Turtle


class Animal(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("black")
        self.penup()
        self.goto(0, -280)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    #def down(self):
    #    new_y = self.ycor() - 10
    #    self.goto(self.xcor(), new_y)

    #def r(self):
    #    new_x = self.xcor() + 10
    #    self.goto(new_x, self.ycor())

    #def l(self):
    #    new_x = self.xcor() - 10
    #    self.goto(new_x, self.ycor())
