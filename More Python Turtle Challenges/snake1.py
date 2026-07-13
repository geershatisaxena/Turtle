# Rainbow Snake Trail Following the Mouse
# Python Turtle

import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Rainbow Snake Trail")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# Colors
colors = [
    "red", "orange", "yellow",
    "lime", "cyan", "blue",
    "magenta", "white"
]

# Snake segments
segments = []

for i in range(40):
    seg = turtle.Turtle()
    seg.shape("circle")
    seg.color(colors[i % len(colors)])
    seg.penup()
    seg.goto(0, 0)
    segments.append(seg)

# Mouse position
target_x = 0
target_y = 0

def move_mouse(x, y):
    global target_x, target_y
    target_x = x
    target_y = y

screen.onscreenclick(move_mouse)

while True:

    # Move head toward mouse
    head = segments[0]

    new_x = head.xcor() + (target_x - head.xcor()) * 0.08
    new_y = head.ycor() + (target_y - head.ycor()) * 0.08

    head.goto(new_x, new_y)

    # Follow effect
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()

        segments[i].goto(
            segments[i].xcor() + (x - segments[i].xcor()) * 0.35,
            segments[i].ycor() + (y - segments[i].ycor()) * 0.35
        )

    screen.update()
    time.sleep(0.01)