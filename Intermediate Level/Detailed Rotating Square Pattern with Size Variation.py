import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(3)

# Draw rotating squares with changing size
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(79):
    size = 50 + i * 2  # Increasing size
    t.pencolor(colors[i % len(colors)])
    
    # Draw square
    for _ in range(4):
        t.forward(size)
        t.left(90)
    
    t.left(5)  # Rotate for next square

t.hideturtle()
turtle.done()