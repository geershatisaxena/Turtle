import turtle

# Setup
t = turtle.Turtle()
t.speed(25)
t.pensize(2)

# Draw concentric circles
radius = 20
for i in range(18):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
    radius += 20

t.hideturtle()
turtle.done()