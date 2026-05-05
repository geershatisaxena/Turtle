import turtle
import math
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Circular Progress Bar Animation")
screen.bgcolor("black")
screen.setup(width=900, height=900)
screen.tracer(0)

# Create turtles
progress_turtle = turtle.Turtle()
progress_turtle.speed(0)
progress_turtle.penup()
progress_turtle.hideturtle()

background_turtle = turtle.Turtle()
background_turtle.speed(0)
background_turtle.penup()
background_turtle.hideturtle()

text_turtle = turtle.Turtle()
text_turtle.speed(0)
text_turtle.penup()
text_turtle.hideturtle()

# Progress bar settings
radius = 200
progress = 0
target_progress = 100
animation_speed = 1
bar_width = 20
current_style = 1

# Color schemes
color_schemes = {
    "rainbow": ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"],
    "sunset": ["#FF6B35", "#F7931E", "#FDC830", "#F37335", "#DC2430", "#8E2DE2"],
    "ocean": ["#00B4DB", "#0083B0", "#00C9FF", "#92FE9D", "#00B4DB", "#00A8C5"],
    "neon": ["#FF0066", "#00FFCC", "#FFCC00", "#9900FF", "#00FF66", "#FF3300"],
    "mono": ["#FFFFFF", "#CCCCCC", "#999999", "#666666", "#333333", "#000000"],
    "fire": ["#FF0000", "#FF4500", "#FF6600", "#FF8C00", "#FFA500", "#FFD700"]
}
current_scheme = "rainbow"

def draw_background_circle():
    """Draw the background (empty) circle"""
    background_turtle.clear()
    background_turtle.penup()
    background_turtle.goto(0, -radius)
    background_turtle.pendown()
    background_turtle.color("gray")
    background_turtle.pensize(bar_width)
    background_turtle.circle(radius)
    background_turtle.penup()

def draw_progress_circle(progress_percent):
    """Draw the progress arc based on percentage"""
    progress_turtle.clear()
    
    # Calculate angle for progress (0-100% = 0-360 degrees)
    angle = (progress_percent / 100) * 360
    
    # Set color based on progress
    colors = color_schemes[current_scheme]
    if progress_percent < 25:
        color = colors[0]
    elif progress_percent < 50:
        color = colors[1]
    elif progress_percent < 75:
        color = colors[2]
    else:
        color = colors[3]
    
    progress_turtle.penup()
    progress_turtle.goto(0, -radius)
    progress_turtle.setheading(0)
    progress_turtle.pendown()
    progress_turtle.color(color)
    progress_turtle.pensize(bar_width)
    progress_turtle.circle(radius, angle)
    progress_turtle.penup()

def draw_gradient_progress(progress_percent):
    """Draw progress arc with gradient color effect"""
    progress_turtle.clear()
    
    angle = (progress_percent / 100) * 360
    colors = color_schemes[current_scheme]
    
    # Draw progress in segments with different colors
    segments = 20
    segment_angle = angle / segments
    
    for i in range(int(segments)):
        start_angle = i * segment_angle
        color_index = int(i / segments * len(colors))
        color = colors[min(color_index, len(colors) - 1)]
        
        progress_turtle.penup()
        progress_turtle.goto(0, -radius)
        progress_turtle.setheading(0)
        progress_turtle.pendown()
        progress_turtle.color(color)
        progress_turtle.pensize(bar_width)
        progress_turtle.circle(radius, segment_angle)
    
    progress_turtle.penup()

def draw_multi_color_progress(progress_percent):
    """Draw progress with multiple color bands"""
    progress_turtle.clear()
    
    angle = (progress_percent / 100) * 360
    colors = color_schemes[current_scheme]
    
    # Draw rainbow effect
    for i in range(int(angle)):
        color = colors[i % len(colors)]
        progress_turtle.penup()
        progress_turtle.goto(0, -radius)
        progress_turtle.setheading(i)
        progress_turtle.pendown()
        progress_turtle.color(color)
        progress_turtle.pensize(bar_width - 2)
        progress_turtle.circle(radius, 1)
    
    progress_turtle.penup()

def draw_thick_progress(progress_percent):
    """Draw thick circular progress with inner glow"""
    progress_turtle.clear()
    
    angle = (progress_percent / 100) * 360
    colors = color_schemes[current_scheme]
    color = colors[min(int(progress_percent / 100 * len(colors)), len(colors) - 1)]
    
    # Outer thick ring
    progress_turtle.penup()
    progress_turtle.goto(0, -radius - 5)
    progress_turtle.setheading(0)
    progress_turtle.pendown()
    progress_turtle.color(color)
    progress_turtle.pensize(bar_width + 8)
    progress_turtle.circle(radius + 5, angle)
    
    # Inner thin ring
    progress_turtle.penup()
    progress_turtle.goto(0, -radius)
    progress_turtle.setheading(0)
    progress_turtle.pendown()
    progress_turtle.color("white")
    progress_turtle.pensize(bar_width)
    progress_turtle.circle(radius, angle)
    
    progress_turtle.penup()

def draw_dashed_progress(progress_percent):
    """Draw progress with dashed line effect"""
    progress_turtle.clear()
    
    angle = (progress_percent / 100) * 360
    colors = color_schemes[current_scheme]
    dash_length = 5
    
    for i in range(0, int(angle), dash_length * 2):
        color = colors[(i // dash_length) % len(colors)]
        progress_turtle.penup()
        progress_turtle.goto(0, -radius)
        progress_turtle.setheading(i)
        progress_turtle.pendown()
        progress_turtle.color(color)
        progress_turtle.pensize(bar_width)
        progress_turtle.circle(radius, dash_length)
    
    progress_turtle.penup()

def draw_progress_text(progress_percent):
    """Draw percentage text in center"""
    text_turtle.clear()
    text_turtle.penup()
    text_turtle.goto(0, -30)
    text_turtle.color("white")
    text_turtle.write(f"{int(progress_percent)}%", align="center", font=("Arial", 48, "bold"))
    
    # Draw status text
    if progress_percent >= 100:
        status = "COMPLETE!"
        status_color = "lime"
    else:
        status = "LOADING..."
        status_color = "yellow"
    
    text_turtle.goto(0, 60)
    text_turtle.color(status_color)
    text_turtle.write(status, align="center", font=("Arial", 16, "normal"))

def draw_end_effects():
    """Draw completion effects when progress reaches 100%"""
    if progress >= 100:
        # Draw celebration particles
        for i in range(36):
            angle = i * 10
            x = (radius + 30) * math.cos(math.radians(angle))
            y = (radius + 30) * math.sin(math.radians(angle))
            particle = turtle.Turtle()
            particle.speed(0)
            particle.shape("circle")
            particle.color(color_schemes[current_scheme][i % len(color_schemes[current_scheme])])
            particle.shapesize(0.3)
            particle.penup()
            particle.goto(x, y)
            screen.update()
            time.sleep(0.02)
            particle.hideturtle()

def update_progress():
    """Main animation loop"""
    global progress
    
    while True:
        # Clear previous drawing
        draw_background_circle()
        
        # Draw progress based on selected style
        if current_style == 1:
            draw_progress_circle(progress)
        elif current_style == 2:
            draw_gradient_progress(progress)
        elif current_style == 3:
            draw_multi_color_progress(progress)
        elif current_style == 4:
            draw_thick_progress(progress)
        elif current_style == 5:
            draw_dashed_progress(progress)
        
        # Draw percentage text
        draw_progress_text(progress)
        
        # Update screen
        screen.update()
        
        # Update progress (continue cycling or stop at 100)
        progress += animation_speed
        
        if progress >= 100:
            draw_end_effects()
            progress = 0  # Reset for continuous animation
            time.sleep(1)
        
        time.sleep(0.02)

# UI Elements
def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 430)
    title.write("🔄 CIRCULAR PROGRESS BAR ANIMATION 🔄", align="center", font=("Arial", 16, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("gray")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -440)
    instructions.write("1-5:Style  C:Color  +/ -:Speed  R:Reset  S:Single Cycle  ESC:Exit", 
                       align="center", font=("Arial", 10, "normal"))

def draw_inner_circles():
    """Draw decorative inner circles"""
    decor = turtle.Turtle()
    decor.speed(0)
    decor.penup()
    decor.hideturtle()
    
    # Inner ring
    decor.goto(0, -radius + 30)
    decor.pendown()
    decor.color("dimgray")
    decor.pensize(1)
    decor.circle(radius - 30)
    decor.penup()
    
    # Center dot
    decor.goto(0, 0)
    decor.dot(10, "white")

def change_style_1(): global current_style; current_style = 1
def change_style_2(): global current_style; current_style = 2
def change_style_3(): global current_style; current_style = 3
def change_style_4(): global current_style; current_style = 4
def change_style_5(): global current_style; current_style = 5

def change_color_scheme():
    global current_scheme
    schemes = list(color_schemes.keys())
    idx = schemes.index(current_scheme)
    current_scheme = schemes[(idx + 1) % len(schemes)]

def increase_speed():
    global animation_speed
    animation_speed = min(animation_speed + 0.5, 8)

def decrease_speed():
    global animation_speed
    animation_speed = max(animation_speed - 0.5, 0.5)

def reset_progress():
    global progress
    progress = 0

def single_cycle():
    """Run one complete cycle from 0 to 100%"""
    global progress
    while progress < 100:
        progress += animation_speed
        draw_background_circle()
        
        if current_style == 1:
            draw_progress_circle(progress)
        elif current_style == 2:
            draw_gradient_progress(progress)
        elif current_style == 3:
            draw_multi_color_progress(progress)
        elif current_style == 4:
            draw_thick_progress(progress)
        elif current_style == 5:
            draw_dashed_progress(progress)
        
        draw_progress_text(progress)
        screen.update()
        time.sleep(0.02)
    
    draw_end_effects()
    time.sleep(1)
    progress = 0

# Keyboard bindings
screen.listen()
screen.onkey(change_style_1, "1")
screen.onkey(change_style_2, "2")
screen.onkey(change_style_3, "3")
screen.onkey(change_style_4, "4")
screen.onkey(change_style_5, "5")
screen.onkey(change_color_scheme, "c")
screen.onkey(increase_speed, "plus")
screen.onkey(increase_speed, "equal")
screen.onkey(decrease_speed, "minus")
screen.onkey(reset_progress, "r")
screen.onkey(single_cycle, "s")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()
draw_inner_circles()
draw_background_circle()

print("=" * 60)
print("        CIRCULAR PROGRESS BAR ANIMATION")
print("=" * 60)
print()
print("Beautiful animated circular progress indicators!")
print()
print("STYLES (Press 1-5):")
print("  1 - Solid: Classic single-color progress arc")
print("  2 - Gradient: Smooth color transition")
print("  3 - Rainbow: Multi-color band effect")
print("  4 - Thick: Double-ring with glow effect")
print("  5 - Dashed: Dashed line progress")
print()
print("COLOR SCHEMES (Press C):")
print("  • Rainbow   • Sunset    • Ocean")
print("  • Neon      • Mono      • Fire")
print()
print("CONTROLS:")
print("  1-5   - Change progress bar style")
print("  C     - Change color scheme")
print("  +/-   - Adjust animation speed")
print("  R     - Reset to 0%")
print("  S     - Run single cycle (0% → 100%)")
print("  ESC   - Exit")
print()
print("Watch the circular progress fill up smoothly!")

# Start animation
try:
    update_progress()
except KeyboardInterrupt:
    screen.bye()
except turtle.Terminator:
    pass

screen.mainloop()