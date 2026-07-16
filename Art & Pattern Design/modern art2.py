import turtle
import random
import math
import time

# Setup
screen = turtle.Screen()
screen.bgcolor("#1a1a2e")
screen.title("Abstract Modern Art Generator")
screen.tracer(0)
screen.setup(1000, 800)

# Create turtles
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

label_t = turtle.Turtle()
label_t.speed(0)
label_t.hideturtle()
label_t.penup()

# Color palettes for modern art
PALETTES = {
    "vibrant": ["#FF6B6B", "#4ECDC4", "#FFD93D", "#6C5CE7", "#FF9FF3", "#54A0FF"],
    "pastel": ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", "#E8BAFF"],
    "monochrome": ["#2C3E50", "#34495E", "#7F8C8D", "#BDC3C7", "#ECF0F1", "#95A5A6"],
    "earth": ["#8B6914", "#CD853F", "#8B4513", "#A0522D", "#D2691E", "#F4A460"],
    "ocean": ["#006994", "#0077BE", "#008B8B", "#20B2AA", "#48D1CC", "#7FFFD4"],
    "sunset": ["#FF4500", "#FF6347", "#FF7F50", "#FFA07A", "#FFD700", "#FF8C00"],
    "neon": ["#FF00FF", "#00FF00", "#00FFFF", "#FF0000", "#FFFF00", "#FF0099"],
    "muted": ["#A8A8A8", "#C4C4C4", "#E0E0E0", "#8B8B8B", "#6B6B6B", "#4B4B4B"]
}

def random_color(palette=None):
    """Get a random color from a palette or generate one"""
    if palette:
        return random.choice(palette)
    else:
        # Generate random vibrant color
        return f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"

def draw_random_shape(x, y, size):
    """Draw a random abstract shape"""
    shape_type = random.choice(["circle", "square", "triangle", "pentagon", "hexagon", "star", "spiral", "blob"])
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    color = random_color(random.choice(list(PALETTES.values())))
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    
    if shape_type == "circle":
        t.circle(size)
    
    elif shape_type == "square":
        for _ in range(4):
            t.forward(size * 2)
            t.left(90)
    
    elif shape_type == "triangle":
        for _ in range(3):
            t.forward(size * 2)
            t.left(120)
    
    elif shape_type == "pentagon":
        for _ in range(5):
            t.forward(size * 1.5)
            t.left(72)
    
    elif shape_type == "hexagon":
        for _ in range(6):
            t.forward(size * 1.2)
            t.left(60)
    
    elif shape_type == "star":
        for _ in range(5):
            t.forward(size * 2)
            t.right(144)
            t.forward(size)
            t.left(72)
    
    elif shape_type == "spiral":
        t.end_fill()
        t.color(color)
        for i in range(30):
            t.forward(size * (i / 30))
            t.left(15)
        return
    
    elif shape_type == "blob":
        t.end_fill()
        t.color(color)
        points = random.randint(6, 12)
        for i in range(points):
            angle = (i / points) * 360
            rad = math.radians(angle)
            r = size * (0.5 + random.random() * 0.5)
            x_pos = x + r * math.cos(rad)
            y_pos = y + r * math.sin(rad)
            t.goto(x_pos, y_pos)
        t.goto(x, y)
        return
    
    t.end_fill()

def draw_random_line():
    """Draw a random abstract line"""
    x1 = random.randint(-400, 400)
    y1 = random.randint(-350, 350)
    x2 = random.randint(-400, 400)
    y2 = random.randint(-350, 350)
    
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    
    color = random_color(random.choice(list(PALETTES.values())))
    t.color(color)
    t.pensize(random.randint(1, 8))
    
    # Random line style
    style = random.choice(["straight", "dashed", "dotted", "curved", "zigzag"])
    
    if style == "straight":
        t.goto(x2, y2)
    
    elif style == "dashed":
        steps = random.randint(5, 15)
        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps
        for i in range(steps):
            t.goto(x1 + (i + 0.5) * dx, y1 + (i + 0.5) * dy)
            t.penup()
            t.goto(x1 + (i + 1) * dx, y1 + (i + 1) * dy)
            t.pendown()
    
    elif style == "dotted":
        steps = random.randint(10, 30)
        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps
        for i in range(steps):
            t.penup()
            t.goto(x1 + i * dx, y1 + i * dy)
            t.pendown()
            t.dot(random.randint(3, 10))
    
    elif style == "curved":
        control_x = random.randint(-400, 400)
        control_y = random.randint(-350, 350)
        for i in range(100):
            frac = i / 100
            # Quadratic bezier
            bx = (1-frac)**2 * x1 + 2*(1-frac)*frac * control_x + frac**2 * x2
            by = (1-frac)**2 * y1 + 2*(1-frac)*frac * control_y + frac**2 * y2
            t.goto(bx, by)
    
    elif style == "zigzag":
        steps = random.randint(5, 12)
        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps
        for i in range(steps):
            zigzag_x = x1 + i * dx + random.randint(-30, 30)
            zigzag_y = y1 + i * dy + random.randint(-30, 30)
            t.goto(zigzag_x, zigzag_y)
    
    t.pensize(1)

def draw_painting():
    """Generate a complete abstract painting"""
    
    # Clear screen
    t.clear()
    
    # Random background color
    bg_color = random.choice(["#1a1a2e", "#16213e", "#0f3460", "#2d3436", "#2c3e50", "#1a1a1a", "#0a0a1a"])
    screen.bgcolor(bg_color)
    
    # Determine number of elements
    num_shapes = random.randint(20, 80)
    num_lines = random.randint(10, 40)
    num_dots = random.randint(30, 100)
    
    # Draw shapes
    for _ in range(num_shapes):
        x = random.randint(-450, 450)
        y = random.randint(-350, 350)
        size = random.randint(10, 60)
        draw_random_shape(x, y, size)
        screen.update()
    
    # Draw lines
    for _ in range(num_lines):
        draw_random_line()
        screen.update()
    
    # Draw dots
    for _ in range(num_dots):
        x = random.randint(-450, 450)
        y = random.randint(-350, 350)
        t.penup()
        t.goto(x, y)
        t.pendown()
        color = random_color(random.choice(list(PALETTES.values())))
        t.color(color)
        t.dot(random.randint(2, 15))
        screen.update()
    
    # Add some random splatters
    for _ in range(random.randint(5, 20)):
        x = random.randint(-450, 450)
        y = random.randint(-350, 350)
        t.penup()
        t.goto(x, y)
        t.pendown()
        color = random_color(random.choice(list(PALETTES.values())))
        t.color(color)
        for _ in range(random.randint(3, 8)):
            angle = random.uniform(0, 360)
            rad = math.radians(angle)
            distance = random.randint(5, 30)
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.goto(x + distance * math.cos(rad), y + distance * math.sin(rad))
            t.dot(random.randint(2, 6))
    
    screen.update()

def draw_generative_pattern():
    """Draw a generative pattern with mathematical beauty"""
    
    pattern_type = random.choice(["waves", "spiral", "mandala", "grid", "radial", "chaos"])
    
    t.penup()
    t.goto(0, 0)
    
    color_palette = random.choice(list(PALETTES.values()))
    
    if pattern_type == "waves":
        # Draw wave patterns
        for i in range(100):
            x = -400 + i * 8
            y = 100 * math.sin(x / 50 + i / 20) + 50 * math.sin(x / 30)
            t.goto(x, y)
            t.pendown()
            t.color(random.choice(color_palette))
            t.dot(random.randint(2, 6))
    
    elif pattern_type == "spiral":
        # Draw spiral pattern
        for i in range(200):
            angle = i * 0.1
            rad = math.radians(angle)
            r = i * 0.5
            x = r * math.cos(rad)
            y = r * math.sin(rad)
            t.goto(x, y)
            t.pendown()
            t.color(random.choice(color_palette))
            t.dot(random.randint(2, 8))
    
    elif pattern_type == "mandala":
        # Draw mandala pattern
        for i in range(36):
            angle = i * 10
            rad = math.radians(angle)
            x = 200 * math.cos(rad)
            y = 200 * math.sin(rad)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.color(random.choice(color_palette))
            t.pensize(random.randint(1, 3))
            t.goto(x, y)
            
            # Draw petals
            for j in range(5):
                petal_angle = rad + j * 0.3
                petal_x = x + 40 * math.cos(petal_angle)
                petal_y = y + 40 * math.sin(petal_angle)
                t.goto(petal_x, petal_y)
    
    elif pattern_type == "grid":
        # Draw abstract grid
        for x in range(-400, 400, 20):
            for y in range(-300, 300, 20):
                if random.random() > 0.7:
                    t.penup()
                    t.goto(x, y)
                    t.pendown()
                    t.color(random.choice(color_palette))
                    size = random.randint(3, 10)
                    t.begin_fill()
                    for _ in range(4):
                        t.forward(size)
                        t.left(90)
                    t.end_fill()
    
    elif pattern_type == "radial":
        # Draw radial pattern
        for i in range(60):
            angle = i * 6
            rad = math.radians(angle)
            for r in range(0, 200, 20):
                x = r * math.cos(rad)
                y = r * math.sin(rad)
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.color(random.choice(color_palette))
                t.dot(random.randint(2, 5))
    
    elif pattern_type == "chaos":
        # Draw chaotic pattern
        x, y = 0, 0
        for i in range(1000):
            choice = random.random()
            if choice < 0.4:
                x, y = -x, -y
            elif choice < 0.7:
                x, y = x + random.uniform(-10, 10), y + random.uniform(-10, 10)
            else:
                x, y = x * random.uniform(0.5, 1.5), y * random.uniform(0.5, 1.5)
            
            t.penup()
            t.goto(x * 3, y * 3)
            t.pendown()
            t.color(random.choice(color_palette))
            t.dot(random.randint(1, 4))
    
    screen.update()

def draw_art_gallery():
    """Draw a gallery of abstract art pieces"""
    
    # Title
    label_t.goto(0, 380)
    label_t.color("#FFD700")
    label_t.write("🎨 ABSTRACT MODERN ART GENERATOR 🎨", font=('Arial', 24, 'bold'), align="center")
    screen.update()
    
    # Draw 6 mini art pieces
    positions = [
        (-300, 200),
        (0, 200),
        (300, 200),
        (-300, -100),
        (0, -100),
        (300, -100)
    ]
    
    for i, (x, y) in enumerate(positions):
        # Save current state
        t.penup()
        t.goto(x - 120, y - 80)
        t.pendown()
        
        # Draw frame
        t.color("white")
        t.pensize(2)
        for _ in range(4):
            t.forward(240)
            t.left(90)
        
        # Draw mini abstract piece inside frame
        t.penup()
        t.goto(x, y)
        
        # Use clipping region (simulate by drawing inside)
        for _ in range(random.randint(5, 15)):
            sx = x + random.randint(-100, 100)
            sy = y + random.randint(-60, 60)
            size = random.randint(5, 30)
            t.penup()
            t.goto(sx, sy)
            t.pendown()
            
            color = random_color(random.choice(list(PALETTES.values())))
            t.color(color)
            t.fillcolor(color)
            t.begin_fill()
            
            # Random shape
            sides = random.randint(3, 8)
            for _ in range(sides):
                t.forward(size)
                t.left(360 / sides)
            t.end_fill()
            
            # Add some dots
            if random.random() > 0.6:
                t.penup()
                t.goto(sx + random.randint(-20, 20), sy + random.randint(-20, 20))
                t.pendown()
                t.color(random_color(random.choice(list(PALETTES.values()))))
                t.dot(random.randint(2, 8))
        
        # Label the piece
        label_t.goto(x, y - 100)
        label_t.color("#87CEEB")
        label_t.write(f"Piece #{i+1}", font=('Arial', 12), align="center")
        screen.update()
        time.sleep(0.2)

# Main execution
print("Generating Abstract Modern Art...")

# Generate a large painting
draw_painting()

# Draw generative patterns
draw_generative_pattern()

# Draw art gallery
draw_art_gallery()

# Add interactive controls
label_t.goto(0, -380)
label_t.color("#95a5a6")
label_t.write("🖱️ Click to generate new art | Press 'r' for random | Press 'c' to clear", 
             font=('Arial', 12), align="center")
screen.update()

# Mouse click handler
def generate_new_art(x, y):
    """Generate new art on click"""
    draw_painting()
    draw_generative_pattern()

# Keyboard handlers
def random_art():
    """Generate completely random art"""
    draw_painting()
    draw_generative_pattern()

def clear_screen():
    """Clear the screen"""
    t.clear()
    screen.bgcolor("#1a1a2e")
    label_t.clear()
    label_t.goto(0, 380)
    label_t.color("#FFD700")
    label_t.write("🎨 ABSTRACT MODERN ART GENERATOR 🎨", font=('Arial', 24, 'bold'), align="center")
    label_t.goto(0, -380)
    label_t.color("#95a5a6")
    label_t.write("🖱️ Click to generate new art | Press 'r' for random | Press 'c' to clear", 
                 font=('Arial', 12), align="center")
    screen.update()

# Bind events
screen.onclick(generate_new_art)
screen.onkey(random_art, "r")
screen.onkey(clear_screen, "c")
screen.listen()

# Keep window open
screen.mainloop()