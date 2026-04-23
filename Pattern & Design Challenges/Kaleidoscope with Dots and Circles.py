import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(1)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw kaleidoscope pattern
for i in range(36):
    t.pencolor(colors[i % len(colors)])
    
    # Draw a circle
    t.circle(50)
    
    # Draw dots along the circle
    t.penup()
    for angle in range(0, 360, 60):
        t.goto(0, 0)
        t.setheading(angle + i * 10)
        t.forward(50)
        t.dot(10)
    
    t.pendown()
    t.left(10)

t.hideturtle()
turtle.done()