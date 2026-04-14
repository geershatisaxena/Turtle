import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(0.5)

# Golden ratio (phi)
phi = (1 + math.sqrt(5)) / 2

# Draw golden spiral
for i in range(800):
    t.pencolor("yellow")
    radius = i * 0.5
    t.circle(radius, 30)  # Draw arc

t.hideturtle()
turtle.done()