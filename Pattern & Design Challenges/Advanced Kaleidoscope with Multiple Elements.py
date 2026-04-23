import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(3)

# Color palette
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta"]

# Draw complex kaleidoscope
for i in range(60):
    t.pencolor(colors[i % len(colors)])
    
    # Draw outer triangle
    for _ in range(3):
        t.forward(150)
        t.left(120)
    
    # Draw inner star
    t.penup()
    t.forward(50)
    t.pendown()
    for _ in range(5):
        t.forward(30)
        t.backward(30)
        t.right(72)
    
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(6)  # 360/60 = 6 degrees

t.hideturtle()
turtle.done()