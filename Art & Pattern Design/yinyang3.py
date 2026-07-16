import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Yin-Yang Symbol")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

radius = 150

# Draw outer circle
t.penup()
t.goto(0, -radius)
t.pendown()

# Black half
t.fillcolor("black")
t.begin_fill()
t.circle(radius, 180)
t.circle(radius / 2, 180)
t.circle(-radius / 2, 180)
t.end_fill()

# White half
t.penup()
t.goto(0, -radius)
t.pendown()

t.fillcolor("white")
t.begin_fill()
t.circle(radius, -180)
t.circle(-radius / 2, -180)
t.circle(radius / 2, -180)
t.end_fill()

# Large black circle
t.penup()
t.goto(0, radius / 2 - radius / 6)
t.pendown()
t.color("black")
t.fillcolor("black")
t.begin_fill()
t.circle(radius / 2)
t.end_fill()

# Large white circle
t.penup()
t.goto(0, -radius / 2 - radius / 6)
t.pendown()
t.color("white")
t.fillcolor("white")
t.begin_fill()
t.circle(radius / 2)
t.end_fill()

# Small white dot
t.penup()
t.goto(0, radius / 2 + 20)
t.pendown()
t.color("white")
t.dot(radius // 5)

# Small black dot
t.penup()
t.goto(0, -radius / 2 + 20)
t.pendown()
t.color("black")
t.dot(radius // 5)

# Outer border
t.penup()
t.goto(0, -radius)
t.pendown()
t.color("black")
t.circle(radius)

t.hideturtle()
screen.mainloop()