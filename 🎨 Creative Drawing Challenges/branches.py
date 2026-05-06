import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Tree with Branches - Non-Fractal")
screen.bgcolor("#87CEEB")  # Sky blue
screen.setup(width=900, height=800)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Color palette
colors = {
    "trunk": "#8B4513",
    "trunk_dark": "#5C3317",
    "branch": "#6B3E1B",
    "branch_light": "#A0522D",
    "leaves": "#2E7D32",
    "leaves_light": "#43A047",
    "leaves_dark": "#1B5E20",
    "leaves_fall": "#FF8C00",
    "flowers": "#FF69B4",
    "ground": "#228B22",
    "ground_dark": "#1B5E20",
    "roots": "#6B3E1B",
    "shadow": "#4A4A4A"
}

def draw_ground():
    """Draw the ground/grass"""
    pen.penup()
    pen.goto(-500, -250)
    pen.pendown()
    pen.color(colors["ground"])
    pen.begin_fill()
    pen.goto(500, -250)
    pen.goto(500, -400)
    pen.goto(-500, -400)
    pen.goto(-500, -250)
    pen.end_fill()
    
    # Add grass texture
    pen.color(colors["ground_dark"])
    for i in range(80):
        x = random.randint(-480, 480)
        y = random.randint(-380, -260)
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(90)
        pen.forward(random.randint(5, 15))
        pen.penup()
    
    pen.penup()

def draw_trunk():
    """Draw the main trunk of the tree"""
    # Trunk (wider at bottom, narrower at top)
    pen.penup()
    pen.goto(-40, -250)
    pen.pendown()
    pen.color(colors["trunk"])
    pen.begin_fill()
    
    # Left side of trunk
    pen.goto(-35, -150)
    pen.goto(-30, -50)
    pen.goto(-25, 0)
    pen.goto(-20, 50)
    pen.goto(-15, 100)
    
    # Top of trunk
    pen.goto(0, 120)
    
    # Right side of trunk
    pen.goto(15, 100)
    pen.goto(20, 50)
    pen.goto(25, 0)
    pen.goto(30, -50)
    pen.goto(35, -150)
    pen.goto(40, -250)
    
    pen.end_fill()
    
    # Trunk texture (lines)
    pen.color(colors["trunk_dark"])
    pen.pensize(2)
    for i in range(-30, 35, 10):
        pen.penup()
        pen.goto(i, -220)
        pen.pendown()
        pen.goto(i - 5, -120)
        pen.penup()
    
    pen.penup()

def draw_branches():
    """Draw all the branches extending from the trunk"""
    
    # Main branch 1 (left)
    pen.penup()
    pen.goto(-20, 80)
    pen.pendown()
    pen.color(colors["branch"])
    pen.pensize(12)
    pen.setheading(160)
    pen.forward(70)
    pen.pensize(8)
    pen.forward(40)
    
    # Sub-branches of branch 1
    pen.penup()
    pen.goto(-65, 130)
    pen.pendown()
    pen.setheading(140)
    pen.forward(35)
    pen.penup()
    pen.goto(-55, 115)
    pen.pendown()
    pen.setheading(200)
    pen.forward(30)
    
    # Main branch 2 (right)
    pen.penup()
    pen.goto(20, 85)
    pen.pendown()
    pen.color(colors["branch"])
    pen.pensize(12)
    pen.setheading(20)
    pen.forward(70)
    pen.pensize(8)
    pen.forward(40)
    
    # Sub-branches of branch 2
    pen.penup()
    pen.goto(65, 130)
    pen.pendown()
    pen.setheading(40)
    pen.forward(35)
    pen.penup()
    pen.goto(55, 115)
    pen.pendown()
    pen.setheading(-20)
    pen.forward(30)
    
    # Main branch 3 (center-left)
    pen.penup()
    pen.goto(-10, 110)
    pen.pendown()
    pen.pensize(10)
    pen.setheading(190)
    pen.forward(50)
    pen.pensize(6)
    pen.forward(30)
    
    # Main branch 4 (center-right)
    pen.penup()
    pen.goto(10, 110)
    pen.pendown()
    pen.pensize(10)
    pen.setheading(-10)
    pen.forward(50)
    pen.pensize(6)
    pen.forward(30)
    
    # Top branches
    pen.penup()
    pen.goto(-5, 115)
    pen.pendown()
    pen.pensize(8)
    pen.setheading(150)
    pen.forward(45)
    pen.pensize(5)
    pen.forward(25)
    
    pen.penup()
    pen.goto(5, 115)
    pen.pendown()
    pen.pensize(8)
    pen.setheading(30)
    pen.forward(45)
    pen.pensize(5)
    pen.forward(25)
    
    pen.penup()
    pen.goto(0, 118)
    pen.pendown()
    pen.pensize(8)
    pen.setheading(90)
    pen.forward(50)
    pen.pensize(5)
    pen.forward(25)
    
    pen.penup()

def draw_leaves():
    """Draw clusters of leaves at branch ends"""
    
    leaf_positions = [
        # Branch 1 leaves
        (-100, 170), (-80, 155), (-110, 145), (-90, 135), (-120, 125),
        (-70, 120), (-85, 110), (-95, 100),
        
        # Branch 2 leaves
        (100, 170), (80, 155), (110, 145), (90, 135), (120, 125),
        (70, 120), (85, 110), (95, 100),
        
        # Branch 3 leaves
        (-70, 160), (-60, 145), (-80, 135), (-50, 125), (-65, 115),
        
        # Branch 4 leaves
        (70, 160), (60, 145), (80, 135), (50, 125), (65, 115),
        
        # Top leaves
        (-50, 180), (-35, 170), (-45, 160), (-30, 150), (-40, 140),
        (50, 180), (35, 170), (45, 160), (30, 150), (40, 140),
        (0, 190), (-10, 180), (10, 180), (-5, 170), (5, 170),
        
        # Additional canopy leaves
        (-30, 200), (30, 200), (0, 210), (-20, 195), (20, 195),
        (-40, 190), (40, 190), (-15, 205), (15, 205), (0, 220),
    ]
    
    # Draw leaf clusters
    for x, y in leaf_positions:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        
        # Random leaf color (mix of light and dark green)
        leaf_color = random.choice([colors["leaves"], colors["leaves_light"], colors["leaves_dark"]])
        pen.color(leaf_color)
        pen.begin_fill()
        
        # Draw leaf cluster (overlapping circles)
        pen.circle(random.randint(8, 15))
        pen.end_fill()
        
        # Add smaller leaves around
        for angle in range(0, 360, 60):
            rad = math.radians(angle)
            px = x + random.randint(5, 12) * math.cos(rad)
            py = y + random.randint(5, 12) * math.sin(rad)
            pen.penup()
            pen.goto(px, py)
            pen.pendown()
            pen.color(colors["leaves_light"])
            pen.begin_fill()
            pen.circle(random.randint(4, 8))
            pen.end_fill()
    
    pen.penup()

def draw_fall_leaves():
    """Draw some falling autumn leaves"""
    pen.penup()
    fall_positions = [
        (-120, 80), (-100, 60), (-80, 40), (-150, 20), (-70, 0),
        (110, 70), (130, 45), (90, 25), (140, 5), (100, -15),
        (-30, 90), (30, 85), (-10, 70), (20, 55), (0, 40),
    ]
    
    for x, y in fall_positions:
        pen.goto(x, y)
        pen.color(colors["leaves_fall"])
        pen.begin_fill()
        pen.circle(5)
        pen.end_fill()

def draw_flowers():
    """Draw flowers on the tree"""
    flower_positions = [
        (-85, 145), (85, 145), (-55, 155), (55, 155),
        (-35, 180), (35, 180), (0, 195), (-15, 190), (15, 190),
        (-100, 135), (100, 135), (-70, 130), (70, 130),
    ]
    
    for x, y in flower_positions:
        # Draw flower petals
        pen.penup()
        pen.goto(x, y)
        pen.color(colors["flowers"])
        
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            px = x + 6 * math.cos(rad)
            py = y + 6 * math.sin(rad)
            pen.goto(px, py)
            pen.pendown()
            pen.dot(4)
            pen.penup()
        
        # Flower center
        pen.goto(x, y)
        pen.dot(5, "#FFD700")
    
    pen.penup()

def draw_shadow():
    """Draw tree shadow on the ground"""
    pen.penup()
    pen.goto(-60, -250)
    pen.pendown()
    pen.color(colors["shadow"])
    pen.begin_fill()
    pen.setheading(0)
    pen.circle(80, 180)
    pen.goto(60, -250)
    pen.goto(-60, -250)
    pen.end_fill()
    pen.penup()

def draw_roots():
    """Draw roots extending from the trunk base"""
    pen.penup()
    pen.goto(-30, -250)
    pen.pendown()
    pen.color(colors["roots"])
    pen.pensize(8)
    pen.setheading(220)
    pen.forward(40)
    pen.pensize(5)
    pen.forward(25)
    
    pen.penup()
    pen.goto(30, -250)
    pen.pendown()
    pen.pensize(8)
    pen.setheading(-40)
    pen.forward(40)
    pen.pensize(5)
    pen.forward(25)
    
    pen.penup()
    pen.goto(-10, -255)
    pen.pendown()
    pen.pensize(6)
    pen.setheading(180)
    pen.forward(35)
    
    pen.penup()
    pen.goto(10, -255)
    pen.pendown()
    pen.pensize(6)
    pen.setheading(0)
    pen.forward(35)
    
    pen.penup()

def draw_birds():
    """Draw birds in the sky"""
    pen.color("#333333")
    pen.pensize(2)
    
    bird_positions = [(-300, 200), (-250, 180), (-200, 220), (250, 190), (300, 170)]
    
    for x, y in bird_positions:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.setheading(-30)
        pen.circle(10, 60)
        pen.setheading(30)
        pen.circle(10, 60)
        pen.penup()

def draw_clouds():
    """Draw decorative clouds"""
    clouds = [(-350, 250, 0.8), (0, 270, 1.0), (300, 230, 0.7), (150, 290, 0.6)]
    
    for x, y, size in clouds:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color("white")
        pen.begin_fill()
        pen.circle(30 * size)
        pen.circle(40 * size)
        pen.penup()
        pen.goto(x + 35 * size, y - 10 * size)
        pen.pendown()
        pen.circle(35 * size)
        pen.penup()
        pen.goto(x - 35 * size, y - 10 * size)
        pen.pendown()
        pen.circle(35 * size)
        pen.penup()
        pen.goto(x + 70 * size, y - 5 * size)
        pen.pendown()
        pen.circle(25 * size)
        pen.penup()
        pen.goto(x - 70 * size, y - 5 * size)
        pen.pendown()
        pen.circle(25 * size)
        pen.end_fill()
    
    pen.penup()

def draw_sun():
    """Draw a sun in the corner"""
    pen.penup()
    pen.goto(350, 280)
    pen.pendown()
    pen.color("#FFD700")
    pen.begin_fill()
    pen.circle(40)
    pen.end_fill()
    
    # Sun rays
    for angle in range(0, 360, 30):
        rad = math.radians(angle)
        x1 = 350 + 50 * math.cos(rad)
        y1 = 280 + 50 * math.sin(rad)
        x2 = 350 + 70 * math.cos(rad)
        y2 = 280 + 70 * math.sin(rad)
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.pensize(2)
        pen.goto(x2, y2)
    
    pen.penup()

def draw_title():
    """Draw title text"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("#2C3E50")
    title.penup()
    title.hideturtle()
    title.goto(0, 370)
    title.write("🌳 TREE WITH BRANCHES (NON-FRACTAL) 🌳", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("#2C3E50")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -390)
    instructions.write("Press R to redraw | ESC to exit", align="center", font=("Arial", 10, "normal"))

def draw_tree():
    """Draw the complete tree"""
    pen.clear()
    
    # Background elements
    draw_sun()
    draw_clouds()
    draw_birds()
    
    # Ground
    draw_ground()
    
    # Shadow
    draw_shadow()
    
    # Roots
    draw_roots()
    
    # Trunk and branches
    draw_trunk()
    draw_branches()
    
    # Leaves and decorations
    draw_leaves()
    draw_flowers()
    draw_fall_leaves()
    
    screen.update()

# Keyboard bindings
screen.listen()
screen.onkey(draw_tree, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()
draw_tree()

print("=" * 60)
print("        TREE WITH BRANCHES (NON-FRACTAL)")
print("=" * 60)
print()
print("A detailed tree created with manual positioning - no recursion!")
print()
print("TREE COMPONENTS:")
print("  🌳 Trunk (tapered shape with texture)")
print("  🌿 8 main branches with sub-branches")
print("  🍃 Leaf clusters (overlapping circles)")
print("  🌸 Flowers scattered throughout")
print("  🍂 Falling autumn leaves")
print("  🌱 Roots extending from base")
print("  ⬛ Ground shadow for depth")
print()
print("BACKGROUND:")
print("  ☀️ Sun with rays")
print("  ☁️ Floating clouds")
print("  🐦 Birds in the sky")
print("  🟢 Grassy ground with texture")
print()
print("CONTROLS:")
print("  R - Redraw the tree")
print("  ESC - Exit program")
print()
print("Unlike fractal trees, this one uses carefully placed branches")

screen.mainloop()