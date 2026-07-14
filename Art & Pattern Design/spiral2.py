import turtle
import math
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Galaxy Spiral Pattern")

# Turtle setup
galaxy = turtle.Turtle()
galaxy.speed(5)
galaxy.width(2)
galaxy.hideturtle()

# Draw galaxy spiral
for i in range(1000):
    hue = i / 1000
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    galaxy.pencolor(color)

    angle = i * 0.3
    radius = 0.4 * i

    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))

    galaxy.goto(x, y)
    galaxy.dot(i / 25 + 2)

screen.mainloop()