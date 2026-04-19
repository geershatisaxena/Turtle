import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("lightblue")
t.pensize(3)

# Draw sun body
t.fillcolor("yellow")
t.begin_fill()
t.circle(70)
t.end_fill()

# Draw triangular rays
for i in range(12):
    t.penup()
    t.goto(0, 70)
    t.setheading(i * 30)  # Point outward
    t.pendown()
    
    # Draw triangle ray
    t.fillcolor("orange")
    t.begin_fill()
    t.forward(40)
    t.left(30)
    t.forward(20)
    t.left(120)
    t.forward(20)
    t.left(30)
    t.forward(40)
    t.end_fill()

t.hideturtle()
turtle.done()