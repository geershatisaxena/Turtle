"""
Neon Tunnel Illusion — Python turtle version.

Concentric polygons shrink toward the center and are redrawn each
frame with a growing "depth offset", so new rings keep spawning at
the edges and rushing inward — the same trick used by real tunnel-
zoom animations, just done frame-by-frame instead of with a canvas.

Turtle has no real glow/blur, so the neon look is faked by drawing
each ring twice: a thicker, dim outer stroke, then a thinner, bright
inner stroke of the same hue. Colors cycle through the spectrum with
depth using colorsys.

Run locally with: python3 neon_tunnel_turtle.py
(Requires a display — turtle needs a GUI window.)
"""

import turtle
import colorsys
import math

# ---- configuration -------------------------------------------------
SIDES = 10          # sides per ring polygon (10 = faceted, tech feel)
RING_COUNT = 18      # how many rings are alive at once
MAX_RADIUS = 320     # radius of the closest ring
DEPTH_SPEED = 0.012  # how fast rings travel from center to edge
SPIN_SPEED = 0.05    # slow overall rotation per frame
FRAME_DELAY = 20     # ms between frames

# ---- screen / turtle setup ------------------------------------------
screen = turtle.Screen()
screen.title("Neon Tunnel — turtle")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0)  # we control redraws manually for smooth animation

artist = turtle.Turtle()
artist.hideturtle()
artist.speed(0)
artist.penup()

state = {"depth_offset": 0.0, "spin": 0.0}


def neon_color(t):
    """t in [0,1] -> cycles hue through the neon spectrum."""
    hue = t % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (r, g, b)


def dim(color, factor):
    """Scale an (r,g,b) color toward black to fake reduced brightness."""
    return tuple(c * factor for c in color)


def draw_ring(radius, sides, rotation, color, glow_width, core_width):
    """Draw one polygon ring with a faux-glow: a dim wide pass, then a
    bright narrow pass on top, both centered on the same vertices."""
    points = []
    for i in range(sides + 1):
        angle = rotation + (i / sides) * 2 * math.pi
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        points.append((x, y))

    # outer glow pass (dim, thick)
    artist.pencolor(dim(color, 0.35))
    artist.pensize(glow_width)
    artist.penup()
    artist.goto(points[0])
    artist.pendown()
    for p in points[1:]:
        artist.goto(p)
    artist.penup()

    # bright core pass (full brightness, thin)
    artist.pencolor(color)
    artist.pensize(core_width)
    artist.goto(points[0])
    artist.pendown()
    for p in points[1:]:
        artist.goto(p)
    artist.penup()


def draw_core_glow(radius, color):
    """Small filled circle at the vanishing point for a bright core."""
    artist.penup()
    artist.goto(0, -radius)
    artist.setheading(0)
    artist.pendown()
    artist.fillcolor(color)
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()
    artist.penup()


def update():
    screen.tracer(0)
    artist.clear()

    state["depth_offset"] = (state["depth_offset"] + DEPTH_SPEED) % 1.0
    state["spin"] += SPIN_SPEED

    # draw from farthest (small/dim) to nearest (large/bright) so
    # closer rings are layered on top
    for i in range(RING_COUNT - 1, -1, -1):
        depth = (i / RING_COUNT + state["depth_offset"]) % 1.0
        eased = depth ** 2.4  # accelerate as rings approach, like real travel
        radius = eased * MAX_RADIUS

        if radius < 2:
            continue

        hue_t = depth * 0.6 + state["spin"] * 0.01
        color = neon_color(hue_t)
        rotation = state["spin"] * (0.05 if i % 2 == 0 else -0.05) + depth * 3

        glow_width = 2 + depth * 10
        core_width = 1 + depth * 3

        draw_ring(radius, SIDES, rotation, color, glow_width, core_width)

    draw_core_glow(10, neon_color(state["spin"] * 0.01))

    screen.update()
    screen.ontimer(update, FRAME_DELAY)


update()
screen.exitonclick()