import turtle
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Cozy Cottage - House with Garden")
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
    "sky_dark": "#6CA6CD",
    "sun": "#FFD700",
    "cloud": "#FFFFFF",
    "grass": "#5D8A3C",
    "grass_light": "#7CB342",
    "house_body": "#F0E68C",  # Khaki/cream
    "house_wall": "#FFF8DC",  # Cornsilk
    "roof": "#CD853F",        # Peru (thatch color)
    "roof_dark": "#B87333",   # Copper
    "door": "#8B4513",        # Saddle brown
    "door_frame": "#6B3410",
    "window": "#ADD8E6",      # Light blue
    "window_frame": "#5C4033", # Dark brown
    "window_shutter": "#2E8B57", # Sea green
    "chimney": "#A0522D",     # Sienna
    "brick": "#CD5C5C",       # Indian red
    "smoke": "#D3D3D3",
    "fence": "#DEB887",
    "path": "#D2B48C",        # Tan
    "stone": "#A9A9A9",
    "bush": "#228B22",
    "bush_dark": "#1B5E20",
    "flower_red": "#FF4500",
    "flower_yellow": "#FFD700",
    "flower_pink": "#FF69B4",
    "flower_purple": "#9370DB"
}

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

def draw_triangle(x, y, width, height, color, fill=True):
    """Draw a triangle pointing up"""
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    pen.goto(x + width/2, y + height)
    pen.goto(x + width, y)
    pen.goto(x, y)
    
    if fill:
        pen.end_fill()
    pen.penup()

def draw_arc(x, y, radius, start_angle, end_angle, color, width=2):
    """Draw an arc"""
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(start_angle)
    pen.pendown()
    pen.color(color)
    pen.pensize(width)
    pen.circle(radius, end_angle - start_angle)
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

def draw_cloud(x, y):
    """Draw a fluffy cloud"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(colors["cloud"])
    pen.begin_fill()
    pen.fillcolor(colors["cloud"])
    pen.circle(25)
    pen.circle(35)
    pen.penup()
    pen.goto(x + 35, y - 10)
    pen.pendown()
    pen.circle(30)
    pen.penup()
    pen.goto(x - 35, y - 10)
    pen.pendown()
    pen.circle(30)
    pen.penup()
    pen.goto(x + 65, y - 5)
    pen.pendown()
    pen.circle(22)
    pen.penup()
    pen.goto(x - 65, y - 5)
    pen.pendown()
    pen.circle(22)
    pen.end_fill()
    pen.penup()

def draw_grass():
    """Draw grassy ground with gradient effect"""
    # Main grass area
    draw_rectangle(-500, -300, 1000, 150, colors["grass"])
    
    # Lighter grass patches
    for i in range(50):
        x = -450 + i * 20
        y = -300
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color(colors["grass_light"])
        pen.begin_fill()
        pen.fillcolor(colors["grass_light"])
        for _ in range(3):
            pen.forward(10)
            pen.left(120)
        pen.end_fill()
    pen.penup()

def draw_house():
    """Draw the main cottage"""
    # House base
    draw_rectangle(-150, -300, 300, 220, colors["house_body"])
    draw_rectangle(-140, -300, 280, 210, colors["house_wall"])
    
    # Stone texture on walls
    pen.color(colors["stone"])
    pen.pensize(1)
    for y in range(-290, -100, 30):
        for x in range(-140, 140, 40):
            draw_rectangle(x, y, 35, 25, colors["stone"], False)
    pen.pensize(1)
    
    # Roof (thatched style - curved)
    pen.penup()
    pen.goto(-170, -80)
    pen.pendown()
    pen.color(colors["roof"])
    pen.begin_fill()
    pen.fillcolor(colors["roof"])
    for i in range(21):
        x = -170 + i * 18
        y = -80 + 20 * math.sin(i * 3.14159 / 20)
        if i == 0:
            pen.goto(x, y)
        else:
            pen.goto(x, y)
    pen.goto(190, -80)
    pen.goto(10, -50)
    pen.goto(-170, -80)
    pen.end_fill()
    
    # Roof tip decoration
    draw_circle(10, -45, 8, colors["roof_dark"])
    
    # Chimney
    draw_rectangle(-100, -100, 35, 90, colors["chimney"])
    draw_rectangle(-105, -110, 45, 15, colors["brick"])
    
    # Brick pattern on chimney
    pen.color(colors["brick"])
    pen.pensize(1)
    for y in range(-100, -20, 15):
        draw_line(-100, y, -65, y, colors["brick"], 1)
    draw_line(-82, -100, -82, -20, colors["brick"], 1)

def draw_chimney_smoke():
    """Draw animated smoke from chimney"""
    smoke_offsets = [(0, 10), (5, 25), (-5, 40), (8, 55), (-2, 70), (3, 85)]
    for i, (dx, dy) in enumerate(smoke_offsets):
        alpha = 1 - i * 0.1
        size = 8 - i * 0.5
        draw_circle(-82 + dx, -15 + dy, size, colors["smoke"])

def draw_door():
    """Draw the front door with details"""
    # Door
    draw_rectangle(-45, -300, 90, 140, colors["door"])
    draw_rectangle(-42, -300, 84, 137, colors["door_frame"])

def draw_door_details():
    """Draw detailed door elements"""
    # Door panels
    draw_rectangle(-35, -280, 28, 60, "#6B3410")
    draw_rectangle(7, -280, 28, 60, "#6B3410")
    draw_rectangle(-35, -210, 28, 25, "#6B3410")
    draw_rectangle(7, -210, 28, 25, "#6B3410")
    
    # Door arch
    pen.penup()
    pen.goto(-45, -160)
    pen.pendown()
    pen.color(colors["door_frame"])
    pen.pensize(3)
    pen.setheading(0)
    pen.circle(45, 180)
    
    # Door knob
    draw_circle(-25, -230, 5, colors["flower_yellow"])
    draw_circle(-25, -230, 3, "#FFA500")
    
    # Door step
    draw_rectangle(-55, -310, 110, 15, colors["stone"])

def draw_windows():
    """Draw windows with shutters and flower boxes"""
    
    # Left window
    draw_rectangle(-120, -220, 55, 55, colors["window"])
    draw_rectangle(-120, -220, 55, 55, colors["window_frame"], False)
    
    # Window panes
    draw_line(-92, -220, -92, -165, colors["window_frame"], 3)
    draw_line(-120, -192, -65, -192, colors["window_frame"], 3)
    
    # Window sill
    draw_rectangle(-125, -225, 65, 8, colors["window_frame"])
    
    # Left shutter
    draw_rectangle(-135, -220, 15, 55, colors["window_shutter"])
    # Shutter slats
    for i in range(3):
        draw_line(-135, -210 + i*18, -120, -210 + i*18, colors["window_frame"], 1)
    
    # Right window
    draw_rectangle(65, -220, 55, 55, colors["window"])
    draw_rectangle(65, -220, 55, 55, colors["window_frame"], False)
    
    # Window panes
    draw_line(92, -220, 92, -165, colors["window_frame"], 3)
    draw_line(65, -192, 120, -192, colors["window_frame"], 3)
    
    # Window sill
    draw_rectangle(60, -225, 65, 8, colors["window_frame"])
    
    # Right shutter
    draw_rectangle(120, -220, 15, 55, colors["window_shutter"])
    for i in range(3):
        draw_line(120, -210 + i*18, 135, -210 + i*18, colors["window_frame"], 1)
    
    # Flower boxes under windows
    draw_rectangle(-130, -230, 75, 12, "#8B4513")
    draw_rectangle(55, -230, 75, 12, "#8B4513")
    
    # Flowers in boxes
    for x in [-115, -100, -85, -70, 65, 80, 95, 110]:
        draw_circle(x, -225, 4, colors["flower_red"])
        draw_circle(x, -228, 3, colors["flower_yellow"])

def draw_attic_window():
    """Draw a round attic window in the roof"""
    draw_circle(10, -80, 22, colors["window"])
    draw_circle(10, -80, 22, colors["window_frame"], False)
    draw_line(10, -102, 10, -58, colors["window_frame"], 2)
    draw_line(-12, -80, 32, -80, colors["window_frame"], 2)
    draw_circle(10, -80, 8, colors["window_frame"])

def draw_path():
    """Draw a winding stone path"""
    pen.penup()
    pen.goto(-45, -300)
    pen.pendown()
    pen.color(colors["path"])
    pen.begin_fill()
    pen.fillcolor(colors["path"])
    pen.goto(-30, -400)
    pen.goto(0, -450)
    pen.goto(30, -470)
    pen.goto(30, -400)
    pen.goto(15, -350)
    pen.goto(0, -310)
    pen.goto(-45, -300)
    pen.end_fill()
    
    # Stone details on path
    stone_positions = [(-20, -350), (-10, -380), (5, -420), (15, -450)]
    for x, y in stone_positions:
        draw_circle(x, y, 5, colors["stone"])

def draw_fence():
    """Draw a wooden fence on the side"""
    for x in range(-300, -150, 35):
        draw_rectangle(x, -310, 6, 40, colors["fence"])
        draw_triangle(x - 3, -270, 12, 15, colors["fence"])
    
    draw_line(-300, -290, -150, -290, colors["fence"], 2)
    draw_line(-300, -280, -150, -280, colors["fence"], 2)

def draw_bushes():
    """Draw bushes around the house"""
    bush_positions = [(-180, -310), (160, -310), (-200, -320), (180, -320)]
    
    for x, y in bush_positions:
        draw_circle(x - 10, y + 10, 15, colors["bush"])
        draw_circle(x + 10, y + 10, 15, colors["bush"])
        draw_circle(x, y, 18, colors["bush_dark"])

def draw_flowers():
    """Draw flowers in the garden"""
    flower_positions = [
        (-250, -320), (-230, -330), (-210, -315), 
        (150, -325), (170, -310), (200, -320),
        (-50, -350), (-70, -360), (60, -340), (80, -355)
    ]
    
    colors_flower = [colors["flower_red"], colors["flower_pink"], colors["flower_purple"], colors["flower_yellow"]]
    
    for i, (x, y) in enumerate(flower_positions):
        # Stem
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("#228B22")
        pen.pensize(2)
        pen.goto(x, y + 15)
        
        # Petals
        pen.color(colors_flower[i % len(colors_flower)])
        for angle in range(0, 360, 60):
            rad = angle * 3.14159 / 180
            px = x + 6 * math.cos(rad)
            py = y + 15 + 6 * math.sin(rad)
            pen.penup()
            pen.goto(px, py)
            pen.pendown()
            pen.dot(5)
        
        # Center
        draw_circle(x, y + 15, 3, colors["flower_yellow"])

def draw_bird():
    """Draw birds in the sky"""
    pen.color("#333333")
    pen.pensize(2)
    
    bird_positions = [(-250, 300), (-200, 280), (250, 310), (300, 290)]
    for x, y in bird_positions:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(-30)
        pen.circle(10, 60)
        pen.setheading(30)
        pen.circle(10, 60)
    pen.penup()

def draw_sun():
    """Draw a warm sun with rays"""
    draw_circle(350, 320, 45, colors["sun"])
    
    # Sun rays
    pen.pensize(3)
    for angle in range(0, 360, 30):
        rad = angle * 3.14159 / 180
        x1 = 350 + 55 * math.cos(rad)
        y1 = 320 + 55 * math.sin(rad)
        x2 = 350 + 75 * math.cos(rad)
        y2 = 320 + 75 * math.sin(rad)
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.color(colors["sun"])
        pen.goto(x2, y2)
    pen.pensize(1)

def draw_title():
    """Draw title and instructions"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("#2C3E50")
    title.penup()
    title.hideturtle()
    title.goto(0, 390)
    title.write("🏡 COZY COTTAGE - HOUSE WITH GARDEN 🏡", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("#2C3E50")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -420)
    instructions.write("Press R to redraw | ESC to exit", align="center", font=("Arial", 12, "normal"))

def draw_scene():
    """Draw the complete cottage scene"""
    pen.clear()
    
    # Sky
    for i in range(50):
        y = -400 + i * 16
        r, g, b = 135, 206, 235
        r = max(100, r - i)
        g = max(150, g - i//2)
        pen.penup()
        pen.goto(-500, y)
        pen.pendown()
        pen.color(f"#{int(r):02x}{int(g):02x}{int(b):02x}")
        pen.begin_fill()
        for _ in range(2):
            pen.forward(1000)
            pen.right(90)
            pen.forward(16)
            pen.right(90)
        pen.end_fill()
    
    # Elements
    draw_sun()
    draw_cloud(-350, 330)
    draw_cloud(50, 350)
    draw_cloud(350, 300)
    draw_bird()
    draw_grass()
    draw_house()
    draw_chimney_smoke()
    draw_door()
    draw_door_details()
    draw_windows()
    draw_attic_window()
    draw_path()
    draw_fence()
    draw_bushes()
    draw_flowers()
    
    screen.update()

def redraw():
    draw_scene()

# Keyboard bindings
screen.listen()
screen.onkey(redraw, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()
draw_scene()

print("=" * 60)
print("           COZY COTTAGE - HOUSE WITH GARDEN")
print("=" * 60)
print()
print("A beautiful detailed cottage scene!")
print()
print("ELEMENTS INCLUDED:")
print("  🏠 Stone-textured cottage walls")
print("  🏡 Thatched curved roof")
print("  🧱 Brick chimney with animated smoke")
print("  🚪 Detailed wooden door with arch")
print("  Window frames with cross panes")
print("  Window shutters (green)")
print("  🌸 Flower boxes under windows")
print("  Round attic window")
print("  🪨 Winding stone path")
print("  🪵 Wooden fence")
print("  🌿 Bushes around the house")
print("  🌹 Colorful garden flowers")
print()
print("BACKGROUND:")
print("  ☀️ Sun with rays")
print("  ☁️ Fluffy clouds")
print("  🐦 Flying birds")
print("  🌈 Sky gradient")
print()
print("SHAPES USED:")
print("  • Rectangles - Walls, doors, windows, chimney")
print("  • Triangles - Roof, fence pickets")
print("  • Circles - Sun, clouds, attic window, flowers")
print("  • Arcs - Thatched roof curve")
print("  • Lines - Window panes, stone texture")
print()
print("CONTROLS:")
print("  R - Redraw the scene")
print("  ESC - Exit program")
print()
print("This cozy cottage is perfect for a storybook scene!")

screen.mainloop()