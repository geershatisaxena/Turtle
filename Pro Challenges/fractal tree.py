import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Fractal Tree - Recursive Drawing")
screen.bgcolor("skyblue")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Create the tree turtle
tree = turtle.Turtle()
tree.speed(0)
tree.penup()
tree.goto(0, -350)
tree.setheading(90)
tree.pendown()
tree.hideturtle()

# Color settings
trunk_color = "saddlebrown"
leaf_colors = ["forestgreen", "limegreen", "green", "darkgreen", "olive", "springgreen"]

# Global settings
angle = 30
branch_ratio = 0.7
min_length = 5
show_leaves = True
colored_leaves = True

# UI elements
ui_display = turtle.Turtle()
ui_display.speed(0)
ui_display.color("black")
ui_display.penup()
ui_display.hideturtle()

def draw_fractal_tree(length, thickness, angle_offset=0):
    """
    Draw a fractal tree recursively
    
    Parameters:
    - length: current branch length
    - thickness: current branch thickness
    - angle_offset: random variation for natural look
    """
    if length < min_length:
        # Draw leaf at the end if enabled
        if show_leaves:
            draw_leaf()
        return
    
    # Set branch color based on length
    if length > 30:
        tree.color("saddlebrown")
    else:
        # Smaller branches are lighter/greenish
        tree.color("peru" if length > 15 else "olivedrab")
    
    # Set pen thickness (tapering effect)
    tree.pensize(max(1, thickness))
    
    # Draw current branch
    tree.forward(length)
    
    # Determine branch angles with some randomness
    left_angle = angle + random.uniform(-5, 5) + angle_offset
    right_angle = angle + random.uniform(-5, 5) - angle_offset
    
    # Calculate new length and thickness
    new_length = length * branch_ratio
    new_thickness = thickness * branch_ratio
    
    # Draw left branch
    tree.left(left_angle)
    draw_fractal_tree(new_length, new_thickness, angle_offset + random.uniform(-3, 3))
    
    # Draw right branch
    tree.right(left_angle + right_angle)
    draw_fractal_tree(new_length, new_thickness, angle_offset + random.uniform(-3, 3))
    
    # Return to original position and angle
    tree.left(right_angle)
    tree.backward(length)

def draw_leaf():
    """Draw a leaf at branch tip"""
    tree.penup()
    tree.forward(5)
    tree.pendown()
    
    # Choose leaf color
    if colored_leaves:
        color = random.choice(leaf_colors)
        tree.color(color)
    else:
        tree.color("forestgreen")
    
    # Draw small leaf
    tree.begin_fill()
    tree.circle(3)
    tree.end_fill()
    
    # Return to branch tip
    tree.penup()
    tree.backward(5)
    tree.pendown()
    tree.color("saddlebrown")

def draw_ground():
    """Draw ground grass"""
    ground = turtle.Turtle()
    ground.speed(0)
    ground.color("darkgreen")
    ground.penup()
    ground.goto(-500, -360)
    ground.pendown()
    ground.begin_fill()
    ground.goto(500, -360)
    ground.goto(500, -400)
    ground.goto(-500, -400)
    ground.goto(-500, -360)
    ground.end_fill()
    ground.hideturtle()

def draw_sun():
    """Draw decorative sun"""
    sun = turtle.Turtle()
    sun.speed(0)
    sun.color("orange")
    sun.penup()
    sun.goto(400, 350)
    sun.pendown()
    sun.begin_fill()
    sun.circle(40)
    sun.end_fill()
    
    # Draw sun rays
    sun.penup()
    sun.goto(400, 350)
    for angle in range(0, 360, 45):
        sun.setheading(angle)
        sun.forward(55)
        sun.dot(5, "yellow")
        sun.goto(400, 350)
    sun.hideturtle()

def draw_clouds():
    """Draw some clouds"""
    cloud = turtle.Turtle()
    cloud.speed(0)
    cloud.color("white")
    cloud.penup()
    
    cloud_positions = [(-300, 300), (0, 320), (250, 280)]
    for x, y in cloud_positions:
        cloud.goto(x, y)
        cloud.pendown()
        cloud.begin_fill()
        for _ in range(3):
            cloud.circle(25)
            cloud.forward(30)
        cloud.end_fill()
        cloud.penup()
    
    cloud.hideturtle()

def update_info():
    """Update UI information"""
    ui_display.clear()
    ui_display.goto(-480, 360)
    ui_display.write(f"Fractal Tree - Angle: {angle}° | Ratio: {branch_ratio:.1f} | Min Length: {min_length}",
                     font=("Arial", 10, "normal"))
    ui_display.goto(-480, 340)
    ui_display.write("Controls: +/- Angle | [/] Ratio | </> Min Length | L: Toggle Leaves | C: Toggle Color | R: Random | Space: Redraw",
                     font=("Arial", 10, "normal"))

def redraw_tree():
    """Clear and redraw the tree with current settings"""
    tree.clear()
    tree.penup()
    tree.goto(0, -350)
    tree.setheading(90)
    tree.pendown()
    draw_fractal_tree(100, 12)
    screen.update()

def increase_angle():
    global angle
    angle = min(angle + 5, 75)
    redraw_tree()
    update_info()

def decrease_angle():
    global angle
    angle = max(angle - 5, 15)
    redraw_tree()
    update_info()

def increase_ratio():
    global branch_ratio
    branch_ratio = min(branch_ratio + 0.05, 0.9)
    redraw_tree()
    update_info()

def decrease_ratio():
    global branch_ratio
    branch_ratio = max(branch_ratio - 0.05, 0.4)
    redraw_tree()
    update_info()

def increase_min_length():
    global min_length
    min_length = min(min_length + 2, 20)
    redraw_tree()
    update_info()

def decrease_min_length():
    global min_length
    min_length = max(min_length - 2, 3)
    redraw_tree()
    update_info()

def toggle_leaves():
    global show_leaves
    show_leaves = not show_leaves
    redraw_tree()
    update_info()

def toggle_leaf_colors():
    global colored_leaves
    colored_leaves = not colored_leaves
    redraw_tree()
    update_info()

def randomize_tree():
    """Randomize all tree parameters"""
    global angle, branch_ratio, min_length
    angle = random.randint(20, 60)
    branch_ratio = random.uniform(0.5, 0.85)
    min_length = random.randint(3, 15)
    redraw_tree()
    update_info()

# Keyboard bindings
screen.listen()
screen.onkey(increase_angle, "plus")
screen.onkey(increase_angle, "equal")
screen.onkey(decrease_angle, "minus")
screen.onkey(increase_ratio, "bracketright")
screen.onkey(decrease_ratio, "bracketleft")
screen.onkey(increase_min_length, "period")
screen.onkey(decrease_min_length, "comma")
screen.onkey(toggle_leaves, "l")
screen.onkey(toggle_leaf_colors, "c")
screen.onkey(randomize_tree, "r")
screen.onkey(redraw_tree, "space")
screen.onkey(lambda: screen.bye(), "Escape")

# Draw environment
draw_ground()
draw_sun()
draw_clouds()
update_info()

# Print console instructions
print("=== FRACTAL TREE - RECURSIVE DRAWING ===")
print()
print("The tree uses recursion to draw branches that split into smaller branches")
print()
print("CONTROLS:")
print("  + / -     - Increase/Decrease branch angle (15°-75°)")
print("  [ / ]     - Decrease/Increase branch length ratio (0.4-0.9)")
print("  < / >     - Decrease/Increase minimum branch length (3-20)")
print("  L         - Toggle leaves on/off")
print("  C         - Toggle leaf colors (random vs green)")
print("  R         - Randomize all tree parameters")
print("  SPACE     - Redraw tree with current settings")
print("  ESC       - Exit program")
print()
print("Watch how the tree changes when you adjust angles and ratios!")

# Draw initial tree
draw_fractal_tree(100, 12)
screen.update()

# Keep window open
screen.mainloop()