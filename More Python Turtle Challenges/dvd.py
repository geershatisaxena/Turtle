# DVD Logo Bouncing Around the Screen
# Python Turtle

import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("DVD Logo Screensaver")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# DVD Logo
dvd = turtle.Turtle()
dvd.shape("square")
dvd.shapesize(stretch_wid=2, stretch_len=4)
dvd.color("red")
dvd.penup()

# Movement speed
dx = 3
dy = 3

# Screen boundaries
WIDTH = 390
HEIGHT = 290

colors = [
    "red", "cyan", "yellow", "lime",
    "magenta", "orange", "white", "blue"
]

while True:
    x = dvd.xcor()
    y = dvd.ycor()

    dvd.goto(x + dx, y + dy)

    # Bounce off left/right walls
    if dvd.xcor() > WIDTH or dvd.xcor() < -WIDTH:
        dx *= -1
        dvd.color(random.choice(colors))

    # Bounce off top/bottom walls
    if dvd.ycor() > HEIGHT or dvd.ycor() < -HEIGHT:
        dy *= -1
        dvd.color(random.choice(colors))

    screen.update()