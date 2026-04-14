import turtle

# Setup
t = turtle.Turtle()
t.speed(1000)
turtle.bgcolor("black")
t.pensize(1)

# Color list
colors = ["red", "cyan", "yellow", "lime", "magenta", "orange"]

# Draw star with changing colors
for i in range(5100):
    t.pencolor(colors[i % len(colors)])
    t.forward(350)
    t.left(123)  # Angle for star pattern

t.hideturtle()
turtle.done()