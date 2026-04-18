import turtle

# Setup5
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(3)

# Draw rotating squares in a spiral pattern
colors = ["red", "cyan", "yellow", "lime", "magenta", "orange", "blue", "purple"]

size = 20
for i in range(60):
    t.pencolor(colors[i % len(colors)])
    
    # Draw square
    for _ in range(4):
        t.forward(size)
        t.left(90)
    
    # Move outward and rotate
    t.penup()
    t.forward(10)
    t.left(15)
    t.pendown()
    
    size += 3  # Increase size

t.hideturtle()
turtle.done()