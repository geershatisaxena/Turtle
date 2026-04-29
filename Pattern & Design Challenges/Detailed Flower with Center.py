import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("lightblue")
t.pensize(3)

# Draw petals
num_petals = 12
petal_color = "pink"
for i in range(num_petals):
    t.fillcolor(petal_color)
    t.begin_fill()
    
    # Draw petal
    t.circle(80, 60)
    t.left(120)
    t.circle(80, 60)
    t.left(120)
    
    t.end_fill()
    t.left(360 / num_petals)

# Draw flower center
t.penup()
t.goto(0, -30)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

# Draw center dots
t.penup()
t.goto(0, 0)
t.dot(15, "orange")
t.dot(8, "brown")

t.hideturtle()
turtle.done()