import turtle
import math

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(1)

# Function for gradient color
def gradient_color(step, max_steps):
    r = math.sin(step / max_steps * math.pi) ** 2
    g = math.sin((step / max_steps * math.pi) + 2) ** 2
    b = math.sin((step / max_steps * math.pi) + 4) ** 2
    return (r, g, b)

# Draw rotating squares with gradient
for i in range(180):
    color = gradient_color(i, 180)
    t.pencolor(color)
    
    for _ in range(4):
        t.forward(120)
        t.left(90)
    
    t.left(2)  # Slow rotation

t.hideturtle()
turtle.done()