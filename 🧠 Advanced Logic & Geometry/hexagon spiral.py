import turtle
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Rotating Hexagon Spiral")
screen.bgcolor("black")
screen.setup(width=1000, height=900)
screen.tracer(0)

# Create the drawing turtle
spiral = turtle.Turtle()
spiral.speed(0)
spiral.penup()
spiral.hideturtle()

# Color palette
colors = [
    "#FF0066", "#FF3366", "#FF6633", "#FF9933", "#FFCC00", "#FFFF00",
    "#99FF33", "#33FF66", "#00FFCC", "#33CCFF", "#6699FF", "#9966FF",
    "#CC33FF", "#FF33CC", "#FF66CC"
]

# Spiral parameters
hexagon_size = 10      # Starting size of hexagon
growth_factor = 1.05   # How much each hexagon grows
rotation_angle = 8     # How much each hexagon rotates (in degrees)
num_hexagons = 120     # Number of hexagons to draw
color_cycle = 0

def draw_hexagon(x, y, size, rotation, color):
    """Draw a single hexagon at given position with rotation"""
    spiral.penup()
    spiral.goto(x, y)
    spiral.setheading(rotation)
    spiral.color(color)
    spiral.pendown()
    spiral.begin_fill()
    spiral.fillcolor(color)
    
    # Draw hexagon (6 sides)
    for _ in range(6):
        spiral.forward(size)
        spiral.left(60)
    
    spiral.end_fill()
    spiral.penup()

def draw_rotating_hexagon_spiral():
    """Main function to draw the rotating hexagon spiral"""
    global color_cycle
    
    x, y = 0, 0
    angle = 0
    size = hexagon_size
    rot = 0
    
    for i in range(num_hexagons):
        # Select color (cycle through palette)
        color = colors[color_cycle % len(colors)]
        
        # Draw hexagon at current position with current rotation
        draw_hexagon(x, y, size, rot, color)
        
        # Update position for next hexagon (spiral outward)
        angle += rotation_angle * 0.5
        radius = size * 1.5
        x += math.cos(math.radians(angle)) * radius
        y += math.sin(math.radians(angle)) * radius
        
        # Update size and rotation for next hexagon
        size *= growth_factor
        rot += rotation_angle
        color_cycle += 1
        
        # Update screen periodically
        if i % 10 == 0:
            screen.update()

def draw_flower_spiral():
    """Alternative: Create a flower-like spiral with hexagons"""
    global color_cycle
    
    x, y = 0, 0
    angle = 0
    size = hexagon_size
    rot = 0
    
    for i in range(num_hexagons):
        # Color based on position
        color = colors[i % len(colors)]
        
        draw_hexagon(x, y, size, rot, color)
        
        # Spiral pattern with alternating directions
        if i % 2 == 0:
            angle += rotation_angle
        else:
            angle -= rotation_angle * 0.7
        
        radius = size * 1.3
        x += math.cos(math.radians(angle)) * radius
        y += math.sin(math.radians(angle)) * radius
        
        size *= growth_factor
        rot += rotation_angle
        color_cycle += 1
        
        if i % 10 == 0:
            screen.update()

def draw_fibonacci_spiral():
    """Draw hexagons in a Fibonacci spiral pattern"""
    global color_cycle
    
    x, y = 0, 0
    angle = 0
    size = hexagon_size
    rot = 0
    a, b = 0, 1  # Fibonacci sequence
    
    for i in range(num_hexagons):
        color = colors[color_cycle % len(colors)]
        draw_hexagon(x, y, size, rot, color)
        
        # Fibonacci spiral (golden ratio)
        angle += 137.5  # Golden angle
        radius = size * 2
        x += math.cos(math.radians(angle)) * radius
        y += math.sin(math.radians(angle)) * radius
        
        size *= 1.03
        rot += rotation_angle * 0.8
        color_cycle += 1
        
        if i % 10 == 0:
            screen.update()

def draw_concentric_hexagons():
    """Draw concentric hexagons that rotate"""
    global color_cycle
    
    for i in range(30):
        size = 15 + i * 6
        rot = i * 12
        color = colors[i % len(colors)]
        draw_hexagon(0, 0, size, rot, color)
        screen.update()

def draw_multi_arm_spiral():
    """Draw a spiral with multiple arms"""
    global color_cycle
    
    num_arms = 6
    arms = []
    
    # Initialize arm positions
    for arm in range(num_arms):
        arms.append({
            'x': 0,
            'y': 0,
            'angle': arm * 60,
            'size': hexagon_size,
            'rot': arm * 10
        })
    
    for step in range(num_hexagons // num_arms):
        for arm_idx, arm in enumerate(arms):
            color = colors[(color_cycle + arm_idx) % len(colors)]
            draw_hexagon(arm['x'], arm['y'], arm['size'], arm['rot'], color)
            
            # Update arm position
            arm['angle'] += rotation_angle * 0.8
            radius = arm['size'] * 1.2
            arm['x'] += math.cos(math.radians(arm['angle'])) * radius
            arm['y'] += math.sin(math.radians(arm['angle'])) * radius
            arm['size'] *= growth_factor
            arm['rot'] += rotation_angle
        
        color_cycle += 1
        if step % 5 == 0:
            screen.update()

def draw_continuous_animation():
    """Animated version - continuous rotation"""
    x, y = 0, 0
    angle = 0
    size = hexagon_size
    rot = 0
    
    while True:
        spiral.clear()
        x, y = 0, 0
        angle = 0
        size = hexagon_size
        rot = 0
        color_cycle_local = 0
        
        for i in range(80):
            color = colors[color_cycle_local % len(colors)]
            draw_hexagon(x, y, size, rot, color)
            
            angle += rotation_angle * 0.6
            radius = size * 1.4
            x += math.cos(math.radians(angle)) * radius
            y += math.sin(math.radians(angle)) * radius
            
            size *= 1.04
            rot += rotation_angle * 0.9
            color_cycle_local += 1
        
        screen.update()
        rotation_angle_local = rotation_angle
        # This would need to be modified for true animation
        break

# UI elements
def draw_title():
    """Draw title and instructions"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 420)
    title.write("ROTATING HEXAGON SPIRAL", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -430)
    instructions.write("Press: 1=Basic Spiral  2=Flower Spiral  3=Fibonacci  4=Concentric  5=Multi-Arm | R=Reset | ESC=Exit",
                       align="center", font=("Arial", 10, "normal"))

def reset_drawing():
    """Clear and redraw current pattern"""
    spiral.clear()
    screen.update()
    draw_current_pattern()

# Current pattern selection
current_pattern = 1

def draw_current_pattern():
    """Draw the currently selected pattern"""
    global color_cycle
    color_cycle = 0
    spiral.clear()
    
    if current_pattern == 1:
        draw_rotating_hexagon_spiral()
    elif current_pattern == 2:
        draw_flower_spiral()
    elif current_pattern == 3:
        draw_fibonacci_spiral()
    elif current_pattern == 4:
        draw_concentric_hexagons()
    elif current_pattern == 5:
        draw_multi_arm_spiral()
    
    screen.update()

def set_pattern_1():
    global current_pattern
    current_pattern = 1
    reset_drawing()

def set_pattern_2():
    global current_pattern
    current_pattern = 2
    reset_drawing()

def set_pattern_3():
    global current_pattern
    current_pattern = 3
    reset_drawing()

def set_pattern_4():
    global current_pattern
    current_pattern = 4
    reset_drawing()

def set_pattern_5():
    global current_pattern
    current_pattern = 5
    reset_drawing()

# Keyboard bindings
screen.listen()
screen.onkey(set_pattern_1, "1")
screen.onkey(set_pattern_2, "2")
screen.onkey(set_pattern_3, "3")
screen.onkey(set_pattern_4, "4")
screen.onkey(set_pattern_5, "5")
screen.onkey(reset_drawing, "r")
screen.onkey(lambda: screen.bye(), "Escape")

# Draw UI
draw_title()

print("=" * 60)
print("        ROTATING HEXAGON SPIRAL")
print("=" * 60)
print()
print("A mesmerizing geometric pattern where each hexagon")
print("grows, rotates, and spirals outward!")
print()
print("PATTERNS:")
print("  1 - Basic Spiral: Classic outward spiraling hexagons")
print("  2 - Flower Spiral: Alternating direction, flower-like pattern")
print("  3 - Fibonacci: Golden angle spiral (nature-inspired)")
print("  4 - Concentric: Rotating rings of hexagons")
print("  5 - Multi-Arm: Six-arm spiral symmetry")
print()
print("FEATURES:")
print("  • Each hexagon is slightly larger than the previous")
print("  • Each hexagon rotates by a fixed angle")
print("  • Smooth color transitions")
print("  • Multiple spiral patterns to explore")
print()
print("CONTROLS:")
print("  1-5 - Switch between spiral patterns")
print("  R   - Redraw current pattern")
print("  ESC - Exit program")
print()
print("Watch the pattern evolve as hexagons grow and rotate!")

# Draw the initial pattern
draw_rotating_hexagon_spiral()
screen.update()

screen.mainloop()