import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("#1a1a2e")  # Deep night blue background
screen.title("Radiant Mandala Flower")
screen.tracer(0)  # Turn off animation for instant rendering

t = turtle.Turtle()
t.speed(0)
t.width(1.5)

# Rich color palette
colors = [
    "#FF6B6B",  # coral red
    "#FF8E72",  # peach
    "#FFB347",  # orange
    "#FFD93D",  # gold
    "#6BCB77",  # mint green
    "#4D96FF",  # sky blue
    "#9B59B6",  # purple
    "#FF6B9E",  # pink
]

def draw_circle(radius, color, x=0, y=0, fill=True):
    """Draw a circle at (x, y) with optional fill."""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    if fill:
        t.begin_fill()
    t.circle(radius)
    if fill:
        t.end_fill()
    t.penup()

def petal_layer(radius, angle, count, color, offset_angle=0):
    """Draw a ring of petal-like shapes (two intersecting arcs)."""
    for i in range(count):
        t.penup()
        t.goto(0, 0)
        t.setheading(offset_angle + i * (360 / count))
        t.forward(radius * 0.6)
        t.pendown()
        
        t.color(color)
        t.begin_fill()
        
        # First arc
        t.circle(radius, angle)
        # Turn and second arc
        t.left(180 - angle)
        t.circle(radius, angle)
        t.left(180 - angle)
        
        t.end_fill()
        t.penup()

# === MAIN DRAWING ===

# 1. Large background circular patterns
for r in [180, 160, 140]:
    t.penup()
    t.goto(0, -r)
    t.pendown()
    t.color("#2d2d5e")
    t.width(2)
    t.circle(r)
    t.penup()

# 2. Outer dotted ring
t.width(1.5)
t.color("#FFD93D")
for angle in range(0, 360, 12):
    x = 170 * math.cos(math.radians(angle))
    y = 170 * math.sin(math.radians(angle))
    draw_circle(4, "#FFD93D", x, y, fill=True)

# 3. First petal layer (large, outer petals)
petal_layer(radius=70, angle=55, count=12, color="#FF6B6B", offset_angle=0)

# 4. Second petal layer (medium, offset)
petal_layer(radius=60, angle=60, count=12, color="#FFB347", offset_angle=15)

# 5. Third petal layer (smaller, different shape)
petal_layer(radius=45, angle=65, count=16, color="#6BCB77", offset_angle=7)

# 6. Fourth petal layer (tiny, many)
petal_layer(radius=30, angle=70, count=20, color="#4D96FF", offset_angle=0)

# 7. Central glowing circles
for r, col in [(50, "#9B59B6"), (35, "#FF6B9E"), (22, "#FFD93D"), (12, "#FFFFFF")]:
    draw_circle(r, col, 0, 0, fill=True)

# 8. Inner decorative circles (stamens)
for angle in range(0, 360, 30):
    x = 28 * math.cos(math.radians(angle))
    y = 28 * math.sin(math.radians(angle))
    draw_circle(6, "#FF8E72", x, y, fill=True)

# 9. Small dot pattern on outer edge
for angle in range(0, 360, 6):
    x = 160 * math.cos(math.radians(angle))
    y = 160 * math.sin(math.radians(angle))
    draw_circle(2.5, "#FFB347", x, y, fill=True)

# 10. Spiral of tiny circles (optional detail)
t.penup()
for i in range(36):
    angle = i * 10
    rad = 90 - i * 1.5
    if rad > 10:
        x = rad * math.cos(math.radians(angle))
        y = rad * math.sin(math.radians(angle))
        draw_circle(2, "#FFFFFF", x, y, fill=True)

# 11. Final touch: highlight arcs
t.width(2)
t.color("#FFFFFF")
for angle in [0, 90, 180, 270]:
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(95)
    t.pendown()
    t.circle(-20, 180)  # Draw small half-circle outward
    t.penup()

# Update screen
t.hideturtle()
screen.update()
screen.mainloop()