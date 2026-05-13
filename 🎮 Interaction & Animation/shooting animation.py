import turtle
import math
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.bgcolor("skyblue")
screen.title("Projectile Motion Animation")

# Ground
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-450, -200)
ground.pendown()
ground.pensize(4)
ground.color("green")
ground.forward(900)

# Projectile turtle
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()

# Physics values
angle = 60               # launch angle
speed = 60               # initial velocity
gravity = 9.8

# Convert angle to radians
theta = math.radians(angle)

# Initial position
x = -400
y = -200

# Velocity components
vx = speed * math.cos(theta)
vy = speed * math.sin(theta)

# Time variable
t = 0

# Animation loop
while y >= -200:
    # Projectile equations
    x = -400 + vx * t
    y = -200 + (vy * t) - (0.5 * gravity * t * t)

    # Move projectile
    ball.goto(x, y)

    # Increase time
    t += 0.1

    # Small delay for smooth animation
    time.sleep(0.03)

# Message after landing
ball.goto(x, y + 40)
ball.write("Boom!", align="center", font=("Arial", 16, "bold"))

turtle.done()