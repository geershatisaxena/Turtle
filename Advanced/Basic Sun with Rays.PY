import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(3)

# Draw sun body (circle)
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

# Draw rays using a loop
for _ in range(12):
    t.penup()
    t.goto(0, 50)  # Start from edge of sun
    t.pendown()
    t.forward(40)  # Ray length
    t.backward(40)  # Return to start
    t.left(30)  # Rotate for next ray

t.hideturtle()
turtle.done()