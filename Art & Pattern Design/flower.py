import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Lotus Flower")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Function to draw a petal using arcs
def draw_petal():
    pen.circle(100, 60)
    pen.left(120)
    pen.circle(100, 60)
    pen.left(120)

# Draw lotus petals
pen.color("deeppink")
pen.fillcolor("pink")

for layer in range(3):
    petals = 8 + layer * 2
    size = 100 - layer * 20

    for _ in range(petals):
        pen.begin_fill()
        pen.circle(size, 60)
        pen.left(120)
        pen.circle(size, 60)
        pen.left(120)
        pen.end_fill()
        pen.left(360 / petals)

# Draw center
pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.color("gold")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Draw stem
pen.penup()
pen.goto(0, -40)
pen.setheading(-90)
pen.pendown()
pen.color("green")
pen.width(5)
pen.forward(180)

pen.hideturtle()
turtle.done()