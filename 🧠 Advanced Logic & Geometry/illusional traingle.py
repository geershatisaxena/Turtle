import turtle
import math
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Rotating Triangle Optical Illusion")
screen.bgcolor("black")
screen.setup(width=900, height=900)
screen.tracer(0)

# Create turtles
main_turtle = turtle.Turtle()
main_turtle.speed(0)
main_turtle.penup()
main_turtle.hideturtle()

# Create multiple triangles for layered effect
triangles = []
for _ in range(3):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()
    triangles.append(t)

# Color schemes
color_schemes = [
    ["#FF0066", "#FF3366", "#FF6633", "#FF9933", "#FFCC00"],  # Warm
    ["#00FFCC", "#00FF99", "#00FF66", "#00FF33", "#00FF00"],  # Neon green
    ["#9900FF", "#AA33FF", "#BB66FF", "#CC99FF", "#DDCCFF"],  # Purple
    ["#FF0000", "#FF4500", "#FF8C00", "#FFD700", "#FFFF00"],  # Fire
    ["#00BFFF", "#1E90FF", "#4169E1", "#0000CD", "#00008B"],  # Blue
    ["white", "lightgray", "gray", "silver", "#CCCCCC"],  # Mono
]

current_scheme = 0
rotation_angle = 0
illusion_active = True
trail_mode = False
trail_positions = []

def draw_triangle(x, y, size, rotation, color, thickness=2):
    """Draw an equilateral triangle at given position with rotation"""
    main_turtle.penup()
    main_turtle.goto(x, y)
    main_turtle.setheading(rotation)
    main_turtle.color(color)
    main_turtle.pensize(thickness)
    main_turtle.pendown()
    
    # Draw equilateral triangle (60 degree internal angles)
    for _ in range(3):
        main_turtle.forward(size)
        main_turtle.left(120)
    
    main_turtle.penup()

def draw_filled_triangle(x, y, size, rotation, color, opacity=1.0):
    """Draw a filled triangle with optional opacity effect"""
    main_turtle.penup()
    main_turtle.goto(x, y)
    main_turtle.setheading(rotation)
    main_turtle.color(color)
    main_turtle.begin_fill()
    main_turtle.fillcolor(color)
    main_turtle.pendown()
    
    for _ in range(3):
        main_turtle.forward(size)
        main_turtle.left(120)
    
    main_turtle.end_fill()
    main_turtle.penup()

def draw_triangle_frame(x, y, size, rotation, color, frame_count=3):
    """Draw concentric triangle frames (nested triangles)"""
    for i in range(frame_count, 0, -1):
        scale = i / frame_count
        new_size = size * scale
        new_color = color
        draw_filled_triangle(x, y, new_size, rotation, new_color)

def draw_optical_illusion_triangle():
    """Draw the main rotating triangle optical illusion"""
    global rotation_angle
    
    # Clear previous drawing
    main_turtle.clear()
    
    colors = color_schemes[current_scheme]
    center_x, center_y = 0, 0
    base_size = 300
    
    # Draw outer ring of triangles (the illusion effect)
    for i in range(3):
        angle_offset = i * 120
        triangle_rot = rotation_angle + angle_offset
        distance = 180
        x = center_x + distance * math.cos(math.radians(triangle_rot))
        y = center_y + distance * math.sin(math.radians(triangle_rot))
        
        # Draw spinning triangles around the center
        draw_filled_triangle(x, y, 60, triangle_rot * 2, colors[i % len(colors)])
        
        # Add highlight dots at vertices
        for v_angle in [0, 120, 240]:
            v_x = x + 30 * math.cos(math.radians(triangle_rot * 2 + v_angle))
            v_y = y + 30 * math.sin(math.radians(triangle_rot * 2 + v_angle))
            main_turtle.penup()
            main_turtle.goto(v_x, v_y)
            main_turtle.dot(6, "white")
    
    # Draw central rotating triangle (the focal point)
    central_rot = -rotation_angle * 2
    draw_triangle_frame(center_x, center_y, base_size, central_rot, colors[4], 5)
    
    # Draw inner inverted triangle (creates the illusion of depth)
    inner_size = base_size * 0.5
    draw_filled_triangle(center_x, center_y, inner_size, central_rot + 60, colors[2])
    
    # Draw small center element
    main_turtle.penup()
    main_turtle.goto(center_x, center_y)
    main_turtle.dot(15, colors[0])
    
    screen.update()

def draw_penrose_triangle():
    """Draw a Penrose triangle illusion (impossible triangle)"""
    global rotation_angle
    
    main_turtle.clear()
    colors = color_schemes[current_scheme]
    
    size = 250
    center_x, center_y = 0, 0
    
    # Draw three bars of the Penrose triangle
    angles = [0, 120, 240]
    bar_length = size
    bar_width = 30
    
    for i, angle in enumerate(angles):
        rot = angle + rotation_angle
        x = center_x + (bar_length / 2) * math.cos(math.radians(rot))
        y = center_y + (bar_length / 2) * math.sin(math.radians(rot))
        
        main_turtle.penup()
        main_turtle.goto(x, y)
        main_turtle.setheading(rot)
        main_turtle.pendown()
        main_turtle.color(colors[i % len(colors)])
        main_turtle.begin_fill()
        main_turtle.fillcolor(colors[i % len(colors)])
        
        # Draw bar
        for _ in range(2):
            main_turtle.forward(bar_length / 2)
            main_turtle.left(90)
            main_turtle.forward(bar_width)
            main_turtle.left(90)
        
        main_turtle.end_fill()
        main_turtle.penup()
    
    # Draw connecting corners
    for i in range(3):
        angle = angles[i] + rotation_angle + 60
        x = center_x + (bar_length / 2) * math.cos(math.radians(angle))
        y = center_y + (bar_length / 2) * math.sin(math.radians(angle))
        main_turtle.penup()
        main_turtle.goto(x, y)
        main_turtle.dot(bar_width, colors[(i + 1) % len(colors)])
    
    screen.update()

def draw_spinning_triangle_ring():
    """Draw a ring of spinning triangles (kaleidoscope effect)"""
    global rotation_angle
    
    main_turtle.clear()
    colors = color_schemes[current_scheme]
    
    num_triangles = 12
    radius = 280
    
    for i in range(num_triangles):
        angle = (360 / num_triangles) * i + rotation_angle
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        
        triangle_rot = angle + 90
        size = 40 + 10 * math.sin(math.radians(rotation_angle * 3 + i * 30))
        
        draw_filled_triangle(x, y, size, triangle_rot, colors[i % len(colors)])
        
        # Add trailing effect
        main_turtle.penup()
        main_turtle.goto(x, y)
        main_turtle.dot(8, colors[(i + 1) % len(colors)])
    
    # Draw center triangle
    draw_triangle_frame(0, 0, 120, -rotation_angle, colors[4], 4)
    
    screen.update()

def draw_moire_triangle():
    """Draw moiré pattern with overlapping triangles"""
    global rotation_angle
    
    main_turtle.clear()
    colors = color_schemes[current_scheme]
    
    layers = 8
    base_size = 350
    
    for i in range(layers):
        scale = 1 - (i / layers) * 0.7
        size = base_size * scale
        rot = rotation_angle * (i + 1) / 2
        opacity = 1 - (i / layers) * 0.3
        
        draw_filled_triangle(0, 0, size, rot, colors[i % len(colors)])
    
    # Add radiating lines for extra illusion
    for i in range(60):
        angle = i * 6 + rotation_angle * 2
        x = 320 * math.cos(math.radians(angle))
        y = 320 * math.sin(math.radians(angle))
        main_turtle.penup()
        main_turtle.goto(0, 0)
        main_turtle.pendown()
        main_turtle.color(colors[i % len(colors)])
        main_turtle.goto(x, y)
        main_turtle.penup()
    
    screen.update()

def draw_rotating_triangle_illusion():
    """The main illusion: rotating triangles that seem to shift direction"""
    global rotation_angle
    
    main_turtle.clear()
    colors = color_schemes[current_scheme]
    
    # Outer triangle (static)
    draw_triangle(0, -180, 360, 0, colors[4], 3)
    
    # Middle rotating triangle
    middle_size = 300
    middle_rot = rotation_angle * 1.5
    draw_triangle(0, -150, middle_size, middle_rot, colors[2], 4)
    
    # Inner rotating triangle (opposite direction)
    inner_size = 240
    inner_rot = -rotation_angle
    draw_triangle(0, -120, inner_size, inner_rot, colors[1], 4)
    
    # Core triangle
    core_size = 180
    core_rot = rotation_angle * 0.5
    draw_filled_triangle(0, -90, core_size, core_rot, colors[0])
    
    # Add spinning corner elements
    for corner in [0, 120, 240]:
        angle = corner + rotation_angle * 2
        x = 200 * math.cos(math.radians(angle))
        y = 200 * math.sin(math.radians(angle))
        draw_filled_triangle(x, y, 40, angle, colors[3])
    
    screen.update()

def add_trail():
    """Add motion trail effect"""
    global trail_positions
    
    if trail_mode:
        trail_positions.append((rotation_angle, time.time()))
        if len(trail_positions) > 20:
            trail_positions.pop(0)
        
        for i, (angle, timestamp) in enumerate(trail_positions):
            alpha = i / len(trail_positions)
            trail_turtle = turtle.Turtle()
            trail_turtle.speed(0)
            trail_turtle.penup()
            trail_turtle.hideturtle()
            # Would draw faded triangles here

# UI Controls
def draw_info():
    info = turtle.Turtle()
    info.speed(0)
    info.color("white")
    info.penup()
    info.hideturtle()
    info.goto(0, 430)
    info.write("🌀 ROTATING TRIANGLE OPTICAL ILLUSION 🌀", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -440)
    instructions.write("1=Classic 2=Penrose 3=Ring 4=Moire 5=Rotating | C=Color | S=Speed +/- | R=Reset | ESC=Exit",
                       align="center", font=("Arial", 9, "normal"))

current_illusion = 1
rotation_speed = 2
rotation_angle = 0

def animate():
    """Main animation loop"""
    global rotation_angle
    
    while True:
        rotation_angle = (rotation_angle + rotation_speed) % 360
        
        if current_illusion == 1:
            draw_optical_illusion_triangle()
        elif current_illusion == 2:
            draw_penrose_triangle()
        elif current_illusion == 3:
            draw_spinning_triangle_ring()
        elif current_illusion == 4:
            draw_moire_triangle()
        elif current_illusion == 5:
            draw_rotating_triangle_illusion()
        
        screen.update()
        time.sleep(0.02)

def set_illusion_1(): global current_illusion; current_illusion = 1
def set_illusion_2(): global current_illusion; current_illusion = 2
def set_illusion_3(): global current_illusion; current_illusion = 3
def set_illusion_4(): global current_illusion; current_illusion = 4
def set_illusion_5(): global current_illusion; current_illusion = 5

def change_color():
    global current_scheme
    current_scheme = (current_scheme + 1) % len(color_schemes)

def increase_speed():
    global rotation_speed
    rotation_speed = min(rotation_speed + 1, 10)

def decrease_speed():
    global rotation_speed
    rotation_speed = max(rotation_speed - 1, 1)

def reset_angle():
    global rotation_angle
    rotation_angle = 0

# Keyboard bindings
screen.listen()
screen.onkey(set_illusion_1, "1")
screen.onkey(set_illusion_2, "2")
screen.onkey(set_illusion_3, "3")
screen.onkey(set_illusion_4, "4")
screen.onkey(set_illusion_5, "5")
screen.onkey(change_color, "c")
screen.onkey(increase_speed, "plus")
screen.onkey(increase_speed, "equal")
screen.onkey(decrease_speed, "minus")
screen.onkey(reset_angle, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_info()

print("=" * 60)
print("     ROTATING TRIANGLE OPTICAL ILLUSION")
print("=" * 60)
print()
print("Mesmerizing triangle-based optical illusions!")
print()
print("ILLUSIONS:")
print("  1 - Classic Illusion: Rotating outer triangles with inverse inner")
print("  2 - Penrose Triangle: Impossible triangle illusion")
print("  3 - Spinning Ring: Kaleidoscope of rotating triangles")
print("  4 - Moiré Pattern: Overlapping triangles create wave effects")
print("  5 - Rotating Triangles: Multiple nested triangles rotating")
print()
print("CONTROLS:")
print("  1-5   - Select illusion type")
print("  C     - Change color scheme")
print("  +/-   - Adjust rotation speed")
print("  R     - Reset rotation angle")
print("  ESC   - Exit")
print()
print("Watch closely - your brain will perceive impossible motion!")
print("The Penrose triangle is a classic impossible object!")

# Start animation
try:
    animate()
except KeyboardInterrupt:
    screen.bye()
except turtle.Terminator:
    pass

screen.mainloop()