import turtle
import math
import time

# Setup
screen = turtle.Screen()
screen.bgcolor("#0a0a1a")
screen.title("3D Cube Grid Illusion")
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

def draw_cube_3d(x, y, size, depth, colors, rotation=0):
    """Draw a 3D cube with perspective"""
    
    # Calculate corner points with rotation
    angle = math.radians(rotation)
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    
    # Cube vertices (3D coordinates)
    vertices = [
        (-size/2, -size/2, -size/2),
        (size/2, -size/2, -size/2),
        (size/2, size/2, -size/2),
        (-size/2, size/2, -size/2),
        (-size/2, -size/2, size/2),
        (size/2, -size/2, size/2),
        (size/2, size/2, size/2),
        (-size/2, size/2, size/2)
    ]
    
    # Project 3D to 2D with rotation
    projected = []
    for v in vertices:
        # Rotate around Y axis
        x1 = v[0] * cos_a - v[2] * sin_a
        y1 = v[1]
        z1 = v[0] * sin_a + v[2] * cos_a
        
        # Simple perspective projection
        scale = depth / (depth + z1)
        px = x + x1 * scale
        py = y + y1 * scale
        projected.append((px, py, z1))
    
    # Define faces (front, back, top, bottom, left, right)
    faces = [
        (0, 1, 2, 3),  # Front
        (4, 5, 6, 7),  # Back
        (3, 2, 6, 7),  # Top
        (0, 1, 5, 4),  # Bottom
        (0, 3, 7, 4),  # Left
        (1, 2, 6, 5)   # Right
    ]
    
    face_colors = [
        colors[0],  # Front
        colors[1],  # Back
        colors[2],  # Top
        colors[3],  # Bottom
        colors[4],  # Left
        colors[5]   # Right
    ]
    
    # Draw faces from back to front
    face_order = sorted(range(len(faces)), 
                       key=lambda i: sum(projected[faces[i][j]][2] for j in range(4)) / 4,
                       reverse=True)
    
    for idx in face_order:
        face = faces[idx]
        pts = [projected[i] for i in face]
        
        # Check if face is visible
        if is_face_visible(pts):
            t.penup()
            t.goto(pts[0][0], pts[0][1])
            t.pendown()
            
            # Set color with transparency effect
            t.fillcolor(face_colors[idx])
            t.color(face_colors[idx])
            t.begin_fill()
            
            # Draw face with slight animation
            for i in range(5):
                pt = pts[i % 4]
                t.goto(pt[0], pt[1])
            
            t.end_fill()
            
            # Draw outline
            t.penup()
            t.goto(pts[0][0], pts[0][1])
            t.pendown()
            t.color("white")
            t.pensize(0.5)
            for i in range(5):
                pt = pts[i % 4]
                t.goto(pt[0], pt[1])
            t.pensize(1)

def is_face_visible(points):
    """Check if a face is visible using normal vector"""
    if len(points) < 3:
        return False
    
    # Calculate normal vector
    v1 = (points[1][0] - points[0][0], points[1][1] - points[0][1])
    v2 = (points[2][0] - points[0][0], points[2][1] - points[0][1])
    
    # Cross product (z component)
    normal_z = v1[0] * v2[1] - v1[1] * v2[0]
    
    # Face is visible if normal points toward viewer
    return normal_z > 0

def draw_cube_grid(rows, cols, spacing, cube_size, depth, color_schemes):
    """Draw a grid of 3D cubes"""
    
    start_x = -(cols - 1) * spacing / 2
    start_y = -(rows - 1) * spacing / 2
    
    total_cubes = rows * cols
    current = 0
    
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * spacing
            y = start_y + row * spacing
            
            # Vary colors based on position
            scheme_index = (row + col) % len(color_schemes)
            colors = color_schemes[scheme_index]
            
            # Vary rotation
            rotation = (row * 15 + col * 25) % 360
            
            # Draw the cube
            draw_cube_3d(x, y, cube_size, depth, colors, rotation)
            
            current += 1
            progress = int(current / total_cubes * 100)
            
            # Update progress
            if current % 5 == 0:
                label_t.goto(0, 350)
                label_t.color("#87CEEB")
                label_t.write(f"Drawing Cube Grid: {progress}%", 
                             font=('Arial', 14), align="center")
                screen.update()
            
            time.sleep(0.02)

def draw_cube_grid_illusion():
    """Create the cube grid illusion with animation"""
    
    # Title
    label_t.goto(0, 380)
    label_t.color("#FFD700")
    label_t.write("🎲 3D CUBE GRID ILLUSION 🎲", font=('Arial', 26, 'bold'), align="center")
    screen.update()
    
    # Color schemes for cubes
    color_schemes = [
        ["#FF6B6B", "#C0392B", "#FF9F9F", "#E74C3C", "#FF8A8A", "#B03A2E"],  # Red
        ["#4ECDC4", "#1ABC9C", "#7FDBB5", "#2ECC71", "#A8E6CF", "#16A085"],  # Teal
        ["#FFD93D", "#F39C12", "#FFEAA7", "#F1C40F", "#F7DC6F", "#D4AC0D"],  # Yellow
        ["#6C5CE7", "#8E44AD", "#A29BFE", "#9B59B6", "#C39BD3", "#7D3C98"],  # Purple
        ["#FF9FF3", "#E74C3C", "#F8C291", "#FD79A8", "#FDCB6E", "#E17055"],  # Pink
        ["#54A0FF", "#2980B9", "#85C1E9", "#3498DB", "#AED6F1", "#1A5276"],  # Blue
    ]
    
    # Draw large grid
    label_t.goto(0, 340)
    label_t.color("#FFD700")
    label_t.write("Large Grid (4x4)", font=('Arial', 16), align="center")
    screen.update()
    
    draw_cube_grid(4, 4, 100, 60, 200, color_schemes)
    
    # Draw medium grid
    label_t.goto(0, -200)
    label_t.color("#FFD700")
    label_t.write("Medium Grid (3x3)", font=('Arial', 16), align="center")
    screen.update()
    
    draw_cube_grid(3, 3, 80, 45, 150, color_schemes[3:6])
    
    # Draw small grid
    label_t.goto(300, -200)
    label_t.color("#FFD700")
    label_t.write("Small Grid (2x2)", font=('Arial', 16), align="center")
    screen.update()
    
    draw_cube_grid(2, 2, 60, 35, 120, color_schemes[0:3])
    
    # Add a single large cube
    label_t.goto(-300, -200)
    label_t.color("#FFD700")
    label_t.write("Detailed Cube", font=('Arial', 16), align="center")
    screen.update()
    
    draw_cube_3d(-300, -50, 80, 250, color_schemes[0])
    
    # Completion message
    label_t.goto(0, -350)
    label_t.color("#2ecc71")
    label_t.write("✓ Cube Grid Illusion Complete!", font=('Arial', 18, 'bold'), align="center")
    screen.update()

def draw_spinning_cubes():
    """Draw animated spinning cubes"""
    
    label_t.goto(0, 450)
    label_t.color("#FFD700")
    label_t.write("🌀 Spinning Cubes Animation 🌀", font=('Arial', 20, 'bold'), align="center")
    screen.update()
    
    # Position cubes in a circle
    num_cubes = 8
    radius = 280
    
    # Color scheme for spinning cubes
    colors = ["#FF6B6B", "#4ECDC4", "#FFD93D", "#6C5CE7", 
              "#FF9FF3", "#54A0FF", "#A8E6CF", "#FF8B94"]
    
    # Animate for 50 frames
    for frame in range(50):
        t.clear()
        
        angle_offset = frame * 3
        
        for i in range(num_cubes):
            angle = math.radians(i * 45 + angle_offset)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle) + 50
            
            # Cube size varies with position
            size = 30 + 15 * math.sin(math.radians(frame * 5 + i * 30))
            depth = 150 + 50 * math.sin(math.radians(frame * 3 + i * 20))
            
            # Rotate each cube
            rotation = frame * 2 + i * 45
            
            color_idx = i % len(colors)
            color = colors[color_idx]
            dark_color = darken_color(color, 0.6)
            
            cube_colors = [
                color, dark_color, lighten_color(color, 1.3),
                darken_color(color, 0.8), dark_color, darken_color(color, 0.4)
            ]
            
            draw_cube_3d(x, y, size, depth, cube_colors, rotation)
        
        # Update rotation status
        label_t.goto(0, 400)
        label_t.color("#87CEEB")
        label_t.write(f"Frame: {frame+1}/50", font=('Arial', 14), align="center")
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

def lighten_color(hex_color, factor):
    """Lighten a hex color by a factor"""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    r = min(255, int(r * factor))
    g = min(255, int(g * factor))
    b = min(255, int(b * factor))
    
    return f"#{r:02x}{g:02x}{b:02x}"

def draw_cube_illusion_explanation():
    """Draw an exploded view showing cube construction"""
    
    label_t.goto(350, 380)
    label_t.color("#3498db")
    label_t.write("🔍 Cube Construction", font=('Arial', 16, 'bold'), align="center")
    screen.update()
    
    # Draw a cube with face labels
    draw_cube_3d(350, 100, 60, 200, 
                ["#FF6B6B", "#4ECDC4", "#FFD93D", "#6C5CE7", "#FF9FF3", "#54A0FF"], 45)
    
    # Add labels for faces
    label_t.goto(350, 250)
    label_t.color("#FF6B6B")
    label_t.write("Front", font=('Arial', 10), align="center")
    
    label_t.goto(450, 150)
    label_t.color("#4ECDC4")
    label_t.write("Right", font=('Arial', 10), align="center")
    
    label_t.goto(350, -50)
    label_t.color("#6C5CE7")
    label_t.write("Bottom", font=('Arial', 10), align="center")
    
    label_t.goto(350, -100)
    label_t.color("#95a5a6")
    label_t.write("6 faces • 12 edges • 8 vertices", font=('Arial', 12), align="center")
    screen.update()

# Main execution
print("Drawing Cube Grid Illusion...")

# Draw the main illusion
draw_cube_grid_illusion()

# Draw spinning cubes animation
draw_spinning_cubes()

# Draw explanation
draw_cube_illusion_explanation()

# Add instructions
label_t.goto(0, -400)
label_t.color("#95a5a6")
label_t.write("🖱️ Click anywhere to exit", font=('Arial', 12), align="center")
screen.update()

# Keep window open
screen.mainloop()