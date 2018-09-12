# Liam Neville
# 9/12/18
# assignment_one.py..py
# This is the first option for assignment one which draws four differently colored octagons

import turtle


turtle.speed(25)


def draw_an_octagon():
    for x in range(8):
        turtle.forward(75)
        turtle.left(45)


turtle.color("red")
turtle.begin_fill()
draw_an_octagon()
turtle.end_fill()


turtle.color("yellow")
turtle.begin_fill()
# I pick the pen up to avoid connecting the octagons with lines
turtle.up()
turtle.forward(200)
turtle.pd()
# I place the pen down once it is in the correct spot
draw_an_octagon()
turtle.end_fill()


turtle.color("blue")
turtle.begin_fill()
turtle.up()
turtle.right(90)
turtle.forward(200)
turtle.right(270)
turtle.pd()
draw_an_octagon()
turtle.end_fill()


turtle.color("green")
turtle.begin_fill()
turtle.up()
turtle.right(180)
turtle.forward(200)
turtle.right(180)
turtle.pd()
draw_an_octagon()
turtle.end_fill()


turtle.exitonclick()
