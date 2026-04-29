import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Rainbow colors
rainbow = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
num_petals = 24

for i in range(num_petals):
    t.fillcolor(rainbow[i % len(rainbow)])
    t.begin_fill()
    
    # Draw petal
    t.circle(80, 60)
    t.left(120)
    t.circle(80, 60)
    t.left(120)
    
    t.end_fill()
    t.left(360 / num_petals)

# Center
t.penup()
t.goto(0, -30)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(30)
t.end_fill()

# Add sparkles
t.pencolor("white")
for i in range(20):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * 18)
    t.forward(95)
    t.pendown()
    t.dot(5)

t.hideturtle()
turtle.done()