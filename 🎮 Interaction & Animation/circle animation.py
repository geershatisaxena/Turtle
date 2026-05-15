import turtle
import time
import math

# Screen setup
screen = turtle.Screen()
screen.title("Spinning Loading Circle")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Turtle setup
loader = turtle.Turtle()
loader.hideturtle()
loader.speed(0)
loader.pensize(8)

colors = [
    "red", "orange", "yellow",
    "green", "cyan", "blue", "magenta"
]

radius = 100
angle = 0

# Animation loop
while True:
    loader.clear()

    # Draw rotating dots
    for i in range(12):

        current_angle = angle + (i * 30)

        # Convert angle to radians
        rad = math.radians(current_angle)

        # Calculate x and y positions
        x = radius * math.cos(rad)
        y = radius * math.sin(rad)

        loader.penup()
        loader.goto(x, y)

        # Dot size decreases for fade effect
        size = 20 - i

        loader.dot(size, colors[i % len(colors)])

    angle += 10

    screen.update()
    time.sleep(0.05)