import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(4)

# List of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a square with changing colors
for i in range(4):
    t.pencolor(colors[i])
    t.forward(100)
    t.left(90)

turtle.done()