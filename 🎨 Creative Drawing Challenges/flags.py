import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Flag Drawing - Turtle Graphics")
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

def draw_triangle(x, y, width, height, color, fill=True):
    """Draw an equilateral triangle"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    for _ in range(3):
        pen.forward(width)
        pen.left(120)
    
    if fill:
        pen.end_fill()
    pen.penup()

# === FLAG 1: INDIA ===
def draw_india_flag():
    pen.clear()
    
    # Saffron (top)
    draw_rectangle(-200, 100, 400, 60, "#FF9933")
    
    # White (middle)
    draw_rectangle(-200, 40, 400, 60, "#FFFFFF")
    
    # Green (bottom)
    draw_rectangle(-200, -20, 400, 60, "#138808")
    
    # Ashoka Chakra (blue wheel)
    draw_circle(0, 70, 22, "#000080")
    
    # Spokes on Chakra (24 spokes approximated)
    pen.penup()
    pen.goto(0, 70)
    pen.pendown()
    pen.color("#000080")
    pen.pensize(2)
    for angle in range(0, 360, 15):
        rad = angle * 3.14159 / 180
        x = 20 * cos(rad)
        y = 20 * sin(rad)
        pen.goto(x, y + 70)
        pen.penup()
        pen.goto(0, 70)
        pen.pendown()
    
    # Center dot
    draw_circle(0, 70, 4, "#000080")
    
    screen.update()

# === FLAG 2: USA ===
def draw_usa_flag():
    pen.clear()
    
    # Flag dimensions
    width = 400
    height = 210
    
    # Red and white stripes (13 stripes)
    stripe_height = height / 13
    for i in range(13):
        y = -height/2 + i * stripe_height
        color = "#B22234" if i % 2 == 0 else "#FFFFFF"
        draw_rectangle(-width/2, y, width, stripe_height, color)
    
    # Blue canton (union)
    canton_width = width * 0.4
    canton_height = height * 0.538
    draw_rectangle(-width/2, height/2 - canton_height, canton_width, canton_height, "#3C3B6E")
    
    # 50 stars (5x6 grid + 4x5 grid alternating)
    star_size = 8
    # Rows with 6 stars
    for row in range(9):
        if row % 2 == 0:
            # 6 stars in this row
            for col in range(6):
                x = -width/2 + canton_width * 0.1 + col * (canton_width * 0.16)
                y = height/2 - canton_height * 0.1 - row * (canton_height * 0.1)
                draw_star(x, y, star_size, "#FFFFFF")
        else:
            # 5 stars in this row
            for col in range(5):
                x = -width/2 + canton_width * 0.18 + col * (canton_width * 0.16)
                y = height/2 - canton_height * 0.1 - row * (canton_height * 0.1)
                draw_star(x, y, star_size, "#FFFFFF")
    
    screen.update()

# === FLAG 3: JAPAN ===
def draw_japan_flag():
    pen.clear()
    
    # White background
    draw_rectangle(-200, -130, 400, 260, "#FFFFFF")
    
    # Red circle
    draw_circle(0, 0, 60, "#BC002D")
    
    screen.update()

# === FLAG 4: GERMANY ===
def draw_germany_flag():
    pen.clear()
    
    # Black (top)
    draw_rectangle(-200, 90, 400, 60, "#000000")
    
    # Red (middle)
    draw_rectangle(-200, 30, 400, 60, "#DD0000")
    
    # Gold (bottom)
    draw_rectangle(-200, -30, 400, 60, "#FFCE00")
    
    screen.update()

# === FLAG 5: FRANCE ===
def draw_france_flag():
    pen.clear()
    
    # Blue (left)
    draw_rectangle(-200, -130, 400/3, 260, "#0055A4")
    
    # White (middle)
    draw_rectangle(-200 + 400/3, -130, 400/3, 260, "#FFFFFF")
    
    # Red (right)
    draw_rectangle(-200 + 2*400/3, -130, 400/3, 260, "#EF4135")
    
    screen.update()

# === FLAG 6: CANADA ===
def draw_canada_flag():
    pen.clear()
    
    width = 400
    height = 200
    
    # Red (left and right)
    draw_rectangle(-width/2, -height/2, width/3, height, "#FF0000")
    draw_rectangle(width/6, -height/2, width/3, height, "#FF0000")
    
    # White (middle)
    draw_rectangle(-width/6, -height/2, width/3, height, "#FFFFFF")
    
    # Maple leaf (simplified)
    pen.penup()
    pen.goto(0, 30)
    pen.pendown()
    pen.color("#FF0000")
    pen.begin_fill()
    pen.fillcolor("#FF0000")
    
    # Draw simplified maple leaf
    for angle in [0, 60, 120, 180, 240, 300]:
        rad = angle * 3.14159 / 180
        x = 25 * cos(rad)
        y = 25 * sin(rad)
        pen.goto(x, y + 20)
    
    pen.end_fill()
    
    # Leaf stem
    pen.penup()
    pen.goto(0, -20)
    pen.pendown()
    pen.pensize(3)
    pen.goto(0, -40)
    
    screen.update()

# === FLAG 7: BRAZIL ===
def draw_brazil_flag():
    pen.clear()
    
    # Green background
    draw_rectangle(-200, -130, 400, 260, "#009B3A")
    
    # Yellow diamond
    pen.penup()
    pen.goto(0, 100)
    pen.pendown()
    pen.color("#FEDF00")
    pen.begin_fill()
    pen.fillcolor("#FEDF00")
    pen.goto(160, 0)
    pen.goto(0, -100)
    pen.goto(-160, 0)
    pen.goto(0, 100)
    pen.end_fill()
    
    # Blue circle
    draw_circle(0, 0, 60, "#002776")
    
    # White band (simplified)
    pen.penup()
    pen.goto(-120, -20)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.pensize(8)
    pen.goto(120, 20)
    
    # Stars (simplified - just a few)
    star_positions = [(-30, 20), (0, 30), (30, 20), (0, -30), (40, -10), (-40, -10)]
    for x, y in star_positions:
        draw_star(x, y, 6, "#FFFFFF")
    
    screen.update()

# === FLAG 8: UNITED KINGDOM (Union Jack) ===
def draw_uk_flag():
    pen.clear()
    
    width = 400
    height = 200
    
    # Blue background
    draw_rectangle(-width/2, -height/2, width, height, "#012169")
    
    # White diagonal stripes
    pen.penup()
    pen.goto(-width/2, -height/2)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.pensize(15)
    pen.goto(width/2, height/2)
    
    pen.penup()
    pen.goto(-width/2, height/2)
    pen.pendown()
    pen.goto(width/2, -height/2)
    
    # Red diagonal stripes
    pen.penup()
    pen.goto(-width/2, -height/2)
    pen.pendown()
    pen.color("#C8102E")
    pen.pensize(8)
    pen.goto(width/2, height/2)
    
    pen.penup()
    pen.goto(-width/2, height/2)
    pen.pendown()
    pen.goto(width/2, -height/2)
    
    # White vertical and horizontal stripes
    pen.penup()
    pen.goto(0, -height/2)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.pensize(30)
    pen.goto(0, height/2)
    
    pen.penup()
    pen.goto(-width/2, 0)
    pen.pendown()
    pen.goto(width/2, 0)
    
    # Red vertical and horizontal stripes
    pen.penup()
    pen.goto(0, -height/2)
    pen.pendown()
    pen.color("#C8102E")
    pen.pensize(15)
    pen.goto(0, height/2)
    
    pen.penup()
    pen.goto(-width/2, 0)
    pen.pendown()
    pen.goto(width/2, 0)
    
    screen.update()

# === FLAG 9: SOUTH AFRICA ===
def draw_south_africa_flag():
    pen.clear()
    
    width = 400
    height = 200
    
    # Red (top)
    draw_rectangle(-width/2, 0, width, height/2, "#DE3831")
    
    # Blue (bottom)
    draw_rectangle(-width/2, -height/2, width, height/2, "#003DA5")
    
    # Green Y-shape (simplified)
    pen.penup()
    pen.goto(-width/2, -height/3)
    pen.pendown()
    pen.color("#007A4D")
    pen.begin_fill()
    pen.fillcolor("#007A4D")
    pen.goto(width/3, -height/3)
    pen.goto(width/3, height/3)
    pen.goto(-width/2, height/3)
    pen.goto(-width/2, -height/3)
    pen.end_fill()
    
    # White and gold stripes
    pen.penup()
    pen.goto(-width/2, -20)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.pensize(6)
    pen.goto(width/2, -20)
    
    pen.penup()
    pen.goto(-width/2, 20)
    pen.pendown()
    pen.goto(width/2, 20)
    
    pen.penup()
    pen.goto(-width/2, -16)
    pen.pendown()
    pen.color("#FFB81C")
    pen.pensize(4)
    pen.goto(width/2, -16)
    
    pen.penup()
    pen.goto(-width/2, 16)
    pen.pendown()
    pen.goto(width/2, 16)
    
    screen.update()

# === FLAG 10: SWITZERLAND ===
def draw_switzerland_flag():
    pen.clear()
    
    # Red square
    draw_rectangle(-150, -150, 300, 300, "#FF0000")
    
    # White cross
    # Vertical bar
    draw_rectangle(-30, -75, 60, 150, "#FFFFFF")
    
    # Horizontal bar
    draw_rectangle(-75, -30, 150, 60, "#FFFFFF")
    
    screen.update()

# Import math for cos, sin
from math import cos, sin

# UI Controls
def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("darkblue")
    title.penup()
    title.hideturtle()
    title.goto(0, 360)
    title.write("🏁 FLAGS OF THE WORLD - TURTLE GRAPHICS 🏁", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("darkblue")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -390)
    instructions.write("1=India 2=USA 3=Japan 4=Germany 5=France 6=Canada 7=Brazil 8=UK 9=South Africa 0=Switzerland | ESC=Exit",
                       align="center", font=("Arial", 9, "normal"))

current_flag = 1

def draw_current():
    """Draw the currently selected flag"""
    if current_flag == 1:
        draw_india_flag()
    elif current_flag == 2:
        draw_usa_flag()
    elif current_flag == 3:
        draw_japan_flag()
    elif current_flag == 4:
        draw_germany_flag()
    elif current_flag == 5:
        draw_france_flag()
    elif current_flag == 6:
        draw_canada_flag()
    elif current_flag == 7:
        draw_brazil_flag()
    elif current_flag == 8:
        draw_uk_flag()
    elif current_flag == 9:
        draw_south_africa_flag()
    elif current_flag == 10:
        draw_switzerland_flag()

def set_flag_1(): global current_flag; current_flag = 1; draw_current()
def set_flag_2(): global current_flag; current_flag = 2; draw_current()
def set_flag_3(): global current_flag; current_flag = 3; draw_current()
def set_flag_4(): global current_flag; current_flag = 4; draw_current()
def set_flag_5(): global current_flag; current_flag = 5; draw_current()
def set_flag_6(): global current_flag; current_flag = 6; draw_current()
def set_flag_7(): global current_flag; current_flag = 7; draw_current()
def set_flag_8(): global current_flag; current_flag = 8; draw_current()
def set_flag_9(): global current_flag; current_flag = 9; draw_current()
def set_flag_0(): global current_flag; current_flag = 10; draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_flag_1, "1")
screen.onkey(set_flag_2, "2")
screen.onkey(set_flag_3, "3")
screen.onkey(set_flag_4, "4")
screen.onkey(set_flag_5, "5")
screen.onkey(set_flag_6, "6")
screen.onkey(set_flag_7, "7")
screen.onkey(set_flag_8, "8")
screen.onkey(set_flag_9, "9")
screen.onkey(set_flag_0, "0")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        FLAGS OF THE WORLD")
print("=" * 60)
print()
print("10 country flags drawn with accurate colors!")
print()
print("FLAGS INCLUDED:")
print("  1 - India 🇮🇳 (Saffron, White, Green with Ashoka Chakra)")
print("  2 - USA 🇺🇸 (13 stripes, 50 stars)")
print("  3 - Japan 🇯🇵 (White with red circle)")
print("  4 - Germany 🇩🇪 (Black, Red, Gold horizontal)")
print("  5 - France 🇫🇷 (Blue, White, Red vertical)")
print("  6 - Canada 🇨🇦 (Red and white with maple leaf)")
print("  7 - Brazil 🇧🇷 (Green, yellow diamond, blue circle)")
print("  8 - United Kingdom 🇬🇧 (Union Jack)")
print("  9 - South Africa 🇿🇦 (Y-shaped pattern)")
print("  0 - Switzerland 🇨🇭 (Red square with white cross)")
print()
print("CONTROLS:")
print("  0-9 - Select flag to display")
print("  ESC - Exit program")
print()
print("Each flag is drawn using basic shapes!")

# Draw default flag (India)
draw_india_flag()
screen.mainloop()