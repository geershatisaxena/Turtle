import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
t.pensize(2)

# Draw a simple spiral
for i in range(300):
    t.forward(i * 2)  # Increasing distance
    t.left(90)        # 90-degree turn

turtle.done()