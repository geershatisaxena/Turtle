import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(3)

# Colors for kaleidoscope
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw kaleidoscope pattern
for i in range(36):
    t.pencolor(colors[i % len(colors)])
    
    # Draw complex shape
    for _ in range(4):
        t.forward(120)
        t.left(90)
    
    t.left(10)

t.hideturtle()
turtle.done()