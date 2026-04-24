import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Draw circular ring of rotating squares
ring_radius = 160
num_squares = 16
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

for i in range(num_squares):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * (360 / num_squares))
    t.forward(ring_radius)
    
    # Rotate square based on position
    t.setheading(i * (360 / num_squares) + 45)
    t.pendown()
    
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+2) % len(colors)])
    t.begin_fill()
    
    # Draw square (diamond orientation)
    for _ in range(4):
        t.forward(35)
        t.left(90)
    
    t.end_fill()

t.hideturtle()
turtle.done()