import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Koch Snowflake Fractal")
screen.bgcolor("darkblue")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Create the drawing turtle
snowflake = turtle.Turtle()
snowflake.speed(0)
snowflake.penup()
snowflake.goto(-300, 200)
snowflake.pendown()
snowflake.hideturtle()

# Color settings
colors = ["white", "cyan", "lightblue", "skyblue", "deepskyblue", "lightcyan", "yellow", "pink"]
current_color_index = 0

# UI elements
info_display = turtle.Turtle()
info_display.speed(0)
info_display.color("white")
info_display.penup()
info_display.hideturtle()

def koch_curve(length, depth):
    """
    Draw a Koch curve recursively
    
    The Koch curve is formed by replacing each line segment
    with 4 segments, each 1/3 the length of the original.
    """
    if depth == 0:
        snowflake.forward(length)
    else:
        # Recursive pattern: _/\_
        koch_curve(length / 3, depth - 1)
        snowflake.left(60)
        koch_curve(length / 3, depth - 1)
        snowflake.right(120)
        koch_curve(length / 3, depth - 1)
        snowflake.left(60)
        koch_curve(length / 3, depth - 1)

def koch_snowflake(side_length, depth):
    """Draw a complete Koch snowflake (3 Koch curves)"""
    for _ in range(3):
        koch_curve(side_length, depth)
        snowflake.right(120)

def draw_colored_snowflake(side_length, depth):
    """Draw snowflake with color progression"""
    global current_color_index
    
    for i in range(3):
        snowflake.color(colors[current_color_index % len(colors)])
        koch_curve(side_length, depth)
        snowflake.right(120)
        current_color_index += 1

def draw_koch_antisnowflake(side_length, depth):
    """Draw an anti-snowflake (inverted spikes)"""
    for _ in range(3):
        koch_antisnowflake_side(side_length, depth)
        snowflake.right(120)

def koch_antisnowflake_side(length, depth):
    """Recursive function for anti-snowflake (inward spikes)"""
    if depth == 0:
        snowflake.forward(length)
    else:
        koch_antisnowflake_side(length / 3, depth - 1)
        snowflake.right(60)
        koch_antisnowflake_side(length / 3, depth - 1)
        snowflake.left(120)
        koch_antisnowflake_side(length / 3, depth - 1)
        snowflake.right(60)
        koch_antisnowflake_side(length / 3, depth - 1)

def draw_pattern():
    """Draw a pattern of multiple snowflakes"""
    snowflake.clear()
    snowflake.penup()
    
    # Draw 3 smaller snowflakes in a triangle pattern
    positions = [(-200, 150), (200, 150), (0, -150)]
    pattern_colors = ["cyan", "skyblue", "lightblue"]
    
    for i, (x, y) in enumerate(positions):
        snowflake.goto(x, y)
        snowflake.pendown()
        snowflake.color(pattern_colors[i])
        for _ in range(3):
            koch_curve(150, 3)
            snowflake.right(120)
        snowflake.penup()
    
    screen.update()

def draw_mandala():
    """Draw a snowflake mandala (6 snowflakes in a circle)"""
    snowflake.clear()
    snowflake.penup()
    snowflake.goto(0, 0)
    snowflake.color("white")
    
    for angle in range(0, 360, 60):
        snowflake.setheading(angle)
        snowflake.forward(200)
        snowflake.pendown()
        snowflake.setheading(angle - 60)
        
        for _ in range(3):
            koch_curve(80, 3)
            snowflake.right(120)
        
        snowflake.penup()
        snowflake.goto(0, 0)
    
    snowflake.penup()
    screen.update()
    info_display.goto(0, 300)
    info_display.write("Snowflake Mandala", align="center", font=("Arial", 14, "bold"))
    screen.ontimer(lambda: info_display.clear(), 2000)

def clear_and_reset():
    """Clear screen and reset for new drawing"""
    snowflake.clear()
    snowflake.penup()
    snowflake.goto(-300, 200)
    snowflake.setheading(0)
    snowflake.pendown()
    snowflake.color("white")
    screen.update()
    update_info()

def change_color():
    """Cycle through snowflake colors"""
    global current_color_index
    current_color_index += 1
    snowflake.color(colors[current_color_index % len(colors)])
    update_info()

def increase_depth():
    """Increase recursion depth (more detail)"""
    global current_depth, side_length
    if current_depth < 5:
        current_depth += 1
        clear_and_reset()
        draw_colored_snowflake(side_length, current_depth)
        update_info()

def decrease_depth():
    """Decrease recursion depth (less detail)"""
    global current_depth, side_length
    if current_depth > 0:
        current_depth -= 1
        clear_and_reset()
        draw_colored_snowflake(side_length, current_depth)
        update_info()

def increase_size():
    """Increase snowflake size"""
    global side_length
    if side_length < 500:
        side_length += 40
        clear_and_reset()
        snowflake.goto(-side_length//2, side_length//3)
        draw_colored_snowflake(side_length, current_depth)
        update_info()

def decrease_size():
    """Decrease snowflake size"""
    global side_length
    if side_length > 100:
        side_length -= 40
        clear_and_reset()
        snowflake.goto(-side_length//2, side_length//3)
        draw_colored_snowflake(side_length, current_depth)
        update_info()

def update_info():
    """Update on-screen information"""
    info_display.clear()
    info_display.goto(-450, 350)
    info_display.write(f"Koch Snowflake - Depth: {current_depth} | Size: {side_length}px | Color: {snowflake.color()[0]}",
                       font=("Arial", 10, "normal"))
    info_display.goto(-450, 330)
    info_display.write("Controls: +/- Depth | [/] Size | C: Color | 1:Normal 2:Anti 3:Pattern 4:Mandala | R:Reset | SPACE:Redraw",
                       font=("Arial", 10, "normal"))

def draw_background():
    """Draw decorative background"""
    bg = turtle.Turtle()
    bg.speed(0)
    bg.penup()
    bg.goto(-500, -400)
    bg.pendown()
    bg.color("midnightblue")
    bg.begin_fill()
    for _ in range(2):
        bg.forward(1000)
        bg.right(90)
        bg.forward(800)
        bg.right(90)
    bg.end_fill()
    
    # Draw stars
    bg.color("white")
    for _ in range(80):
        x = random.randint(-450, 450)
        y = random.randint(-350, 350)
        bg.penup()
        bg.goto(x, y)
        bg.dot(random.randint(1, 3))
    
    bg.hideturtle()

# Global variables
current_depth = 3
side_length = 400

# Draw background
draw_background()

# Draw initial snowflake
snowflake.goto(-side_length//2, side_length//3)
draw_colored_snowflake(side_length, current_depth)
update_info()

# Keyboard bindings
screen.listen()
screen.onkey(increase_depth, "plus")
screen.onkey(increase_depth, "equal")
screen.onkey(decrease_depth, "minus")
screen.onkey(increase_size, "bracketright")
screen.onkey(decrease_size, "bracketleft")
screen.onkey(change_color, "c")
screen.onkey(lambda: [clear_and_reset(), draw_colored_snowflake(side_length, current_depth)], "space")
screen.onkey(lambda: [clear_and_reset(), draw_koch_antisnowflake(side_length, current_depth)], "2")
screen.onkey(lambda: [draw_pattern()], "3")
screen.onkey(lambda: [draw_mandala()], "4")
screen.onkey(lambda: [clear_and_reset(), draw_colored_snowflake(side_length, current_depth)], "1")
screen.onkey(clear_and_reset, "r")
screen.onkey(lambda: screen.bye(), "Escape")

# Print console instructions
print("=== KOCH SNOWFLAKE FRACTAL ===")
print()
print("The Koch snowflake is one of the earliest fractals described mathematically.")
print("It has an infinite perimeter but finite area!")
print()
print("CONTROLS:")
print("  + / -     - Increase/Decrease recursion depth (0-5)")
print("  [ / ]     - Decrease/Increase snowflake size")
print("  C         - Cycle through colors")
print("  1         - Draw normal snowflake")
print("  2         - Draw anti-snowflake (inward spikes)")
print("  3         - Draw pattern of 3 snowflakes")
print("  4         - Draw snowflake mandala (6 snowflakes)")
print("  R         - Reset to default")
print("  SPACE     - Redraw current snowflake")
print("  ESC       - Exit program")
print()
print("Mathematical fact: At depth infinity, the Koch snowflake")
print("has infinite perimeter but finite area!")

# Keep window open
screen.mainloop()