import turtle

# Setup
t = turtle.Turtle()
t.speed(8)

# Draw a five-point star
side_length = 200

for _ in range(5):
    t.forward(side_length)
    t.right(144)  # 180 - 36 = 144 degrees

turtle.done()