# Moving Snake Trail Effect
# Python Turtle

import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Snake Trail Effect")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("circle")
head.color("lime")
head.penup()
head.speed(0)

# Trail segments
segments = []

for _ in range(20):
    segment = turtle.Turtle()
    segment.shape("circle")
    segment.color("green")
    segment.penup()
    segment.goto(1000, 1000)  # Hide initially
    segments.append(segment)

# Movement
dx = 4
dy = 3

colors = [
    "lime", "cyan", "yellow",
    "orange", "magenta", "white"
]

while True:

    # Move segments
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    # Move head
    head.goto(head.xcor() + dx, head.ycor() + dy)

    # Bounce off walls
    if head.xcor() > 390 or head.xcor() < -390:
        dx *= -1
        new_color = random.choice(colors)
        head.color(new_color)

        for seg in segments:
            seg.color(new_color)

    if head.ycor() > 290 or head.ycor() < -290:
        dy *= -1
        new_color = random.choice(colors)
        head.color(new_color)

        for seg in segments:
            seg.color(new_color)

    screen.update()
    time.sleep(0.01)