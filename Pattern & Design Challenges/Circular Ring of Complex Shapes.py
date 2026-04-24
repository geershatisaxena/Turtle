import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw circular ring of complex shapes
ring_radius = 170
num_shapes = 16

for i in range(num_shapes):
    angle = i * (360 / num_shapes)
    
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(ring_radius)
    t.pendown()
    
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+2) % len(colors)])
    t.begin_fill()
    
    # Draw combined shape (square + triangle)
    # Square part
    for _ in range(4):
        t.forward(30)
        t.left(90)
    
    # Triangle part on top
    t.penup()
    t.goto(t.xcor() - 15, t.ycor())
    t.pendown()
    for _ in range(3):
        t.forward(30)
        t.left(120)
    
    t.end_fill()

t.hideturtle()
turtle.done()