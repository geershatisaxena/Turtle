import turtle
import random
import math
import time

# Setup
screen = turtle.Screen()
screen.bgcolor("#0a0a1a")
screen.title("Abstract Art Generator 2.0")
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

# Extended color palettes
PALETTES = {
    "rainbow": ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"],
    "candy": ["#FF6B9D", "#FFA07A", "#FFD700", "#98FB98", "#87CEEB", "#DDA0DD"],
    "retro": ["#F4A460", "#D2691E", "#8B4513", "#CD853F", "#DEB887", "#F5DEB3"],
    "cyberpunk": ["#FF00FF", "#00FFFF", "#FF0000", "#00FF00", "#FFFF00", "#FF0099"],
    "watercolor": ["#FFB6C1", "#FFDAB9", "#FFFACD", "#B0E0E6", "#D8BFD8", "#E6E6FA"],
    "minimal": ["#000000", "#FFFFFF", "#808080", "#C0C0C0", "#333333", "#666666"],
    "autumn": ["#FF6347", "#FF8C00", "#FFD700", "#8B4513", "#A0522D", "#D2691E"],
    "spring": ["#FF69B4", "#FFB6C1", "#98FB98", "#7FFF00", "#00FA9A", "#00CED1"],
    "cosmic": ["#191970", "#483D8B", "#6A5ACD", "#7B68EE", "#9370DB", "#8A2BE2"],
    "tropical": ["#FF1493", "#FF4500", "#FFD700", "#00FF7F", "#00BFFF", "#FF69B4"]
}

def random_color_from_palette(palette_name=None):
    """Get random color from palette or generate random"""
    if palette_name and palette_name in PALETTES:
        return random.choice(PALETTES[palette_name])
    else:
        palette_name = random.choice(list(PALETTES.keys()))
        return random.choice(PALETTES[palette_name])

def random_palette():
    """Get random palette name"""
    return random.choice(list(PALETTES.keys()))

# ============ SHAPE GENERATORS ============

def draw_organic_shape(x, y, size):
    """Draw organic, free-form shapes"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    color = random_color_from_palette()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    
    points = random.randint(8, 20)
    for i in range(points):
        angle = (i / points) * 360 + random.uniform(-15, 15)
        rad = math.radians(angle)
        r = size * (0.3 + random.uniform(0.3, 0.7))
        x_pos = x + r * math.cos(rad)
        y_pos = y + r * math.sin(rad)
        t.goto(x_pos, y_pos)
    
    t.goto(x, y)
    t.end_fill()

def draw_geometric_abstract(x, y, size):
    """Draw geometric abstract shapes"""
    shape = random.choice(["triangle", "square", "pentagon", "hexagon", "octagon", "star"])
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    color = random_color_from_palette()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    
    sides = {
        "triangle": 3, "square": 4, "pentagon": 5,
        "hexagon": 6, "octagon": 8, "star": 10
    }[shape]
    
    angle = 360 / sides
    
    if shape == "star":
        for i in range(sides):
            t.forward(size)
            t.right(144)
            t.forward(size * 0.5)
            t.left(72)
    else:
        for i in range(sides):
            t.forward(size * 1.5)
            t.left(angle)
    
    t.end_fill()

def draw_flow_field(x, y, size):
    """Draw flowing organic lines"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    color = random_color_from_palette()
    t.color(color)
    t.pensize(random.uniform(1, 3))
    
    steps = random.randint(20, 50)
    for i in range(steps):
        angle = (i / steps) * 360 + random.uniform(-30, 30)
        rad = math.radians(angle)
        r = size * (i / steps)
        x_pos = x + r * math.cos(rad + i * 0.1)
        y_pos = y + r * math.sin(rad + i * 0.1)
        t.goto(x_pos, y_pos)
    
    t.pensize(1)

def draw_cellular_pattern(x, y, size):
    """Draw cellular/biological patterns"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    color = random_color_from_palette()
    t.color(color)
    
    cells = random.randint(4, 10)
    for i in range(cells):
        angle = (i / cells) * 360
        rad = math.radians(angle)
        cx = x + size * 0.8 * math.cos(rad)
        cy = y + size * 0.8 * math.sin(rad)
        
        t.penup()
        t.goto(cx, cy)
        t.pendown()
        t.fillcolor(random_color_from_palette())
        t.begin_fill()
        t.circle(random.uniform(size * 0.2, size * 0.4))
        t.end_fill()

def draw_chaos_pattern(x, y, size):
    """Draw chaotic fractal-like patterns"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    color = random_color_from_palette()
    t.color(color)
    t.pensize(random.uniform(0.5, 1.5))
    
    iterations = random.randint(30, 80)
    for i in range(iterations):
        angle = random.uniform(0, 360)
        rad = math.radians(angle)
        distance = random.uniform(0, size)
        x_pos = x + distance * math.cos(rad)
        y_pos = y + distance * math.sin(rad)
        
        if random.random() > 0.5:
            t.goto(x_pos, y_pos)
        else:
            t.penup()
            t.goto(x_pos, y_pos)
            t.pendown()
        
        if random.random() > 0.95:
            t.color(random_color_from_palette())
            t.dot(random.randint(3, 8))
    
    t.pensize(1)

# ============ LINE GENERATORS ============

def draw_calligraphic_line(x1, y1, x2, y2):
    """Draw calligraphic-style lines"""
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    
    color = random_color_from_palette()
    t.color(color)
    t.pensize(random.uniform(1, 5))
    
    steps = random.randint(20, 60)
    for i in range(steps):
        frac = i / steps
        # Bezier curve with random control points
        cx1 = random.uniform(x1, x2)
        cy1 = random.uniform(y1, y2)
        cx2 = random.uniform(x1, x2)
        cy2 = random.uniform(y1, y2)
        
        bx = (1-frac)**3 * x1 + 3*(1-frac)**2*frac * cx1 + 3*(1-frac)*frac**2 * cx2 + frac**3 * x2
        by = (1-frac)**3 * y1 + 3*(1-frac)**2*frac * cy1 + 3*(1-frac)*frac**2 * cy2 + frac**3 * y2
        t.goto(bx, by)
        
        # Vary thickness
        if random.random() > 0.9:
            t.pensize(random.uniform(1, 5))
    
    t.pensize(1)

def draw_gesture_line(x1, y1, x2, y2):
    """Draw expressive gesture lines"""
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    
    color = random_color_from_palette()
    t.color(color)
    t.pensize(random.uniform(2, 6))
    
    # Add energy to the line
    for i in range(20):
        frac = i / 20
        x = x1 + (x2 - x1) * frac + random.uniform(-20, 20) * (1 - frac)
        y = y1 + (y2 - y1) * frac + random.uniform(-20, 20) * (1 - frac)
        t.goto(x, y)
    
    t.pensize(1)

def draw_drip_line(x1, y1, x2, y2):
    """Draw drip/paint splatter lines"""
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    
    color = random_color_from_palette()
    t.color(color)
    
    # Main line
    for i in range(30):
        frac = i / 30
        x = x1 + (x2 - x1) * frac
        y = y1 + (y2 - y1) * frac + 10 * math.sin(frac * 10)
        t.goto(x, y)
        
        # Add drips
        if random.random() > 0.9:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(random.randint(2, 6))
            t.penup()
            t.goto(x, y - random.randint(10, 30))
            t.pendown()
            t.dot(random.randint(1, 3))
            t.penup()
            t.goto(x, y)
            t.pendown()

# ============ COMPOSITION GENERATORS ============

def generate_abstract_composition():
    """Generate a complete abstract composition"""
    
    # Random background
    bg_options = ["#0a0a1a", "#1a1a2e", "#2d1b3d", "#1b2d3d", "#2d2d1b", "#3d1b1b"]
    screen.bgcolor(random.choice(bg_options))
    
    # Clear previous
    t.clear()
    
    # Choose art style
    style = random.choice(["organic", "geometric", "expressionist", "minimal", "chaotic"])
    
    # Determine number of elements
    num_layers = random.randint(3, 7)
    
    # Draw layers from background to foreground
    for layer in range(num_layers):
        # Layer-specific settings
        alpha = (layer + 1) / num_layers
        size_multiplier = 1 - layer * 0.1
        
        # Number of elements per layer
        num_elements = random.randint(5, 20)
        
        for _ in range(num_elements):
            x = random.randint(-450, 450)
            y = random.randint(-350, 350)
            size = random.randint(20, 80) * size_multiplier
            
            # Choose function based on style
            if style == "organic":
                draw_organic_shape(x, y, size)
            elif style == "geometric":
                draw_geometric_abstract(x, y, size)
            elif style == "expressionist":
                if random.random() > 0.5:
                    draw_organic_shape(x, y, size)
                else:
                    draw_flow_field(x, y, size)
            elif style == "minimal":
                if random.random() > 0.7:
                    draw_geometric_abstract(x, y, size)
            else:  # chaotic
                draw_chaos_pattern(x, y, size)
            
            screen.update()
    
    # Add lines
    num_lines = random.randint(5, 20)
    for _ in range(num_lines):
        x1 = random.randint(-450, 450)
        y1 = random.randint(-350, 350)
        x2 = random.randint(-450, 450)
        y2 = random.randint(-350, 350)
        
        line_style = random.choice(["calligraphic", "gesture", "drip"])
        if line_style == "calligraphic":
            draw_calligraphic_line(x1, y1, x2, y2)
        elif line_style == "gesture":
            draw_gesture_line(x1, y1, x2, y2)
        else:
            draw_drip_line(x1, y1, x2, y2)
        
        screen.update()
    
    # Add random dots and splatters
    for _ in range(random.randint(20, 60)):
        x = random.randint(-450, 450)
        y = random.randint(-350, 350)
        t.penup()
        t.goto(x, y)
        t.pendown()
        color = random_color_from_palette()
        t.color(color)
        t.dot(random.randint(2, 12))
        screen.update()

def generate_art_with_movement():
    """Generate art that appears to have movement"""
    
    label_t.goto(0, 370)
    label_t.color("#FFD700")
    label_t.write("🎨 ABSTRACT ART WITH MOVEMENT 🎨", font=('Arial', 24, 'bold'), align="center")
    screen.update()
    
    # Create flowing lines with motion
    for _ in range(20):
        x_start = random.randint(-450, 450)
        y_start = random.randint(-350, 350)
        
        t.penup()
        t.goto(x_start, y_start)
        t.pendown()
        
        color = random_color_from_palette()
        t.color(color)
        t.pensize(random.uniform(1, 4))
        
        # Draw a flowing path
        x, y = x_start, y_start
        for _ in range(random.randint(30, 80)):
            angle = random.uniform(0, 360)
            distance = random.uniform(5, 20)
            x += distance * math.cos(math.radians(angle))
            y += distance * math.sin(math.radians(angle))
            
            # Keep within bounds
            x = max(-450, min(450, x))
            y = max(-350, min(350, y))
            
            t.goto(x, y)
            
            # Add dots along the path
            if random.random() > 0.95:
                t.dot(random.randint(3, 8))
            
            screen.update()
        
        t.pensize(1)

def generate_art_with_texture():
    """Generate art with textured effects"""
    
    label_t.goto(0, 370)
    label_t.color("#FFD700")
    label_t.write("🎨 TEXTURED ABSTRACT ART 🎨", font=('Arial', 24, 'bold'), align="center")
    screen.update()
    
    # Create textured backgrounds
    for x in range(-450, 450, 5):
        for y in range(-350, 350, 5):
            if random.random() > 0.7:
                t.penup()
                t.goto(x, y)
                t.pendown()
                color = random_color_from_palette()
                t.color(color)
                t.dot(random.randint(1, 3))
        
        # Update progress
        if x % 50 == 0:
            screen.update()
    
    # Add larger elements on top
    for _ in range(random.randint(10, 20)):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(20, 50)
        
        if random.random() > 0.5:
            draw_organic_shape(x, y, size)
        else:
            draw_flow_field(x, y, size)
        
        screen.update()

# ============ MAIN EXECUTION ============

print("Generating Abstract Modern Art 2.0...")

# Generate main compositions
generate_abstract_composition()
generate_art_with_movement()

# Move to bottom
t.penup()
t.goto(0, -350)
t.pendown()

# Add status
label_t.goto(0, 330)
label_t.color("#87CEEB")
label_t.write("✨ Abstract Art Generator 2.0 ✨", font=('Arial', 18), align="center")
screen.update()

# Generate textured art at bottom
label_t.goto(0, -100)
label_t.color("#FFD700")
label_t.write("Textured Art Style", font=('Arial', 16), align="center")
screen.update()

t.clear()
generate_art_with_texture()

# Add interactive instructions
label_t.goto(0, -380)
label_t.color("#95a5a6")
label_t.write("🖱️ Click to generate new art | 'r' for random | 's' for style | 'c' to clear", 
             font=('Arial', 11), align="center")
screen.update()

# Event handlers
def generate_new_art(x, y):
    """Generate new art on click"""
    t.clear()
    generate_abstract_composition()

def generate_random_art():
    """Generate completely random art"""
    t.clear()
    generate_abstract_composition()

def generate_style_art():
    """Generate art with a specific style"""
    t.clear()
    styles = ["organic", "geometric", "expressionist", "minimal", "chaotic"]
    label_t.goto(0, 330)
    label_t.color("#FFD700")
    label_t.write(f"Style: {random.choice(styles)}", font=('Arial', 14), align="center")
    screen.update()
    generate_abstract_composition()

def clear_screen():
    """Clear everything"""
    t.clear()
    screen.bgcolor("#0a0a1a")
    label_t.clear()

# Bind events
screen.onclick(generate_new_art)
screen.onkey(generate_random_art, "r")
screen.onkey(generate_style_art, "s")
screen.onkey(clear_screen, "c")
screen.listen()

# Keep window open
screen.mainloop()