import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Random Speed Turtle")

# Create turtle
runner = turtle.Turtle()
runner.shape("turtle")
runner.color("lime")
runner.pensize(3)

# Move turtle with random speed
while True:
    # Random turtle speed (1 to 10)
    speed_value = random.randint(1, 10)
    runner.speed(speed_value)

    # Random movement
    runner.forward(random.randint(30, 100))
    runner.right(random.randint(20, 120))

    # Display current speed
    screen.title(f"Random Speed Turtle - Speed: {speed_value}")

    time.sleep(0.5)

turtle.done()