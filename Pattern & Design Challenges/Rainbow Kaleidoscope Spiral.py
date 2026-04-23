import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw kaleidoscope spiral
for i in range(180):
    t.pencolor(colors[i % len(colors)])
    
    # Draw expanding shape
    for _ in range(4):
        t.forward(i * 0.5)
        t.left(90)
    
    t.left(2)

t.hideturtle()
turtle.done()