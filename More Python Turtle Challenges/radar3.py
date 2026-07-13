"""
Rotating Radar Scanner Effect
-------------------------------
Run this locally with: python radar.py
(Requires a display — turtle won't run in a headless/remote environment.)

Features:
  - Concentric range rings and crosshair grid lines
  - A rotating sweep beam with a fading "phosphor" trail
  - Random blips that appear on the scope and briefly light up
    when the sweep passes over them, then slowly fade
"""

import turtle
import math
import random

# ---------- Screen setup ----------
screen = turtle.Screen()
screen.title("Radar Scanner")
screen.bgcolor("#000000")
screen.setup(width=750, height=750)
screen.tracer(0)

RADIUS = 300
CENTER = (0, 0)
GREEN = "#00ff41"

# ---------- Static scope: rings + crosshairs ----------
scope = turtle.Turtle()
scope.hideturtle()
scope.penup()
scope.color(GREEN)
scope.pensize(1)
scope.speed(0)

def draw_circle(r):
    scope.goto(0, -r)
    scope.setheading(0)
    scope.pendown()
    scope.circle(r)
    scope.penup()

for frac in (0.25, 0.5, 0.75, 1.0):
    draw_circle(RADIUS * frac)

# crosshairs
scope.goto(-RADIUS, 0)
scope.pendown()
scope.goto(RADIUS, 0)
scope.penup()
scope.goto(0, -RADIUS)
scope.pendown()
scope.goto(0, RADIUS)
scope.penup()

# diagonal lines for extra radar-style flair
for ang in (45, 135, 225, 315):
    scope.goto(0, 0)
    scope.setheading(ang)
    scope.pendown()
    scope.forward(RADIUS)
    scope.penup()

# ---------- Blips (random targets on the scope) ----------
NUM_BLIPS = 9
blips = []   # each: [angle_deg, distance, turtle, brightness]

blip_layer = []
for _ in range(NUM_BLIPS):
    angle = random.uniform(0, 360)
    dist = random.uniform(RADIUS * 0.15, RADIUS * 0.95)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.shape("circle")
    t.shapesize(0.5)
    t.color("#003b0f")   # start dim
    x = dist * math.cos(math.radians(angle))
    y = dist * math.sin(math.radians(angle))
    t.goto(x, y)
    t.showturtle()
    blips.append({"angle": angle, "dist": dist, "turtle": t, "brightness": 0.0})

# ---------- Sweep beam ----------
sweep = turtle.Turtle()
sweep.hideturtle()
sweep.penup()
sweep.speed(0)
sweep.pensize(2)

def draw_sweep(angle_deg):
    sweep.clear()
    rad = math.radians(angle_deg)
    x = RADIUS * math.cos(rad)
    y = RADIUS * math.sin(rad)

    # Draw a faded "wedge" trail behind the beam using several fading lines
    trail_span = 40   # degrees behind the beam that stay lit
    steps = 18
    for i in range(steps):
        frac = i / steps
        trail_angle = angle_deg - frac * trail_span
        trad = math.radians(trail_angle)
        tx = RADIUS * math.cos(trad)
        ty = RADIUS * math.sin(trad)
        brightness = (1 - frac) ** 2
        shade = f"#{int(0):02x}{int(60 + 195 * brightness):02x}{int(20 + 65*brightness):02x}"
        sweep.goto(0, 0)
        sweep.pendown()
        sweep.color(shade)
        sweep.pensize(2)
        sweep.goto(tx, ty)
        sweep.penup()

    # bright leading edge line
    sweep.goto(0, 0)
    sweep.pendown()
    sweep.color(GREEN)
    sweep.pensize(3)
    sweep.goto(x, y)
    sweep.penup()

# ---------- Label ----------
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color(GREEN)
label.goto(-RADIUS, RADIUS + 15)
label.write("RADAR SCAN", font=("Courier", 16, "bold"))

status = turtle.Turtle()
status.hideturtle()
status.penup()
status.color(GREEN)
status.goto(-RADIUS, -RADIUS - 30)

# ---------- Main animation loop ----------
angle = 0.0
rotation_speed = 2.2   # degrees per frame
frame = 0
total_frames = 2000    # roughly enough for several full sweeps

while frame < total_frames:
    draw_sweep(angle)

    # update blip brightness: light up when sweep beam passes near them,
    # otherwise decay gradually (afterglow effect)
    for b in blips:
        angular_diff = (angle - b["angle"]) % 360
        if angular_diff < 6:   # beam is currently passing over this blip
            b["brightness"] = 1.0
        else:
            b["brightness"] *= 0.965   # slow fade

        g = int(60 + 195 * b["brightness"])
        r_ = int(0)
        bcol = int(20 + 40 * b["brightness"])
        b["turtle"].color(f"#{r_:02x}{g:02x}{bcol:02x}")
        size = 0.5 + 0.5 * b["brightness"]
        b["turtle"].shapesize(size)

    if frame % 10 == 0:
        detected = sum(1 for b in blips if b["brightness"] > 0.5)
        status.clear()
        status.write(f"Sweep angle: {angle % 360:5.1f}°   Contacts: {detected}",
                     font=("Courier", 14, "normal"))

    screen.update()
    angle += rotation_speed
    frame += 1

status.clear()
status.write("Scan complete. Click window to close.", font=("Courier", 14, "normal"))
screen.update()

screen.exitonclick()