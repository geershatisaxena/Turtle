import turtle

# Setup
t = turtle.Turtle()
t.speed(19)
turtle.bgcolor("white")
t.pensize(2)

# Draw target pattern with alternating fills
radius = 200
colors = ["red", "green", "blue", "white", "yellow", "pink", "purple", "black","cyan","magenta","lime","orange"]

for i in range(12):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    radius -= 25

t.hideturtle()
turtle.done()