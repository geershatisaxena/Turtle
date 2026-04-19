import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("skyblue")
t.pensize(3)

# Draw sun body
t.fillcolor("gold")
t.begin_fill()
t.circle(75)
t.end_fill()

# Draw zigzag rays
for i in range(12):
    t.penup()
    t.goto(0, 75)
    t.setheading(i * 30)
    t.pendown()
    t.pencolor("orange")
    t.pensize(4)
    
    # Draw zigzag ray
    for _ in range(3):
        t.forward(15)
        t.left(45)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.left(45)
    
    t.forward(15)

t.hideturtle()
turtle.done()