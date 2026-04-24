import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
rings = [(120, 20, 12), (180, 15, 16), (240, 10, 20)]  # (radius, shape_size, count)

# Function to draw a flower/circle shape
def draw_flower(size):
    for _ in range(6):
        t.circle(size, 60)
        t.left(120)
        t.circle(size, 60)
        t.left(60)

# Draw multiple rings
for ring_radius, shape_size, num_shapes in rings:
    for i in range(num_shapes):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * (360 / num_shapes))
        t.forward(ring_radius)
        t.pendown()
        
        t.pencolor(colors[i % len(colors)])
        t.fillcolor(colors[(i + ring_radius // 20) % len(colors)])
        t.begin_fill()
        
        draw_flower(shape_size)
        
        t.end_fill()

t.hideturtle()
turtle.done()