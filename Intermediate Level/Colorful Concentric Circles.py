import turtle

# Setup
t = turtle.Turtle()
t.speed(60)
turtle.bgcolor("black")
t.pensize(2)

# Colors for circles
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "cyan", "magenta"]

# Draw concentric circles with different colors
radius = 30
for i in range(10):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.pencolor(colors[i % len(colors)])
    t.circle(radius)
    radius += 30

t.hideturtle()
turtle.done()