import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(4)

# Function to draw dashed line
def dashed_forward(distance, dash, gap):
    segments = distance // (dash + gap)
    for _ in range(segments):
        t.forward(dash)
        t.penup()
        t.forward(gap)
        t.pendown()

# Draw a dashed square
t.fillcolor("lightblue")
t.begin_fill()

for _ in range(4):
    dashed_forward(200, 20, 15)
    t.left(90)

t.end_fill()

# Add title
t.penup()
t.goto(0, 150)
t.pencolor("darkblue")
t.write("Dashed Square", align="center", font=("Arial", 20, "bold"))

t.hideturtle()
turtle.done()