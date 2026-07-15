import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Neon Tunnel Illusion")
screen.setup(width=800, height=800)
screen.tracer(0)

# Create turtle
tunnel = turtle.Turtle()
tunnel.speed(0)
tunnel.hideturtle()

# Neon color palette
neon_colors = [
    '#FF00FF',  # Neon Pink
    '#00FFFF',  # Cyan
    '#FF0066',  # Neon Red
    '#33FF33',  # Neon Green
    '#FF6600',  # Neon Orange
    '#9933FF',  # Purple
    '#FF3399',  # Hot Pink
    '#00FFCC',  # Aqua
]

def draw_neon_tunnel(radius, rings, segments, color_shift=False):
    """Draw a neon tunnel with perspective illusion"""
    
    for ring in range(rings):
        # Calculate size for perspective (smaller rings go deeper)
        scale = 1 - (ring / rings) * 0.85
        r = radius * scale
        
        # Calculate depth offset for 3D effect
        depth_offset = ring * 2
        
        # Select color
        if color_shift:
            color_index = int((ring / rings) * len(neon_colors))
            color = neon_colors[color_index % len(neon_colors)]
        else:
            color = neon_colors[ring % len(neon_colors)]
        
        # Draw ring with segments
        for seg in range(segments):
            angle1 = (seg / segments) * 360
            angle2 = ((seg + 1) / segments) * 360
            
            # Calculate positions with slight randomness for neon glow effect
            x1 = r * math.cos(math.radians(angle1))
            y1 = r * math.sin(math.radians(angle1))
            x2 = r * math.cos(math.radians(angle2))
            y2 = r * math.sin(math.radians(angle2))
            
            # Add small offset for organic feel
            offset = 2 * math.sin(ring * 0.5 + seg * 0.3)
            
            tunnel.penup()
            tunnel.goto(x1 + offset, y1 + offset)
            tunnel.pendown()
            
            # Set neon color with glow
            tunnel.color(color)
            tunnel.width(2 + ring * 0.1)
            
            # Draw segment with slight curve
            tunnel.goto(x2 - offset, y2 - offset)
            
            # Add glow effect with smaller dots
            if seg % 3 == 0:
                tunnel.penup()
                tunnel.goto((x1 + x2)/2, (y1 + y2)/2)
                tunnel.pendown()
                tunnel.color(color)
                tunnel.dot(3 + ring * 0.1)
                tunnel.penup()

def draw_perspective_tunnel(radius, depth, segments):
    """Draw a tunnel with strong perspective effect"""
    
    for i in range(depth):
        # Calculate perspective scale
        scale = 1 - (i / depth) * 0.9
        r = radius * scale
        
        # Calculate z-position for 3D effect
        z = i * 3
        
        # Color cycling
        color1 = neon_colors[i % len(neon_colors)]
        color2 = neon_colors[(i + 3) % len(neon_colors)]
        
        # Draw connecting lines for depth
        if i > 0:
            prev_scale = 1 - ((i - 1) / depth) * 0.9
            prev_r = radius * prev_scale
            
            for seg in range(segments):
                angle = (seg / segments) * 360
                
                # Current point
                x1 = r * math.cos(math.radians(angle))
                y1 = r * math.sin(math.radians(angle))
                
                # Previous point
                x2 = prev_r * math.cos(math.radians(angle))
                y2 = prev_r * math.sin(math.radians(angle))
                
                tunnel.penup()
                tunnel.goto(x1, y1)
                tunnel.pendown()
                tunnel.color(color1)
                tunnel.width(1)
                tunnel.goto(x2, y2)
        
        # Draw ring
        tunnel.penup()
        tunnel.goto(r, 0)
        tunnel.pendown()
        tunnel.color(color2)
        tunnel.width(2 + (depth - i) * 0.05)
        
        # Draw circle with segments for neon effect
        for seg in range(segments * 2):
            angle = (seg / (segments * 2)) * 360
            x = r * math.cos(math.radians(angle))
            y = r * math.sin(math.radians(angle))
            tunnel.goto(x, y)
            
            # Add glow dots
            if seg % 4 == 0:
                tunnel.penup()
                tunnel.goto(x, y)
                tunnel.pendown()
                tunnel.color(neon_colors[(seg + i) % len(neon_colors)])
                tunnel.dot(2)
                tunnel.penup()
                tunnel.goto(r, 0)
                tunnel.pendown()

def draw_spiral_tunnel(radius, turns, segments):
    """Draw a spiral tunnel illusion"""
    
    total_points = turns * segments
    
    for i in range(total_points):
        # Spiral parameters
        t = i / segments
        r = radius * (1 - t / turns * 0.8)
        angle = t * 360
        
        x = r * math.cos(math.radians(angle))
        y = r * math.sin(math.radians(angle))
        
        # Color based on position
        color_index = int((t / turns) * len(neon_colors))
        color = neon_colors[color_index % len(neon_colors)]
        
        # Draw spiral line
        tunnel.penup()
        tunnel.goto(x, y)
        tunnel.pendown()
        tunnel.color(color)
        tunnel.width(1.5 + (1 - t/turns) * 2)
        
        # Connect to previous point
        if i > 0:
            prev_t = (i - 1) / segments
            prev_r = radius * (1 - prev_t / turns * 0.8)
            prev_angle = prev_t * 360
            prev_x = prev_r * math.cos(math.radians(prev_angle))
            prev_y = prev_r * math.sin(math.radians(prev_angle))
            tunnel.goto(prev_x, prev_y)
        
        # Add neon glow dots
        if i % 3 == 0:
            tunnel.penup()
            tunnel.goto(x, y)
            tunnel.pendown()
            tunnel.color(color)
            tunnel.dot(3 + (1 - t/turns) * 3)
            tunnel.penup()

def draw_animated_tunnel():
    """Draw a complete neon tunnel with multiple effects"""
    
    # Draw outer glow rings
    for i in range(30, 0, -1):
        r = 350 * (i / 30)
        tunnel.penup()
        tunnel.goto(0, -r)
        tunnel.pendown()
        tunnel.color(f"#{int(100*(1-i/30)):02x}{int(50*(1-i/30)):02x}{int(200*(1-i/30)):02x}")
        tunnel.width(1)
        tunnel.circle(r)
    
    # Main tunnel with perspective
    draw_perspective_tunnel(300, 40, 24)
    
    # Overlay spiral for optical illusion
    draw_spiral_tunnel(280, 8, 60)
    
    # Add neon rings with color shift
    draw_neon_tunnel(250, 30, 36, True)
    
    # Draw center bright point
    tunnel.penup()
    tunnel.goto(0, 0)
    tunnel.pendown()
    
    # Glowing center
    for r in range(20, 0, -2):
        tunnel.penup()
        tunnel.goto(0, -r)
        tunnel.pendown()
        intensity = 255 * (1 - r/20)
        tunnel.color(f"#{int(intensity):02x}{int(intensity*0.5):02x}{int(intensity):02x}")
        tunnel.width(1)
        tunnel.circle(r)
    
    # Final neon burst
    for i in range(36):
        angle = i * 10
        tunnel.penup()
        tunnel.goto(0, 0)
        tunnel.setheading(angle)
        tunnel.forward(20)
        tunnel.pendown()
        tunnel.color(neon_colors[i % len(neon_colors)])
        tunnel.width(2)
        tunnel.forward(30)
        tunnel.penup()

def create_moving_illusion():
    """Create a tunnel with motion illusion using staggered rings"""
    
    # Draw staggered rings for motion effect
    for ring in range(50):
        r = 350 * (1 - ring / 50 * 0.9)
        offset = ring * 5 % 20 - 10  # Create wobble
        
        color = neon_colors[ring % len(neon_colors)]
        tunnel.color(color)
        tunnel.width(1 + ring * 0.02)
        
        tunnel.penup()
        tunnel.goto(offset, -r)
        tunnel.pendown()
        
        # Draw incomplete rings for motion illusion
        if ring % 2 == 0:
            tunnel.circle(r, 300)  # Partial circle
        else:
            tunnel.circle(r, 330)  # Different partial circle
        
        # Add connecting lines for depth
        if ring > 0 and ring % 3 == 0:
            prev_r = 350 * (1 - (ring - 1) / 50 * 0.9)
            for i in range(8):
                angle = i * 45 + ring * 3
                x1 = r * math.cos(math.radians(angle))
                y1 = r * math.sin(math.radians(angle))
                x2 = prev_r * math.cos(math.radians(angle))
                y2 = prev_r * math.sin(math.radians(angle))
                
                tunnel.penup()
                tunnel.goto(x1, y1)
                tunnel.pendown()
                tunnel.color(neon_colors[(ring + i) % len(neon_colors)])
                tunnel.width(1)
                tunnel.goto(x2, y2)

# Choose which tunnel to draw
print("Drawing neon tunnel illusion...")

# Main tunnel with multiple effects
draw_animated_tunnel()

# Uncomment to see the moving illusion version
# create_moving_illusion()

# Update screen
screen.update()

# Keep window open
turtle.done()