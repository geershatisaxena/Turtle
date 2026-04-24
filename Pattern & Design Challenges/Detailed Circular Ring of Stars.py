import turtle

# Setup
t = turtle.Turtle()
t.speed(100)
turtle.bgcolor("black")
t.pensize(2)

# Draw circular ring of stars
radius = 180
num_stars = 12
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

for i in range(num_stars):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * (360 / num_stars))
    t.forward(radius)
    t.pendown()
    
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+1) % len(colors)])
    t.begin_fill()
    
    # Draw a 5-point star
    for _ in range(5):
        t.forward(40)
        t.left(144)
    
    t.end_fill()

t.hideturtle()
turtle.done()