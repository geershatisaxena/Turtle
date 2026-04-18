import turtle
import time
import math

# Setup
turtle.setup(800, 700)
turtle.bgcolor("#87CEEB")
turtle.speed(0)
turtle.tracer(0)

# Colors
rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8F00FF"]

# Settings
radius_start = 250
radius_step = 22
center_x = 0
center_y = 50
arc_angle = 180

# --- Draw rainbow (once, no clearing later) ---
turtle.pensize(radius_step - 5)

for i, color in enumerate(rainbow_colors):
    radius = radius_start - (i * radius_step)
    step_angle = 3
    steps = arc_angle // step_angle
    
    for step in range(steps + 1):
        current_angle = step * step_angle
        angle_rad = math.radians(current_angle)
        x = center_x + radius * math.cos(angle_rad)
        y = center_y + radius * math.sin(angle_rad)
        
        if step == 0:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.color(color)
            turtle.pensize(radius_step - 3)
        else:
            turtle.goto(x, y)
        
        turtle.update()
        time.sleep(0.008)
    
    turtle.penup()

# --- Clouds ---
def draw_cloud(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color("white")
    turtle.begin_fill()
    for dx, dy in [(0, 0), (25, -8), (50, 0), (38, 15), (12, 18)]:
        turtle.penup()
        turtle.goto(x + dx, y + dy)
        turtle.pendown()
        turtle.circle(18)
    turtle.end_fill()

draw_cloud(-280, 250)
draw_cloud(200, 260)
draw_cloud(-80, 280)
draw_cloud(280, 240)

# --- Sun ---
turtle.penup()
turtle.goto(320, 230)
turtle.color("#FFD700")
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

turtle.color("#FFA500")
turtle.pensize(3)
for angle in range(0, 360, 30):
    rad = math.radians(angle)
    x1 = 320 + 40 * math.cos(rad)
    y1 = 230 + 40 * math.sin(rad)
    x2 = 320 + 65 * math.cos(rad)
    y2 = 230 + 65 * math.sin(rad)
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.update()

# --- Pot of gold ---
turtle.penup()
turtle.goto(-60, -20)
turtle.color("#8B4513")
turtle.begin_fill()
turtle.pendown()
for _ in range(2):
    turtle.forward(120)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
turtle.end_fill()

turtle.color("#FFD700")
coin_positions = [(-80, -30), (-60, -35), (-40, -32), (-20, -38), (0, -35), (20, -40)]
for x, y in coin_positions:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()
    turtle.update()

# --- ANIMATED TEXT (without clearing the rainbow) ---
# Create a separate turtle just for text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()
text_turtle.speed(0)

# Animate title growing
for size in range(10, 28, 3):
    text_turtle.clear()  # This only clears text_turtle's drawings, not the main rainbow
    text_turtle.goto(0, -180)
    text_turtle.color("#FF1493")
    text_turtle.write("🌈 RAINBOW MAGIC 🌈", align="center", font=("Arial", size, "bold"))
    turtle.update()
    time.sleep(0.08)

# Final title
text_turtle.goto(0, -180)
text_turtle.write("🌈 RAINBOW MAGIC 🌈", align="center", font=("Arial", 24, "bold"))

# Animate subtitle
for size in range(8, 16, 2):
    text_turtle.clear()
    text_turtle.goto(0, -220)
    text_turtle.color("#4169E1")
    text_turtle.write("Where dreams meet colors", align="center", font=("Arial", size, "italic"))
    turtle.update()
    time.sleep(0.06)

text_turtle.goto(0, -220)
text_turtle.write("Where dreams meet colors", align="center", font=("Arial", 14, "italic"))

# --- Sparkles on rainbow ---
sparkle_turtle = turtle.Turtle()
sparkle_turtle.hideturtle()
sparkle_turtle.penup()
sparkle_turtle.color("white")

sparkle_positions = [(-200, 120), (-120, 170), (-40, 200), (40, 205), (120, 185), (190, 140)]

for x, y in sparkle_positions:
    sparkle_turtle.goto(x, y)
    for size in range(5, 16, 3):
        sparkle_turtle.clear()
        sparkle_turtle.write("✨", align="center", font=("Arial", size, "normal"))
        turtle.update()
        time.sleep(0.05)
    sparkle_turtle.write("✨", align="center", font=("Arial", 14, "normal"))

# --- Stars around title ---
star_turtle = turtle.Turtle()
star_turtle.hideturtle()
star_turtle.penup()
star_turtle.color("#FFD700")

star_positions = [(-300, -170), (-250, -200), (250, -195), (300, -165), (0, -250)]
for x, y in star_positions:
    star_turtle.goto(x, y)
    star_turtle.write("★", align="center", font=("Arial", 16, "normal"))
    turtle.update()
    time.sleep(0.05)

# --- Finish ---
turtle.hideturtle()
turtle.update()
turtle.done()