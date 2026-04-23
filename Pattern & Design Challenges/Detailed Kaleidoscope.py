import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(1)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "cyan"]

# Draw kaleidoscope with multiple elements
for i in range(48):
    t.pencolor(colors[i % len(colors)])
    
    # Draw star-like pattern
    for _ in range(5):
        t.forward(80)
        t.backward(80)
        t.right(72)
    
    t.left(7.5)  # 360/48 = 7.5 degrees

t.hideturtle()
turtle.done()