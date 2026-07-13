# Typewriter Animation with Multiple Messages
# Python Turtle

import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Typewriter Animation")
screen.bgcolor("black")

# Writer
writer = turtle.Turtle()
writer.hideturtle()
writer.color("lime")
writer.penup()

messages = [
    "Initializing system...",
    "Loading modules...",
    "Connecting to server...",
    "Access Granted!",
    "Welcome, Geershati."
]

while True:
    for message in messages:

        typed = ""

        # Type text letter by letter
        for char in message:
            typed += char
            writer.clear()
            writer.goto(-300, 0)
            writer.write(
                typed + "_",
                font=("Courier New", 24, "bold")
            )
            time.sleep(0.08)

        time.sleep(1.5)

        # Delete text letter by letter
        for i in range(len(message), -1, -1):
            writer.clear()
            writer.goto(-300, 0)
            writer.write(
                message[:i] + "_",
                font=("Courier New", 24, "bold")
            )
            time.sleep(0.04)

        time.sleep(0.3)