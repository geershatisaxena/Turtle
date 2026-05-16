# Trail Effect Animation (Fading Path Illusion)
# A glowing turtle leaves colorful fading trails.

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fading Trail Animation")
screen.setup(900, 700)

# Turn off automatic updates for smooth animation
screen.tracer(0)

# Create turtle
trail = turtle.Turtle()
trail.shape("circle")
trail.shapesize(0.7)
trail.speed(0)
trail.width(3)

colors = [
    "red", "orange", "yellow",
    "lime", "cyan", "blue",
    "magenta", "white"
]

angle = 0

while True:

    # Spiral movement
    x = math.cos(math.radians(angle)) * angle * 0.4
    y = math.sin(math.radians(angle)) * angle * 0.4

    trail.goto(x, y)

    # Change color continuously
    trail.pencolor(colors[angle % len(colors)])

    # Stamp creates fading illusion
    trail.stamp()

    # Remove older stamps slowly
    if angle > 40:
        trail.clearstamps(1)

    angle += 5

    # Reset when too large
    if angle > 720:
        angle = 0
        trail.clear()

    screen.update()

turtle.done()