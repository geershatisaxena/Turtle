import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
t.pensize(2)

# Draw a circular ring of squares
radius = 150
num_shapes = 12

for i in range(num_shapes):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * (360 / num_shapes))
    t.forward(radius)
    t.pendown()
    
    # Draw square
    for _ in range(4):
        t.forward(40)
        t.left(90)

t.hideturtle()
turtle.done()