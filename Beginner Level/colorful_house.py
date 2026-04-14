import turtle
import math

# ── Setup ──────────────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.title("Minimalist Advanced Colorful House")
screen.bgcolor("#0D1117")
screen.setup(width=900, height=700)
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)


# ── Helpers ────────────────────────────────────────────────────────────────────
def goto(x, y):
    t.penup(); t.goto(x, y); t.pendown()

def filled_rect(x, y, w, h, fill, outline=None, lw=2):
    t.pensize(lw)
    t.fillcolor(fill)
    t.pencolor(outline or fill)
    t.begin_fill()
    goto(x, y)
    for dx, dy in [(w,0),(0,h),(-w,0),(0,-h)]:
        t.goto(t.xcor()+dx, t.ycor()+dy)
    t.end_fill()

def filled_poly(pts, fill, outline=None, lw=2):
    t.pensize(lw)
    t.fillcolor(fill)
    t.pencolor(outline or fill)
    t.begin_fill()
    goto(*pts[0])
    for p in pts[1:]:
        t.goto(*p)
    t.goto(*pts[0])
    t.end_fill()

def draw_circle(cx, cy, r, fill, outline=None, lw=2):
    t.pensize(lw)
    t.fillcolor(fill)
    t.pencolor(outline or fill)
    goto(cx, cy - r)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def gradient_rect_h(x, y, w, h, colors, steps=None):
    """Fake horizontal gradient by drawing thin vertical strips."""
    n = steps or len(colors)
    sw = w / n
    for i in range(n):
        a = i / max(n-1, 1)
        # lerp between first and last color
        c1 = hex_to_rgb(colors[0])
        c2 = hex_to_rgb(colors[-1])
        r = int(c1[0] + (c2[0]-c1[0])*a)
        g = int(c1[1] + (c2[1]-c1[1])*a)
        b = int(c1[2] + (c2[2]-c1[2])*a)
        col = f"#{r:02x}{g:02x}{b:02x}"
        filled_rect(x + i*sw, y, sw+1, h, col, col, 0)

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def draw_line(x1, y1, x2, y2, color, lw=2):
    t.pensize(lw)
    t.pencolor(color)
    goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)


# ══════════════════════════════════════════════════════════════════════════════
#  SCENE
# ══════════════════════════════════════════════════════════════════════════════

# ── Sky gradient (top → bottom: deep navy → midnight teal) ────────────────────
sky_h = 700
strip_h = 4
for i in range(sky_h // strip_h):
    a = i / (sky_h // strip_h)
    r = int(0x0D + (0x0A - 0x0D)*a)
    g = int(0x11 + (0x2A - 0x11)*a)
    b = int(0x17 + (0x3A - 0x17)*a)
    col = f"#{r:02x}{g:02x}{b:02x}"
    filled_rect(-450, 350 - (i+1)*strip_h, 900, strip_h+1, col, col, 0)

# ── Stars ─────────────────────────────────────────────────────────────────────
import random; random.seed(42)
for _ in range(120):
    sx = random.randint(-430, 430)
    sy = random.randint(50, 340)
    sr = random.uniform(1, 2.5)
    alpha_col = random.choice(["#FFFFFF","#E0F7FF","#FFE8C2","#C8E6FF"])
    draw_circle(sx, sy, sr, alpha_col, alpha_col, 0)

# ── Moon ──────────────────────────────────────────────────────────────────────
draw_circle(340, 240, 38, "#FFF5C2", "#FFD966", 2)
draw_circle(356, 254, 30, "#0D1520", "#0D1520", 0)   # crescent cutout

# ── Ground ────────────────────────────────────────────────────────────────────
# Lawn
filled_rect(-450, -350, 900, 200, "#0B3D1A", "#0B3D1A", 0)
# Subtle path
filled_rect(-50, -350, 100, 170, "#1A2A10", "#1A2A10", 0)
# Path stones
for py in range(-330, -185, 40):
    filled_rect(-30, py, 60, 20, "#2C3E25", "#3A5030", 1)

# ── House body ────────────────────────────────────────────────────────────────
HX, HY, HW, HH = -200, -180, 400, 270

# Main wall – warm off-white
gradient_rect_h(HX, HY, HW, HH, ["#F5ECD7","#EDE0CC"], steps=80)

# Thin accent line top of wall
filled_rect(HX, HY+HH-4, HW, 4, "#E8A020", "#E8A020", 0)

# Wall outline
t.pencolor("#BFA060"); t.pensize(2)
goto(HX, HY)
for dx,dy in [(HW,0),(0,HH),(-HW,0),(0,-HH)]: t.goto(t.xcor()+dx, t.ycor()+dy)

# ── Roof ──────────────────────────────────────────────────────────────────────
roof_pts = [
    (HX - 30, HY + HH),
    (HX + HW/2, HY + HH + 130),
    (HX + HW + 30, HY + HH),
]
# Roof fill – deep teal-slate
filled_poly(roof_pts, "#1A3C4A", "#0E2530", 2)

# Roof tiles – horizontal lines
for ti in range(1, 8):
    frac = ti / 8
    lx1 = roof_pts[0][0] + (roof_pts[1][0]-roof_pts[0][0])*frac
    ly1 = roof_pts[0][1] + (roof_pts[1][1]-roof_pts[0][1])*frac
    lx2 = roof_pts[2][0] + (roof_pts[1][0]-roof_pts[2][0])*frac
    ly2 = roof_pts[2][1] + (roof_pts[1][1]-roof_pts[2][1])*frac
    draw_line(lx1, ly1, lx2, ly2, "#2E6070", 1)

# Roof ridge cap
filled_poly([
    (HX + HW/2 - 10, HY + HH + 110),
    (HX + HW/2 + 10, HY + HH + 110),
    (HX + HW/2 + 6,  HY + HH + 140),
    (HX + HW/2 - 6,  HY + HH + 140),
], "#E8A020", "#C07010", 1)

# Eave trim
filled_poly([
    (HX - 30, HY + HH),
    (HX + HW + 30, HY + HH),
    (HX + HW + 20, HY + HH - 14),
    (HX - 20, HY + HH - 14),
], "#2A5060", "#0E2530", 1)

# ── Chimney ───────────────────────────────────────────────────────────────────
filled_rect(90, HY+HH+30, 50, 90, "#8B4513", "#5A2D0C", 2)
filled_rect(84, HY+HH+114, 62, 12, "#A0522D", "#5A2D0C", 2)
# Smoke puffs
for i, (ox, oy, or_) in enumerate([(112,HY+HH+155,10),(105,HY+HH+172,13),(118,HY+HH+188,9)]):
    col = f"#{0xAA+i*5:02x}{0xAA+i*5:02x}{0xB0+i*5:02x}"
    draw_circle(ox, oy, or_, col, col, 0)

# ── Front door ────────────────────────────────────────────────────────────────
DX, DY, DW, DH = -35, HY, 70, 110
# Door frame
filled_rect(DX-5, DY-3, DW+10, DH+8, "#8B4513", "#5A2D0C", 2)
# Door panels
filled_rect(DX, DY, DW, DH, "#1A1A2E", "#2C2C4A", 2)
# Door arch
t.pencolor("#2C2C4A"); t.pensize(2)
t.fillcolor("#1A1A2E")
goto(DX, DY+DH)
t.begin_fill()
t.goto(DX+DW, DY+DH)
t.circle(DW/2, 180)
t.end_fill()

# Door glass panel
filled_rect(DX+10, DY+DH//2, DW-20, DH//3, "#1E3A5F", "#2A5090", 1)
# Door knob
draw_circle(DX+DW-14, DY+DH//2-5, 5, "#FFD700", "#C0A000", 1)
# Door number
t.penup(); t.goto(DX+DW//2-6, DY+20); t.pendown()
t.pencolor("#E8A020"); t.write("42", font=("Courier", 10, "bold"))

# ── Windows ───────────────────────────────────────────────────────────────────
def draw_window(wx, wy, ww=80, wh=70):
    # Frame
    filled_rect(wx-4, wy-4, ww+8, wh+8, "#8B4513", "#5A2D0C", 2)
    # Glass – night-sky blue
    filled_rect(wx, wy, ww, wh, "#0A1628", "#1A3A5F", 2)
    # Warm interior glow
    filled_rect(wx+5, wy+5, ww-10, wh-10, "#1E2D4A", "#1A3A5F", 0)
    # Light glow strips (blinds up)
    for li in range(3):
        gy = wy + 10 + li*18
        col = "#2A4A7A" if li < 2 else "#3A6AAA"
        filled_rect(wx+6, gy, ww-12, 8, col, col, 0)
    # Cross divider
    draw_line(wx + ww//2, wy, wx + ww//2, wy+wh, "#5A2D0C", 2)
    draw_line(wx, wy + wh//2, wx+ww, wy + wh//2, "#5A2D0C", 2)
    # Sill
    filled_rect(wx-6, wy-10, ww+12, 8, "#A0522D", "#5A2D0C", 1)

draw_window(-170, HY + 80)     # left window
draw_window(90,  HY + 80)      # right window

# Attic window (circular)
draw_circle(HX+HW//2, HY+HH+30, 24, "#0A1628", "#5A2D0C", 3)
draw_circle(HX+HW//2, HY+HH+30, 18, "#1E2D4A", "#1E2D4A", 0)
draw_circle(HX+HW//2, HY+HH+30, 12, "#2A4A7A", "#2A4A7A", 0)
draw_line(HX+HW//2, HY+HH+6, HX+HW//2, HY+HH+54, "#5A2D0C", 2)
draw_line(HX+HW//2-18, HY+HH+30, HX+HW//2+18, HY+HH+30, "#5A2D0C", 2)

# ── Garage / side wing ────────────────────────────────────────────────────────
GX, GY, GW, GH = HX+HW, HY+40, 90, HH-40
gradient_rect_h(GX, GY, GW, GH, ["#EDE0CC","#D8CAAA"], steps=30)
t.pencolor("#BFA060"); t.pensize(2)
goto(GX, GY)
for dx,dy in [(GW,0),(0,GH),(-GW,0),(0,-GH)]: t.goto(t.xcor()+dx, t.ycor()+dy)

# Garage door
filled_rect(GX+5, GY, GW-10, GH-20, "#2A3B2A", "#1A2A1A", 2)
for gi in range(4):
    gy2 = GY + 15 + gi*(GH-35)//4
    draw_line(GX+5, gy2, GX+GW-5, gy2, "#3A5A3A", 1)
draw_line(GX+GW//2+5, GY, GX+GW//2+5, GY+GH-20, "#3A5A3A", 1)

# Side roof
filled_poly([
    (GX-2,  GY+GH),
    (GX+GW+20, GY+GH),
    (GX+GW+10, GY+GH+50),
    (GX-2,  GY+GH+50),
], "#1A3C4A", "#0E2530", 2)

# ── Garden & landscaping ──────────────────────────────────────────────────────
def draw_tree(tx, ty, trunk_h=60, canopy_r=35, col="#2D7A2D"):
    filled_rect(tx-6, ty, 12, trunk_h, "#5A3010", "#3A1A00", 1)
    draw_circle(tx, ty+trunk_h+canopy_r-10, canopy_r, col, "#1A5A1A", 1)
    draw_circle(tx-12, ty+trunk_h+canopy_r-20, canopy_r-8, "#3A9A3A", "#1A5A1A", 1)
    draw_circle(tx+14, ty+trunk_h+canopy_r-18, canopy_r-10, "#1A6A1A", "#1A5A1A", 1)

draw_tree(-310, -185, 70, 42, "#2D7A2D")
draw_tree(330,  -185, 55, 36, "#1A6A3A")

# Bushes
for bx, by, br, bc in [(-220,-180,18,"#2D8A2D"),(-190,-180,14,"#3AAA3A"),
                       (220,-180,16,"#1A7A3A"),(245,-180,12,"#2D8A4A")]:
    draw_circle(bx, by, br, bc, "#1A5A1A", 1)

# Flower bed (left of door)
flower_colors = ["#FF6B6B","#FFD93D","#6BCB77","#4D96FF","#FF6BFF"]
for fi, (fx, fy) in enumerate([(-100,-175),(-85,-165),(-115,-163),(-70,-175),(-130,-175)]):
    draw_circle(fx, fy, 6, flower_colors[fi % len(flower_colors)], "#1A5A1A", 1)
    draw_circle(fx, fy, 3, "#FFFACD", "#FFFACD", 0)

# ── Fence ─────────────────────────────────────────────────────────────────────
for fx in range(-420, 430, 28):
    filled_rect(fx, -215, 10, 55, "#C8A060", "#8B6030", 1)
    filled_poly([(fx, -160),(fx+5,-148),(fx+10,-160)], "#C8A060","#8B6030",1)
draw_line(-420, -195, 420, -195, "#A07840", 2)
draw_line(-420, -175, 420, -175, "#A07840", 2)

# ── Porch light ───────────────────────────────────────────────────────────────
# Bracket
filled_rect(DX+DW+4, HY+DH-10, 5, 25, "#8B6030","#5A3A10",1)
filled_rect(DX+DW+1, HY+DH+12, 12, 5, "#8B6030","#5A3A10",1)
# Lantern body
filled_rect(DX+DW+1, HY+DH-2, 12, 16, "#1A1A1A","#333",1)
# Glow
draw_circle(DX+DW+7, HY+DH+6, 9, "#FFEC8B","#FFEC8B",0)
draw_circle(DX+DW+7, HY+DH+6, 5, "#FFF5A0","#FFF5A0",0)

# ── Reflection / puddle ───────────────────────────────────────────────────────
t.pencolor("#1A4A5A"); t.fillcolor("#0D2030"); t.pensize(1)
t.begin_fill()
goto(-60, -210)
t.goto(60, -210); t.goto(55, -220); t.goto(-55, -220); t.goto(-60, -210)
t.end_fill()
# Reflection shimmer
draw_line(-40, -213, -20, -213, "#3A7AAA", 1)
draw_line(10, -216, 40, -216, "#2A6A9A", 1)

# ── Text label ────────────────────────────────────────────────────────────────
t.penup(); t.goto(-120, -335); t.pendown()
t.pencolor("#E8A020")
t.write("✦  Minimalist House  ✦", font=("Courier", 13, "bold"))

screen.update()
turtle.done()
