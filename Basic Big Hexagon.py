import turtle

# Setup
t = turtle.Turtle()
t.speed(8)

# Big hexagon
side_length = 200

# Draw hexagon using loop
for _ in range(6):
    t.forward(side_length)
    t.left(60)  # 360/6 = 60 degrees

turtle.done()