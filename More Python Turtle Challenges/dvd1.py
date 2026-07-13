# Bouncing DVD Logo with Trail Effect
# Python Turtle

import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("DVD Logo Trail Animation")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# Logo
logo = turtle.Turtle()
logo.shape("square")
logo.shapesize(stretch_wid=2, stretch_len=5)
logo.color("cyan")
logo.penup()

# Movement
dx = 4
dy = 4

colors = [
    "red", "yellow", "lime", "cyan",
    "magenta", "orange", "white", "blue"
]

while True:
    x = logo.xcor()
    y = logo.ycor()

    # Stamp current position to create trail
    logo.stamp()

    logo.goto(x + dx, y + dy)

    # Wall collisions
    if logo.xcor() > 380 or logo.xcor() < -380:
        dx *= -1
        logo.color(random.choice(colors))

    if logo.ycor() > 280 or logo.ycor() < -280:
        dy *= -1
        logo.color(random.choice(colors))

    screen.update()

    # Prevent too many trail stamps
    if len(screen.turtles()) > 200:
        logo.clearstamps()