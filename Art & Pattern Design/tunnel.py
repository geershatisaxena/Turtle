import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Tunnel Illusion")
screen.setup(width=900, height=900)

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Draw nested glowing squares
size = 20

for i in range(120):
    # Rainbow neon color
    hue = i / 120
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(r, g, b)

    t.penup()
    t.goto(-size / 2, -size / 2)
    t.pendown()

    # Rotate slightly each frame to create tunnel effect
    t.setheading(i * 4)

    for _ in range(4):
        t.forward(size)
        t.left(90)

    size += 8

screen.mainloop()