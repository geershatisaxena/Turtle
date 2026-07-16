import turtle
import random
import math

# ======================================
# Generative Neon Modern Art
# ======================================

screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Neon Modern Art Generator")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

screen.tracer(0)
screen.colormode(255)

# Neon palette
colors = [
    (0, 255, 255),
    (255, 0, 255),
    (255, 255, 0),
    (0, 255, 120),
    (255, 120, 0),
    (255, 255, 255)
]

# Draw glowing geometric flower
def flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.pencolor(random.choice(colors))
    t.pensize(random.randint(2, 5))

    petals = random.randint(12, 36)
    radius = random.randint(40, 120)

    for i in range(petals):
        angle = 360 / petals

        t.circle(radius, 60)
        t.left(120)
        t.circle(radius, 60)
        t.left(180 - angle)

# Draw random wave
def wave(y):
    t.penup()
    t.goto(-500, y)
    t.pendown()

    t.pencolor(random.choice(colors))
    t.pensize(random.randint(2, 4))

    for x in range(-500, 501, 5):
        yy = y + 40 * math.sin(x / 40 + random.random())
        t.goto(x, yy)

# Draw radial explosion
def explosion(x, y):
    rays = random.randint(20, 60)

    for _ in range(rays):
        t.penup()
        t.goto(x, y)
        t.pendown()

        t.pencolor(random.choice(colors))
        t.pensize(random.randint(1, 4))

        t.setheading(random.randint(0, 360))
        t.forward(random.randint(50, 250))

# Draw floating squares
def square_cluster():
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)

    for _ in range(random.randint(5, 15)):
        t.penup()
        t.goto(
            x + random.randint(-50, 50),
            y + random.randint(-50, 50)
        )
        t.pendown()

        size = random.randint(20, 80)

        t.pencolor(random.choice(colors))
        t.setheading(random.randint(0, 360))

        for _ in range(4):
            t.forward(size)
            t.left(90)

# Create artwork
for _ in range(5):
    flower(
        random.randint(-350, 350),
        random.randint(-250, 250)
    )

for y in range(-250, 251, 80):
    wave(y)

for _ in range(6):
    explosion(
        random.randint(-350, 350),
        random.randint(-250, 250)
    )

for _ in range(10):
    square_cluster()

# Add glowing stars
for _ in range(1000):
    t.penup()
    t.goto(
        random.randint(-500, 500),
        random.randint(-400, 400)
    )
    t.dot(
        random.randint(2, 6),
        random.choice(colors)
    )

screen.update()
screen.mainloop()