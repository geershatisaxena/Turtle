import turtle
import math

# Setup
screen = turtle.Screen()
screen.bgcolor("#1a1a2e")
screen.title("Yin-Yang Symbol")
screen.tracer(0)

# Create turtles
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Drawing turtle for labels
label_t = turtle.Turtle()
label_t.speed(0)
label_t.hideturtle()
label_t.penup()

def draw_circle(x, y, radius, color, outline_color=None, outline_width=0):
    """Draw a filled circle"""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    
    if outline_color:
        t.color(outline_color)
        t.pensize(outline_width)
    else:
        t.color(color)
    
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.pensize(1)

def draw_semicircle(x, y, radius, color, start_angle, end_angle):
    """Draw a filled semicircle"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    
    # Draw arc
    t.setheading(start_angle)
    t.circle(radius, end_angle - start_angle)
    
    # Close the shape
    t.goto(x, y)
    t.end_fill()

def draw_yin_yang(x, y, radius, colors):
    """Draw a yin-yang symbol at given position"""
    
    # Save current position
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Colors
    color1, color2 = colors
    
    # === Draw outer circle ===
    draw_circle(x, y, radius, color1, "white", 2)
    
    # === Draw the two halves ===
    # Right half (color2) - from 90° to -90°
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color2)
    t.begin_fill()
    t.setheading(90)
    t.circle(radius, 180)  # Draw semicircle from top to bottom
    t.end_fill()
    
    # Left half is already color1 from the base circle
    
    # === Draw top small circle (color2) ===
    small_radius = radius / 2
    draw_circle(x, y + small_radius, small_radius, color2, "white", 1)
    
    # === Draw bottom small circle (color1) ===
    draw_circle(x, y - small_radius, small_radius, color1, "white", 1)
    
    # === Draw tiny circles (the "eyes") ===
    tiny_radius = radius / 6
    draw_circle(x, y + small_radius, tiny_radius, color1, "white", 1)
    draw_circle(x, y - small_radius, tiny_radius, color2, "white", 1)
    
    # === Draw the S-curve line ===
    t.penup()
    t.goto(x, y + radius)
    t.pendown()
    t.color("white")
    t.pensize(2)
    t.setheading(270)
    
    # Draw S-curve
    for angle in range(0, 181, 2):
        rad = math.radians(angle)
        # Parametric equation for the S-curve
        cx = x + radius * math.sin(rad) * math.cos(rad)
        cy = y - radius * math.cos(rad)
        t.goto(cx, cy)
        screen.update()
    
    t.pensize(1)

def draw_yin_yang_animated(x, y, radius, colors, rotation=0):
    """Draw yin-yang with animation effect"""
    
    color1, color2 = colors
    
    # Draw outer circle with animation
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color1, color1)
    t.begin_fill()
    
    # Animate outer circle
    for angle in range(0, 361, 5):
        rad = math.radians(angle + rotation)
        cx = x + radius * math.cos(rad)
        cy = y + radius * math.sin(rad)
        t.goto(cx, cy)
        screen.update()
        time.sleep(0.001)
    t.end_fill()
    
    # Draw second half with animation
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color2, color2)
    t.begin_fill()
    t.setheading(90 + rotation)
    
    for angle in range(0, 181, 2):
        t.circle(radius, 2)
        screen.update()
        time.sleep(0.001)
    t.end_fill()
    
    # Draw top small circle
    small_radius = radius / 2
    draw_circle_animated(x, y + small_radius, small_radius, color2, rotation)
    
    # Draw bottom small circle
    draw_circle_animated(x, y - small_radius, small_radius, color1, rotation)
    
    # Draw tiny circles
    tiny_radius = radius / 6
    draw_circle_animated(x, y + small_radius, tiny_radius, color1, rotation)
    draw_circle_animated(x, y - small_radius, tiny_radius, color2, rotation)

def draw_circle_animated(x, y, radius, color, rotation=0):
    """Draw a circle with animation"""
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.fillcolor(color)
    t.color(color)
    t.begin_fill()
    
    for angle in range(0, 361, 3):
        rad = math.radians(angle + rotation)
        cx = x + radius * math.cos(rad)
        cy = y + radius * math.sin(rad)
        t.goto(cx, cy)
        screen.update()
        time.sleep(0.001)
    t.end_fill()

def draw_rotating_yin_yang():
    """Draw multiple yin-yang symbols with different styles"""
    
    # Title
    label_t.goto(0, 350)
    label_t.color("#FFD700")
    label_t.write("☯ YIN-YANG SYMBOL ☯", font=('Arial', 28, 'bold'), align="center")
    screen.update()
    
    # === Main Yin-Yang (Center) ===
    label_t.goto(0, 310)
    label_t.color("#87CEEB")
    label_t.write("Classic Yin-Yang", font=('Arial', 14), align="center")
    screen.update()
    
    draw_yin_yang(0, 100, 150, ("white", "black"))
    
    # === Yin-Yang with colors (Left) ===
    label_t.goto(-280, 310)
    label_t.color("#FF6B6B")
    label_t.write("Fire & Water", font=('Arial', 12), align="center")
    screen.update()
    
    draw_yin_yang(-280, 100, 80, ("#FF6B6B", "#4ECDC4"))
    
    # === Yin-Yang with colors (Right) ===
    label_t.goto(280, 310)
    label_t.color("#FFD93D")
    label_t.write("Sun & Moon", font=('Arial', 12), align="center")
    screen.update()
    
    draw_yin_yang(280, 100, 80, ("#FFD93D", "#6C5CE7"))
    
    # === Small Yin-Yang (Bottom Left) ===
    label_t.goto(-280, -100)
    label_t.color("#A8E6CF")
    label_t.write("Earth & Sky", font=('Arial', 12), align="center")
    screen.update()
    
    draw_yin_yang(-280, -200, 60, ("#A8E6CF", "#355C7D"))
    
    # === Small Yin-Yang (Bottom Right) ===
    label_t.goto(280, -100)
    label_t.color("#F8B195")
    label_t.write("Day & Night", font=('Arial', 12), align="center")
    screen.update()
    
    draw_yin_yang(280, -200, 60, ("#F8B195", "#355C7D"))
    
    # === Draw decorative elements ===
    draw_decorative_border()
    
    # === Draw the philosophy text ===
    label_t.goto(0, -310)
    label_t.color("#95a5a6")
    label_t.write("☯ Balance • Harmony • Unity ☯", font=('Arial', 16), align="center")
    screen.update()

def draw_decorative_border():
    """Draw a decorative border around the symbol"""
    t.penup()
    t.goto(-400, -350)
    t.pendown()
    t.color("#FFD700")
    t.pensize(1)
    
    # Draw an ornate border
    for i in range(4):
        t.forward(800)
        t.left(90)
    
    # Decorative corners
    for x, y in [(-400, -350), (-400, 350), (400, 350), (400, -350)]:
        t.penup()
        t.goto(x, y)
        t.pendown()
        for _ in range(4):
            t.forward(20)
            t.backward(20)
            t.left(90)

def draw_philosophical_yin_yang():
    """Draw a yin-yang with philosophical elements"""
    
    # Draw a larger yin-yang with calligraphy
    t.penup()
    t.goto(0, -250)
    t.pendown()
    
    # Draw the great yin-yang with gradient effect
    draw_yin_yang(0, -100, 180, ("#F0F0F0", "#1A1A1A"))
    
    # Add eight trigrams around it (Bagua)
    trigrams = ["☰", "☱", "☲", "☳", "☴", "☵", "☶", "☷"]
    angles = [0, 45, 90, 135, 180, 225, 270, 315]
    radius = 230
    
    label_t.goto(0, 100)
    label_t.color("#FFD700")
    label_t.write("☯ The Tao of Balance ☯", font=('Arial', 20, 'bold'), align="center")
    screen.update()
    
    for i, angle in enumerate(angles):
        rad = math.radians(angle)
        x = radius * math.cos(rad)
        y = radius * math.sin(rad) - 100
        
        label_t.goto(x, y)
        label_t.color("#FF6B6B")
        label_t.write(trigrams[i], font=('Arial', 18), align="center")
        screen.update()

# Main execution
import time

print("Drawing Yin-Yang Symbol...")

# Draw the main composition
draw_rotating_yin_yang()

# Draw the philosophical version
draw_philosophical_yin_yang()

# Add interactive note
label_t.goto(0, -380)
label_t.color("#95a5a6")
label_t.write("🖱️ Click anywhere to exit", font=('Arial', 12), align="center")
screen.update()

# Keep window open
screen.mainloop()