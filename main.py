from turtle import Turtle, Screen
from animal import Animal
from car import Car
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(600, 600)
s.tracer(0)
s.listen()

a = Animal()
c = Car()
sb = Scoreboard()

s.onkeypress(a.up, "Up")
#s.onkeypress(a.down, "Down")
#s.onkeypress(a.l, "Left")
#s.onkeypress(a.r, "Right")
loop = 0

game_is_on = True
while game_is_on:
    loop += 1
    time.sleep(0.1)
    s.update()
    c.add()
    c.move()
    if a.ycor() == 280:
        sb.level_counter()
        a.goto(0, -280)
        c.speed_c += 10

    for _ in c.all_c:
        if _.distance(a) < 20:
            c.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
            game_is_on = False













s.exitonclick()