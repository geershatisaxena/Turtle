import turtle

# Setup
t = turtle.Turtle()
t.speed(8)

# Draw 5 squares in a row
square_size = 80
spacing = 20
start_x = -250

for i in range(5):
    t.penup()
    t.goto(start_x + i * (square_size + spacing), 0)
    t.pendown()
    
    for _ in range(4):
        t.forward(square_size)
        t.right(90)

turtle.done()