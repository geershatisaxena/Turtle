import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw filled kaleidoscope pattern
for i in range(36):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+2) % len(colors)])
    t.begin_fill()
    
    # Draw triangle
    for _ in range(3):
        t.forward(100)
        t.left(120)
    
    t.end_fill()
    t.left(10)

t.hideturtle()
turtle.done()