import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw main rotating squares
for i in range(36):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+2) % len(colors)])
    t.begin_fill()
    
    # Draw outer square
    for _ in range(4):
        t.forward(150)
        t.left(90)
    
    t.end_fill()
    
    # Draw inner square
    t.penup()
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.pendown()
    
    t.pencolor("white")
    for _ in range(4):
        t.forward(90)
        t.left(90)
    
    # Return to center
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    
    t.left(10)  # Rotate

t.hideturtle()
turtle.done()