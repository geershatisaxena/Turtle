import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
t.pensize(2)

# Draw spiral of triangles
length = 20
for i in range(50):
    # Draw triangle
    for _ in range(3):
        t.forward(length)
        t.left(120)
    
    # Move and rotate for next triangle
    t.left(15)
    length += 3

t.hideturtle()
turtle.done()