import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(3)

# Colors for squares
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw rotating colorful squares
for i in range(36):
    t.pencolor(colors[i % len(colors)])
    for _ in range(4):
        t.forward(120)
        t.left(90)
    t.left(10)

t.hideturtle()
turtle.done()