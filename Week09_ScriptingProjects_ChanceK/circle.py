import turtle
import math

t = turtle.Turtle()

def drawCircle(t, centerX, centerY, radius):
    t.penup()
    t.goto(centerX + radius, centerY)
    t.setheading(90)
    t.pendown()

    distance = 2.0 * math.pi * radius / 120.0

    for _ in range(120):
        t.forward(distance)
        t.left(3)

drawCircle(t, 0, 0, 100)

turtle.done()