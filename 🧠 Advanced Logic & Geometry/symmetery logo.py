import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Symmetrical Logo Design")

# Turtle setup
logo = turtle.Turtle()
logo.speed(0)
logo.pensize(3)
logo.color("cyan")

# Function to draw one symmetrical pattern
def draw_pattern(size):
    for _ in range(6):
        logo.forward(size)
        logo.right(60)
        logo.forward(size // 2)
        logo.backward(size // 2)
        logo.left(120)

# Draw logo using symmetry
for i in range(12):
    draw_pattern(100)
    logo.right(30)

# Add center circle
logo.penup()
logo.goto(0, -40)
logo.pendown()
logo.color("white")
logo.circle(40)

logo.hideturtle()

turtle.done()