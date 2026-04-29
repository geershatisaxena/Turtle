import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Colors for petals
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]
num_petals = 12

for i in range(num_petals):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+1) % len(colors)])
    t.begin_fill()
    
    # Draw petal
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(120)
    
    t.end_fill()
    t.left(360 / num_petals)

t.hideturtle()
turtle.done()