import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Tribal Art Symmetry Pattern")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.color("white")
t.pensize(2)

# Function to draw a tribal motif
def tribal_motif(size):
    for _ in range(6):
        t.forward(size)
        t.right(45)
        t.forward(size / 2)
        t.backward(size / 2)
        t.left(90)
        t.forward(size / 2)
        t.backward(size / 2)
        t.right(45)
        t.left(60)

# Draw symmetrical tribal pattern
for angle in range(0, 360, 15):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(40)
    t.pendown()

    tribal_motif(50)

# Central decorative circle
t.penup()
t.goto(0, -30)
t.pendown()
t.color("cyan")
t.circle(30)

# Inner star
t.color("gold")
for _ in range(8):
    t.forward(60)
    t.backward(60)
    t.left(45)

t.hideturtle()
turtle.done()