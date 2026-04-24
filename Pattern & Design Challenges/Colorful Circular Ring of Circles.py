import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Draw circular ring of circles
radius = 160
num_circles = 16
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

for i in range(num_circles):
    t.penup()
    t.goto(0, 0)
    t.setheading(i * (360 / num_circles))
    t.forward(radius)
    t.pendown()
    
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+1) % len(colors)])
    t.begin_fill()
    t.circle(25)
    t.end_fill()

t.hideturtle()
turtle.done()