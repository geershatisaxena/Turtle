import turtle
import time

# Screen Setup
screen = turtle.Screen()
screen.title("Water Ripple Animation")
screen.bgcolor("midnight blue")
screen.setup(width=800, height=600)
screen.tracer(0)

# Ripple Turtle
ripple = turtle.Turtle()
ripple.hideturtle()
ripple.speed(0)
ripple.pensize(2)
ripple.color("cyan")

# Store active ripples
ripples = []

# Create a new ripple
def create_ripple():
    ripples.append({
        "radius": 5,
        "x": 0,
        "y": 0
    })

# Animation Loop
frame = 0

while True:

    ripple.clear()

    # Generate a new ripple every 30 frames
    if frame % 30 == 0:
        create_ripple()

    # Draw all ripples
    for r in ripples[:]:

        ripple.penup()
        ripple.goto(r["x"], r["y"] - r["radius"])
        ripple.pendown()

        ripple.circle(r["radius"])

        # Expand ripple
        r["radius"] += 2

        # Remove old ripple
        if r["radius"] > 250:
            ripples.remove(r)

    screen.update()
    time.sleep(0.03)

    frame += 1