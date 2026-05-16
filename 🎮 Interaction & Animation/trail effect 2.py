# Neon Snake Trail Effect Animation
# Creates a smooth fading neon trail illusion.

import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Trail Animation")
screen.setup(900, 700)
screen.tracer(0)

# Main turtle
snake = turtle.Turtle()
snake.shape("circle")
snake.color("cyan")
snake.penup()
snake.speed(0)

# Trail turtles list
trails = []

# Colors for glowing effect
colors = [
    "#00FFFF",
    "#00CCFF",
    "#0099FF",
    "#0066FF",
    "#0033FF",
    "#0011AA"
]

angle = 0

while True:

    # Move in wave pattern
    x = math.sin(math.radians(angle)) * 250
    y = math.sin(math.radians(angle * 2)) * 150

    snake.goto(x, y)

    # Create new trail dot
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.shape("circle")
    t.shapesize(0.8)
    t.color(colors[angle % len(colors)])
    t.goto(x, y)
    t.stamp()

    trails.append(t)

    # Remove oldest trails for fading illusion
    if len(trails) > 25:
        old = trails.pop(0)
        old.clear()

    angle += 5

    screen.update()

turtle.done()