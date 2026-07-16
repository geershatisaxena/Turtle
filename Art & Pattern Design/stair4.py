import turtle
import time

# Setup
screen = turtle.Screen()
screen.bgcolor("#1a1a2e")
screen.title("3D Staircase Illusion - Drawing Process")
screen.tracer(0)  # Turn off auto-update for smooth animation

# Create turtles
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Create a second turtle for labels
label_t = turtle.Turtle()
label_t.speed(0)
label_t.hideturtle()
label_t.penup()

# Color palette
colors = {
    'top': '#e74c3c',
    'front': '#c0392b',
    'side': '#922b21',
    'bg': '#1a1a2e'
}

def draw_step_with_animation(x, y, width, height, depth, step_num, total_steps):
    """Draw a single 3D step with animation"""
    
    # Calculate color based on step position (gradient effect)
    ratio = step_num / total_steps
    r = int(231 - 80 * ratio)
    g = int(76 - 40 * ratio)
    b = int(60 - 30 * ratio)
    top_color = f"#{r:02x}{g:02x}{b:02x}"
    
    # Darker versions for 3D effect
    front_color = f"#{int(r*0.8):02x}{int(g*0.8):02x}{int(b*0.8):02x}"
    side_color = f"#{int(r*0.6):02x}{int(g*0.6):02x}{int(b*0.6):02x}"
    
    # --- Draw TOP face with animation ---
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(top_color)
    t.begin_fill()
    
    # Animate the top face
    points = [
        (x, y),
        (x + width, y),
        (x + width + depth, y + depth),
        (x + depth, y + depth)
    ]
    
    for i in range(len(points) + 1):
        t.goto(points[i % len(points)])
        screen.update()
        time.sleep(0.02)
    t.end_fill()
    
    # --- Draw FRONT face with animation ---
    t.penup()
    t.goto(x, y - depth)
    t.pendown()
    t.fillcolor(front_color)
    t.begin_fill()
    
    points_front = [
        (x, y - depth),
        (x, y),
        (x + width, y),
        (x + width, y - depth)
    ]
    
    for i in range(len(points_front) + 1):
        t.goto(points_front[i % len(points_front)])
        screen.update()
        time.sleep(0.02)
    t.end_fill()
    
    # --- Draw SIDE face with animation ---
    t.penup()
    t.goto(x + width, y - depth)
    t.pendown()
    t.fillcolor(side_color)
    t.begin_fill()
    
    points_side = [
        (x + width, y - depth),
        (x + width, y),
        (x + width + depth, y + depth),
        (x + width + depth, y)
    ]
    
    for i in range(len(points_side) + 1):
        t.goto(points_side[i % len(points_side)])
        screen.update()
        time.sleep(0.02)
    t.end_fill()
    
    # --- Draw step number ---
    label_t.goto(x + width/2 - 5, y - depth/2)
    label_t.color("white")
    label_t.write(str(step_num + 1), font=('Arial', 12, 'bold'), align="center")

def draw_complete_staircase():
    """Draw the complete staircase with animation"""
    
    # Display title
    label_t.goto(0, 280)
    label_t.color("#f1c40f")
    label_t.write("3D Staircase Illusion", font=('Arial', 24, 'bold'), align="center")
    
    label_t.goto(0, 250)
    label_t.color("#ecf0f1")
    label_t.write("Watch the drawing process...", font=('Arial', 14), align="center")
    screen.update()
    
    # Staircase parameters
    steps = 12
    step_width = 50
    step_height = 25
    depth = 30
    
    # Draw each step with animation
    for i in range(steps):
        x = -300 + i * (step_width - 8)
        y = -150 + i * step_height
        
        # Draw step with animation
        draw_step_with_animation(x, y, step_width, step_height, depth, i, steps)
        
        # Update progress
        progress = int((i + 1) / steps * 100)
        label_t.goto(0, 220)
        label_t.color("#2ecc71")
        label_t.clear()
        label_t.write(f"Progress: {progress}%", font=('Arial', 14), align="center")
        screen.update()
        
        # Small delay between steps
        time.sleep(0.3)
    
    # Final message
    label_t.goto(0, 190)
    label_t.color("#f1c40f")
    label_t.write("✓ Complete! 3D Illusion Created!", font=('Arial', 16, 'bold'), align="center")
    screen.update()

def draw_exploded_view():
    """Draw an exploded view showing each face separately"""
    
    label_t.goto(300, 280)
    label_t.color("#3498db")
    label_t.write("Exploded View", font=('Arial', 18, 'bold'), align="center")
    
    # Draw a single step with faces separated
    x = 200
    y = 100
    width = 60
    height = 30
    depth = 25
    
    # Draw top face (shifted up)
    t.penup()
    t.goto(x, y + 40)
    t.pendown()
    t.fillcolor("#e74c3c")
    t.begin_fill()
    t.goto(x + width, y + 40)
    t.goto(x + width + depth, y + 40 + depth)
    t.goto(x + depth, y + 40 + depth)
    t.goto(x, y + 40)
    t.end_fill()
    
    label_t.goto(x + width/2, y + 40 + depth + 20)
    label_t.color("#e74c3c")
    label_t.write("TOP", font=('Arial', 10, 'bold'), align="center")
    
    # Draw front face (shifted forward)
    t.penup()
    t.goto(x - 30, y - depth - 20)
    t.pendown()
    t.fillcolor("#c0392b")
    t.begin_fill()
    t.goto(x - 30, y - 20)
    t.goto(x + width - 30, y - 20)
    t.goto(x + width - 30, y - depth - 20)
    t.goto(x - 30, y - depth - 20)
    t.end_fill()
    
    label_t.goto(x + width/2 - 30, y - depth/2 - 20)
    label_t.color("#c0392b")
    label_t.write("FRONT", font=('Arial', 10, 'bold'), align="center")
    
    # Draw side face (shifted right)
    t.penup()
    t.goto(x + width + 30, y - depth - 20)
    t.pendown()
    t.fillcolor("#922b21")
    t.begin_fill()
    t.goto(x + width + 30, y - 20)
    t.goto(x + width + depth + 30, y + depth - 20)
    t.goto(x + width + depth + 30, y - 20)
    t.goto(x + width + 30, y - depth - 20)
    t.end_fill()
    
    label_t.goto(x + width + depth/2 + 30, y - 10)
    label_t.color("#922b21")
    label_t.write("SIDE", font=('Arial', 10, 'bold'), align="center")
    
    # Draw the combined step (normal position)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("#e74c3c")
    t.begin_fill()
    t.goto(x + width, y)
    t.goto(x + width + depth, y + depth)
    t.goto(x + depth, y + depth)
    t.goto(x, y)
    t.end_fill()
    
    t.penup()
    t.goto(x, y - depth)
    t.pendown()
    t.fillcolor("#c0392b")
    t.begin_fill()
    t.goto(x, y)
    t.goto(x + width, y)
    t.goto(x + width, y - depth)
    t.goto(x, y - depth)
    t.end_fill()
    
    t.penup()
    t.goto(x + width, y - depth)
    t.pendown()
    t.fillcolor("#922b21")
    t.begin_fill()
    t.goto(x + width, y)
    t.goto(x + width + depth, y + depth)
    t.goto(x + width + depth, y)
    t.goto(x + width, y - depth)
    t.end_fill()
    
    label_t.goto(x + width/2, y - depth - 30)
    label_t.color("white")
    label_t.write("COMBINED", font=('Arial', 10, 'bold'), align="center")

# Main execution
print("Drawing 3D Staircase with Animation...")

# Clear any previous drawings
t.clear()
label_t.clear()

# Draw the main animated staircase
draw_complete_staircase()

# Draw the exploded view
draw_exploded_view()

# Add interactive instructions
label_t.goto(0, -300)
label_t.color("#95a5a6")
label_t.write("Click anywhere to exit", font=('Arial', 12), align="center")
screen.update()

# Keep window open
screen.mainloop()