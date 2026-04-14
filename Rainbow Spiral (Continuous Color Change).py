import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(3)

# Rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw a colorful spiral
for i in range(155):
    t.pencolor(colors[i % len(colors)])
    t.forward(i * 2)
    t.left(59)

t.hideturtle()
turtle.done()