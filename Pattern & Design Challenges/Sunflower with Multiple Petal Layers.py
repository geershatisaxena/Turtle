import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Colors
petal_colors = ["gold", "orange", "darkorange"]
center_colors = ["brown", "saddlebrown"]

# Outer petals
num_petals = 24
for i in range(num_petals):
    t.fillcolor(petal_colors[i % len(petal_colors)])
    t.begin_fill()
    
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(120)
    
    t.end_fill()
    t.left(360 / num_petals)

# Inner petals
t.penup()
t.goto(0, -30)
t.pendown()
num_petals = 12
for i in range(num_petals):
    t.fillcolor(petal_colors[(i+1) % len(petal_colors)])
    t.begin_fill()
    
    t.circle(50, 60)
    t.left(120)
    t.circle(50, 60)
    t.left(120)
    
    t.end_fill()
    t.left(360 / num_petals)

# Center
t.penup()
t.goto(0, -25)
t.pendown()
t.fillcolor("saddlebrown")
t.begin_fill()
t.circle(25)
t.end_fill()

# Center seeds pattern
t.pencolor("gold")
t.pensize(1)
for i in range(20):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 18)
    t.forward(15)
    t.pendown()
    t.dot(3, "gold")

t.hideturtle()
turtle.done()