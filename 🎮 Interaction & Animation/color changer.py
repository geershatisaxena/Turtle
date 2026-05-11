import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Color-Changing Bouncing Shape")

# Create turtle object
ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2)
ball.penup()
ball.speed(0)

# Starting movement speed
dx = 4
dy = 4

# Colors list
colors = ["red", "cyan", "yellow", "lime", "orange", "magenta", "white"]

# Main animation loop
while True:
    # Current position
    x = ball.xcor()
    y = ball.ycor()

    # Move the ball
    ball.goto(x + dx, y + dy)

    # Bounce from left/right walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        dx *= -1
        ball.color(random.choice(colors))

    # Bounce from top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        dy *= -1
        ball.color(random.choice(colors))

    screen.update()