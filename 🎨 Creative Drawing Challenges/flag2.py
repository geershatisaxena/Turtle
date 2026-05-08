import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("More Flags - Turtle Graphics")
screen.bgcolor("#F0F0F0")  # Light gray background
screen.setup(width=1000, height=800)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

def draw_rectangle(x, y, width, height, color, fill=True):
    """Draw a rectangle from bottom-left corner"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    
    if fill:
        pen.end_fill()
    pen.penup()

def draw_circle(x, y, radius, color, fill=True):
    """Draw a circle at given center"""
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    pen.circle(radius)
    if fill:
        pen.end_fill()
    pen.penup()

def draw_star(x, y, size, color, points=5):
    """Draw a star at given position"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.fillcolor(color)
    
    angle = 180 - (180 / points)
    for _ in range(points):
        pen.forward(size)
        pen.right(angle)
        pen.forward(size)
        pen.left(180 - angle)
    
    pen.end_fill()
    pen.penup()

def draw_crescent(x, y, radius, color):
    """Draw a crescent moon shape"""
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.fillcolor(color)
    pen.circle(radius)
    pen.end_fill()
    
    # Cut out the inner circle to create crescent
    pen.penup()
    pen.goto(x + radius * 0.4, y - radius * 0.7)
    pen.pendown()
    pen.color("#F0F0F0")  # Background color
    pen.begin_fill()
    pen.fillcolor("#F0F0F0")
    pen.circle(radius * 0.6)
    pen.end_fill()
    pen.penup()

# === FLAG 11: AUSTRALIA ===
def draw_australia_flag():
    pen.clear()
    
    width = 400
    height = 200
    
    # Blue background
    draw_rectangle(-width/2, -height/2, width, height, "#00008B")
    
    # Union Jack in canton (simplified)
    canton_size = height * 0.5
    # White diagonal stripes
    pen.penup()
    pen.goto(-width/2, height/2)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.pensize(8)
    pen.goto(-width/2 + canton_size, height/2 - canton_size)
    
    pen.penup()
    pen.goto(-width/2, height/2 - canton_size)
    pen.pendown()
    pen.goto(-width/2 + canton_size, height/2)
    
    # Red diagonal stripes
    pen.penup()
    pen.goto(-width/2, height/2)
    pen.pendown()
    pen.color("#C8102E")
    pen.pensize(4)
    pen.goto(-width/2 + canton_size, height/2 - canton_size)
    
    pen.penup()
    pen.goto(-width/2, height/2 - canton_size)
    pen.pendown()
    pen.goto(-width/2 + canton_size, height/2)
    
    # White cross stripes
    pen.penup()
    pen.goto(-width/2 + canton_size/2, height/2)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.pensize(12)
    pen.goto(-width/2 + canton_size/2, height/2 - canton_size)
    
    pen.penup()
    pen.goto(-width/2, height/2 - canton_size/2)
    pen.pendown()
    pen.goto(-width/2 + canton_size, height/2 - canton_size/2)
    
    # Commonwealth Star (7-pointed, simplified as 5-point)
    draw_star(-width/2 + canton_size * 0.7, height/2 - canton_size * 0.3, 10, "#FFFFFF")
    
    # Southern Cross stars
    star_positions = [(50, -30), (80, -60), (30, -80), (100, -40), (120, -70)]
    for x, y in star_positions:
        draw_star(x, y, 6, "#FFFFFF")
    
    screen.update()

# === FLAG 12: PAKISTAN ===
def draw_pakistan_flag():
    pen.clear()
    
    width = 400
    height = 200
    
    # Green background
    draw_rectangle(-width/2, -height/2, width, height, "#01411C")
    
    # White stripe on left
    draw_rectangle(-width/2, -height/2, width/4, height, "#FFFFFF")
    
    # Crescent moon
    pen.penup()
    pen.goto(50, 20)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.begin_fill()
    pen.fillcolor("#FFFFFF")
    pen.circle(40)
    pen.end_fill()
    
    # Cut out inner circle for crescent
    pen.penup()
    pen.goto(65, 25)
    pen.pendown()
    pen.color("#01411C")
    pen.begin_fill()
    pen.fillcolor("#01411C")
    pen.circle(30)
    pen.end_fill()
    
    # Star
    draw_star(110, 20, 15, "#FFFFFF")
    
    screen.update()

# === FLAG 13: NEPAL (unique shape, simplified) ===
def draw_nepal_flag():
    pen.clear()
    
    # Blue border (simulated by drawing larger then smaller)
    draw_rectangle(-100, -150, 200, 280, "#003893")
    
    # Red background (simplified shape with triangle top)
    pen.penup()
    pen.goto(-90, -140)
    pen.pendown()
    pen.color("#DC143C")
    pen.begin_fill()
    pen.fillcolor("#DC143C")
    pen.goto(-90, 40)
    pen.goto(0, 120)
    pen.goto(90, 40)
    pen.goto(90, -140)
    pen.goto(-90, -140)
    pen.end_fill()
    
    # Moon crescent (top)
    pen.penup()
    pen.goto(-30, 90)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.begin_fill()
    pen.fillcolor("#FFFFFF")
    pen.circle(15)
    pen.end_fill()
    
    pen.penup()
    pen.goto(-20, 93)
    pen.pendown()
    pen.color("#DC143C")
    pen.begin_fill()
    pen.fillcolor("#DC143C")
    pen.circle(10)
    pen.end_fill()
    
    # Sun (bottom)
    draw_circle(0, 30, 15, "#FFFFFF")
    
    # Sun rays
    pen.penup()
    pen.goto(0, 30)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.pensize(2)
    for angle in range(0, 360, 45):
        rad = angle * 3.14159 / 180
        x = 22 * cos(rad)
        y = 22 * sin(rad)
        pen.goto(x, y + 30)
        pen.penup()
        pen.goto(0, 30)
        pen.pendown()
    
    screen.update()

# === FLAG 14: ARGENTINA ===
def draw_argentina_flag():
    pen.clear()
    
    width = 400
    height = 200
    stripe_height = height / 3
    
    # Light blue stripes (top and bottom)
    draw_rectangle(-width/2, height/2 - stripe_height, width, stripe_height, "#75AADB")
    draw_rectangle(-width/2, -height/2, width, stripe_height, "#75AADB")
    
    # White stripe (middle)
    draw_rectangle(-width/2, height/2 - 2*stripe_height, width, stripe_height, "#FFFFFF")
    
    # Sun of May
    draw_circle(0, 20, 30, "#F5B700")
    
    # Sun rays (simplified)
    pen.penup()
    pen.goto(0, 20)
    pen.pendown()
    pen.color("#F5B700")
    pen.pensize(2)
    for angle in range(0, 360, 30):
        rad = angle * 3.14159 / 180
        x = 45 * cos(rad)
        y = 45 * sin(rad)
        pen.goto(x, y + 20)
        pen.penup()
        pen.goto(0, 20)
        pen.pendown()
    
    # Sun face (simplified)
    draw_circle(0, 18, 8, "#8B4513")
    
    screen.update()

# === FLAG 15: CHINA ===
def draw_china_flag():
    pen.clear()
    
    width = 400
    height = 267  # 2:3 ratio
    
    # Red background
    draw_rectangle(-width/2, -height/2, width, height, "#DE2910")
    
    # Large star
    draw_star(-140, 60, 25, "#FFDE00")
    
    # Four smaller stars in arc
    small_star_positions = [
        (-80, 100), (-60, 80), (-60, 50), (-80, 30)
    ]
    for x, y in small_star_positions:
        draw_star(x, y, 10, "#FFDE00")
    
    screen.update()

# === FLAG 16: SOUTH KOREA ===
def draw_south_korea_flag():
    pen.clear()
    
    width = 400
    height = 267
    
    # White background
    draw_rectangle(-width/2, -height/2, width, height, "#FFFFFF")
    
    # Red and blue Taegeuk (yin-yang)
    # Top red half
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color("#C60C30")
    pen.begin_fill()
    pen.fillcolor("#C60C30")
    pen.circle(50, 180)
    pen.end_fill()
    
    # Bottom blue half
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color("#003478")
    pen.begin_fill()
    pen.fillcolor("#003478")
    pen.setheading(180)
    pen.circle(50, 180)
    pen.end_fill()
    
    # Small inner circles (yin-yang dots)
    draw_circle(0, 25, 8, "#003478")
    draw_circle(0, -25, 8, "#C60C30")
    
    # Four trigrams (simplified as groups of bars)
    # Top-left
    pen.penup()
    pen.goto(-120, 100)
    pen.pendown()
    for i in range(3):
        draw_rectangle(-120 + i*8, 100, 5, 25, "#000000")
    
    # Top-right
    pen.penup()
    pen.goto(100, 100)
    pen.pendown()
    for i in range(3):
        draw_rectangle(100 + i*8, 100, 5, 25, "#000000")
    
    # Bottom-left  
    pen.penup()
    pen.goto(-120, -125)
    pen.pendown()
    for i in range(3):
        draw_rectangle(-120 + i*8, -125, 5, 25, "#000000")
    
    # Bottom-right
    pen.penup()
    pen.goto(100, -125)
    pen.pendown()
    for i in range(3):
        draw_rectangle(100 + i*8, -125, 5, 25, "#000000")
    
    screen.update()

# === FLAG 17: MEXICO ===
def draw_mexico_flag():
    pen.clear()
    
    width = 400
    height = 240
    
    # Green stripe
    draw_rectangle(-width/2, -height/2, width/3, height, "#006847")
    
    # White stripe
    draw_rectangle(-width/6, -height/2, width/3, height, "#FFFFFF")
    
    # Red stripe
    draw_rectangle(width/6, -height/2, width/3, height, "#CE1126")
    
    # Eagle and cactus (simplified - just a symbol)
    draw_circle(0, 20, 25, "#8B4513")  # Cactus base
    # Eagle (simplified as a bird shape)
    pen.penup()
    pen.goto(-15, 45)
    pen.pendown()
    pen.color("#000000")
    pen.begin_fill()
    pen.fillcolor("#000000")
    pen.goto(0, 70)
    pen.goto(15, 45)
    pen.goto(-15, 45)
    pen.end_fill()
    
    # Wings
    pen.penup()
    pen.goto(-5, 55)
    pen.pendown()
    pen.goto(-20, 50)
    pen.penup()
    pen.goto(5, 55)
    pen.pendown()
    pen.goto(20, 50)
    
    screen.update()

# === FLAG 18: SPAIN ===
def draw_spain_flag():
    pen.clear()
    
    width = 400
    height = 240
    stripe_height = height / 4
    
    # Top red stripe
    draw_rectangle(-width/2, height/2 - stripe_height, width, stripe_height, "#AA151B")
    
    # Yellow stripe (center, double height)
    draw_rectangle(-width/2, height/2 - 3*stripe_height, width, stripe_height*2, "#F1BF00")
    
    # Bottom red stripe
    draw_rectangle(-width/2, -height/2, width, stripe_height, "#AA151B")
    
    # Coat of arms (simplified - shield shape)
    pen.penup()
    pen.goto(-25, -10)
    pen.pendown()
    pen.color("#AA151B")
    pen.begin_fill()
    pen.fillcolor("#AA151B")
    pen.goto(0, 40)
    pen.goto(25, -10)
    pen.goto(-25, -10)
    pen.end_fill()
    
    # Shield details
    draw_rectangle(-15, 0, 30, 20, "#F1BF00", True)
    
    screen.update()

# === FLAG 19: EGYPT ===
def draw_egypt_flag():
    pen.clear()
    
    width = 400
    height = 240
    stripe_height = height / 3
    
    # Red stripe (top)
    draw_rectangle(-width/2, height/2 - stripe_height, width, stripe_height, "#CE1126")
    
    # White stripe (middle)
    draw_rectangle(-width/2, height/2 - 2*stripe_height, width, stripe_height, "#FFFFFF")
    
    # Black stripe (bottom)
    draw_rectangle(-width/2, -height/2, width, stripe_height, "#000000")
    
    # Eagle of Saladin (simplified)
    draw_circle(0, 15, 20, "#C99700")  # Eagle body
    
    # Eagle head
    pen.penup()
    pen.goto(-8, 40)
    pen.pendown()
    pen.color("#C99700")
    pen.begin_fill()
    pen.fillcolor("#C99700")
    pen.goto(0, 55)
    pen.goto(8, 40)
    pen.goto(-8, 40)
    pen.end_fill()
    
    screen.update()

# === FLAG 20: GREECE ===
def draw_greece_flag():
    pen.clear()
    
    width = 400
    height = 267
    stripe_height = height / 9
    
    # Blue stripes (5 stripes, alternating with white)
    for i in range(5):
        y = height/2 - (i*2) * stripe_height
        draw_rectangle(-width/2, y - stripe_height, width, stripe_height, "#0D5EAF")
    
    # Blue canton (top-left)
    canton_width = width * 0.4
    canton_height = height * 0.45
    draw_rectangle(-width/2, height/2 - canton_height, canton_width, canton_height, "#0D5EAF")
    
    # White cross in canton
    # Horizontal bar
    draw_rectangle(-width/2 + canton_width*0.3, height/2 - canton_height*0.45, canton_width*0.4, canton_height*0.1, "#FFFFFF")
    # Vertical bar
    draw_rectangle(-width/2 + canton_width*0.45, height/2 - canton_height*0.65, canton_width*0.1, canton_height*0.5, "#FFFFFF")
    
    screen.update()

# Import math for cos, sin
from math import cos, sin

def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("darkblue")
    title.penup()
    title.hideturtle()
    title.goto(0, 370)
    title.write("🏁 MORE FLAGS OF THE WORLD 🏁", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("darkblue")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -390)
    instructions.write("1=Australia 2=Pakistan 3=Nepal 4=Argentina 5=China 6=South Korea 7=Mexico 8=Spain 9=Egypt 0=Greece | ESC=Exit",
                       align="center", font=("Arial", 8, "normal"))

current_flag = 11

def draw_current():
    """Draw the currently selected flag"""
    if current_flag == 11:
        draw_australia_flag()
    elif current_flag == 12:
        draw_pakistan_flag()
    elif current_flag == 13:
        draw_nepal_flag()
    elif current_flag == 14:
        draw_argentina_flag()
    elif current_flag == 15:
        draw_china_flag()
    elif current_flag == 16:
        draw_south_korea_flag()
    elif current_flag == 17:
        draw_mexico_flag()
    elif current_flag == 18:
        draw_spain_flag()
    elif current_flag == 19:
        draw_egypt_flag()
    elif current_flag == 20:
        draw_greece_flag()

def set_flag_11(): global current_flag; current_flag = 11; draw_current()
def set_flag_12(): global current_flag; current_flag = 12; draw_current()
def set_flag_13(): global current_flag; current_flag = 13; draw_current()
def set_flag_14(): global current_flag; current_flag = 14; draw_current()
def set_flag_15(): global current_flag; current_flag = 15; draw_current()
def set_flag_16(): global current_flag; current_flag = 16; draw_current()
def set_flag_17(): global current_flag; current_flag = 17; draw_current()
def set_flag_18(): global current_flag; current_flag = 18; draw_current()
def set_flag_19(): global current_flag; current_flag = 19; draw_current()
def set_flag_20(): global current_flag; current_flag = 20; draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_flag_11, "1")
screen.onkey(set_flag_12, "2")
screen.onkey(set_flag_13, "3")
screen.onkey(set_flag_14, "4")
screen.onkey(set_flag_15, "5")
screen.onkey(set_flag_16, "6")
screen.onkey(set_flag_17, "7")
screen.onkey(set_flag_18, "8")
screen.onkey(set_flag_19, "9")
screen.onkey(set_flag_20, "0")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        MORE FLAGS OF THE WORLD")
print("=" * 60)
print()
print("Another 10 country flags from around the world!")
print()
print("FLAGS INCLUDED:")
print("  1 - Australia 🇦🇺 (Union Jack + Southern Cross)")
print("  2 - Pakistan 🇵🇰 (Green with crescent and star)")
print("  3 - Nepal 🇳🇵 (Unique triangular shape)")
print("  4 - Argentina 🇦🇷 (Sun of May on light blue/white)")
print("  5 - China 🇨🇳 (Red with 5 golden stars)")
print("  6 - South Korea 🇰🇷 (Yin-yang with trigrams)")
print("  7 - Mexico 🇲🇽 (Green, white, red with eagle)")
print("  8 - Spain 🇪🇸 (Red-yellow-red with coat of arms)")
print("  9 - Egypt 🇪🇬 (Red, white, black with eagle)")
print("  0 - Greece 🇬🇷 (Blue and white with cross)")
print()
print("CONTROLS:")
print("  0-9 - Select flag to display")
print("  ESC - Exit program")
print()
print("This completes 20 flags from around the world!")

# Draw default flag (Australia)
draw_australia_flag()
screen.mainloop()