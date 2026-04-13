import turtle

t = turtle.Turtle()
t.pensize(3)  # Thicker outline

width = 400
height = 200

t.fillcolor("skyblue")
t.begin_fill()

for _ in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)

t.end_fill()
t.hideturtle()
turtle.done()