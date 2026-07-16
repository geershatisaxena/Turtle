import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("3D Staircase Illusion")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

def draw_3d_staircase():
    """Draw a 3D staircase illusion"""
    
    # Position
    t.penup()
    t.goto(-200, -100)
    t.pendown()
    
    # Number of steps
    steps = 12
    step_width = 40
    step_height = 30
    depth = 20  # 3D depth effect
    
    # Colors for 3D effect
    top_color = "#4A90D9"      # Blue
    front_color = "#2E6AA8"    # Darker blue
    side_color = "#1B4F7A"     # Darkest blue
    
    # Draw each step
    for i in range(steps):
        x = -200 + i * step_width
        y = -100 + i * step_height
        
        # --- Draw top face ---
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(top_color)
        t.begin_fill()
        for _ in range(4):
            t.forward(step_width)
            t.left(90)
        t.end_fill()
        
        # --- Draw front face (3D illusion) ---
        t.penup()
        t.goto(x, y - depth)
        t.pendown()
        t.fillcolor(front_color)
        t.begin_fill()
        t.goto(x, y)
        t.goto(x + step_width, y)
        t.goto(x + step_width, y - depth)
        t.goto(x, y - depth)
        t.end_fill()
        
        # --- Draw right side face (3D illusion) ---
        t.penup()
        t.goto(x + step_width, y - depth)
        t.pendown()
        t.fillcolor(side_color)
        t.begin_fill()
        t.goto(x + step_width, y)
        t.goto(x + step_width + depth, y + depth)
        t.goto(x + step_width + depth, y)
        t.goto(x + step_width, y - depth)
        t.end_fill()
        
        # --- Draw top of the side (3D illusion) ---
        t.penup()
        t.goto(x + step_width, y)
        t.pendown()
        t.fillcolor(top_color)
        t.begin_fill()
        t.goto(x + step_width + depth, y + depth)
        t.goto(x + step_width + depth + step_width, y + depth)
        t.goto(x + step_width + step_width, y)
        t.end_fill()

def draw_3d_staircase_advanced():
    """Draw an enhanced 3D staircase with better perspective"""
    
    t.penup()
    t.goto(-250, -150)
    t.pendown()
    
    steps = 15
    step_width = 45
    step_height = 25
    depth = 30
    
    # Colors
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7", 
              "#DDA0DD", "#98D8C8", "#F7DC6F", "#BB8FCE", "#85C1E9"]
    
    for i in range(steps):
        x = -250 + i * step_width
        y = -150 + i * step_height
        
        color_index = i % len(colors)
        base_color = colors[color_index]
        
        # Darken for 3D effect
        front_color = darken_color(base_color, 0.7)
        side_color = darken_color(base_color, 0.5)
        
        # Draw top
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(base_color)
        t.begin_fill()
        t.goto(x + step_width, y)
        t.goto(x + step_width + depth, y + depth)
        t.goto(x + depth, y + depth)
        t.goto(x, y)
        t.end_fill()
        
        # Draw front
        t.penup()
        t.goto(x, y - depth)
        t.pendown()
        t.fillcolor(front_color)
        t.begin_fill()
        t.goto(x, y)
        t.goto(x + step_width, y)
        t.goto(x + step_width, y - depth)
        t.goto(x, y - depth)
        t.end_fill()
        
        # Draw side
        t.penup()
        t.goto(x + step_width, y - depth)
        t.pendown()
        t.fillcolor(side_color)
        t.begin_fill()
        t.goto(x + step_width, y)
        t.goto(x + step_width + depth, y + depth)
        t.goto(x + step_width + depth, y)
        t.goto(x + step_width, y - depth)
        t.end_fill()

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

def draw_spiral_staircase():
    """Draw a spiral 3D staircase illusion"""
    
    t.penup()
    t.goto(0, -200)
    t.pendown()
    
    steps = 20
    radius = 150
    angle_step = 15
    height_step = 15
    
    for i in range(steps):
        angle = math.radians(i * angle_step)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle) - 100 + i * height_step / 2
        
        # Calculate next position for step
        next_angle = math.radians((i + 1) * angle_step)
        next_x = radius * math.cos(next_angle)
        next_y = radius * math.sin(next_angle) - 100 + (i + 1) * height_step / 2
        
        # Draw step
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        # Color based on height
        r = int(100 + 155 * (i / steps))
        g = int(100 + 100 * (i / steps))
        b = int(255 - 155 * (i / steps))
        color = f"#{r:02x}{g:02x}{b:02x}"
        
        t.fillcolor(color)
        t.begin_fill()
        
        # Draw a 3D step
        t.goto(next_x, next_y)
        t.goto(next_x, next_y - 20)
        t.goto(x, y - 20)
        t.goto(x, y)
        
        t.end_fill()

# Main drawing
print("Drawing 3D Staircase Illusion...")

# Draw the main staircase
draw_3d_staircase()

# Move to draw another variation
t.penup()
t.goto(200, 100)
t.pendown()

# Draw advanced staircase with colors
draw_3d_staircase_advanced()

# Draw spiral staircase on the side
t.penup()
t.goto(300, -200)
t.pendown()
draw_spiral_staircase()

# Add some text
t.penup()
t.goto(-100, 250)
t.pendown()
t.color("black")
style = ('Arial', 20, 'bold')
t.write("3D Staircase Illusion", font=style, align="center")

# Keep window open
screen.mainloop()