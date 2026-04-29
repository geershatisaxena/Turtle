import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("darkgreen")
t.pensize(2)

# Draw rose-like flower
colors = ["crimson", "red", "darkred", "firebrick", "indianred"]
num_petals = 18

for i in range(num_petals):
    t.fillcolor(colors[i % len(colors)])
    t.begin_fill()
    
    # Draw petal with varying size
    size = 80 - i * 2
    t.circle(size, 80)
    t.left(100)
    t.circle(size, 80)
    t.left(100)
    
    t.end_fill()
    t.left(360 / num_petals)

# Center
t.penup()
t.goto(0, -20)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(20)
t.end_fill()

t.hideturtle()
turtle.done()