import turtle

# Setup
t = turtle.Turtle()
t.speed(8)
t.pensize(4)
turtle.bgcolor("black")

# Draw dashed line with increasing dash sizes
x = -350
y = 0

t.penup()
t.goto(x, y)
t.pendown()
t.pencolor("yellow")

dash_size = 5
for _ in range(20):
    t.forward(dash_size)
    t.penup()
    t.forward(10)  # Constant gap
    t.pendown()
    dash_size += 3  # Increase dash size each time

# Add explanation
t.penup()
t.goto(-350, -40)
t.pencolor("white")
t.write("Dashed line with INCREASING dash sizes", font=("Arial", 14, "bold"))

t.hideturtle()
turtle.done()