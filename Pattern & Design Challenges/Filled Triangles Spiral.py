import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Draw spiral of filled triangles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
size = 10

for i in range(60):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+2) % len(colors)])
    t.begin_fill()
    
    # Draw equilateral triangle
    for _ in range(3):
        t.forward(size)
        t.left(120)
    
    t.end_fill()
    
    # Rotate and increase size
    t.left(18)
    size += 2.5

t.hideturtle()
turtle.done()