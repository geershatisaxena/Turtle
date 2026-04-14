import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(1000)
turtle.bgcolor("black")
t.pensize(15)

# Function to get gradient colors
def gradient_color(step, total_steps):
    """Return a color based on position in gradient"""
    r = math.sin(step / total_steps * math.pi) ** 2
    g = math.sin((step / total_steps * math.pi) + 2) ** 2
    b = math.sin((step / total_steps * math.pi) + 4) ** 2
    return (r, g, b)

# Draw circle with gradient
radius = 200
steps = 360

for i in range(steps):
    color = gradient_color(i, steps)
    t.pencolor(color)
    t.circle(radius, 1)  # Draw 1 degree at a time

t.hideturtle()
turtle.done()