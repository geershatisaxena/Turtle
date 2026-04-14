import turtle
import math

# ── Setup ──────────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Color Changing Pen - Turtle Art")
screen.bgcolor("#0D0D1A")
screen.setup(width=850, height=850)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

# ── Color Palette ──────────────────────────────────────────────────────────────
RAINBOW   = ["#FF0000","#FF4500","#FF7F00","#FFD700","#ADFF2F",
             "#00FF7F","#00FFFF","#007FFF","#7F00FF","#FF00FF"]

NEON      = ["#FF073A","#FF6B00","#FFE000","#39FF14","#00FFFF",
             "#0080FF","#BF00FF","#FF00BF"]

PASTEL    = ["#FFB3BA","#FFDFBA","#FFFFBA","#BAFFC9","#BAE1FF",
             "#D4BAFF","#FFBAEE"]

FIRE      = ["#FF0000","#FF2200","#FF4400","#FF6600","#FF8800",
             "#FFAA00","#FFCC00","#FFEE00","#FFFF44"]

OCEAN     = ["#001F5B","#003F8A","#0066CC","#0088FF","#00AAFF",
             "#00CCFF","#55EEFF","#AAFFFF"]

# ── Helper: interpolate hex colors ────────────────────────────────────────────
def lerp_color(c1, c2, t_val):
    def h(c): return (int(c[1:3],16), int(c[3:5],16), int(c[5:7],16))
    r1,g1,b1 = h(c1);  r2,g2,b2 = h(c2)
    r = int(r1 + (r2-r1)*t_val)
    g = int(g1 + (g2-g1)*t_val)
    b = int(b1 + (b2-b1)*t_val)
    return f"#{r:02x}{g:02x}{b:02x}"

def cycle_color(palette, index):
    """Return smoothly interpolated color cycling through palette."""
    n   = len(palette)
    idx = index % n
    nxt = (idx + 1) % n
    frac= (index % 1.0)
    return lerp_color(palette[idx], palette[nxt], frac)

# ── Section label ─────────────────────────────────────────────────────────────
label = turtle.Turtle()
label.hideturtle(); label.penup(); label.speed(0)

def write_label(text, x, y, color="#FFFFFF", size=10):
    label.goto(x, y)
    label.pencolor(color)
    label.write(text, align="center", font=("Courier", size, "bold"))

# ══════════════════════════════════════════════════════════════════════════════
#  1. RAINBOW SPIRAL  (top-left)
# ══════════════════════════════════════════════════════════════════════════════
write_label("Rainbow Spiral", -210, 355, "#FFD700", 10)

t.penup(); t.goto(-210, 310); t.pendown()
t.setheading(0)
for i in range(180):
    col = RAINBOW[i % len(RAINBOW)]
    t.pencolor(col)
    t.pensize(1 + i*0.02)
    t.forward(1.5 + i * 0.5)
    t.left(29)

# ══════════════════════════════════════════════════════════════════════════════
#  2. NEON STAR BURST  (top-right)
# ══════════════════════════════════════════════════════════════════════════════
write_label("Neon Star Burst", 210, 355, "#39FF14", 10)

cx, cy = 210, 200
for spike in range(72):
    angle = spike * 5
    col   = NEON[spike % len(NEON)]
    t.pencolor(col)
    t.pensize(1.5)
    rad   = math.radians(angle)
    r_out = 130 + 20 * math.sin(math.radians(spike * 7))
    t.penup();  t.goto(cx, cy)
    t.pendown()
    t.goto(cx + r_out * math.cos(rad),
           cy + r_out * math.sin(rad))

# ══════════════════════════════════════════════════════════════════════════════
#  3. FIRE WAVE  (middle-left)
# ══════════════════════════════════════════════════════════════════════════════
write_label("Fire Wave", -210, 45, "#FF6600", 10)

t.penup(); t.goto(-370, 10); t.pendown()
for i in range(300):
    x  = -370 + i * 1.1
    y  =  10  + 35 * math.sin(i * 0.08) * math.sin(i * 0.03)
    col_idx = i / len(FIRE)
    col = FIRE[i % len(FIRE)]
    t.pencolor(col)
    t.pensize(2 + abs(math.sin(i * 0.05)) * 3)
    t.goto(x, y)

# ══════════════════════════════════════════════════════════════════════════════
#  4. OCEAN LISSAJOUS  (middle-right)
# ══════════════════════════════════════════════════════════════════════════════
write_label("Ocean Lissajous", 210, 45, "#00CCFF", 10)

steps = 600
t.penup()
for i in range(steps+1):
    angle = i * (2 * math.pi / steps)
    x =  210 + 110 * math.sin(3 * angle + math.pi/4)
    y = -110 + 110 * math.cos(5 * angle)
    col = OCEAN[i % len(OCEAN)]
    t.pencolor(col)
    t.pensize(1.5)
    if i == 0:
        t.penup(); t.goto(x, y); t.pendown()
    else:
        t.goto(x, y)

# ══════════════════════════════════════════════════════════════════════════════
#  5. PASTEL ROSE CURVE  (bottom-left)
# ══════════════════════════════════════════════════════════════════════════════
write_label("Pastel Rose", -210, -275, "#FFB3BA", 10)

steps = 720
t.penup()
for i in range(steps+1):
    angle = i * (2 * math.pi / steps)
    r     = 110 * math.cos(4 * angle)
    x     = -210 + r * math.cos(angle)
    y     = -390 + r * math.sin(angle)
    col   = PASTEL[i % len(PASTEL)]
    t.pencolor(col)
    t.pensize(2)
    if i == 0:
        t.penup(); t.goto(x, y); t.pendown()
    else:
        t.goto(x, y)

# ══════════════════════════════════════════════════════════════════════════════
#  6. FULL-SPECTRUM POLYGON VORTEX  (bottom-right)
# ══════════════════════════════════════════════════════════════════════════════
write_label("Spectrum Vortex", 210, -275, "#BF00FF", 10)

ALL_COLORS = RAINBOW + NEON + PASTEL
t.penup(); t.goto(210, -390); t.setheading(0)
t.pendown()
for i in range(150):
    col = ALL_COLORS[i % len(ALL_COLORS)]
    t.pencolor(col)
    t.pensize(1 + i * 0.02)
    t.forward(2 + i * 0.6)
    t.left(91)

# ── Divider lines ─────────────────────────────────────────────────────────────
dividers = turtle.Turtle()
dividers.hideturtle(); dividers.speed(0)
dividers.pencolor("#2A2A4A"); dividers.pensize(1)
dividers.penup(); dividers.goto(0, 420); dividers.pendown(); dividers.goto(0, -420)
dividers.penup(); dividers.goto(-425, -60); dividers.pendown(); dividers.goto(425, -60)
dividers.penup(); dividers.goto(-425, 55); dividers.pendown(); dividers.goto(425, 55)

# ── Title ─────────────────────────────────────────────────────────────────────
write_label("✦  Color Changing Pen  ✦", 0, -430, "#FFD700", 12)

screen.update()
turtle.done()