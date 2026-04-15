import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Draw concentric circles
radii = [50, 100, 150, 200, 250]
colors = ["cyan", "blue", "green", "yellow", "red"]

# Draw circles
for i, radius in enumerate(radii):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.pencolor(colors[i])
    t.circle(radius)

# Draw radial lines (spokes)
t.pencolor("white")
t.pensize(1)
for angle in range(0, 360, 50):
    x = 280 * math.cos(math.radians(angle))
    y = 280 * math.sin(math.radians(angle))
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(x, y)

# Center point
t.penup()
t.goto(0, 0)
t.dot(20, "red")
t.dot(10, "white")

t.hideturtle()
turtle.done()