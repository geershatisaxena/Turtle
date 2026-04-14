import turtle

# Setup
t = turtle.Turtle()
t.speed(9)
t.pensize(4)
turtle.bgcolor("black")

# Colors for each side
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw octagon with different color per side
for i in range(8):
    t.pencolor(colors[i % len(colors)])
    t.forward(100)
    t.left(45)

# Draw inner hexagon with color change
t.penup()
t.goto(0, 0)
t.pendown()

for i in range(6):
    t.pencolor(colors[i + 2 % len(colors)])
    t.forward(80)
    t.left(60)

t.hideturtle()
turtle.done()