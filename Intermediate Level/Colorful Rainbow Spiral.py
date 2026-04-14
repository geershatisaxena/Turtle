import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw colorful spiral
for i in range(400):
    t.pencolor(colors[i % len(colors)])
    t.forward(i)
    t.left(59)  # Angle for spiral effect

t.hideturtle()
turtle.done()