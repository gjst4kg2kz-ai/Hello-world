import turtle

def drawFractalLine(t, distance, angle, level):
    if level == 0:
        t.setheading(angle)
        t.forward(distance)
    else:
        segment = distance / 3
        drawFractalLine(t, segment, angle, level - 1)
        drawFractalLine(t, segment, angle + 60, level - 1)
        drawFractalLine(t, segment, angle - 60, level - 1)
        drawFractalLine(t, segment, angle, level - 1)

def drawKochSnowflake(t, distance, level):
    for angle in [0, -120, 120]:
        drawFractalLine(t, distance, angle, level)

def main():
    t = turtle.Turtle()
    t.speed(0)  # fastest drawing
    t.penup()
    t.goto(-150, 100)  # starting position
    t.pendown()

    distance = 300  # length of each side
    level = 3       # recursion depth
    drawKochSnowflake(t, distance, level)

    turtle.done()

if __name__ == "__main__":
    main()