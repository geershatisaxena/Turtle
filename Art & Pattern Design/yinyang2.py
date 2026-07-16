import turtle
import math
import random

# Setup
screen = turtle.Screen()
screen.bgcolor("#0a0a1a")
screen.title("Yin-Yang - Animated & Glowing")
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

# Glow effect turtle
glow_t = turtle.Turtle()
glow_t.speed(0)
glow_t.hideturtle()

def draw_glowing_yin_yang(x, y, radius, color1, color2, glow_color, glow_size=20):
    """Draw a yin-yang with glowing effect"""
    
    # Draw glow effect (outer halo)
    for i in range(10, 0, -1):
        glow_t.penup()
        glow_t.goto(x, y - (radius + glow_size * i/10))
        glow_t.pendown()
        alpha = i / 10
        glow_t.color(glow_color, glow_color)
        glow_t.pensize(1)
        glow_t.begin_fill()
        glow_t.circle(radius + glow_size * i/10)
        glow_t.end_fill()
        screen.update()
    
    # Draw the main yin-yang
    draw_yin_yang_advanced(x, y, radius, color1, color2)
    
    # Add sparkle effects
    for _ in range(15):
        angle = random.uniform(0, 2 * math.pi)
        dist = random.uniform(radius * 0.3, radius * 1.3)
        sx = x + dist * math.cos(angle)
        sy = y + dist * math.sin(angle)
        
        glow_t.penup()
        glow_t.goto(sx, sy)
        glow_t.pendown()
        glow_t.color(glow_color)
        glow_t.dot(random.randint(2, 5))
        screen.update()

def draw_yin_yang_advanced(x, y, radius, color1, color2):
    """Draw a yin-yang with advanced styling"""
    
    # Outer circle with gradient border
    t.penup()
    t.goto(x, y - radius - 5)
    t.pendown()
    t.color("#FFD700", color1)
    t.pensize(3)
    t.begin_fill()
    t.circle(radius + 5)
    t.end_fill()
    t.pensize(1)
    
    # Main circle
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color1, color1)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
    # Second half
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color2, color2)
    t.begin_fill()
    t.setheading(90)
    t.circle(radius, 180)
    t.end_fill()
    
    # S-curve with glow
    t.penup()
    t.goto(x, y + radius)
    t.pendown()
    t.color("#FFD700")
    t.pensize(2)
    t.setheading(270)
    
    # Draw smooth S-curve
    points = 100
    for i in range(points + 1):
        angle = (i / points) * 180
        rad = math.radians(angle)
        cx = x + radius * math.sin(rad) * math.cos(rad)
        cy = y - radius * math.cos(rad)
        t.goto(cx, cy)
    
    # Small circles
    small_radius = radius / 2
    tiny_radius = radius / 6
    
    # Top eye
    draw_eye(x, y + small_radius, small_radius, color2, color1, tiny_radius)
    
    # Bottom eye
    draw_eye(x, y - small_radius, small_radius, color1, color2, tiny_radius)
    
    t.pensize(1)

def draw_eye(x, y, outer_radius, outer_color, inner_color, inner_radius):
    """Draw an eye with detail"""
    # Outer circle
    t.penup()
    t.goto(x, y - outer_radius)
    t.pendown()
    t.color(outer_color, outer_color)
    t.begin_fill()
    t.circle(outer_radius)
    t.end_fill()
    
    # Inner circle
    t.penup()
    t.goto(x, y - inner_radius)
    t.pendown()
    t.color(inner_color, inner_color)
    t.begin_fill()
    t.circle(inner_radius)
    t.end_fill()
    
    # Highlight
    highlight_radius = inner_radius * 0.3
    t.penup()
    t.goto(x + highlight_radius, y + highlight_radius)
    t.pendown()
    t.color("white", "white")
    t.begin_fill()
    t.circle(highlight_radius * 0.5)
    t.end_fill()

def draw_animated_yin_yang():
    """Draw a rotating, animated yin-yang"""
    
    # Title
    label_t.goto(0, 370)
    label_t.color("#FFD700")
    label_t.write("✨ ANIMATED YIN-YANG ✨", font=('Arial', 26, 'bold'), align="center")
    screen.update()
    
    # Parameters
    x, y = 0, 80
    radius = 200
    colors = [
        ("#FF6B6B", "#4ECDC4"),  # Fire & Ice
        ("#FFD93D", "#6C5CE7"),  # Sun & Moon
        ("#A8E6CF", "#FF8B94"),  # Spring & Autumn
        ("#FF9FF3", "#54A0FF"),  # Love & Peace
    ]
    
    # Draw animated frames
    for frame in range(36):  # 36 frames for rotation
        # Clear previous frame
        if frame > 0:
            # Don't clear, overlay with slight transparency effect
            pass
        
        angle = frame * 10  # Rotation angle
        color_pair = colors[frame % len(colors)]
        
        # Draw with rotation
        t.clear()
        
        # Draw with current rotation
        draw_rotated_yin_yang(x, y, radius, color_pair[0], color_pair[1], angle)
        
        # Update status
        label_t.goto(0, 330)
        label_t.color("#87CEEB")
        label_t.write(f"Rotation: {angle}°", font=('Arial', 14), align="center")
        screen.update()
        time.sleep(0.05)
    
    # Final drawing
    draw_glowing_yin_yang(x, y, radius, "#FF6B6B", "#4ECDC4", "#FF6B6B")

def draw_rotated_yin_yang(x, y, radius, color1, color2, angle):
    """Draw a rotated yin-yang"""
    
    # Rotate the entire drawing
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    
    # Outer circle
    t.penup()
    t.goto(x + radius * math.cos(math.radians(angle)), 
            y + radius * math.sin(math.radians(angle)))
    t.pendown()
    t.color(color1, color1)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    
    # Second half
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color2, color2)
    t.begin_fill()
    t.setheading(90 + angle)
    t.circle(radius, 180)
    t.end_fill()
    
    # S-curve
    t.penup()
    t.goto(x, y + radius)
    t.pendown()
    t.color("white")
    t.pensize(2)
    t.setheading(270 + angle)
    
    for i in range(101):
        a = (i / 100) * 180
        rad = math.radians(a)
        cx = x + radius * math.sin(rad) * math.cos(rad)
        cy = y - radius * math.cos(rad)
        # Apply rotation
        rx = x + (cx - x) * math.cos(math.radians(angle)) - (cy - y) * math.sin(math.radians(angle))
        ry = y + (cx - x) * math.sin(math.radians(angle)) + (cy - y) * math.cos(math.radians(angle))
        t.goto(rx, ry)
    
    # Eyes
    small_r = radius / 2
    tiny_r = radius / 6
    
    # Top eye
    ex = x + small_r * math.cos(math.radians(angle))
    ey = y + small_r * math.sin(math.radians(angle))
    draw_eye(ex, ey, small_r, color2, color1, tiny_r)
    
    # Bottom eye
    ex = x - small_r * math.cos(math.radians(angle))
    ey = y - small_r * math.sin(math.radians(angle))
    draw_eye(ex, ey, small_r, color1, color2, tiny_r)

def draw_yin_yang_mandala():
    """Draw a yin-yang mandala with concentric rings"""
    
    label_t.goto(0, -100)
    label_t.color("#FFD700")
    label_t.write("🌸 Yin-Yang Mandala 🌸", font=('Arial', 20, 'bold'), align="center")
    screen.update()
    
    center_x, center_y = 0, -250
    radius = 180
    
    # Draw 8 yin-yangs in a circle
    for i in range(8):
        angle = i * 45
        rad = math.radians(angle)
        x = center_x + 220 * math.cos(rad)
        y = center_y + 220 * math.sin(rad)
        
        # Alternate colors
        if i % 2 == 0:
            colors = ("#FF6B6B", "#4ECDC4")
        else:
            colors = ("#FFD93D", "#6C5CE7")
        
        draw_yin_yang_advanced(x, y, 35, colors[0], colors[1])
        screen.update()
        time.sleep(0.1)
    
    # Draw center yin-yang
    draw_glowing_yin_yang(center_x, center_y, 80, "#FFD700", "#6C5CE7", "#FFD700", 15)
    
    # Connect them with decorative lines
    t.penup()
    t.goto(center_x, center_y - 180)
    t.pendown()
    t.color("#FFD700")
    t.pensize(1)
    t.circle(180)
    
    # Draw spokes
    for i in range(8):
        angle = i * 45
        rad = math.radians(angle)
        t.penup()
        t.goto(center_x, center_y)
        t.pendown()
        t.goto(center_x + 180 * math.cos(rad), center_y + 180 * math.sin(rad))
    
    t.pensize(1)

def draw_pattern_yin_yang():
    """Draw a pattern of yin-yangs"""
    
    label_t.goto(0, 400)
    label_t.color("#FF6B6B")
    label_t.write("🌀 Yin-Yang Pattern 🌀", font=('Arial', 22, 'bold'), align="center")
    screen.update()
    
    # Draw a grid of yin-yangs
    rows, cols = 3, 3
    spacing = 150
    start_x = - (cols - 1) * spacing / 2
    start_y = 250
    
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * spacing
            y = start_y - row * spacing
            
            # Different colors for each position
            hue1 = (row * 3 + col) / (rows * cols)
            hue2 = 1 - hue1
            color1 = f"hsv({hue1 * 360}, 1, 0.9)"
            color2 = f"hsv({hue2 * 360}, 1, 0.9)"
            
            # Draw small yin-yang
            draw_yin_yang_advanced(x, y, 50, color1, color2)
            screen.update()
            time.sleep(0.05)
    
    # Draw connecting lines
    t.penup()
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * spacing
            y = start_y - row * spacing
            t.goto(x, y)
            t.pendown()
            t.color("#FFD700")
            t.pensize(1)
            t.dot(5)
            t.penup()

# Main execution
print("Drawing Animated Yin-Yang...")

# Draw the animated version
draw_animated_yin_yang()

# Draw mandala
draw_yin_yang_mandala()

# Draw pattern
draw_pattern_yin_yang()

# Add instructions
label_t.goto(0, -400)
label_t.color("#95a5a6")
label_t.write("🖱️ Click anywhere to exit", font=('Arial', 12), align="center")
screen.update()

# Keep window open
screen.mainloop()