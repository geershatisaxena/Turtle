import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(3)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Draw kaleidoscope pattern using nested loops
segments = 12  # Number of segments

for i in range(segments):
    t.pencolor(colors[i % len(colors)])
    
    # Draw a triangle segment
    for _ in range(10):
        t.forward(150)
        t.left(120)
    
    t.left(360 / segments)  # Rotate for next segment

t.hideturtle()
turtle.done()