# Turtle Chasing Another Turtle
# One turtle moves randomly, the other chases it.

import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Chase Game")
screen.setup(width=800, height=600)

# Runner turtle
runner = turtle.Turtle()
runner.shape("turtle")
runner.color("cyan")
runner.penup()
runner.speed(0)

# Chaser turtle
chaser = turtle.Turtle()
chaser.shape("turtle")
chaser.color("red")
chaser.penup()
chaser.speed(0)

# Starting positions
runner.goto(100, 100)
chaser.goto(-200, -150)

# Move runner randomly
def move_runner():
    angle = random.randint(0, 360)
    distance = random.randint(20, 50)

    runner.setheading(angle)
    runner.forward(distance)

    # Keep inside screen
    x, y = runner.position()

    if x > 390:
        runner.setx(390)
    if x < -390:
        runner.setx(-390)

    if y > 290:
        runner.sety(290)
    if y < -290:
        runner.sety(-290)

# Chaser follows runner
def chase():
    chaser.setheading(chaser.towards(runner))
    chaser.forward(5)

    # Check collision
    if chaser.distance(runner) < 20:
        print("Caught!")
        screen.bye()
        return

    move_runner()

    # Repeat every 100 ms
    screen.ontimer(chase, 100)

# Start chasing
chase()

screen.mainloop()