import turtle
import time

screen = turtle.Screen()
screen.title("Typing Animation with Cursor")
screen.bgcolor("black")

writer = turtle.Turtle()
writer.hideturtle()
writer.color("cyan")
writer.penup()
writer.goto(-350, 0)

message = "Hello, Geershati! "

typed = ""

for char in message:
    typed += char

    # Show cursor
    writer.clear()
    writer.write(
        typed + "|",
        font=("Courier New", 24, "bold")
    )

    time.sleep(0.08)

# Blinking cursor after typing
while True:
    writer.clear()
    writer.write(
        typed + "|",
        font=("Courier New", 24, "bold")
    )
    time.sleep(0.5)

    writer.clear()
    writer.write(
        typed,
        font=("Courier New", 24, "bold")
    )
    time.sleep(0.5)