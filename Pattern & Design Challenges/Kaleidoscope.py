import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Draw kaleidoscope pattern
for i in range(36):  # 36 segments
    # Draw a shape
    for _ in range(3):  # Triangle shape
        t.forward(100)
        t.left(120)
    
    t.left(10)  # Rotate for next segment

t.hideturtle()
turtle.done()