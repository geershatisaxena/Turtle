"""
Pendulum Swing Simulation
--------------------------
Run this locally with: python pendulum.py
(Requires a display — turtle won't run in a headless/remote environment.)

Physics: simple pendulum using the small/large-angle equation
    d2(theta)/dt2 = -(g / L) * sin(theta)
integrated step-by-step (semi-implicit Euler) for a smooth, stable swing.
A light damping factor slowly bleeds energy so the pendulum settles,
like a real one affected by air resistance and friction at the pivot.
"""

import turtle
import math

# ---------- Screen setup ----------
screen = turtle.Screen()
screen.title("Pendulum Swing Simulation")
screen.bgcolor("#101418")
screen.setup(width=800, height=700)
screen.tracer(0)

# ---------- Pivot point ----------
pivot_x, pivot_y = 0, 250

# ---------- Pendulum physics parameters ----------
length = 220          # rod length in pixels
gravity = 900.0        # tuned for pixel-scale, not real-world meters
theta = math.radians(70)   # initial angle from vertical (start displacement)
omega = 0.0            # angular velocity
damping = 0.999         # energy loss per step (close to 1 = slow damping)
dt = 0.016              # simulation timestep (~60fps)

# ---------- Drawing turtles ----------
rod = turtle.Turtle()
rod.hideturtle()
rod.color("#d0d0d0")
rod.pensize(3)
rod.speed(0)
rod.penup()

bob = turtle.Turtle()
bob.hideturtle()
bob.shape("circle")
bob.shapesize(1.6)
bob.color("#ff7043", "#ffab91")
bob.penup()
bob.speed(0)
bob.showturtle()

pivot_dot = turtle.Turtle()
pivot_dot.hideturtle()
pivot_dot.penup()
pivot_dot.goto(pivot_x, pivot_y)
pivot_dot.shape("circle")
pivot_dot.shapesize(0.5)
pivot_dot.color("#eeeeee")
pivot_dot.showturtle()

# ---------- Trail effect (fading arc trace of the bob's path) ----------
trail_points = []
max_trail = 40

trail_pen = turtle.Turtle()
trail_pen.hideturtle()
trail_pen.penup()
trail_pen.speed(0)

def draw_trail():
    trail_pen.clear()
    n = len(trail_points)
    for i, (tx, ty) in enumerate(trail_points):
        shade = int(255 * (i / max(n, 1)))
        color = (shade / 255, shade / 255 * 0.6, shade / 255 * 0.4)
        trail_pen.goto(tx, ty)
        trail_pen.dot(4, color)

# ---------- Angle / info readout ----------
info_pen = turtle.Turtle()
info_pen.hideturtle()
info_pen.penup()
info_pen.color("#cccccc")
info_pen.goto(-380, 300)

# ---------- Main simulation loop ----------
frame = 0
running_frames = 2400   # roughly 40 seconds at 60fps before window waits for click

while frame < running_frames:
    # --- physics update (semi-implicit Euler) ---
    angular_acc = -(gravity / length) * math.sin(theta)
    omega += angular_acc * dt
    omega *= damping
    theta += omega * dt

    # --- convert angle to bob position ---
    bob_x = pivot_x + length * math.sin(theta)
    bob_y = pivot_y - length * math.cos(theta)

    # --- draw rod ---
    rod.clear()
    rod.goto(pivot_x, pivot_y)
    rod.pendown()
    rod.goto(bob_x, bob_y)
    rod.penup()

    # --- draw bob ---
    bob.goto(bob_x, bob_y)

    # --- update trail ---
    trail_points.append((bob_x, bob_y))
    if len(trail_points) > max_trail:
        trail_points.pop(0)
    draw_trail()

    # --- info text ---
    if frame % 5 == 0:
        info_pen.clear()
        deg = math.degrees(theta)
        info_pen.write(f"Angle: {deg:6.1f}°   Angular velocity: {omega:5.2f} rad/s",
                       font=("Courier", 14, "normal"))

    screen.update()
    frame += 1

info_pen.clear()
info_pen.write("Pendulum settling... click window to close.",
               font=("Courier", 14, "normal"))
screen.update()

screen.exitonclick()