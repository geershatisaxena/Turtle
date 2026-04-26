import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw colorful spiral of triangles
length = 15
for i in range(80):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+1) % len(colors)])
    t.begin_fill()
    
    # Draw triangle
    for _ in range(3):
        t.forward(length)
        t.left(120)
    
    t.end_fill()
    
    # Move and rotate
    t.left(20)
    length += 2

t.hideturtle()
turtle.done()