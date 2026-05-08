import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("House with Windows, Door, and Chimney")
screen.bgcolor("#87CEEB")  # Sky blue
screen.setup(width=900, height=800)
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
    "cloud": "#FFFFFF",
    "grass": "#228B22",
    "house_body": "#F4A460",  # Sandy brown
    "roof": "#8B4513",         # Saddle brown
    "door": "#654321",         # Dark brown
    "door_handle": "#FFD700",  # Gold
    "window": "#87CEEB",       # Light blue
    "window_frame": "#5C4033", # Dark brown
    "chimney": "#B22222",      # Firebrick red
    "smoke": "#D3D3D3",        # Light gray
    "fence": "#DEB887",        # Burlywood
    "path": "#C0A080"          # Tan
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

def draw_sun():
    """Draw a sun in the corner"""
    draw_circle(300, 280, 40, colors["sun"])
    
    # Sun rays
    pen.pensize(3)
    for angle in range(0, 360, 30):
        rad = angle * 3.14159 / 180
        x1 = 300 + 50 * math.cos(rad)
        y1 = 280 + 50 * math.sin(rad)
        x2 = 300 + 70 * math.cos(rad)
        y2 = 280 + 70 * math.sin(rad)
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.color(colors["sun"])
        pen.goto(x2, y2)
    pen.pensize(1)

def draw_cloud(x, y):
    """Draw a cloud"""
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
    """Draw grass at the bottom"""
    draw_rectangle(-400, -250, 800, 50, colors["grass"])
    
    # Grass blades
    pen.color("#006400")
    pen.pensize(2)
    for i in range(30):
        x = -380 + i * 25
        pen.penup()
        pen.goto(x, -250)
        pen.pendown()
        pen.goto(x - 5, -265)
        pen.penup()
        pen.goto(x, -250)
        pen.pendown()
        pen.goto(x + 5, -265)
    pen.pensize(1)

def draw_house():
    """Draw the main house body"""
    # House base
    draw_rectangle(-150, -250, 300, 200, colors["house_body"])
    
    # Roof (triangle)
    draw_triangle(-170, -50, 340, 130, colors["roof"])
    
    # Roof ridge line
    draw_line(-170, -50, 170, -50, colors["roof"], 4)
    
    # Chimney
    draw_rectangle(80, -20, 40, 100, colors["chimney"])
    
    # Chimney top
    draw_rectangle(75, 80, 50, 15, "#8B0000")
    
    # Chimney bricks (texture lines)
    pen.color("#8B0000")
    pen.pensize(2)
    for y in range(-10, 80, 20):
        draw_line(80, y, 120, y, "#8B0000", 2)
    draw_line(100, -20, 100, 80, "#8B0000", 2)
    
    # Smoke from chimney
    smoke_positions = [(100, 95), (110, 110), (95, 125), (120, 140)]
    for i, (x, y) in enumerate(smoke_positions):
        draw_circle(x, y, 8 - i, colors["smoke"])

def draw_door():
    """Draw the front door"""
    # Door
    draw_rectangle(-40, -250, 80, 120, colors["door"])
    
    # Door frame
    draw_rectangle(-45, -255, 90, 10, colors["window_frame"])
    
    # Door panels
    draw_rectangle(-30, -230, 25, 60, "#4A3020")
    draw_rectangle(5, -230, 25, 60, "#4A3020")
    
    # Door knob
    draw_circle(-25, -190, 5, colors["door_handle"])
    
    # Door step
    draw_rectangle(-50, -260, 100, 10, "#808080")

def draw_windows():
    """Draw windows on the house"""
    
    # Left window
    draw_rectangle(-100, -180, 50, 50, colors["window"])
    draw_rectangle(-100, -180, 50, 50, colors["window_frame"], False)
    
    # Window panes (left)
    draw_line(-75, -180, -75, -130, colors["window_frame"], 3)
    draw_line(-100, -155, -50, -155, colors["window_frame"], 3)
    
    # Window sill (left)
    draw_rectangle(-105, -185, 60, 8, colors["window_frame"])
    
    # Right window
    draw_rectangle(50, -180, 50, 50, colors["window"])
    draw_rectangle(50, -180, 50, 50, colors["window_frame"], False)
    
    # Window panes (right)
    draw_line(75, -180, 75, -130, colors["window_frame"], 3)
    draw_line(50, -155, 100, -155, colors["window_frame"], 3)
    
    # Window sill (right)
    draw_rectangle(45, -185, 60, 8, colors["window_frame"])
    
    # Attic window (round)
    draw_circle(0, 10, 20, colors["window"])
    draw_circle(0, 10, 20, colors["window_frame"], False)
    draw_line(0, -10, 0, 30, colors["window_frame"], 2)
    draw_line(-20, 10, 20, 10, colors["window_frame"], 2)

def draw_path():
    """Draw a path from door to bottom"""
    pen.penup()
    pen.goto(-40, -250)
    pen.pendown()
    pen.color(colors["path"])
    pen.begin_fill()
    pen.fillcolor(colors["path"])
    pen.goto(-20, -350)
    pen.goto(20, -350)
    pen.goto(40, -250)
    pen.goto(-40, -250)
    pen.end_fill()
    pen.penup()

def draw_fence():
    """Draw a wooden fence"""
    pen.color(colors["fence"])
    pen.pensize(3)
    
    for x in range(-380, 320, 50):
        if x < -90 or x > 50:  # Avoid blocking the house
            # Fence post
            draw_rectangle(x, -260, 8, 35, colors["fence"])
            # Fence picket top
            draw_triangle(x - 4, -225, 16, 15, colors["fence"])
    
    # Horizontal rails
    draw_line(-380, -245, 300, -245, colors["fence"], 3)
    draw_line(-380, -235, 300, -235, colors["fence"], 3)

def draw_flowers():
    """Draw flowers in the yard"""
    flower_positions = [(-300, -260), (-250, -270), (180, -265), (230, -255)]
    
    for x, y in flower_positions:
        # Stem
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("#228B22")
        pen.pensize(2)
        pen.goto(x, y + 15)
        
        # Flower petals
        pen.color("#FF69B4")
        for angle in range(0, 360, 60):
            rad = angle * 3.14159 / 180
            px = x + 6 * math.cos(rad)
            py = y + 15 + 6 * math.sin(rad)
            pen.penup()
            pen.goto(px, py)
            pen.pendown()
            pen.dot(6)
        
        # Flower center
        draw_circle(x, y + 15, 4, "#FFD700")
    
    pen.pensize(1)

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

def draw_birds():
    """Draw birds in the sky"""
    pen.color("#333333")
    pen.pensize(2)
    
    bird_positions = [(-200, 250), (-150, 230), (200, 260)]
    for x, y in bird_positions:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(-30)
        pen.circle(10, 60)
        pen.setheading(30)
        pen.circle(10, 60)
    pen.penup()

def draw_title():
    """Draw title text"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("#2C3E50")
    title.penup()
    title.hideturtle()
    title.goto(0, 380)
    title.write("🏠 HOUSE WITH WINDOWS, DOOR & CHIMNEY 🏠", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("#2C3E50")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -400)
    instructions.write("Press R to redraw | ESC to exit", align="center", font=("Arial", 12, "normal"))

def draw_house_scene():
    """Draw the complete house scene"""
    pen.clear()
    
    # Sky is already set as background color
    draw_sun()
    draw_cloud(-300, 300)
    draw_cloud(100, 320)
    draw_cloud(350, 290)
    draw_birds()
    
    draw_grass()
    draw_house()
    draw_chimney_smoke()
    draw_door()
    draw_windows()
    draw_path()
    draw_fence()
    draw_flowers()
    
    screen.update()

def draw_chimney_smoke():
    """Draw smoke coming from chimney"""
    smoke_colors = ["#E0E0E0", "#D0D0D0", "#C0C0C0", "#B0B0B0"]
    smoke_positions = [(100, 85), (105, 100), (95, 115), (110, 130), (100, 145)]
    
    for i, (x, y) in enumerate(smoke_positions):
        draw_circle(x, y, 8 - i * 0.5, smoke_colors[i % len(smoke_colors)])

def redraw():
    draw_house_scene()

# Import math for trig functions
import math

# Keyboard bindings
screen.listen()
screen.onkey(redraw, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()
draw_house_scene()

print("=" * 60)
print("        HOUSE WITH WINDOWS, DOOR & CHIMNEY")
print("=" * 60)
print()
print("A beautiful house scene with many details!")
print()
print("ELEMENTS INCLUDED:")
print("  🏠 House body (sandy brown walls)")
print("  🔺 Roof (saddle brown triangle)")
print("  🧱 Chimney with smoke")
print("  🚪 Front door with panels and knob")
print("  Window frames (left, right, and attic)")
print("  Window panes (cross pattern)")
print("  🪵 Wooden fence with pickets")
print("  🌿 Grass with blades")
print("  🪨 Stone path to door")
print("  🌸 Flowers in the yard")
print()
print("BACKGROUND:")
print("  ☀️ Sun with rays")
print("  ☁️ Floating clouds")
print("  🐦 Birds in the sky")
print()
print("SHAPES USED:")
print("  • Rectangles - House body, door, windows, chimney, fence")
print("  • Triangles - Roof, fence pickets")
print("  • Circles - Sun, clouds, flowers, smoke, doorknob")
print("  • Lines - Window panes, roof ridge, grass blades")
print()
print("CONTROLS:")
print("  R - Redraw the scene")
print("  ESC - Exit program")

screen.mainloop()