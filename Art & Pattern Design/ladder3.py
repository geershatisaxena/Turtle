import turtle
import time

# Setup
screen = turtle.Screen()
screen.bgcolor("#0a0a1a")
screen.title("3D Ladder - Step by Step Drawing")
screen.tracer(0)
screen.setup(900, 700)

# Create turtles
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

label_t = turtle.Turtle()
label_t.speed(0)
label_t.hideturtle()
label_t.penup()

# Drawing state
current_step = 0
total_steps = 0

def draw_line_with_animation(x1, y1, x2, y2, color, width=2, delay=0.02):
    """Draw a line with animation showing the drawing process"""
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(color)
    t.pensize(width)
    
    # Animate the line being drawn
    steps = 30
    for i in range(steps + 1):
        progress = i / steps
        x = x1 + (x2 - x1) * progress
        y = y1 + (y2 - y1) * progress
        t.goto(x, y)
        screen.update()
        time.sleep(delay)
    
    t.pensize(1)

def draw_filled_shape_with_animation(points, color, delay=0.02):
    """Draw a filled shape with animation showing each edge"""
    t.fillcolor(color)
    t.begin_fill()
    
    # Draw each edge with animation
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        
        # Animate this edge
        steps = 20
        for j in range(steps + 1):
            progress = j / steps
            x = x1 + (x2 - x1) * progress
            y = y1 + (y2 - y1) * progress
            t.goto(x, y)
            screen.update()
            time.sleep(delay)
    
    t.end_fill()

def update_status(text, color="white", y_offset=0):
    """Update status text"""
    label_t.goto(0, 280 + y_offset)
    label_t.color(color)
    label_t.clear()
    label_t.write(text, font=('Arial', 14, 'bold'), align="center")
    screen.update()

def draw_3d_ladder_with_animation():
    """Draw a 3D ladder with detailed animation showing each step"""
    
    global current_step, total_steps
    
    # Ladder parameters
    rungs = 10
    rung_spacing = 40
    rung_length = 140
    rail_width = 12
    depth = 25
    
    # Starting position
    start_x = -300
    start_y = -200
    
    # Colors
    rail_front = "#D4A017"
    rail_side = "#8B6914"
    rail_top = "#F0C040"
    rung_front = "#E8B830"
    rung_side = "#A67C00"
    rung_top = "#F5D060"
    
    # Total steps for progress
    total_steps = rungs * 3 + 9  # 3 faces per rung + rails
    current_step = 0
    
    # Title
    label_t.goto(0, 330)
    label_t.color("#FFD700")
    label_t.write("🎯 3D Ladder - Step by Step Drawing", font=('Arial', 24, 'bold'), align="center")
    screen.update()
    
    time.sleep(1)
    
    # === DRAW LEFT RAIL ===
    update_status("📐 Step 1: Drawing Left Rail - Front Face", "#FF6B6B")
    
    # Left rail front face
    points = [
        (start_x, start_y),
        (start_x, start_y + rung_spacing * (rungs - 1) + 40),
        (start_x + rail_width, start_y + rung_spacing * (rungs - 1) + 40),
        (start_x + rail_width, start_y)
    ]
    draw_filled_shape_with_animation(points, rail_front, 0.015)
    current_step += 1
    update_status(f"📐 Step {current_step}: Left Rail - Front Face ✓", "#2ecc71")
    time.sleep(0.3)
    
    # Left rail side face
    update_status(f"📐 Step {current_step + 1}: Left Rail - Side Face (3D depth)", "#FF6B6B")
    points = [
        (start_x, start_y),
        (start_x + depth, start_y + depth),
        (start_x + depth, start_y + rung_spacing * (rungs - 1) + 40 + depth),
        (start_x, start_y + rung_spacing * (rungs - 1) + 40)
    ]
    draw_filled_shape_with_animation(points, rail_side, 0.015)
    current_step += 1
    update_status(f"📐 Step {current_step}: Left Rail - Side Face ✓", "#2ecc71")
    time.sleep(0.3)
    
    # Left rail top face
    update_status(f"📐 Step {current_step + 1}: Left Rail - Top Face", "#FF6B6B")
    points = [
        (start_x, start_y + rung_spacing * (rungs - 1) + 40),
        (start_x + rail_width, start_y + rung_spacing * (rungs - 1) + 40),
        (start_x + rail_width + depth, start_y + rung_spacing * (rungs - 1) + 40 + depth),
        (start_x + depth, start_y + rung_spacing * (rungs - 1) + 40 + depth)
    ]
    draw_filled_shape_with_animation(points, rail_top, 0.015)
    current_step += 1
    update_status(f"📐 Step {current_step}: Left Rail - Top Face ✓", "#2ecc71")
    time.sleep(0.3)
    
    # === DRAW RIGHT RAIL ===
    right_x = start_x + rung_length
    
    update_status(f"📐 Step {current_step + 1}: Drawing Right Rail - Front Face", "#FF6B6B")
    
    # Right rail front face
    points = [
        (right_x, start_y),
        (right_x, start_y + rung_spacing * (rungs - 1) + 40),
        (right_x + rail_width, start_y + rung_spacing * (rungs - 1) + 40),
        (right_x + rail_width, start_y)
    ]
    draw_filled_shape_with_animation(points, rail_front, 0.015)
    current_step += 1
    update_status(f"📐 Step {current_step}: Right Rail - Front Face ✓", "#2ecc71")
    time.sleep(0.3)
    
    # Right rail side face
    update_status(f"📐 Step {current_step + 1}: Right Rail - Side Face", "#FF6B6B")
    points = [
        (right_x, start_y),
        (right_x + depth, start_y + depth),
        (right_x + depth, start_y + rung_spacing * (rungs - 1) + 40 + depth),
        (right_x, start_y + rung_spacing * (rungs - 1) + 40)
    ]
    draw_filled_shape_with_animation(points, rail_side, 0.015)
    current_step += 1
    update_status(f"📐 Step {current_step}: Right Rail - Side Face ✓", "#2ecc71")
    time.sleep(0.3)
    
    # Right rail top face
    update_status(f"📐 Step {current_step + 1}: Right Rail - Top Face", "#FF6B6B")
    points = [
        (right_x, start_y + rung_spacing * (rungs - 1) + 40),
        (right_x + rail_width, start_y + rung_spacing * (rungs - 1) + 40),
        (right_x + rail_width + depth, start_y + rung_spacing * (rungs - 1) + 40 + depth),
        (right_x + depth, start_y + rung_spacing * (rungs - 1) + 40 + depth)
    ]
    draw_filled_shape_with_animation(points, rail_top, 0.015)
    current_step += 1
    update_status(f"📐 Step {current_step}: Right Rail - Top Face ✓", "#2ecc71")
    time.sleep(0.3)
    
    # === DRAW RUNGS ===
    update_status("🪜 Drawing Rungs...", "#FFD700", -30)
    
    for i in range(rungs):
        y_pos = start_y + i * rung_spacing
        
        # Update progress
        progress = int((i + 1) / rungs * 100)
        update_status(f"🪜 Drawing Rung {i+1}/{rungs} - {progress}%", "#87CEEB", -30)
        
        # Rung front face
        update_status(f"📐 Step {current_step + 1}: Rung {i+1} - Front Face", "#FF6B6B", -60)
        points = [
            (start_x + rail_width, y_pos),
            (right_x, y_pos),
            (right_x, y_pos + 12),
            (start_x + rail_width, y_pos + 12)
        ]
        draw_filled_shape_with_animation(points, rung_front, 0.01)
        current_step += 1
        
        # Rung side face
        update_status(f"📐 Step {current_step + 1}: Rung {i+1} - Side Face", "#FF6B6B", -60)
        points = [
            (right_x, y_pos),
            (right_x + depth, y_pos + depth),
            (right_x + depth, y_pos + 12 + depth),
            (right_x, y_pos + 12)
        ]
        draw_filled_shape_with_animation(points, rung_side, 0.01)
        current_step += 1
        
        # Rung top face
        update_status(f"📐 Step {current_step + 1}: Rung {i+1} - Top Face", "#FF6B6B", -60)
        points = [
            (start_x + rail_width, y_pos + 12),
            (right_x, y_pos + 12),
            (right_x + depth, y_pos + 12 + depth),
            (start_x + rail_width + depth, y_pos + 12 + depth)
        ]
        draw_filled_shape_with_animation(points, rung_top, 0.01)
        current_step += 1
        
        # Highlight the rung being drawn
        update_status(f"✅ Rung {i+1} Complete!", "#2ecc71", -60)
        
        # Add rung number label
        label_t.goto(start_x + rung_length/2, y_pos + 6)
        label_t.color("white")
        label_t.write(f"{i+1}", font=('Arial', 10, 'bold'), align="center")
        screen.update()
        
        time.sleep(0.15)
    
    # === ADD FINISHING TOUCHES ===
    
    # Draw outline for 3D effect (shadow)
    update_status("✨ Adding final touches...", "#FFD700", -30)
    
    # Draw a subtle shadow
    t.penup()
    t.goto(start_x + 20, start_y - 20)
    t.pendown()
    t.color("black", "black")
    t.pensize(1)
    t.begin_fill()
    t.goto(start_x + 20, start_y + rung_spacing * (rungs - 1) + 40 - 20)
    t.goto(start_x + rung_length + 20, start_y + rung_spacing * (rungs - 1) + 40 - 20)
    t.goto(start_x + rung_length + 20, start_y - 20)
    t.goto(start_x + 20, start_y - 20)
    t.end_fill()
    screen.update()
    
    # Highlight edges
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("#FFD700")
    t.pensize(1)
    for i in range(rungs):
        y_pos = start_y + i * rung_spacing
        t.goto(start_x + rail_width, y_pos)
        t.goto(right_x, y_pos)
    t.pensize(1)
    screen.update()
    
    # === COMPLETION ===
    time.sleep(0.5)
    update_status("🎉 LADDER COMPLETE! 3D Illusion Created!", "#FFD700", -30)
    
    label_t.goto(0, -320)
    label_t.color("#2ecc71")
    label_t.write(f"✓ {current_step} drawing steps completed successfully!", font=('Arial', 14), align="center")
    screen.update()

def draw_exploded_view():
    """Draw an exploded view showing how the 3D ladder is constructed"""
    
    label_t.goto(350, 330)
    label_t.color("#3498db")
    label_t.write("🔍 Exploded View", font=('Arial', 18, 'bold'), align="center")
    
    label_t.goto(350, 300)
    label_t.color("#87CEEB")
    label_t.write("See each part separately", font=('Arial', 12), align="center")
    
    # Draw a single rung exploded
    x = 280
    y = 200
    
    # Draw front face (shifted left)
    t.penup()
    t.goto(x - 40, y)
    t.pendown()
    t.fillcolor("#E8B830")
    t.begin_fill()
    t.goto(x + 20, y)
    t.goto(x + 20, y + 15)
    t.goto(x - 40, y + 15)
    t.goto(x - 40, y)
    t.end_fill()
    
    label_t.goto(x - 10, y - 20)
    label_t.color("#E8B830")
    label_t.write("Front", font=('Arial', 10, 'bold'), align="center")
    
    # Draw side face (shifted right)
    t.penup()
    t.goto(x + 60, y)
    t.pendown()
    t.fillcolor("#A67C00")
    t.begin_fill()
    t.goto(x + 60 + 20, y + 20)
    t.goto(x + 60 + 20, y + 20 + 15)
    t.goto(x + 60, y + 15)
    t.goto(x + 60, y)
    t.end_fill()
    
    label_t.goto(x + 70, y - 20)
    label_t.color("#A67C00")
    label_t.write("Side", font=('Arial', 10, 'bold'), align="center")
    
    # Draw top face (shifted up)
    t.penup()
    t.goto(x, y + 40)
    t.pendown()
    t.fillcolor("#F5D060")
    t.begin_fill()
    t.goto(x + 60, y + 40)
    t.goto(x + 60 + 20, y + 40 + 20)
    t.goto(x + 20, y + 40 + 20)
    t.goto(x, y + 40)
    t.end_fill()
    
    label_t.goto(x + 30, y + 80)
    label_t.color("#F5D060")
    label_t.write("Top", font=('Arial', 10, 'bold'), align="center")
    
    # Draw combined rung (center)
    x = 280
    y = 80
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("#E8B830")
    t.begin_fill()
    t.goto(x + 60, y)
    t.goto(x + 60, y + 15)
    t.goto(x, y + 15)
    t.goto(x, y)
    t.end_fill()
    
    t.penup()
    t.goto(x + 60, y)
    t.pendown()
    t.fillcolor("#A67C00")
    t.begin_fill()
    t.goto(x + 60 + 20, y + 20)
    t.goto(x + 60 + 20, y + 20 + 15)
    t.goto(x + 60, y + 15)
    t.goto(x + 60, y)
    t.end_fill()
    
    t.penup()
    t.goto(x, y + 15)
    t.pendown()
    t.fillcolor("#F5D060")
    t.begin_fill()
    t.goto(x + 60, y + 15)
    t.goto(x + 60 + 20, y + 15 + 20)
    t.goto(x + 20, y + 15 + 20)
    t.goto(x, y + 15)
    t.end_fill()
    
    label_t.goto(x + 30, y - 30)
    label_t.color("white")
    label_t.write("Combined", font=('Arial', 10, 'bold'), align="center")
    
    # Arrows
    t.penup()
    t.goto(280, 170)
    t.pendown()
    t.color("#FF6B6B")
    t.pensize(2)
    t.goto(280, 150)
    t.goto(275, 155)
    t.penup()
    t.goto(280, 150)
    t.pendown()
    t.goto(285, 155)
    t.pensize(1)
    
    t.penup()
    t.goto(340, 110)
    t.pendown()
    t.color("#FF6B6B")
    t.pensize(2)
    t.goto(320, 100)
    t.goto(325, 97)
    t.penup()
    t.goto(320, 100)
    t.pendown()
    t.goto(320, 105)
    t.pensize(1)
    
    t.penup()
    t.goto(320, 140)
    t.pendown()
    t.color("#FF6B6B")
    t.pensize(2)
    t.goto(320, 120)
    t.goto(315, 125)
    t.penup()
    t.goto(320, 120)
    t.pendown()
    t.goto(325, 125)
    t.pensize(1)

# Main execution
print("Drawing 3D Ladder with Detailed Animation...")

# Clear
t.clear()
label_t.clear()

# Draw the main animated ladder
draw_3d_ladder_with_animation()

# Draw exploded view
draw_exploded_view()

# Add instructions
label_t.goto(0, -370)
label_t.color("#95a5a6")
label_t.write("🖱️ Click anywhere to exit", font=('Arial', 12), align="center")
screen.update()

# Keep window open
screen.mainloop()