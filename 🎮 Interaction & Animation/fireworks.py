import turtle
import random
import math

# Screen setup
screen = turtle.Screen()
screen.title("Random Fireworks Burst")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Turtle for drawing
firework = turtle.Turtle()
firework.hideturtle()
firework.speed(0)
firework.pensize(2)

colors = [
    "red", "yellow", "cyan", "orange",
    "lime", "pink", "white", "magenta"
]

# Function to draw firework burst
def burst(x, y):
    firework.penup()
    firework.goto(x, y)

    # Random color
    color = random.choice(colors)

    # Draw explosion rays
    for _ in range(40):
        angle = random.randint(0, 360)
        length = random.randint(50, 120)

        firework.goto(x, y)
        firework.setheading(angle)
        firework.pendown()
        firework.color(color)

        # Draw ray
        for i in range(length):
            firework.forward(1)

            # Spark effect
            if i % 10 == 0:
                firework.dot(random.randint(3, 6), random.choice(colors))

        firework.penup()

    screen.update()

# Click event
screen.onclick(burst)

# Message
writer = turtle.Turtle()
writer.hideturtle()
writer.color("white")
writer.penup()
writer.goto(0, 260)
writer.write(
    "Click Anywhere to Create Fireworks!",
    align="center",
    font=("Arial", 18, "bold")
)

screen.mainloop()