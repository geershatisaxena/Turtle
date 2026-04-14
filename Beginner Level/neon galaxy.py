import turtle
import math
import random
import colorsys

# ── Setup ──────────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("✦ Neon Cyberpunk Galaxy ✦")
screen.bgcolor("#000008")
screen.setup(width=1000, height=1000)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

random.seed(42)

# ── Color helpers ──────────────────────────────────────────────────────────────
def hsv(h, s=1.0, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, s, v)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"

NEON = ["#FF073A","#FF6B00","#FFE000","#39FF14","#00FFFF","#0080FF","#BF00FF","#FF00BF"]

def neon(i):   
    return NEON[i % len(NEON)]

def draw_dot(x, y, r, fill, outline=None, lw=1):
    t.penup()
    t.goto(x, y - r)
    t.pendown()
    t.fillcolor(fill)
    t.pencolor(outline if outline else fill)
    t.pensize(lw)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

# ══════════════════════════════════════════════════════════════════════════════
#  STAR FIELD
# ══════════════════════════════════════════════════════════════════════════════
for _ in range(200):
    sx, sy = random.randint(-490,490), random.randint(-490,490)
    sc = random.choice(["#FFFFFF","#CCDDFF","#FFCCFF","#CCFFFF"])
    draw_dot(sx, sy, random.uniform(0.8,1.6), sc, sc, 0)

for _ in range(60):
    sx, sy = random.randint(-480,480), random.randint(-480,480)
    sc = random.choice(NEON)
    draw_dot(sx, sy, random.uniform(1.5,2.5), sc, sc, 0)

screen.update()

# ══════════════════════════════════════════════════════════════════════════════
#  NEBULA
# ══════════════════════════════════════════════════════════════════════════════
nebula_centers = [(-180, 140), (160, -100), (0, -210)]
nebula_colors  = [
    ["#1A003A","#2A005A","#3A0070"],
    ["#001A3A","#002A5A","#003A80"],
    ["#003A1A","#005A2A","#006A30"],
]

for (nx, ny), nc in zip(nebula_centers, nebula_colors):
    for _ in range(12):
        ox = nx + random.randint(-80, 80)
        oy = ny + random.randint(-80, 80)
        r  = random.randint(20, 50)
        col = random.choice(nc)
        t.penup()
        t.goto(ox, oy - r)
        t.pendown()
        t.fillcolor(col)
        t.pencolor(col)
        t.begin_fill()
        t.circle(r)
        t.end_fill()

screen.update()

# ══════════════════════════════════════════════════════════════════════════════
#  GALAXY SPIRAL
# ══════════════════════════════════════════════════════════════════════════════
for arm in range(4):
    offset = (arm / 4) * 2 * math.pi
    for i in range(300):
        frac = i / 300
        angle = offset + frac * 4 * math.pi
        r = 10 + frac * 300

        px = r * math.cos(angle)
        py = r * math.sin(angle)

        col = hsv(frac + arm*0.2, 1, 1)
        draw_dot(px, py, random.uniform(1, 2.5), col, col, 0)

screen.update()

# ══════════════════════════════════════════════════════════════════════════════
#  CORE
# ══════════════════════════════════════════════════════════════════════════════
for r, col in [(60,"#FFFFFF"), (45,"#CCCCFF"), (30,"#8844FF"), (15,"#440088")]:
    t.penup()
    t.goto(0, -r)
    t.pendown()
    t.fillcolor(col)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

screen.update()

# ══════════════════════════════════════════════════════════════════════════════
#  PLANET
# ══════════════════════════════════════════════════════════════════════════════
PX, PY, PR = 300, 250, 60

# glow
for g in range(4, 0, -1):
    draw_dot(PX, PY, PR + g*10, "#0033AA", "#0033AA", 0)

# body
for y in range(-PR, PR):
    half = int(math.sqrt(PR**2 - y**2))
    col = hsv(0.5 + (y/PR)*0.2, 1, 1)
    t.penup()
    t.goto(PX - half, PY + y)
    t.pendown()
    t.pencolor(col)
    t.goto(PX + half, PY + y)

# rings (FIXED)
for rr in [80, 95]:
    t.penup()
    for i in range(100):
        ang = i / 100 * 2 * math.pi
        x = PX + rr * math.cos(ang)
        y = PY + rr * 0.4 * math.sin(ang)
        if i == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)
    t.penup()

screen.update()

# ══════════════════════════════════════════════════════════════════════════════
#  SHOOTING STAR
# ══════════════════════════════════════════════════════════════════════════════
for _ in range(3):
    x1, y1 = random.randint(-400,400), random.randint(-400,400)
    x2, y2 = x1 + random.randint(80,150), y1 - random.randint(80,150)

    for i in range(15):
        frac = i / 15
        x = x1 + (x2-x1)*frac
        y = y1 + (y2-y1)*frac

        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pensize(2*(1-frac))
        t.pencolor("#FFFFFF")
        t.goto(x+2, y-2)

screen.update()

# ══════════════════════════════════════════════════════════════════════════════
#  TITLE
# ══════════════════════════════════════════════════════════════════════════════
t.penup()
t.goto(0, -470)
t.pencolor("#00FFFF")
t.write("✦ NEON CYBERPUNK GALAXY ✦", align="center", font=("Courier", 16, "bold"))

screen.update()
turtle.done()