# Typing Text Animation (Letter by Letter)
# Python Turtle

import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Typing Animation")
screen.bgcolor("black")

# Writer turtle
writer = turtle.Turtle()
writer.hideturtle()
writer.color("lime")
writer.penup()
writer.goto(-350, 0)

text = "GEERSHATI SAXENA"

typed_text = ""

for letter in text:
    typed_text += letter
    writer.clear()
    writer.write(
        typed_text,
        font=("Courier", 24, "bold")
    )
    time.sleep(0.1)

screen.mainloop()