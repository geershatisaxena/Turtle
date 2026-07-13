"""
Rocket Launch Animation with Smoke Effects
--------------------------------------------
Run this locally with: python rocket_launch.py
(Requires a display — turtle won't run in a headless/remote environment.)
"""

import turtle
import random

# ---------- Screen setup ----------
screen = turtle.Screen()
screen.title("Rocket Launch")
screen.bgcolor("#0b1026")          # night-sky blue
screen.setup(width=800, height=700)
screen.tracer(0)                   # manual screen updates for smooth animation

# ---------- Draw some stars (static background) ----------
star_pen = turtle.Turtle()
star_pen.hideturtle()
star_pen.penup()
star_pen.color("white")
for _ in range(80):
    x = random.randint(-390, 390)
    y = random.randint(-340, 340)
    star_pen.goto(x, y)
    star_pen.dot(random.choice([2, 2, 3]))

# ---------- Draw the ground ----------
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-400, -300)
ground.color("#2e2b26")
ground.begin_fill()
for _ in range(2):
    ground.forward(800)
    ground.left(90)
    ground.forward(20)
    ground.left(90)
ground.end_fill()

# ---------- Rocket turtle (drawn as a stamped shape) ----------
def draw_rocket(t):
    """Draw a rocket centered on t's current position, pointing up."""
    t.clear()
    x, y = t.position()

    # Body
    t.penup()
    t.goto(x - 15, y - 40)
    t.setheading(90)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.forward(70)                  # left side of body up
    t.circle(-15, 90)              # nose cone curve start
    t.circle(-15, 90)
    t.forward(70)                  # right side down
    t.right(90)
    t.forward(30)                  # bottom
    t.end_fill()

    # Window
    t.penup()
    t.goto(x, y + 5)
    t.pendown()
    t.fillcolor("#4fc3f7")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

    # Left fin
    t.penup()
    t.goto(x - 15, y - 40)
    t.pendown()
    t.fillcolor("#d32f2f")
    t.begin_fill()
    t.goto(x - 35, y - 60)
    t.goto(x - 15, y - 25)
    t.end_fill()

    # Right fin
    t.penup()
    t.goto(x + 15, y - 40)
    t.pendown()
    t.fillcolor("#d32f2f")
    t.begin_fill()
    t.goto(x + 35, y - 60)
    t.goto(x + 15, y - 25)
    t.end_fill()

    t.penup()
    t.goto(x, y)


rocket = turtle.Turtle()
rocket.hideturtle()
rocket.penup()
rocket.speed(0)
rocket.goto(0, -260)               # base position (nose-tip reference point)
draw_rocket(rocket)
rocket.showturtle()

# ---------- Flame turtle (engine fire under the rocket) ----------
flame = turtle.Turtle()
flame.hideturtle()
flame.penup()
flame.speed(0)

def draw_flame(x, y):
    flame.clear()
    flame.goto(x, y - 40)
    flame.pendown()
    flame.fillcolor(random.choice(["#ff9800", "#ff5722", "#ffeb3b"]))
    flame.begin_fill()
    size = random.randint(15, 30)
    flame.goto(x - 10, y - 40 - size)
    flame.goto(x + 10, y - 40 - size)
    flame.goto(x, y - 40)
    flame.end_fill()
    flame.penup()

# ---------- Smoke particle system ----------
smoke_particles = []   # each: [turtle, dx, dy, life]

def spawn_smoke(x, y):
    puff = turtle.Turtle()
    puff.hideturtle()
    puff.penup()
    puff.shape("circle")
    puff.shapesize(stretch_wid=random.uniform(0.3, 0.8),
                   stretch_len=random.uniform(0.3, 0.8))
    gray = random.uniform(0.55, 0.85)
    puff.color((gray, gray, gray))
    puff.goto(x + random.randint(-15, 15), y - 45)
    puff.showturtle()
    dx = random.uniform(-1.2, 1.2)
    dy = random.uniform(-0.3, 0.5)
    life = random.randint(30, 50)
    smoke_particles.append([puff, dx, dy, life])

def update_smoke():
    for particle in smoke_particles[:]:
        puff, dx, dy, life = particle
        puff.goto(puff.xcor() + dx, puff.ycor() + dy)
        size = puff.shapesize()[0] + 0.02
        puff.shapesize(stretch_wid=size, stretch_len=size)
        particle[3] -= 1
        if particle[3] <= 0:
            puff.hideturtle()
            smoke_particles.remove(particle)
            del puff

# ---------- Countdown text ----------
text_pen = turtle.Turtle()
text_pen.hideturtle()
text_pen.penup()
text_pen.color("white")
text_pen.goto(0, 250)

def countdown():
    for i in ["3", "2", "1", "LIFTOFF!"]:
        text_pen.clear()
        text_pen.write(i, align="center", font=("Arial", 36, "bold"))
        screen.update()
        # small busy-wait based animation frames instead of time.sleep for responsiveness
        for _ in range(25):
            screen.update()
    text_pen.clear()

countdown()

# ---------- Main launch animation loop ----------
y_pos = -260
velocity = 0.0
acceleration = 0.06
frame = 0
max_height = 320   # roughly top of screen before rocket "exits"

while y_pos < max_height:
    velocity += acceleration
    y_pos += velocity
    rocket.goto(0, y_pos)
    draw_rocket(rocket)
    draw_flame(0, y_pos)

    # spawn smoke every couple frames, more furiously while still low
    if frame % 2 == 0:
        spawn_smoke(0, y_pos)

    update_smoke()
    screen.update()
    frame += 1

# Let remaining smoke drift and fade after rocket leaves the screen
flame.clear()
for _ in range(60):
    update_smoke()
    screen.update()

text_pen.goto(0, 0)
text_pen.write("The rocket has left the atmosphere!", align="center",
               font=("Arial", 20, "bold"))
screen.update()

screen.exitonclick()