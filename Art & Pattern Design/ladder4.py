import turtle
import time

# Setup
screen = turtle.Screen()
screen.bgcolor("#0f0f23")
screen.title("3D Ladder Illusion - Drawing Process")
screen.tracer(0)

# Create turtles
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

label_t = turtle.Turtle()
label_t.speed(0)
label_t.hideturtle()
label_t.penup()

def draw_3d_ladder():
    """Draw a 3D ladder with animation"""
    
    # Ladder parameters
    rungs = 12
    rung_spacing = 35
    rung_length = 120
    rail_width = 10
    depth = 20  # 3D depth
    
    # Starting position
    start_x = -200
    start_y = -180
    
    # Colors
    rail_color = "#8B6914"  # Dark gold
    rail_color_dark = "#5C4A0E"
    rung_color = "#D4A017"  # Golden
    rung_color_dark = "#A67C00"
    
    # Display title
    label_t.goto(0, 280)
    label_t.color("#FFD700")
    label_t.write("3D Ladder Illusion", font=('Arial', 26, 'bold'), align="center")
    
    label_t.goto(0, 240)
    label_t.color("#87CEEB")
    label_t.write("Watch the ladder being drawn in 3D...", font=('Arial', 14), align="center")
    screen.update()
    time.sleep(1)
    
    # --- Draw LEFT RAIL (3D) ---
    label_t.goto(-300, 200)
    label_t.color("#FFD700")
    label_t.write("Left Rail", font=('Arial', 12, 'bold'), align="center")
    screen.update()
    
    # Left rail front face
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.fillcolor(rail_color)
    t.begin_fill()
    t.goto(start_x, start_y + rung_spacing * (rungs - 1) + 30)
    t.goto(start_x + rail_width, start_y + rung_spacing * (rungs - 1) + 30)
    t.goto(start_x + rail_width, start_y)
    t.goto(start_x, start_y)
    t.end_fill()
    screen.update()
    time.sleep(0.3)
    
    # Left rail side face (3D effect)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.fillcolor(rail_color_dark)
    t.begin_fill()
    t.goto(start_x + depth, start_y + depth)
    t.goto(start_x + depth, start_y + rung_spacing * (rungs - 1) + 30 + depth)
    t.goto(start_x, start_y + rung_spacing * (rungs - 1) + 30)
    t.goto(start_x, start_y)
    t.end_fill()
    screen.update()
    time.sleep(0.3)
    
    # Left rail top (3D)
    t.penup()
    t.goto(start_x, start_y + rung_spacing * (rungs - 1) + 30)
    t.pendown()
    t.fillcolor("#A67C00")
    t.begin_fill()
    t.goto(start_x + rail_width, start_y + rung_spacing * (rungs - 1) + 30)
    t.goto(start_x + rail_width + depth, start_y + rung_spacing * (rungs - 1) + 30 + depth)
    t.goto(start_x + depth, start_y + rung_spacing * (rungs - 1) + 30 + depth)
    t.goto(start_x, start_y + rung_spacing * (rungs - 1) + 30)
    t.end_fill()
    screen.update()
    time.sleep(0.3)
    
    # --- Draw RIGHT RAIL (3D) ---
    label_t.goto(200, 200)
    label_t.color("#FFD700")
    label_t.write("Right Rail", font=('Arial', 12, 'bold'), align="center")
    screen.update()
    
    right_x = start_x + rung_length
    
    # Right rail front face
    t.penup()
    t.goto(right_x, start_y)
    t.pendown()
    t.fillcolor(rail_color)
    t.begin_fill()
    t.goto(right_x, start_y + rung_spacing * (rungs - 1) + 30)
    t.goto(right_x + rail_width, start_y + rung_spacing * (rungs - 1) + 30)
    t.goto(right_x + rail_width, start_y)
    t.goto(right_x, start_y)
    t.end_fill()
    screen.update()
    time.sleep(0.3)
    
    # Right rail side face (3D effect)
    t.penup()
    t.goto(right_x, start_y)
    t.pendown()
    t.fillcolor(rail_color_dark)
    t.begin_fill()
    t.goto(right_x + depth, start_y + depth)
    t.goto(right_x + depth, start_y + rung_spacing * (rungs - 1) + 30 + depth)
    t.goto(right_x, start_y + rung_spacing * (rungs - 1) + 30)
    t.goto(right_x, start_y)
    t.end_fill()
    screen.update()
    time.sleep(0.3)
    
    # Right rail top (3D)
    t.penup()
    t.goto(right_x, start_y + rung_spacing * (rungs - 1) + 30)
    t.pendown()
    t.fillcolor("#A67C00")
    t.begin_fill()
    t.goto(right_x + rail_width, start_y + rung_spacing * (rungs - 1) + 30)
    t.goto(right_x + rail_width + depth, start_y + rung_spacing * (rungs - 1) + 30 + depth)
    t.goto(right_x + depth, start_y + rung_spacing * (rungs - 1) + 30 + depth)
    t.goto(right_x, start_y + rung_spacing * (rungs - 1) + 30)
    t.end_fill()
    screen.update()
    time.sleep(0.3)
    
    # --- Draw RUNGS (3D) with animation ---
    label_t.goto(0, 170)
    label_t.color("#FFD700")
    label_t.write("Drawing Rungs...", font=('Arial', 14, 'bold'), align="center")
    screen.update()
    
    for i in range(rungs):
        y_pos = start_y + i * rung_spacing
        
        # Calculate progress
        progress = int((i + 1) / rungs * 100)
        label_t.goto(0, 140)
        label_t.color("#2ecc71")
        label_t.write(f"Progress: {progress}%", font=('Arial', 14), align="center")
        screen.update()
        
        # Rung front face
        t.penup()
        t.goto(start_x + rail_width, y_pos)
        t.pendown()
        t.fillcolor(rung_color)
        t.begin_fill()
        t.goto(right_x, y_pos)
        t.goto(right_x, y_pos + 10)
        t.goto(start_x + rail_width, y_pos + 10)
        t.goto(start_x + rail_width, y_pos)
        t.end_fill()
        screen.update()
        time.sleep(0.08)
        
        # Rung side face (3D effect)
        t.penup()
        t.goto(right_x, y_pos)
        t.pendown()
        t.fillcolor(rung_color_dark)
        t.begin_fill()
        t.goto(right_x + depth, y_pos + depth)
        t.goto(right_x + depth, y_pos + 10 + depth)
        t.goto(right_x, y_pos + 10)
        t.goto(right_x, y_pos)
        t.end_fill()
        screen.update()
        time.sleep(0.08)
        
        # Rung top face (3D effect)
        t.penup()
        t.goto(start_x + rail_width, y_pos + 10)
        t.pendown()
        t.fillcolor("#E8B830")
        t.begin_fill()
        t.goto(right_x, y_pos + 10)
        t.goto(right_x + depth, y_pos + 10 + depth)
        t.goto(start_x + rail_width + depth, y_pos + 10 + depth)
        t.goto(start_x + rail_width, y_pos + 10)
        t.end_fill()
        screen.update()
        time.sleep(0.08)
        
        # Show rung number
        if i % 2 == 0:  # Show every other rung number to avoid clutter
            label_t.goto(start_x + rung_length/2, y_pos + 5)
            label_t.color("white")
            label_t.write(f"{i+1}", font=('Arial', 8), align="center")
            screen.update()
    
    # Final message
    label_t.goto(0, 100)
    label_t.color("#f1c40f")
    label_t.write("✓ 3D Ladder Complete!", font=('Arial', 18, 'bold'), align="center")
    screen.update()
    
    # Draw shadow (extra 3D effect)
    draw_shadow(start_x, start_y, rungs, rung_spacing, rung_length)

def draw_shadow(x, y, rungs, spacing, length):
    """Draw a shadow for extra 3D effect"""
    t.penup()
    t.goto(x + 15, y - 15)
    t.pendown()
    t.color("black")
    t.pensize(2)
    t.goto(x + 15, y + spacing * (rungs - 1) + 30 - 15)
    t.goto(x + length + 15, y + spacing * (rungs - 1) + 30 - 15)
    t.goto(x + length + 15, y - 15)
    t.goto(x + 15, y - 15)
    t.pensize(1)
    screen.update()

def draw_perspective_ladder():
    """Draw a ladder with perspective (converging rails)"""
    
    label_t.goto(300, 280)
    label_t.color("#3498db")
    label_t.write("Perspective View", font=('Arial', 16, 'bold'), align="center")
    
    # Perspective ladder parameters
    rungs = 10
    rung_spacing = 25
    bottom_width = 100
    top_width = 40
    start_x = 250
    start_y = -150
    
    for i in range(rungs):
        y_pos = start_y + i * rung_spacing
        # Width decreases as we go up (perspective)
        current_width = bottom_width - (bottom_width - top_width) * (i / rungs)
        x_offset = (bottom_width - current_width) / 2
        
        # Color gradient (darker at bottom, lighter at top)
        ratio = i / rungs
        r = int(139 + 116 * ratio)
        g = int(69 - 20 * ratio)
        b = int(19 - 10 * ratio)
        color = f"#{r:02x}{g:02x}{b:02x}"
        
        # Draw rung
        t.penup()
        t.goto(start_x + x_offset, y_pos)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.goto(start_x + x_offset + current_width, y_pos)
        t.goto(start_x + x_offset + current_width, y_pos + 8)
        t.goto(start_x + x_offset, y_pos + 8)
        t.goto(start_x + x_offset, y_pos)
        t.end_fill()
        
        # 3D side of rung
        t.penup()
        t.goto(start_x + x_offset + current_width, y_pos)
        t.pendown()
        t.fillcolor(f"#{int(r*0.7):02x}{int(g*0.7):02x}{int(b*0.7):02x}")
        t.begin_fill()
        t.goto(start_x + x_offset + current_width + 10, y_pos + 10)
        t.goto(start_x + x_offset + current_width + 10, y_pos + 10 + 8)
        t.goto(start_x + x_offset + current_width, y_pos + 8)
        t.goto(start_x + x_offset + current_width, y_pos)
        t.end_fill()
        
        screen.update()
        time.sleep(0.05)
    
    # Draw converging rails (lines)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("#8B6914")
    t.pensize(4)
    t.goto(start_x + (bottom_width - top_width)/2, start_y + rung_spacing * (rungs - 1))
    t.pensize(1)
    
    t.penup()
    t.goto(start_x + bottom_width, start_y)
    t.pendown()
    t.color("#8B6914")
    t.pensize(4)
    t.goto(start_x + bottom_width - (bottom_width - top_width)/2, start_y + rung_spacing * (rungs - 1))
    t.pensize(1)
    
    screen.update()

# Main execution
print("Drawing 3D Ladder with Animation...")

# Clear
t.clear()
label_t.clear()

# Draw the main animated ladder
draw_3d_ladder()

# Draw perspective ladder
draw_perspective_ladder()

# Add instructions
label_t.goto(0, -320)
label_t.color("#95a5a6")
label_t.write("Click anywhere to exit", font=('Arial', 12), align="center")
screen.update()

# Keep window open
screen.mainloop()