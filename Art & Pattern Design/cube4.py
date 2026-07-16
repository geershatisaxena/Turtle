import turtle
import math
import time
import random

# Setup
screen = turtle.Screen()
screen.bgcolor("#1a1a2e")
screen.title("Isometric Cube Grid Illusion")
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

def draw_isometric_cube(x, y, size, colors, shadow=True):
    """Draw an isometric 3D cube"""
    
    # Isometric projection angles
    angle1 = math.radians(30)
    angle2 = math.radians(150)
    angle3 = math.radians(90)
    
    # Cube vertices in isometric projection
    dx = size * math.cos(angle1)
    dy = size * math.sin(angle1)
    dx2 = size * math.cos(angle2)
    dy2 = size * math.sin(angle2)
    dz = size * 0.7  # Height
    
    # Calculate points
    p1 = (x, y)  # Top front
    p2 = (x + dx, y - dy)  # Top right
    p3 = (x + dx - dx2, y - dy - dy2)  # Bottom right
    p4 = (x - dx2, y - dy2)  # Bottom front
    p5 = (x, y + dz)  # Top back
    p6 = (x + dx, y - dy + dz)  # Back right
    p7 = (x + dx - dx2, y - dy - dy2 + dz)  # Bottom back right
    p8 = (x - dx2, y - dy2 + dz)  # Bottom back left
    
    # Draw shadow first
    if shadow:
        t.penup()
        t.goto(p4)
        t.pendown()
        t.color("black", "black")
        t.begin_fill()
        t.goto(p3)
        t.goto(p7)
        t.goto(p8)
        t.goto(p4)
        t.end_fill()
    
    # Draw faces (back to front)
    faces = [
        # Top face
        [p1, p2, p6, p5],
        # Right face
        [p2, p3, p7, p6],
        # Left face
        [p1, p5, p8, p4],
        # Front face
        [p1, p4, p3, p2]
    ]
    
    face_colors = [colors[0], colors[1], colors[2], colors[3]]
    
    # Draw each face
    for face, color in zip(faces, face_colors):
        t.penup()
        t.goto(face[0])
        t.pendown()
        t.fillcolor(color)
        t.color(color)
        t.begin_fill()
        for point in face:
            t.goto(point)
        t.end_fill()
        
        # Add outline
        t.penup()
        t.goto(face[0])
        t.pendown()
        t.color("white")
        t.pensize(0.5)
        for point in face:
            t.goto(point)
        t.pensize(1)

def draw_cube_grid_isometric(rows, cols, spacing, cube_size, color_scheme):
    """Draw an isometric grid of cubes"""
    
    # Offset for isometric grid
    offset_x = spacing * 0.866  # cos(30°)
    offset_y = spacing * 0.5    # sin(30°)
    
    start_x = -(cols - 1) * offset_x / 2
    start_y = -(rows - 1) * offset_y / 2
    
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * offset_x - row * offset_x
            y = start_y + col * offset_y + row * offset_y
            
            # Vary colors
            color_idx = (row + col) % len(color_scheme)
            colors = color_scheme[color_idx]
            
            # Vary size slightly for organic feel
            size_var = cube_size * (0.9 + 0.1 * math.sin(row * 0.5 + col * 0.7))
            
            draw_isometric_cube(x, y, size_var, colors)
            screen.update()
            time.sleep(0.02)

def draw_optical_illusion_grid():
    """Draw a cube grid that creates optical illusions"""
    
    # Title
    label_t.goto(0, 370)
    label_t.color("#FFD700")
    label_t.write("🌀 OPTICAL ILLUSION CUBE GRID 🌀", font=('Arial', 24, 'bold'), align="center")
    screen.update()
    
    # Color schemes for illusion effect
    schemes = [
        # High contrast
        [["#FF6B6B", "#C0392B", "#FF9F9F", "#E74C3C"],
         ["#4ECDC4", "#1ABC9C", "#7FDBB5", "#2ECC71"],
         ["#FFD93D", "#F39C12", "#FFEAA7", "#F1C40F"]],
        
        # Monochromatic
        [["#3498DB", "#2980B9", "#5DADE2", "#2471A3"],
         ["#3498DB", "#2980B9", "#5DADE2", "#2471A3"],
         ["#3498DB", "#2980B9", "#5DADE2", "#2471A3"]],
        
        # Neon
        [["#FF00FF", "#CC00CC", "#FF33FF", "#990099"],
         ["#00FF00", "#00CC00", "#33FF33", "#009900"],
         ["#00FFFF", "#00CCCC", "#33FFFF", "#009999"]]
    ]
    
    # Draw different grid patterns
    patterns = [
        (4, 4, 60, 35),   # Standard grid
        (5, 5, 50, 28),   # Dense grid
        (3, 3, 80, 45),   # Sparse grid
    ]
    
    positions = [
        (-300, 100),
        (300, 100),
        (0, -150)
    ]
    
    for idx, ((rows, cols, spacing, size), pos) in enumerate(zip(patterns, positions)):
        scheme = schemes[idx % len(schemes)]
        
        # Draw grid
        draw_cube_grid_isometric_subset(rows, cols, spacing, size, scheme, pos[0], pos[1])
        
        # Label
        label_t.goto(pos[0], pos[1] + rows * spacing * 0.4 + 40)
        label_t.color("#87CEEB")
        label_t.write(f"{rows}x{cols} Grid", font=('Arial', 12), align="center")
        screen.update()

def draw_cube_grid_isometric_subset(rows, cols, spacing, cube_size, color_scheme, offset_x, offset_y):
    """Draw a subset of isometric grid"""
    
    spacing_x = spacing * 0.866
    spacing_y = spacing * 0.5
    
    start_x = offset_x - (cols - 1) * spacing_x / 2
    start_y = offset_y - (rows - 1) * spacing_y / 2
    
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * spacing_x - row * spacing_x
            y = start_y + col * spacing_y + row * spacing_y
            
            # Create illusion by alternating colors
            if (row + col) % 2 == 0:
                colors = color_scheme[0]
            else:
                colors = color_scheme[1] if len(color_scheme) > 1 else color_scheme[0]
            
            # Add rotation illusion (some cubes appear to flip)
            if row == col or row + col == rows - 1:
                # Swap colors for illusion
                colors = colors[::-1]
            
            draw_isometric_cube(x, y, cube_size, colors)

def draw_floating_cubes():
    """Draw cubes that appear to float in 3D space"""
    
    label_t.goto(0, -250)
    label_t.color("#FFD700")
    label_t.write("🌟 Floating Cubes Illusion 🌟", font=('Arial', 20, 'bold'), align="center")
    screen.update()
    
    # Draw cubes in a spiral pattern
    num_cubes = 20
    radius = 200
    
    for i in range(num_cubes):
        angle = (i / num_cubes) * 2 * math.pi * 3  # 3 full rotations
        r = radius * (i / num_cubes)
        x = r * math.cos(angle)
        y = r * math.sin(angle) - 80
        
        # Size increases with distance from center
        size = 15 + 25 * (i / num_cubes)
        
        # Colors shift along spiral
        hue = (i / num_cubes) * 360
        color1 = f"hsv({hue}, 0.9, 0.9)"
        color2 = f"hsv({hue + 60}, 0.9, 0.8)"
        color3 = f"hsv({hue + 120}, 0.9, 0.7)"
        color4 = f"hsv({hue + 180}, 0.9, 0.6)"
        
        # Add floating effect with shadows
        draw_isometric_cube(x, y, size, [color1, color2, color3, color4], shadow=True)
        screen.update()
        time.sleep(0.05)

def draw_impossible_cube_illusion():
    """Draw an impossible cube illusion"""
    
    label_t.goto(350, 370)
    label_t.color("#FFD700")
    label_t.write("🔲 Impossible Cube", font=('Arial', 16, 'bold'), align="center")
    screen.update()
    
    # Draw an impossible cube (Penrose triangle style)
    size = 60
    x, y = 350, 100
    
    # Draw overlapping cubes to create impossible effect
    for i in range(3):
        offset = i * 15
        colors = ["#FF6B6B", "#4ECDC4", "#FFD93D", "#6C5CE7"]
        draw_isometric_cube(x + offset, y - offset, size - i * 5, colors)
        screen.update()
        time.sleep(0.3)

def draw_animated_cube_wave():
    """Draw an animated wave of cubes"""
    
    label_t.goto(0, 450)
    label_t.color("#FFD700")
    label_t.write("🌊 Cube Wave Animation 🌊", font=('Arial', 20, 'bold'), align="center")
    screen.update()
    
    # Parameters
    cols, rows = 8, 5
    spacing = 45
    cube_size = 20
    
    # Animate for 40 frames
    for frame in range(40):
        t.clear()
        
        for row in range(rows):
            for col in range(cols):
                # Calculate wave height
                wave = math.sin((col / cols) * 2 * math.pi + (frame / 10)) * 20
                wave += math.cos((row / rows) * 2 * math.pi + (frame / 15)) * 15
                
                # Position with wave
                x = - (cols - 1) * spacing / 2 + col * spacing
                y = - (rows - 1) * spacing / 2 + row * spacing + wave
                
                # Color based on wave height
                height_norm = (wave + 35) / 70
                r = int(255 * height_norm)
                g = int(100 + 155 * (1 - height_norm))
                b = int(255 * (1 - height_norm))
                color = f"#{r:02x}{g:02x}{b:02x}"
                
                colors = [color, darken_color(color, 0.7), darken_color(color, 0.5), darken_color(color, 0.8)]
                
                draw_isometric_cube(x, y, cube_size, colors, shadow=False)
        
        screen.update()
        time.sleep(0.05)

def darken_color(hex_color, factor):
    """Darken a hex color by a factor"""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    
    return f"#{r:02x}{g:02x}{b:02x}"

# Main execution
print("Drawing Isometric Cube Grid Illusion...")

# Draw the main illusion
draw_optical_illusion_grid()

# Draw floating cubes
draw_floating_cubes()

# Draw impossible cube
draw_impossible_cube_illusion()

# Draw animated cube wave
draw_animated_cube_wave()

# Add instructions
label_t.goto(0, -400)
label_t.color("#95a5a6")
label_t.write("🖱️ Click anywhere to exit", font=('Arial', 12), align="center")
screen.update()

# Keep window open
screen.mainloop()