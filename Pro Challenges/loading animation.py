import turtle
import math
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Loading Animation - Rotating Arcs")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the loading turtle
loader = turtle.Turtle()
loader.speed(0)
loader.penup()
loader.hideturtle()

# Create text display
text_display = turtle.Turtle()
text_display.speed(0)
text_display.color("white")
text_display.penup()
text_display.hideturtle()

# Animation variables
angle = 0
radius = 80
arc_length = 90
loading_text = "LOADING"
dot_count = 0
style = "spinner"  # spinner, circular, double, multi

def draw_spinner(x, y, radius, angle, color):
    """Draw a single rotating arc (spinner style)"""
    loader.penup()
    loader.goto(x, y)
    loader.pendown()
    loader.color(color)
    loader.setheading(angle)
    loader.pensize(8)
    
    # Draw arc
    loader.circle(radius, arc_length)
    loader.penup()

def draw_circular_progress(x, y, radius, percentage, color):
    """Draw a circular progress indicator"""
    loader.penup()
    loader.goto(x, y - radius)
    loader.pendown()
    loader.color(color)
    loader.pensize(12)
    loader.setheading(0)
    
    # Draw full circle outline (dim)
    loader.pencolor("gray")
    loader.circle(radius)
    
    # Draw progress arc
    loader.pencolor(color)
    loader.penup()
    loader.goto(x, y - radius)
    loader.pendown()
    loader.setheading(0)
    loader.circle(radius, 360 * percentage / 100)
    loader.penup()

def draw_double_spinner(x, y, radius, angle1, angle2, color1, color2):
    """Draw two counter-rotating spinners"""
    draw_spinner(x - 40, y, radius, angle1, color1)
    draw_spinner(x + 40, y, radius, -angle2, color2)

def draw_multi_spinner(x, y, radius, base_angle, count=4):
    """Draw multiple spinners in a circle"""
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta"]
    for i in range(count):
        angle_offset = i * (360 / count)
        spinner_angle = base_angle + angle_offset
        loader.penup()
        loader.goto(x + math.cos(math.radians(angle_offset)) * (radius + 30),
                    y + math.sin(math.radians(angle_offset)) * (radius + 30))
        loader.pendown()
        loader.color(colors[i % len(colors)])
        loader.setheading(spinner_angle)
        loader.pensize(5)
        loader.circle(radius // 2, arc_length)
        loader.penup()

def draw_dots_loading(x, y, text, dot_count):
    """Draw loading text with animated dots"""
    text_display.clear()
    
    # Draw main text
    text_display.goto(x, y)
    text_display.color("cyan")
    text_display.write(text, align="center", font=("Arial", 24, "bold"))
    
    # Draw animated dots
    dots = "." * (dot_count % 4)
    text_display.goto(x + 100, y)
    text_display.color("yellow")
    text_display.write(dots, align="center", font=("Arial", 24, "bold"))

def draw_percentage(x, y, percentage):
    """Draw percentage text"""
    text_display.goto(x, y - 60)
    text_display.color("lime")
    text_display.write(f"{percentage}%", align="center", font=("Arial", 18, "bold"))

def draw_pulse_circle(x, y, radius, pulse_scale):
    """Draw a pulsing circle effect"""
    loader.penup()
    loader.goto(x, y - radius * pulse_scale)
    loader.pendown()
    alpha = int(255 * (1 - pulse_scale / 2))
    loader.color(f"#{alpha:02x}{100:02x}{255:02x}")
    loader.pensize(3)
    loader.circle(radius * pulse_scale)
    loader.penup()

def update_loading_text(style_name):
    """Update the style name display"""
    style_text = turtle.Turtle()
    style_text.speed(0)
    style_text.color("gray")
    style_text.penup()
    style_text.hideturtle()
    style_text.goto(0, -250)
    style_text.clear()
    style_text.write(f"Style: {style_name.upper()}", align="center", font=("Arial", 12, "normal"))
    style_text.goto(0, -280)
    style_text.write("Press 1-5 to change style | ESC to exit", align="center", font=("Arial", 10, "normal"))

def animate():
    """Main animation loop"""
    global angle, dot_count, style, loading_text, arc_length
    
    frame = 0
    percentage = 0
    pulse_scale = 1
    pulse_direction = 1
    
    while True:
        # Clear previous drawings
        loader.clear()
        text_display.clear()
        
        # Update animation variables
        angle += 8
        dot_count += 1
        frame += 1
        
        # Simulate loading progress (cycles 0-100)
        percentage = (frame // 3) % 101
        
        # Pulse effect for some styles
        pulse_scale += 0.03 * pulse_direction
        if pulse_scale >= 1.3:
            pulse_direction = -1
        elif pulse_scale <= 0.7:
            pulse_direction = 1
        
        # Draw based on selected style
        if style == "spinner":
            draw_spinner(0, 0, radius, angle, "cyan")
            draw_spinner(0, 0, radius, angle + 180, "blue")
            draw_dots_loading(0, 120, "LOADING", dot_count)
            draw_percentage(0, 0, percentage)
            
        elif style == "circular":
            draw_circular_progress(0, 0, radius + 20, percentage, "lime")
            draw_dots_loading(0, 120, "LOADING", dot_count)
            draw_percentage(0, 0, percentage)
            
        elif style == "double":
            draw_double_spinner(0, 0, radius - 20, angle, angle, "magenta", "cyan")
            draw_dots_loading(0, 120, "LOADING", dot_count)
            draw_percentage(0, 0, percentage)
            
        elif style == "multi":
            draw_multi_spinner(0, 0, radius, angle, 6)
            draw_dots_loading(0, 120, "LOADING", dot_count)
            
        elif style == "pulse":
            draw_pulse_circle(0, 0, radius + 20, pulse_scale)
            draw_spinner(0, 0, radius, angle, "white")
            draw_dots_loading(0, 120, "PULSING", dot_count)
            draw_percentage(0, 0, percentage)
        
        # Draw decorative rings
        if style != "circular":
            loader.penup()
            loader.goto(0, -radius - 10)
            loader.pendown()
            loader.color("gray")
            loader.pensize(2)
            loader.circle(radius + 10)
            loader.penup()
        
        # Update style label
        update_loading_text(style)
        
        # Refresh screen
        screen.update()
        time.sleep(0.03)

# Style selection functions
def set_style_spinner():
    global style
    style = "spinner"

def set_style_circular():
    global style
    style = "circular"

def set_style_double():
    global style
    style = "double"

def set_style_multi():
    global style
    style = "multi"

def set_style_pulse():
    global style
    style = "pulse"

# Keyboard bindings
screen.listen()
screen.onkey(set_style_spinner, "1")
screen.onkey(set_style_circular, "2")
screen.onkey(set_style_double, "3")
screen.onkey(set_style_multi, "4")
screen.onkey(set_style_pulse, "5")
screen.onkey(lambda: screen.bye(), "Escape")

# Print instructions
print("=" * 50)
print("     LOADING ANIMATION - ROTATING ARCS")
print("=" * 50)
print()
print("Multiple loading spinner styles with rotating arcs!")
print()
print("STYLES:")
print("  1 - Single Spinner (Classic loading spinner)")
print("  2 - Circular Progress (Progress ring with percentage)")
print("  3 - Double Spinner (Two counter-rotating spinners)")
print("  4 - Multi Spinner (6 spinners in a circle)")
print("  5 - Pulse Spinner (Pulsing ring with spinner)")
print()
print("CONTROLS:")
print("  1-5   - Change loading style")
print("  ESC   - Exit program")
print()
print("Watch the arcs rotate and the percentage increase!")

# Draw title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 220)
title.write("🌀 LOADING ANIMATION 🌀", align="center", font=("Arial", 20, "bold"))
title.goto(0, 190)
title.color("gray")
title.write("Rotating Arcs", align="center", font=("Arial", 12, "normal"))

# Run animation
try:
    animate()
except KeyboardInterrupt:
    screen.bye()
except turtle.Terminator:
    pass

screen.mainloop()