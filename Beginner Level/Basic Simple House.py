import turtle

# Setup
t = turtle.Turtle()
t.speed(5)
t.pensize(3)

# Draw square base
for _ in range(4):
    t.forward(150)  # Wall length
    t.left(90)

# Draw triangle roof
t.left(45)          # Angle for roof
t.forward(106)      # Roof side (approx: 150 / cos(45))
t.left(90)          # Turn for other side
t.forward(106)      # Other roof side

turtle.done()