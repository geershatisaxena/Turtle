import turtle
import random

# Setup
t = turtle.Turtle()
t.speed(15)
t.pensize(2)
turtle.bgcolor("black")

# Function to get random color
def random_color():
    """Generate a random RGB color"""
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Draw pattern with random colors
for i in range(500):
    t.pencolor(random_color())
    t.forward(i)
    t.left(91)

t.hideturtle()
turtle.done()