import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(5)

# Rainbow colors
rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw concentric circles with rainbow effect
radius = 280
for i in range(7):
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.pencolor(rainbow[i])
    t.circle(radius)
    radius -= 40

# Add center glow
t.penup()
t.goto(0, 0)
t.dot(30, "white")
t.dot(15, "yellow")

t.hideturtle()
turtle.done()