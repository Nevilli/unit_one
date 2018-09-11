import turtle


turtle.speed(25)


def draw_an_octagon():
    for x in range(8):
        turtle.forward(75)
        turtle.left(45)


turtle.color("red")
draw_an_octagon()


turtle.up()
turtle.forward(200)
turtle.pd()
draw_an_octagon()


turtle.up()
turtle.right(90)
turtle.forward(200)
turtle.right(270)
turtle.pd()
draw_an_octagon()


turtle.up()
turtle.right(180)
turtle.forward(200)
turtle.right(180)
turtle.pd()
draw_an_octagon()


turtle.exitonclick()
