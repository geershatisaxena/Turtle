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

# Draw kaleidoscope with gradient
for i in range(72):
    color = gradient_color(i, 72)
    t.pencolor(color)
    
    # Draw star pattern
    for _ in range(5):
        t.forward(100)
        t.left(144)
    
    t.left(5)

t.hideturtle()
turtle.done()