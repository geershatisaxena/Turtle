import turtle
import math
import time

# Screen Setup
screen = turtle.Screen()
screen.title("Radar Scanner Effect")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0)

# Radar Drawer
radar = turtle.Turtle()
radar.hideturtle()
radar.speed(0)
radar.color("lime")
radar.pensize(2)

# Scanner Beam
beam = turtle.Turtle()
beam.hideturtle()
beam.speed(0)
beam.color("lime")
beam.pensize(3)

# Draw Radar Background
def draw_radar():
    radar.penup()
    radar.goto(0, -300)

    # Concentric Circles
    for radius in [75, 150, 225, 300]:
        radar.penup()
        radar.goto(0, -radius)
        radar.pendown()
        radar.circle(radius)

    # Cross Lines
    radar.penup()
    radar.goto(-300, 0)
    radar.pendown()
    radar.goto(300, 0)

    radar.penup()
    radar.goto(0, -300)
    radar.pendown()
    radar.goto(0, 300)

draw_radar()

# Random Targets
targets = []
for _ in range(15):
    x = math.cos(math.radians(_ * 24)) * (50 + _ * 15)
    y = math.sin(math.radians(_ * 24)) * (50 + _ * 15)
    targets.append((x, y))

# Scanner Animation
angle = 0

while True:

    beam.clear()

    # Scanner beam endpoint
    x = 300 * math.cos(math.radians(angle))
    y = 300 * math.sin(math.radians(angle))

    # Draw beam
    beam.penup()
    beam.goto(0, 0)
    beam.pendown()
    beam.goto(x, y)

    # Draw sweep glow effect
    for i in range(5):
        glow_x = (300 - i * 20) * math.cos(math.radians(angle))
        glow_y = (300 - i * 20) * math.sin(math.radians(angle))
        beam.dot(8 - i, "lime")

    # Detect Targets
    for tx, ty in targets:
        target_angle = math.degrees(math.atan2(ty, tx))

        if target_angle < 0:
            target_angle += 360

        diff = abs(target_angle - angle)

        if diff < 3:
            beam.penup()
            beam.goto(tx, ty)
            beam.dot(15, "red")
        else:
            beam.penup()
            beam.goto(tx, ty)
            beam.dot(8, "green")

    angle = (angle + 2) % 360

    screen.update()
    time.sleep(0.02)