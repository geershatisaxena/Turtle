"""
Lotus Flower — drawn with Python turtle using repeated arcs.

Each petal is made of two mirrored arcs (like a pointed leaf/petal
shape). Petals are arranged in concentric rings, rotated evenly
around the center, with each ring slightly smaller and lighter
in color to create a layered lotus bloom effect.

Run locally with: python3 lotus_turtle.py
(Requires a display — turtle needs a GUI window, so this won't
run in a headless server environment.)
"""

import turtle
import math


def draw_petal(t, length, width_angle, color):
    """
    Draw a single petal using two arcs that meet at a point.

    length      -> radius of each arc (controls petal length)
    width_angle -> how far each arc sweeps (controls petal width)
    color       -> fill color of the petal
    """
    t.fillcolor(color)
    t.begin_fill()

    # First arc: curves outward to the left
    t.circle(length, width_angle)
    # Turn to start the mirrored arc back to the starting point
    t.left(180 - width_angle)
    t.circle(length, width_angle)
    t.left(180 - width_angle)

    t.end_fill()


def draw_ring(t, num_petals, length, width_angle, color, start_heading=90):
    """
    Draw a full ring of petals evenly spaced around the center.
    The turtle always returns to the same center point/heading
    between petals.
    """
    angle_step = 360 / num_petals
    for i in range(num_petals):
        t.penup()
        t.goto(0, 0)
        t.setheading(start_heading + i * angle_step)
        t.pendown()
        draw_petal(t, length, width_angle, color)


def draw_center(t, radius, color):
    """Draw the small circular seed-head at the center of the lotus."""
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def main():
    screen = turtle.Screen()
    screen.title("Lotus Flower — drawn with arcs")
    screen.bgcolor("#eaf6ff")
    screen.setup(width=800, height=800)
    screen.tracer(0)  # turn off animation for fast, clean drawing

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1.5)
    t.pencolor("#b5395b")

    # Outer ring: largest, palest petals
    draw_ring(t, num_petals=8, length=160, width_angle=55,
              color="#ffd6e7", start_heading=90 + 22.5)

    # Middle ring: medium petals, offset so they peek between outer ones
    draw_ring(t, num_petals=8, length=120, width_angle=50,
              color="#ff9dc0", start_heading=90)

    # Inner ring: smallest, most saturated petals
    draw_ring(t, num_petals=6, length=80, width_angle=45,
              color="#ff5c96", start_heading=90 + 30)

    # Seed-head center
    draw_center(t, radius=18, color="#ffe066")

    t.hideturtle()
    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()