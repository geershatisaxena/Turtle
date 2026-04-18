import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Draw 3D-like rotating squares
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]
num_squares = 90

for i in range(num_squares):
    t.pencolor(colors[i % len(colors)])
    
    # Vary pen size for depth effect
    t.pensize((i % 5) + 1)
    
    # Draw square with perspective (different side lengths)
    t.forward(150)
    t.left(90)
    t.forward(150 - i * 1.5)
    t.left(90)
    t.forward(150 - i * 3)
    t.left(90)
    t.forward(150 - i * 1.5)
    t.left(90)
    
    t.left(4)  # Rotate

t.update()
t.hideturtle()
turtle.done()