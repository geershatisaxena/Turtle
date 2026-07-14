"""
Galaxy Spiral Pattern using Python Turtle
Run this locally with: python galaxy_spiral.py
"""
import turtle
import math
import colorsys

# ---- Screen setup ----
screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Galaxy Spiral")
screen.tracer(0, 0)  # turn off auto-refresh for fast drawing

# ---- Turtle setup ----
artist = turtle.Turtle()
artist.hideturtle()
artist.speed(0)
artist.penup()

# ---- Galaxy parameters ----
NUM_ARMS = 4          # number of spiral arms
POINTS_PER_ARM = 260  # points drawn per arm
MAX_RADIUS = 380      # how far the galaxy extends
TURNS = 2.6           # how many full rotations the spiral makes
ARM_SPREAD = 18       # scatter width around each arm (star jitter)
CORE_STARS = 400      # extra stars packed in the galactic core

import random
random.seed(42)

def draw_star(x, y, size, color):
    artist.goto(x, y)
    artist.setheading(0)
    artist.pendown()
    artist.color(color)
    artist.dot(size)
    artist.penup()

def hue_color(t):
    """t in [0,1] -> color shifting from hot core (yellow/white) to cool tips (blue/purple)"""
    # Hue moves from ~0.13 (gold) to ~0.75 (violet) as t increases
    hue = 0.13 + t * 0.62
    sat = 0.55 + 0.4 * t
    val = 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, sat, val)
    return (r, g, b)

# ---- Draw the spiral arms ----
for arm in range(NUM_ARMS):
    arm_offset = (2 * math.pi / NUM_ARMS) * arm
    for i in range(POINTS_PER_ARM):
        t = i / POINTS_PER_ARM                      # 0 -> 1 progress along arm
        radius = t * MAX_RADIUS
        angle = arm_offset + t * TURNS * 2 * math.pi

        # base position on the logarithmic-ish spiral
        base_x = radius * math.cos(angle)
        base_y = radius * math.sin(angle)

        # scatter stars around the arm for a natural galaxy look
        jitter_amount = ARM_SPREAD * (0.3 + t)  # more scatter further out
        x = base_x + random.uniform(-jitter_amount, jitter_amount)
        y = base_y + random.uniform(-jitter_amount, jitter_amount)

        size = random.uniform(1.5, 4.5) * (1.2 - 0.5 * t)  # bigger near core
        color = hue_color(t)

        draw_star(x, y, size, color)

        # occasionally add a bright highlight star
        if random.random() < 0.05:
            draw_star(x, y, size + 3, (1, 1, 1))

# ---- Draw the galactic core (dense bright cluster) ----
for _ in range(CORE_STARS):
    r = abs(random.gauss(0, 40))  # concentrated near center
    theta = random.uniform(0, 2 * math.pi)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    size = random.uniform(1.5, 3.5)
    brightness = max(0.7, 1 - r / 120)
    color = (1, 1, brightness)  # warm white/yellow core
    draw_star(x, y, size, color)

# ---- Sprinkle a faint background starfield ----
for _ in range(150):
    x = random.uniform(-440, 440)
    y = random.uniform(-440, 440)
    size = random.uniform(0.5, 1.8)
    shade = random.uniform(0.4, 0.9)
    draw_star(x, y, size, (shade, shade, shade))

screen.update()
turtle.done()