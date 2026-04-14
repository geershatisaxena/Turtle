import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(3)
turtle.bgcolor("skyblue")  # Sky background

# Draw ground
t.penup()
t.goto(-250, -150)
t.pendown()
t.fillcolor("lightgreen")
t.begin_fill()
t.forward(500)
t.right(90)
t.forward(50)
t.right(90)
t.forward(500)
t.end_fill()

# Position for house
t.penup()
t.goto(-100, -150)
t.pendown()

# Draw square base (house body)
t.fillcolor("wheat")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Draw triangle roof
t.fillcolor("saddlebrown")
t.begin_fill()
t.left(45)
t.forward(141)  # 200 / cos(45) ≈ 141
t.left(90)
t.forward(141)
t.end_fill()

# Draw chimney
t.penup()
t.goto(50, 50)
t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.left(135)  # Reset angle
t.forward(30)
t.left(90)
t.forward(60)
t.left(90)
t.forward(30)
t.end_fill()

# Chimney smoke
t.penup()
t.goto(65, 110)
t.pencolor("lightgray")
t.pensize(5)
t.pendown()
t.circle(10)
t.penup()
t.goto(75, 125)
t.pendown()
t.circle(15)

# Draw door
t.penup()
t.goto(-30, -150)
t.pendown()
t.fillcolor("chocolate")
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(80)
t.left(90)
t.forward(50)
t.end_fill()

# Door knob
t.penup()
t.goto(5, -110)
t.pendown()
t.fillcolor("gold")
t.begin_fill()
t.circle(5)
t.end_fill()

# Draw left window
t.penup()
t.goto(-80, -70)
t.pendown()
t.fillcolor("lightyellow")
t.begin_fill()
for _ in range(4):
    t.forward(45)
    t.left(90)
t.end_fill()

# Window cross
t.penup()
t.goto(-57.5, -70)
t.pendown()
t.forward(45)
t.penup()
t.goto(-80, -47.5)
t.pendown()
t.left(90)
t.forward(45)

# Draw right window
t.penup()
t.goto(35, -70)
t.pendown()
t.fillcolor("lightyellow")
t.begin_fill()
for _ in range(4):
    t.forward(45)
    t.left(90)
t.end_fill()

# Window cross
t.penup()
t.goto(57.5, -70)
t.pendown()
t.forward(45)
t.penup()
t.goto(35, -47.5)
t.pendown()
t.left(90)
t.forward(45)

# Draw sun
t.penup()
t.goto(150, 150)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(40)
t.end_fill()

# Sun rays
t.pencolor("orange")
t.pensize(2)
for _ in range(12):
    t.penup()
    t.goto(150, 150)
    t.pendown()
    t.forward(60)
    t.backward(60)
    t.left(30)

# Draw flowers
def draw_flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(6):
        t.forward(10)
        t.backward(10)
        t.left(60)
    t.end_fill()
    t.penup()
    t.goto(x, y - 10)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.forward(5)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(5)
    t.end_fill()

draw_flower(-150, -150)
draw_flower(-120, -150)
draw_flower(130, -150)
draw_flower(160, -150)

# Title
t.penup()
t.goto(0, 200)
t.pencolor("darkblue")
t.write("MY DREAM HOUSE", align="center", font=("Arial", 24, "bold"))

t.hideturtle()
turtle.done()