import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(5)

# Colors for gradient
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw gradient dashed line
x = -350
y = 0

for i in range(30):  # 30 dashes
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(colors[i % len(colors)])
    t.forward(25)  # Dash length
    t.penup()
    t.forward(15)  # Gap
    x += 40

t.hideturtle()
turtle.done()