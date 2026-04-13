import turtle

# Setup
t = turtle.Turtle()
t.speed(9)
turtle.bgcolor("black")
t.pensize(3)

# Square parameters
square_size = 100
spacing = 30
start_x = -300
start_y = -50

# Colors for each square
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# Draw 7 filled squares in a row
for i in range(7):
    t.penup()
    t.goto(start_x + i * (square_size + spacing), start_y)
    t.pendown()
    
    t.fillcolor(colors[i % len(colors)])
    t.begin_fill()
    
    for _ in range(4):
        t.forward(square_size)
        t.right(90)
    
    t.end_fill()

t.hideturtle()
turtle.done()