import turtle
import random
import math

# ==================================
# Abstract Modern Art Generator
# ==================================

screen = turtle.Screen()
screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("Abstract Modern Art Generator")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

screen.tracer(0)
screen.colormode(255)

# Color palette
palette = [
    (255, 99, 71),    # Tomato
    (0, 255, 255),    # Cyan
    (255, 215, 0),    # Gold
    (255, 105, 180),  # Pink
    (50, 205, 50),    # Lime
    (138, 43, 226),   # Violet
    (255, 255, 255)   # White
]

# Draw random circles
def random_circle():
    t.penup()
    x = random.randint(-450, 450)
    y = random.randint(-350, 350)
    r = random.randint(10, 80)

    t.goto(x, y - r)
    t.pendown()

    t.color(random.choice(palette))
    t.pensize(random.randint(1, 5))

    if random.random() < 0.5:
        t.fillcolor(random.choice(palette))
        t.begin_fill()
        t.circle(r)
        t.end_fill()
    else:
        t.circle(r)

# Draw random polygon
def random_polygon():
    sides = random.randint(3, 8)

    t.penup()
    t.goto(
        random.randint(-400, 400),
        random.randint(-300, 300)
    )
    t.setheading(random.randint(0, 360))
    t.pendown()

    t.color(random.choice(palette))
    t.fillcolor(random.choice(palette))

    size = random.randint(20, 120)

    if random.random() < 0.7:
        t.begin_fill()

    for _ in range(sides):
        t.forward(size)
        t.left(360 / sides)

    if random.random() < 0.7:
        t.end_fill()

# Draw random line burst
def random_lines():
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)

    for _ in range(random.randint(5, 20)):
        t.penup()
        t.goto(x, y)
        t.pendown()

        t.color(random.choice(palette))
        t.pensize(random.randint(1, 6))

        angle = random.randint(0, 360)
        length = random.randint(30, 200)

        t.setheading(angle)
        t.forward(length)

# Draw random spiral
def random_spiral():
    t.penup()
    t.goto(
        random.randint(-300, 300),
        random.randint(-250, 250)
    )
    t.pendown()

    t.color(random.choice(palette))
    t.pensize(random.randint(1, 4))

    size = random.randint(1, 5)

    for i in range(random.randint(30, 80)):
        t.forward(i * size / 5)
        t.left(random.randint(15, 45))

# Generate artwork
for _ in range(25):
    random_circle()

for _ in range(20):
    random_polygon()

for _ in range(15):
    random_lines()

for _ in range(10):
    random_spiral()

# Add random dots for texture
for _ in range(500):
    t.penup()
    t.goto(
        random.randint(-500, 500),
        random.randint(-400, 400)
    )
    t.dot(
        random.randint(2, 8),
        random.choice(palette)
    )

screen.update()
screen.mainloop()