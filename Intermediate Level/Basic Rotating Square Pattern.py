import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
t.pensize(2)

# Draw rotating squares
for i in range(36):  # 36 squares, each rotated by 10 degrees
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.left(10)  # Rotate for next square

t.hideturtle()
turtle.done()