import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(4)

# Rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
side_length = 200

# Draw each point with different color
for i in range(5):
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[i % len(colors)])
    t.begin_fill()
    
    # Draw one point of the star
    t.forward(side_length)
    t.right(144)
    
    t.end_fill()

# Complete the star
t.pencolor("white")
t.pensize(5)
for _ in range(5):
    t.forward(side_length)
    t.right(144)

t.hideturtle()
turtle.done()