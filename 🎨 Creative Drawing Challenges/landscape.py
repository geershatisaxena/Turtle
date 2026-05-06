import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Landscape - Sun, Mountains, River")
screen.bgcolor("#87CEEB")  # Sky blue
screen.setup(width=1000, height=800)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Color palette
colors = {
    "sky": "#87CEEB",
    "sun": "#FFD700",
    "sun_glow": "#FFA500",
    "mountain1": "#5D6D7E",
    "mountain2": "#4A5568",
    "mountain3": "#6B7B8D",
    "mountain_snow": "#FFFFFF",
    "river": "#4A90E2",
    "river_light": "#7FB3D5",
    "grass": "#228B22",
    "grass_dark": "#1B5E20",
    "tree_trunk": "#8B4513",
    "tree_green": "#2E7D32",
    "tree_light": "#43A047",
    "cloud": "#FFFFFF",
    "cloud_shadow": "#E0E0E0",
    "flower": "#FF69B4"
}

def draw_sky_gradient():
    """Draw a gradient sky effect"""
    for i in range(30):
        y = -200 + i * 20
        # Gradient from dark blue at top to light blue at bottom
        r = max(0, 135 - i * 2)
        g = max(0, 206 - i)
        b = max(0, 235 - i)
        pen.penup()
        pen.goto(-500, y)
        pen.pendown()
        pen.color(f"#{int(r):02x}{int(g):02x}{int(b):02x}")
        pen.begin_fill()
        for _ in range(2):
            pen.forward(1000)
            pen.right(90)
            pen.forward(20)
            pen.right(90)
        pen.end_fill()
    pen.penup()

def draw_sun():
    """Draw the sun with rays"""
    # Sun glow (outer circle)
    pen.goto(200, 100)
    pen.pendown()
    pen.color(colors["sun_glow"])
    pen.begin_fill()
    pen.circle(70)
    pen.end_fill()
    
    # Sun rays
    pen.pensize(3)
    pen.color(colors["sun"])
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x1 = 200 + 80 * math.cos(rad)
        y1 = 100 + 80 * math.sin(rad)
        x2 = 200 + 110 * math.cos(rad)
        y2 = 100 + 110 * math.sin(rad)
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.goto(x2, y2)
    
    # Sun body
    pen.penup()
    pen.goto(200, 100)
    pen.pendown()
    pen.color(colors["sun"])
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()
    
    # Sun face (optional - happy face)
    pen.penup()
    pen.goto(185, 115)
    pen.pendown()
    pen.color("#FF6600")
    pen.pensize(3)
    pen.dot(5)
    pen.penup()
    pen.goto(215, 115)
    pen.pendown()
    pen.dot(5)
    
    # Smile
    pen.penup()
    pen.goto(185, 85)
    pen.pendown()
    pen.setheading(-60)
    pen.circle(20, 120)
    
    pen.penup()

def draw_mountains():
    """Draw mountains in the background"""
    # Back mountain (left)
    pen.penup()
    pen.goto(-500, -50)
    pen.pendown()
    pen.color(colors["mountain2"])
    pen.begin_fill()
    pen.goto(-300, 180)
    pen.goto(-100, -50)
    pen.goto(-500, -50)
    pen.end_fill()
    
    # Snow cap on back mountain
    pen.penup()
    pen.goto(-320, 160)
    pen.pendown()
    pen.color(colors["mountain_snow"])
    pen.begin_fill()
    pen.goto(-300, 180)
    pen.goto(-280, 160)
    pen.goto(-300, 150)
    pen.goto(-320, 160)
    pen.end_fill()
    
    # Middle mountain
    pen.penup()
    pen.goto(-350, -50)
    pen.pendown()
    pen.color(colors["mountain1"])
    pen.begin_fill()
    pen.goto(-100, 220)
    pen.goto(150, -50)
    pen.goto(-350, -50)
    pen.end_fill()
    
    # Snow cap on middle mountain
    pen.penup()
    pen.goto(-120, 200)
    pen.pendown()
    pen.color(colors["mountain_snow"])
    pen.begin_fill()
    pen.goto(-100, 220)
    pen.goto(-80, 200)
    pen.goto(-100, 190)
    pen.goto(-120, 200)
    pen.end_fill()
    
    # Front mountain (right)
    pen.penup()
    pen.goto(-50, -50)
    pen.pendown()
    pen.color(colors["mountain3"])
    pen.begin_fill()
    pen.goto(150, 150)
    pen.goto(400, -50)
    pen.goto(-50, -50)
    pen.end_fill()
    
    # Snow cap on front mountain
    pen.penup()
    pen.goto(130, 135)
    pen.pendown()
    pen.color(colors["mountain_snow"])
    pen.begin_fill()
    pen.goto(150, 150)
    pen.goto(170, 135)
    pen.goto(150, 125)
    pen.goto(130, 135)
    pen.end_fill()

def draw_river():
    """Draw a winding river"""
    pen.pensize(30)
    pen.color(colors["river"])
    
    # River path using curves
    pen.penup()
    pen.goto(-200, -400)
    pen.pendown()
    pen.setheading(30)
    
    for i in range(20):
        pen.circle(80, 25)
        pen.circle(-80, 25)
    
    pen.penup()
    
    # River highlights
    pen.pensize(15)
    pen.color(colors["river_light"])
    pen.penup()
    pen.goto(-190, -390)
    pen.pendown()
    pen.setheading(30)
    
    for i in range(15):
        pen.circle(60, 25)
        pen.circle(-60, 25)
    
    pen.penup()

def draw_ground():
    """Draw the grassy ground"""
    pen.penup()
    pen.goto(-500, -50)
    pen.pendown()
    pen.color(colors["grass"])
    pen.begin_fill()
    pen.goto(500, -50)
    pen.goto(500, -400)
    pen.goto(-500, -400)
    pen.goto(-500, -50)
    pen.end_fill()
    
    # Add darker grass patches
    pen.color(colors["grass_dark"])
    for i in range(30):
        x = random.randint(-480, 480)
        y = random.randint(-380, -60)  # Fixed: low to high
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.begin_fill()
        for _ in range(3):
            pen.forward(15)
            pen.left(120)
        pen.end_fill()
    pen.penup()

def draw_tree(x, y, size=1.0):
    """Draw a tree at given position"""
    # Tree trunk
    pen.penup()
    pen.goto(x - 10 * size, y)
    pen.pendown()
    pen.color(colors["tree_trunk"])
    pen.begin_fill()
    pen.goto(x - 10 * size, y + 40 * size)
    pen.goto(x + 10 * size, y + 40 * size)
    pen.goto(x + 10 * size, y)
    pen.goto(x - 10 * size, y)
    pen.end_fill()
    
    # Tree foliage (3 overlapping circles)
    pen.penup()
    pen.goto(x, y + 50 * size)
    pen.pendown()
    pen.color(colors["tree_green"])
    pen.begin_fill()
    pen.circle(25 * size)
    pen.end_fill()
    
    pen.penup()
    pen.goto(x - 18 * size, y + 35 * size)
    pen.pendown()
    pen.begin_fill()
    pen.circle(22 * size)
    pen.end_fill()
    
    pen.penup()
    pen.goto(x + 18 * size, y + 35 * size)
    pen.pendown()
    pen.begin_fill()
    pen.circle(22 * size)
    pen.end_fill()
    
    # Tree highlight
    pen.penup()
    pen.goto(x - 8 * size, y + 60 * size)
    pen.pendown()
    pen.color(colors["tree_light"])
    pen.begin_fill()
    pen.circle(8 * size)
    pen.end_fill()

def draw_cloud(x, y, size=1.0):
    """Draw a cloud at given position"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(colors["cloud"])
    pen.begin_fill()
    
    # Cloud made of overlapping circles
    pen.circle(30 * size)
    pen.circle(40 * size)
    
    pen.penup()
    pen.goto(x + 35 * size, y - 10 * size)
    pen.pendown()
    pen.circle(35 * size)
    
    pen.penup()
    pen.goto(x - 35 * size, y - 10 * size)
    pen.pendown()
    pen.circle(35 * size)
    
    pen.penup()
    pen.goto(x + 70 * size, y - 5 * size)
    pen.pendown()
    pen.circle(25 * size)
    
    pen.penup()
    pen.goto(x - 70 * size, y - 5 * size)
    pen.pendown()
    pen.circle(25 * size)
    
    pen.end_fill()

def draw_flowers():
    """Draw small flowers on the grass"""
    for i in range(40):
        x = random.randint(-450, 450)
        y = random.randint(-350, -80)  # Fixed: low to high
        
        # Draw flower (5 petals)
        pen.penup()
        pen.goto(x, y)
        pen.color(colors["flower"])
        
        for angle in range(0, 360, 72):
            rad = math.radians(angle)
            px = x + 8 * math.cos(rad)
            py = y + 8 * math.sin(rad)
            pen.goto(px, py)
            pen.pendown()
            pen.dot(6)
            pen.penup()
        
        # Center
        pen.goto(x, y)
        pen.dot(4, "#FFD700")
        
        # Stem
        pen.pendown()
        pen.color("#228B22")
        pen.pensize(2)
        pen.goto(x, y - 10)
        pen.penup()

def draw_birds():
    """Draw birds in the sky"""
    pen.color("#333333")
    pen.pensize(2)
    
    bird_positions = [(-300, 200), (-250, 180), (-200, 220), (300, 150), (350, 170)]
    
    for x, y in bird_positions:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(-30)
        pen.circle(10, 60)
        pen.setheading(30)
        pen.circle(10, 60)
        pen.penup()

def draw_grass_blades():
    """Draw individual grass blades"""
    pen.color("#2E7D32")
    pen.pensize(2)
    
    for i in range(100):
        x = random.randint(-480, 480)
        y = random.randint(-100, -60)  # Fixed: low to high
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(80)
        pen.forward(12)
        pen.backward(12)
        pen.setheading(100)
        pen.forward(10)
        pen.penup()

def draw_water_reflection():
    """Add water reflection effect on river"""
    pen.pensize(2)
    pen.color("#87CEEB")
    
    for i in range(30):
        x = random.randint(-180, -20)  # Fixed: low to high
        y = random.randint(-350, -250)  # Fixed: low to high
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.forward(15)
        pen.penup()

def draw_fence():
    """Draw a wooden fence in the foreground"""
    pen.color("#8B4513")
    pen.pensize(4)
    
    for x in range(-450, 500, 50):
        # Fence posts
        pen.penup()
        pen.goto(x, -320)
        pen.pendown()
        pen.goto(x, -270)
        
        # Horizontal bars
        if x % 100 == 0:
            pen.penup()
            pen.goto(x - 25, -300)
            pen.pendown()
            pen.goto(x + 25, -300)
            pen.penup()
            pen.goto(x - 25, -285)
            pen.pendown()
            pen.goto(x + 25, -285)

def draw_title():
    """Draw title text"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 370)
    title.write("🏞️ LANDSCAPE - SUN, MOUNTAINS, RIVER 🏞️", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("white")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -390)
    instructions.write("Press R to redraw | ESC to exit", align="center", font=("Arial", 10, "normal"))

def draw_landscape():
    """Draw the complete landscape"""
    pen.clear()
    
    # Sky
    draw_sky_gradient()
    
    # Sun
    draw_sun()
    
    # Clouds
    draw_cloud(-350, 250, 0.8)
    draw_cloud(0, 280, 1.0)
    draw_cloud(300, 220, 0.7)
    draw_cloud(150, 300, 0.6)
    
    # Birds
    draw_birds()
    
    # Mountains (behind river)
    draw_mountains()
    
    # Ground
    draw_ground()
    
    # River
    draw_river()
    
    # Water reflection
    draw_water_reflection()
    
    # Trees
    draw_tree(-350, -80, 1.2)
    draw_tree(-280, -70, 1.0)
    draw_tree(300, -90, 1.3)
    draw_tree(380, -80, 1.1)
    draw_tree(-150, -100, 0.9)
    draw_tree(50, -95, 1.0)
    
    # Flowers
    draw_flowers()
    
    # Grass blades
    draw_grass_blades()
    
    # Fence
    draw_fence()
    
    screen.update()

# Keyboard bindings
screen.listen()
screen.onkey(draw_landscape, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()
draw_landscape()

print("=" * 60)
print("        LANDSCAPE - SUN, MOUNTAINS, RIVER")
print("=" * 60)
print()
print("A beautiful scenic landscape created with Turtle graphics!")
print()
print("ELEMENTS INCLUDED:")
print("  ☀️ Sun with glowing rays and happy face")
print("  ⛰️ Mountains (back, middle, front with snow caps)")
print("  🌊 Winding river with reflections")
print("  🌳 Trees with trunks and foliage")
print("  ☁️ Floating clouds")
print("  🌸 Flowers scattered on grass")
print("  🐦 Birds in the sky")
print("  🪵 Wooden fence in foreground")
print("  🟢 Gradient sky and grassy ground")
print()
print("CONTROLS:")
print("  R - Redraw the landscape")
print("  ESC - Exit program")
print()
print("Every element is drawn using basic shapes!")

screen.mainloop()