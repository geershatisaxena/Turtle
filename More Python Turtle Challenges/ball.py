# Jumping Ball Animation with Increasing Height
# Python Turtle

import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Jumping Ball Animation")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Ground
ground = turtle.Turtle()
ground.hideturtle()
ground.color("white")
ground.penup()
ground.goto(-400, -200)
ground.pendown()
ground.forward(800)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()

ground_y = -180
ball.goto(0, ground_y)

# Animation variables
jump_height = 50
gravity = 0.5
max_height = 250

while True:
    velocity = (2 * gravity * jump_height) ** 0.5

    # Upward motion
    y = ground_y
    while velocity > 0:
        y += velocity
        velocity -= gravity
        ball.goto(0, y)
        screen.update()
        time.sleep(0.01)

    # Downward motion
    while y > ground_y:
        velocity += gravity
        y -= velocity
        if y < ground_y:
            y = ground_y
        ball.goto(0, y)
        screen.update()
        time.sleep(0.01)

    # Increase jump height after each bounce
    jump_height += 20

    # Reset after reaching maximum height
    if jump_height > max_height:
        jump_height = 50