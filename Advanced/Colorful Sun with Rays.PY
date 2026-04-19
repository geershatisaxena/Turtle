import turtle

# Setup
t = turtle.Turtle()
t.speed(9)
turtle.bgcolor("skyblue")
t.pensize(4)

# Draw sun body
t.fillcolor("gold")
t.begin_fill()
t.circle(60)
t.end_fill()

# Draw rays with different colors
colors = ["orange", "red", "orange", "yellow", "orange", "red", "orange", "yellow"]

for i in range(16):
    t.pencolor(colors[i % len(colors)])
    t.penup()
    t.goto(0, 60)
    t.pendown()
    t.forward(50)
    t.backward(50)
    t.left(22.5)  # 360/16 = 22.5 degrees

t.hideturtle()
turtle.done()