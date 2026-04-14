import turtle
import math
import colorsys

# ── Setup ──────────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("✦ Pro Color Flower ✦")
screen.bgcolor("#020008")
screen.setup(width=1000, height=1000)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# ── Color helpers ──────────────────────────────────────────────────────────────
def hsv_color(h, s=1.0, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, s, v)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

def lerp_hex(c1, c2, t_val):
    def parse(c): return (int(c[1:3],16), int(c[3:5],16), int(c[5:7],16))
    r1,g1,b1 = parse(c1); r2,g2,b2 = parse(c2)
    return f"#{int(r1+(r2-r1)*t_val):02x}{int(g1+(g2-g1)*t_val):02x}{int(b1+(b2-b1)*t_val):02x}"

# ── Layer 1: Outermost glow ring (large thin petals) ─────────────────────────
PETALS_L1 = 72
for i in range(PETALS_L1):
    hue   = i / PETALS_L1
    fill  = hsv_color(hue,       0.9, 0.95)
    edge  = hsv_color(hue+0.08,  1.0, 1.0)
    t.pencolor(edge)
    t.fillcolor(fill)
    t.pensize(1)
    t.begin_fill()
    t.circle(145, 55)
    t.left(125)
    t.circle(145, 55)
    t.left(125)
    t.end_fill()
    t.left(360 / PETALS_L1)

screen.update()

# ── Layer 2: Mid ring – wider petals ─────────────────────────────────────────
PETALS_L2 = 48
for i in range(PETALS_L2):
    hue  = (i / PETALS_L2) + 0.12
    fill = hsv_color(hue,      1.0, 0.90)
    edge = hsv_color(hue+0.1,  1.0, 1.0)
    t.pencolor(edge)
    t.fillcolor(fill)
    t.pensize(1.5)
    t.begin_fill()
    t.circle(100, 65)
    t.left(115)
    t.circle(100, 65)
    t.left(115)
    t.end_fill()
    t.left(360 / PETALS_L2)

screen.update()

# ── Layer 3: Inner ring – fat petals ─────────────────────────────────────────
PETALS_L3 = 36
for i in range(PETALS_L3):
    hue  = (i / PETALS_L3) + 0.30
    sat  = 0.85 + 0.15 * math.sin(i * 0.5)
    fill = hsv_color(hue,     sat,  0.95)
    edge = hsv_color(hue+0.12, 1.0, 1.0)
    t.pencolor(edge)
    t.fillcolor(fill)
    t.pensize(2)
    t.begin_fill()
    t.circle(65, 75)
    t.left(105)
    t.circle(65, 75)
    t.left(105)
    t.end_fill()
    t.left(360 / PETALS_L3)

screen.update()

# ── Layer 4: Small accent petals ─────────────────────────────────────────────
PETALS_L4 = 24
for i in range(PETALS_L4):
    hue  = (i / PETALS_L4) + 0.55
    fill = hsv_color(hue,     1.0, 1.0)
    edge = hsv_color(hue+0.15, 0.6, 1.0)
    t.pencolor(edge)
    t.fillcolor(fill)
    t.pensize(2)
    t.begin_fill()
    t.circle(38, 80)
    t.left(100)
    t.circle(38, 80)
    t.left(100)
    t.end_fill()
    t.left(360 / PETALS_L4)

screen.update()

# ── Layer 5: Tiny inner star petals ──────────────────────────────────────────
PETALS_L5 = 18
for i in range(PETALS_L5):
    hue  = (i / PETALS_L5) + 0.70
    fill = hsv_color(hue, 0.7, 1.0)
    edge = hsv_color(hue+0.2, 1.0, 1.0)
    t.pencolor(edge)
    t.fillcolor(fill)
    t.pensize(2)
    t.begin_fill()
    t.circle(22, 85)
    t.left(95)
    t.circle(22, 85)
    t.left(95)
    t.end_fill()
    t.left(360 / PETALS_L5)

screen.update()

# ── Swirl lines over the petals ───────────────────────────────────────────────
for i in range(200):
    hue = i / 200
    t.pencolor(hsv_color(hue, 1.0, 1.0))
    t.pensize(1)
    t.penup()
    angle = math.radians(i * 1.8)
    r = 15 + i * 0.72
    t.goto(r * math.cos(angle), r * math.sin(angle))
    t.pendown()
    r2 = r + 3
    t.goto(r2 * math.cos(angle + 0.12), r2 * math.sin(angle + 0.12))

screen.update()

# ── Center disc ───────────────────────────────────────────────────────────────
# Outer glow rings
for ring in range(12, 0, -1):
    hue = ring / 12 * 0.15  # gold → deep orange
    t.penup()
    t.goto(0, -ring * 4)
    t.pendown()
    t.fillcolor(hsv_color(hue, 1.0, 1.0 - ring * 0.04))
    t.pencolor(hsv_color(hue + 0.05, 1.0, 1.0))
    t.pensize(1)
    t.begin_fill()
    t.circle(ring * 4)
    t.end_fill()

# White hot core
t.penup(); t.goto(0, -16); t.pendown()
t.fillcolor("#FFFFFF"); t.pencolor("#FFFAAA"); t.pensize(1)
t.begin_fill(); t.circle(16); t.end_fill()

t.penup(); t.goto(0, -8); t.pendown()
t.fillcolor("#FFFFFF"); t.pencolor("#FFFFFF"); t.pensize(1)
t.begin_fill(); t.circle(8); t.end_fill()

screen.update()

# ── Stamen dots ───────────────────────────────────────────────────────────────
for i in range(12):
    angle = math.radians(i * 30)
    r = 28
    sx, sy = r * math.cos(angle), r * math.sin(angle)
    hue = i / 12
    t.penup(); t.goto(sx, sy - 6); t.pendown()
    t.fillcolor(hsv_color(hue, 1.0, 1.0))
    t.pencolor("#FFFFFF"); t.pensize(1)
    t.begin_fill(); t.circle(6); t.end_fill()

screen.update()

# ── Outer sparkle dots ────────────────────────────────────────────────────────
import random; random.seed(7)
for i in range(80):
    angle = random.uniform(0, 2 * math.pi)
    r     = random.uniform(170, 430)
    sx    = r * math.cos(angle)
    sy    = r * math.sin(angle)
    size  = random.uniform(1.5, 5)
    hue   = random.random()
    t.penup(); t.goto(sx, sy - size); t.pendown()
    t.fillcolor(hsv_color(hue, 0.6, 1.0))
    t.pencolor(hsv_color(hue, 0.3, 1.0))
    t.pensize(1)
    t.begin_fill(); t.circle(size); t.end_fill()

screen.update()

# ── Title ─────────────────────────────────────────────────────────────────────
title = turtle.Turtle()
title.hideturtle(); title.penup()
title.goto(0, -465)
title.pencolor("#FFD700")
title.write("✦  Pro Color Flower  ✦", align="center",
            font=("Courier", 14, "bold"))

screen.update()
turtle.done()