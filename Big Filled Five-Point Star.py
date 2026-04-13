import turtle

# Setup
t = turtle.Turtle()
t.speed(9)
turtle.bgcolor("black")
t.pensize(3)

# Draw filled star
side_length = 250
t.fillcolor("gold")
t.begin_fill()

for _ in range(5):
    t.forward(side_length)
    t.right(144)

t.end_fill()

t.hideturtle()
turtle.done()