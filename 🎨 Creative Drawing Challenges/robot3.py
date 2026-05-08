import turtle
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Futuristic Robot - Rectangles & Circles")
screen.bgcolor("#0D0D2B")  # Dark space blue
screen.setup(width=900, height=800)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

def draw_rectangle(x, y, width, height, color, fill=True):
    """Draw a rectangle from bottom-left corner"""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    
    if fill:
        pen.end_fill()
    pen.penup()

def draw_circle(x, y, radius, color, fill=True):
    """Draw a circle at given center"""
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    pen.circle(radius)
    if fill:
        pen.end_fill()
    pen.penup()

def draw_line(x1, y1, x2, y2, color, width=2):
    """Draw a line between two points"""
    pen.penup()
    pen.goto(x1, y1)
    pen.setheading(pen.towards(x2, y2))
    pen.pendown()
    pen.color(color)
    pen.pensize(width)
    pen.goto(x2, y2)
    pen.penup()

def draw_triangle(x, y, width, color, fill=True):
    """Draw an equilateral triangle pointing up"""
    height = width * 0.866
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    for _ in range(3):
        pen.forward(width)
        pen.left(120)
    
    if fill:
        pen.end_fill()
    pen.penup()

def draw_glow(x, y, radius, color):
    """Draw a glowing effect with multiple circles"""
    for r in range(radius, radius - 15, -3):
        alpha = 1 - (radius - r) / 15
        pen.penup()
        pen.goto(x, y - r)
        pen.pendown()
        pen.color(color)
        pen.pensize(1)
        pen.circle(r)
    pen.penup()

def draw_futuristic_robot():
    """Draw a futuristic robot with glowing elements"""
    pen.clear()
    
    # === GLOWING AURA ===
    draw_glow(0, 140, 75, "#00FFFF")
    draw_glow(0, -20, 100, "#FF00FF")
    
    # === HEAD ===
    # Main head (hexagon-like using rectangles)
    draw_rectangle(-50, 90, 100, 100, "#1A1A3A")
    draw_rectangle(-40, 100, 80, 80, "#2A2A5A")
    
    # Visor (T-shaped)
    draw_rectangle(-35, 130, 70, 30, "#00FFFF")
    draw_rectangle(-15, 100, 30, 60, "#00FFFF")
    
    # Visor glow
    draw_rectangle(-33, 132, 66, 26, "#00FFCC")
    draw_rectangle(-13, 102, 26, 56, "#00FFCC")
    
    # === EYES (cyber style) ===
    draw_circle(-20, 118, 5, "#FFFFFF")
    draw_circle(20, 118, 5, "#FFFFFF")
    draw_circle(-20, 118, 3, "#00FFFF")
    draw_circle(20, 118, 3, "#00FFFF")
    
    # === HEAD DECORATIONS ===
    # Forehead crystal
    draw_triangle(0, 170, 20, "#FF00FF")
    draw_triangle(0, 168, 15, "#FF66FF")
    
    # Side panels
    draw_rectangle(-60, 115, 15, 40, "#3A3A6A")
    draw_rectangle(45, 115, 15, 40, "#3A3A6A")
    
    # Ear pieces
    draw_circle(-60, 135, 8, "#00FFFF")
    draw_circle(60, 135, 8, "#00FFFF")
    
    # === ANTENNA ===
    draw_line(0, 190, 0, 220, "#00FFFF", 3)
    draw_circle(0, 225, 6, "#FF00FF")
    draw_circle(0, 222, 3, "#FFFFFF")
    
    # === NECK ===
    draw_rectangle(-12, 80, 24, 15, "#3A3A6A")
    
    # === BODY ===
    draw_rectangle(-70, -40, 140, 120, "#1A1A3A")
    draw_rectangle(-60, -30, 120, 100, "#2A2A5A")
    
    # Chest armor plates
    draw_rectangle(-50, -10, 100, 60, "#3A3A6A")
    draw_rectangle(-40, 0, 80, 40, "#4A4A7A")
    
    # POWER CORE
    draw_circle(0, 15, 20, "#FF00FF")
    draw_circle(0, 15, 15, "#FF33CC")
    draw_circle(0, 15, 10, "#FF66FF")
    draw_circle(0, 15, 5, "#FFFFFF")
    
    # Power core glow
    draw_glow(0, 15, 25, "#FF00FF")
    
    # Chest gauges/lights
    draw_circle(-25, -5, 4, "#00FF00")
    draw_circle(25, -5, 4, "#FF0000")
    draw_circle(0, -20, 4, "#FFFF00")
    
    # === SHOULDER ARMOR ===
    draw_rectangle(-85, -10, 25, 45, "#E74C3C")
    draw_rectangle(60, -10, 25, 45, "#E74C3C")
    draw_circle(-72, 5, 8, "#FF6666")
    draw_circle(72, 5, 8, "#FF6666")
    
    # === ARMS ===
    # Left arm
    draw_rectangle(-110, -30, 30, 35, "#2A2A5A")
    draw_rectangle(-140, -35, 35, 25, "#3A3A6A")
    draw_circle(-140, -22, 8, "#00FFFF")  # Energy cannon
    
    # Right arm
    draw_rectangle(80, -30, 30, 35, "#2A2A5A")
    draw_rectangle(105, -35, 35, 25, "#3A3A6A")
    draw_circle(122, -22, 8, "#00FFFF")  # Energy cannon
    
    # Arm energy lines
    draw_line(-125, -20, -110, -15, "#00FFFF", 2)
    draw_line(110, -20, 125, -15, "#00FFFF", 2)
    
    # === LEGS ===
    # Left leg
    draw_rectangle(-45, -150, 35, 110, "#2A2A5A")
    draw_rectangle(-50, -160, 45, 20, "#E74C3C")  # Boot
    
    # Right leg
    draw_rectangle(10, -150, 35, 110, "#2A2A5A")
    draw_rectangle(5, -160, 45, 20, "#E74C3C")  # Boot
    
    # Knee joints
    draw_circle(-28, -90, 10, "#00FFFF")
    draw_circle(28, -90, 10, "#00FFFF")
    
    # Knee energy rings
    draw_circle(-28, -90, 14, "#00FFFF")
    draw_circle(28, -90, 14, "#00FFFF")
    
    # === ENERGY SHIELD (transparent effect) ===
    pen.penup()
    pen.goto(0, -60)
    pen.pendown()
    pen.color("#00FFFF")
    pen.pensize(2)
    for angle in range(0, 360, 20):
        rad = math.radians(angle)
        x = 120 * math.cos(rad)
        y = 30 + 60 * math.sin(rad)
        pen.goto(x, y)
        pen.penup()
        pen.goto(0, -60)
        pen.pendown()
    pen.penup()
    
    # === HOVER EFFECT (energy rings under feet) ===
    for x in [-30, 30]:
        for r in range(15, 30, 5):
            pen.penup()
            pen.goto(x, -175)
            pen.pendown()
            pen.color("#00FFFF")
            pen.pensize(1)
            pen.circle(r)
    
    # === DECORATIVE SCANNER LINES ===
    for i in range(-50, 60, 20):
        draw_line(i, -35, i + 10, -25, "#00FFFF", 1)
    
    # === STATUS INDICATORS ===
    colors_status = ["#00FF00", "#00FF00", "#FFFF00", "#FF0000"]
    for i, col in enumerate(colors_status):
        draw_circle(-65 + i * 12, -45, 4, col)
    
    screen.update()

def draw_mech_robot():
    """Draw a heavy mech robot"""
    pen.clear()
    
    # === HEAD ===
    draw_rectangle(-45, 100, 90, 85, "#4A4A4A")
    draw_rectangle(-35, 110, 70, 65, "#6A6A6A")
    
    # Visor (single red line)
    draw_rectangle(-30, 135, 60, 15, "#FF0000")
    draw_rectangle(-25, 137, 50, 11, "#FF4444")
    
    # === HEAD SENSORS ===
    draw_circle(-25, 125, 5, "#00FF00")
    draw_circle(25, 125, 5, "#00FF00")
    
    # === NECK ===
    draw_rectangle(-15, 85, 30, 20, "#3A3A3A")
    
    # === BODY ===
    draw_rectangle(-80, -40, 160, 125, "#4A4A4A")
    draw_rectangle(-70, -30, 140, 105, "#5A5A5A")
    
    # Cockpit window
    draw_rectangle(-30, 5, 60, 40, "#1A5A8A")
    draw_rectangle(-25, 10, 50, 30, "#2A7AAA")
    
    # === POWER REACTOR ===
    draw_circle(0, -15, 22, "#FF6600")
    draw_circle(0, -15, 15, "#FF8800")
    draw_circle(0, -15, 8, "#FFAA00")
    
    # === HEAVY ARMS ===
    # Left arm (with drill)
    draw_rectangle(-120, -30, 45, 40, "#5A5A5A")
    draw_rectangle(-155, -25, 40, 30, "#4A4A4A")
    draw_circle(-175, -15, 15, "#888888")  # Drill head
    draw_line(-185, -15, -165, -15, "#CCCCCC", 4)  # Drill bit
    
    # Right arm (with claw)
    draw_rectangle(75, -30, 45, 40, "#5A5A5A")
    draw_rectangle(115, -25, 40, 30, "#4A4A4A")
    draw_triangle(140, -10, 20, "#888888")
    draw_triangle(140, -30, 20, "#888888")
    
    # === LEGS (sturdy mech legs) ===
    draw_rectangle(-50, -150, 40, 110, "#5A5A5A")
    draw_rectangle(10, -150, 40, 110, "#5A5A5A")
    
    # Knee armor
    draw_circle(-30, -90, 14, "#E74C3C")
    draw_circle(30, -90, 14, "#E74C3C")
    
    # Feet (tank treads)
    draw_rectangle(-65, -165, 70, 25, "#3A3A3A")
    draw_rectangle(-5, -165, 70, 25, "#3A3A3A")
    
    # Tread details
    for x in range(-60, 0, 10):
        draw_line(x, -165, x, -150, "#666666", 2)
    for x in range(0, 60, 10):
        draw_line(x, -165, x, -150, "#666666", 2)
    
    # === EXHAUST PIPES ===
    draw_rectangle(-90, -20, 15, 30, "#E74C3C")
    draw_rectangle(75, -20, 15, 30, "#E74C3C")
    draw_circle(-82, 5, 5, "#FF6600")
    draw_circle(82, 5, 5, "#FF6600")
    
    # === SMOKE/EXHAUST ===
    for i in range(3):
        draw_circle(-90, 10 + i*8, 4 + i, "#888888")
        draw_circle(90, 10 + i*8, 4 + i, "#888888")
    
    screen.update()

def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("#00FFFF")
    title.penup()
    title.hideturtle()
    title.goto(0, 370)
    title.write("🤖 FUTURISTIC ROBOT - GLOWING DESIGN 🤖", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("white")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -390)
    instructions.write("5=Futuristic Robot  6=Mech Robot | ESC=Exit", align="center", font=("Arial", 14, "normal"))

current_robot = 5

def draw_current():
    """Draw the currently selected robot"""
    if current_robot == 5:
        draw_futuristic_robot()
    elif current_robot == 6:
        draw_mech_robot()

def set_robot_5(): global current_robot; current_robot = 5; draw_current()
def set_robot_6(): global current_robot; current_robot = 6; draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_robot_5, "5")
screen.onkey(set_robot_6, "6")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        FUTURISTIC & MECH ROBOTS")
print("=" * 60)
print()
print("2 new advanced robot designs!")
print()
print("ROBOT DESIGNS:")
print("  5 - Futuristic Robot: Cyber-style with glowing elements")
print("      • Glowing visor and energy core")
print("      • Energy cannons on arms")
print("      • Hover effects and energy shield")
print("      • Neon cyberpunk aesthetic")
print()
print("  6 - Mech Robot: Heavy industrial design")
print("      • Drill weapon on left arm")
print("      • Claw weapon on right arm")
print("      • Tank tread feet")
print("      • Exhaust pipes with smoke")
print()
print("NEW FEATURES:")
print("  • Glowing aura effects")
print("  • Energy rings and shields")
print("  • Multiple layered colors")
print("  • Moving parts (drills, claws)")
print("  • Exhaust effects")
print()
print("CONTROLS:")
print("  5 - Futuristic Robot")
print("  6 - Mech Robot")
print("  ESC - Exit")
print()
print("Now you have 6 robot designs total!")

# Draw default robot
draw_futuristic_robot()
screen.mainloop()