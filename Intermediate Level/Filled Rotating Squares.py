import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Draw filled rotating squares
colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "cyan"]

for i in range(48):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+4) % len(colors)])
    t.begin_fill()
    
    for _ in range(4):
        t.forward(150)
        t.left(90)
    
    t.end_fill()
    t.left(7.5)  # Rotate 7.5 degrees each time

t.hideturtle()
turtle.done()