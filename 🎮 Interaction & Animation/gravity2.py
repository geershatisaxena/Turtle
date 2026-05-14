import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Gravity Simulation - Falling & Bouncing Ball")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Ground
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-400, -250)
ground.pendown()
ground.color("white")
ground.pensize(3)
ground.forward(800)

# Ball setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, 200)

# Physics variables
y_velocity = 0
gravity = -0.5
bounce_damping = 0.8

# Animation loop
while True:
    # Apply gravity
    y_velocity += gravity

    # Move ball
    ball.sety(ball.ycor() + y_velocity)

    # Bounce condition
    if ball.ycor() < -230:
        ball.sety(-230)
        y_velocity = -y_velocity * bounce_damping

    # Small delay for smooth animation
    screen.update()
    time.sleep(0.01)