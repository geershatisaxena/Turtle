import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Draw circular ring of triangles
radius = 170
num_triangles = 12
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

for i in range(num_triangles):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * (360 / num_triangles))
    t.forward(radius)
    t.pendown()
    
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+2) % len(colors)])
    t.begin_fill()
    
    # Draw equilateral triangle
    for _ in range(3):
        t.forward(50)
        t.left(120)
    
    t.end_fill()

t.hideturtle()
turtle.done()