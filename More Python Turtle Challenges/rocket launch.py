import turtle
import random
import time

# Screen Setup
screen = turtle.Screen()
screen.title("🚀 Rocket Launch Animation")
screen.bgcolor("midnight blue")
screen.setup(width=800, height=700)
screen.tracer(0)

# Ground
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-400, -250)
ground.pendown()
ground.color("green")
ground.pensize(5)
ground.forward(800)

# Rocket
rocket = turtle.Turtle()
rocket.shape("triangle")
rocket.shapesize(2, 1)
rocket.color("white", "red")
rocket.setheading(90)
rocket.penup()
rocket.goto(0, -220)

# Smoke Particles
smokes = []

def create_smoke():
    smoke = turtle.Turtle()
    smoke.shape("circle")
    smoke.shapesize(random.uniform(0.3, 1.0))
    smoke.color("lightgray")
    smoke.penup()
    smoke.goto(
        random.randint(-15, 15),
        rocket.ycor() - 20
    )
    smoke.speed(0)
    smokes.append(smoke)

# Stars Background
stars = turtle.Turtle()
stars.hideturtle()
stars.penup()

for _ in range(100):
    stars.goto(
        random.randint(-390, 390),
        random.randint(-100, 340)
    )
    stars.dot(random.randint(2, 4), "white")

# Launch Animation
for _ in range(300):

    # Move Rocket Up
    rocket.sety(rocket.ycor() + 2)

    # Generate Smoke
    for _ in range(3):
        create_smoke()

    # Animate Smoke
    for smoke in smokes[:]:
        smoke.sety(smoke.ycor() - random.randint(1, 3))
        smoke.shapesize(
            smoke.shapesize()[0] + 0.02
        )

        # Remove old smoke
        if smoke.ycor() < -300:
            smoke.hideturtle()
            smokes.remove(smoke)

    screen.update()
    time.sleep(0.02)

# Message
message = turtle.Turtle()
message.hideturtle()
message.color("gold")
message.penup()
message.goto(0, 0)
message.write(
    "🚀 Mission Successful!",
    align="center",
    font=("Arial", 24, "bold")
)

screen.update()
screen.mainloop()