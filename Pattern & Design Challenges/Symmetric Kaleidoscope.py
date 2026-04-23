import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(3)

# Colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]

# Function to draw a petal
def draw_petal(size, angle):
    t.circle(size, angle)
    t.left(180 - angle)
    t.circle(size, angle)
    t.left(180 - angle)

# Draw kaleidoscope with petals
for i in range(24):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[(i+4) % len(colors)])
    t.begin_fill()
    
    draw_petal(80, 60)
    
    t.end_fill()
    t.left(15)

t.hideturtle()
turtle.done()