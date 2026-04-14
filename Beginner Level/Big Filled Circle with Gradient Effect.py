import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")  # Black background for contrast

# Make circle BIG
radius = 200

# Position to center
t.penup()
t.goto(0, -radius)
t.pendown()

# Draw filled circle with gradient-like effect
t.fillcolor("deepskyblue")
t.begin_fill()
t.circle(radius)
t.end_fill()

# Add outline
t.pencolor("gold")
t.pensize(5)
t.circle(radius)

t.hideturtle()
turtle.done()