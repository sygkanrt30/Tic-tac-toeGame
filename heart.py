import turtle

pen = turtle.Turtle()
pen.speed(10**1000)
pen.color("red")
a = 20


def squard():
    for i in range(4):
        pen.forward(a)
        pen.left(90)


def love():
    for i in range(75):
        squard()
        pen.left(2)
        global a
        a = a + 2.5

    for i in range(75):
        squard()
        pen.left(2)
        a = a - 2.5


pen.penup()
pen.left(75)
pen.sety(150)
pen.pendown()
love()

turtle.done()
