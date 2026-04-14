import turtle

# Setup
t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# Draw a simple dashed line
for _ in range(10):
    t.forward(20)   # Draw line
    t.penup()       # Lift pen
    t.forward(10)   # Skip space
    t.pendown()     # Lower pen

turtle.done()