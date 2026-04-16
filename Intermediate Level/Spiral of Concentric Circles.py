import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Draw offset concentric circles (spiral effect)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

for i in range(50):
    t.pencolor(colors[i % len(colors)])
    radius = i * 8
    t.penup()
    t.goto(i * 2, -radius)  # Offset center
    t.pendown()
    t.circle(radius)

t.hideturtle()
turtle.done()