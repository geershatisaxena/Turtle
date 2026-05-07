import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Cute Cartoon Car - Turtle Shapes")
screen.bgcolor("#87CEEB")  # Sky blue
screen.setup(width=800, height=600)
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

def draw_rounded_rect(x, y, width, height, color, fill=True):
    """Draw a rectangle with rounded corners"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    # Draw with rounded corners
    for _ in range(2):
        pen.forward(width)
        pen.circle(5, 90)
        pen.forward(height)
        pen.circle(5, 90)
    
    if fill:
        pen.end_fill()
    pen.penup()

def draw_cute_car():
    """Draw a cute cartoon-style car"""
    pen.clear()
    
    # === CAR BODY ===
    # Main body (rounded rectangle)
    draw_rounded_rect(-130, -40, 260, 55, "#FF69B4")  # Hot pink
    
    # Car roof
    draw_rounded_rect(-70, 15, 140, 45, "#FF1493")  # Deep pink
    
    # === WINDOWS (with cute shape) ===
    # Front window (tilted)
    pen.penup()
    pen.goto(-55, 25)
    pen.pendown()
    pen.color("#ADD8E6")
    pen.begin_fill()
    pen.fillcolor("#ADD8E6")
    pen.goto(-55, 50)
    pen.goto(-15, 55)
    pen.goto(-15, 25)
    pen.goto(-55, 25)
    pen.end_fill()
    
    # Rear window
    pen.penup()
    pen.goto(0, 25)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("#ADD8E6")
    pen.goto(0, 55)
    pen.goto(40, 50)
    pen.goto(40, 25)
    pen.goto(0, 25)
    pen.end_fill()
    
    # Middle window divider
    pen.penup()
    pen.goto(-5, 20)
    pen.pendown()
    pen.color("#FF1493")
    pen.pensize(5)
    pen.goto(-5, 55)
    pen.penup()
    
    # === WHEELS ===
    # Back wheel
    draw_circle(-80, -40, 22, "#333333")
    draw_circle(-80, -40, 14, "#CCCCCC")
    draw_circle(-80, -40, 6, "#999999")
    
    # Front wheel
    draw_circle(80, -40, 22, "#333333")
    draw_circle(80, -40, 14, "#CCCCCC")
    draw_circle(80, -40, 6, "#999999")
    
    # === WHEEL HUBCAPS (star shape) ===
    for x in [-80, 80]:
        for angle in [0, 72, 144, 216, 288]:
            rad = angle * 3.14159 / 180
            px = x + 8 * cos(rad)
            py = -40 + 8 * sin(rad)
            pen.penup()
            pen.goto(px, py)
            pen.pendown()
            pen.dot(3, "#FFD700")
    
    # === HEADLIGHTS (big cute eyes) ===
    # Left headlight
    pen.penup()
    pen.goto(-125, -15)
    pen.pendown()
    pen.color("#FFFF00")
    pen.begin_fill()
    pen.fillcolor("#FFFF00")
    pen.circle(10)
    pen.end_fill()
    
    pen.penup()
    pen.goto(-125, -17)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.fillcolor("black")
    pen.circle(4)
    pen.end_fill()
    
    # Right headlight
    pen.penup()
    pen.goto(125, -15)
    pen.pendown()
    pen.color("#FFFF00")
    pen.begin_fill()
    pen.fillcolor("#FFFF00")
    pen.circle(10)
    pen.end_fill()
    
    pen.penup()
    pen.goto(125, -17)
    pen.pendown()
    pen.color("black")
    pen.begin_fill()
    pen.fillcolor("black")
    pen.circle(4)
    pen.end_fill()
    
    # === GRILLE (smiling mouth) ===
    pen.penup()
    pen.goto(-90, -35)
    pen.pendown()
    pen.color("#333333")
    pen.pensize(3)
    pen.setheading(-60)
    pen.circle(50, 120)
    
    # Teeth
    pen.penup()
    pen.goto(-60, -32)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.fillcolor("white")
    pen.goto(-50, -32)
    pen.goto(-55, -25)
    pen.goto(-60, -32)
    pen.end_fill()
    
    pen.penup()
    pen.goto(-45, -32)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("white")
    pen.goto(-35, -32)
    pen.goto(-40, -25)
    pen.goto(-45, -32)
    pen.end_fill()
    
    # === EXHAUST ===
    pen.penup()
    pen.goto(110, -45)
    pen.pendown()
    pen.color("#888888")
    pen.pensize(8)
    pen.goto(130, -45)
    pen.penup()
    pen.goto(130, -45)
    pen.pendown()
    pen.color("#444444")
    pen.pensize(4)
    pen.goto(135, -45)
    
    # === DECORATIVE STRIPES ===
    pen.penup()
    pen.goto(-120, -5)
    pen.pendown()
    pen.color("#FFFFFF")
    pen.pensize(3)
    pen.goto(120, -5)
    
    pen.penup()
    pen.goto(-115, 0)
    pen.pendown()
    pen.pensize(2)
    pen.goto(115, 0)
    
    # === HEART DECORATION ===
    pen.penup()
    pen.goto(0, 10)
    pen.pendown()
    pen.color("#FF0000")
    pen.begin_fill()
    pen.fillcolor("#FF0000")
    pen.left(45)
    pen.forward(10)
    pen.circle(5, 180)
    pen.right(90)
    pen.circle(5, 180)
    pen.forward(10)
    pen.end_fill()
    
    # === ANTENNA ===
    pen.penup()
    pen.goto(-40, 65)
    pen.pendown()
    pen.color("#333333")
    pen.pensize(3)
    pen.goto(-40, 85)
    
    # Antenna ball
    pen.penup()
    pen.goto(-40, 85)
    pen.pendown()
    pen.color("#FF0000")
    pen.begin_fill()
    pen.fillcolor("#FF0000")
    pen.circle(4)
    pen.end_fill()
    
    # === GROUND ===
    pen.penup()
    pen.goto(-150, -62)
    pen.pendown()
    pen.color("#228B22")
    pen.pensize(3)
    pen.goto(150, -62)
    
    # Shadow under car
    pen.penup()
    pen.goto(-120, -55)
    pen.pendown()
    pen.color("gray")
    pen.pensize(1)
    pen.goto(120, -55)
    
    screen.update()

def draw_police_car():
    """Draw a police car"""
    pen.clear()
    
    # Car body
    draw_rectangle(-130, -40, 260, 50, "#FFFFFF")
    
    # Police stripe
    draw_rectangle(-130, -20, 260, 15, "#0000FF")
    
    # Car roof
    draw_rectangle(-70, 10, 140, 35, "#CCCCCC")
    
    # Windows
    draw_rectangle(-60, 15, 50, 25, "#ADD8E6")
    draw_rectangle(10, 15, 50, 25, "#ADD8E6")
    
    # POLICE text
    pen.penup()
    pen.goto(-30, -10)
    pen.pendown()
    pen.color("#0000FF")
    pen.write("POLICE", align="center", font=("Arial", 14, "bold"))
    
    # Light bar
    pen.penup()
    pen.goto(-50, 48)
    pen.pendown()
    pen.color("#FF0000")
    pen.begin_fill()
    pen.fillcolor("#FF0000")
    pen.goto(-30, 48)
    pen.goto(-30, 55)
    pen.goto(-50, 55)
    pen.goto(-50, 48)
    pen.end_fill()
    
    pen.penup()
    pen.goto(-30, 48)
    pen.pendown()
    pen.color("#0000FF")
    pen.begin_fill()
    pen.fillcolor("#0000FF")
    pen.goto(-10, 48)
    pen.goto(-10, 55)
    pen.goto(-30, 55)
    pen.goto(-30, 48)
    pen.end_fill()
    
    pen.penup()
    pen.goto(-10, 48)
    pen.pendown()
    pen.color("#FF0000")
    pen.begin_fill()
    pen.fillcolor("#FF0000")
    pen.goto(10, 48)
    pen.goto(10, 55)
    pen.goto(-10, 55)
    pen.goto(-10, 48)
    pen.end_fill()
    
    pen.penup()
    pen.goto(10, 48)
    pen.pendown()
    pen.color("#0000FF")
    pen.begin_fill()
    pen.fillcolor("#0000FF")
    pen.goto(30, 48)
    pen.goto(30, 55)
    pen.goto(10, 55)
    pen.goto(10, 48)
    pen.end_fill()
    
    # Wheels
    draw_circle(-80, -40, 20, "#333333")
    draw_circle(-80, -40, 12, "#CCCCCC")
    draw_circle(80, -40, 20, "#333333")
    draw_circle(80, -40, 12, "#CCCCCC")
    
    # Headlights
    draw_circle(-125, -15, 7, "#FFFF99")
    draw_circle(125, -15, 7, "#FF6600")
    
    screen.update()

def draw_ice_cream_truck():
    """Draw an ice cream truck"""
    pen.clear()
    
    # Truck body
    draw_rectangle(-140, -40, 280, 50, "#FFF8DC")  # Cream color
    
    # Stripes
    draw_rectangle(-140, -25, 280, 10, "#FF69B4")
    draw_rectangle(-140, -40, 280, 8, "#87CEEB")
    
    # Roof
    draw_rectangle(-80, 10, 200, 30, "#FFE4B5")
    
    # Windows
    draw_rectangle(-60, 15, 40, 20, "#ADD8E6")
    draw_rectangle(-10, 15, 40, 20, "#ADD8E6")
    draw_rectangle(40, 15, 40, 20, "#ADD8E6")
    
    # ICE CREAM text
    pen.penup()
    pen.goto(0, -5)
    pen.pendown()
    pen.color("#FF69B4")
    pen.write("ICE CREAM", align="center", font=("Arial", 14, "bold"))
    
    # Wheels
    draw_circle(-90, -38, 18, "#333333")
    draw_circle(-90, -38, 10, "#CCCCCC")
    draw_circle(90, -38, 18, "#333333")
    draw_circle(90, -38, 10, "#CCCCCC")
    
    # Ice cream cone on roof
    pen.penup()
    pen.goto(80, 15)
    pen.pendown()
    pen.color("#DEB887")
    pen.begin_fill()
    pen.fillcolor("#DEB887")
    pen.goto(80, 40)
    pen.goto(70, 40)
    pen.goto(70, 15)
    pen.end_fill()
    
    # Ice cream scoop
    draw_circle(75, 45, 12, "#FFB6C1")
    draw_circle(75, 45, 8, "#FF69B4")
    
    screen.update()

# Import math for cos and sin
from math import cos, sin

def draw_title():
    """Draw title and instructions"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("darkblue")
    title.penup()
    title.hideturtle()
    title.goto(0, 270)
    title.write("🚗 CUTE CAR DESIGNS - TURTLE SHAPES 🚗", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("darkblue")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -280)
    instructions.write("1=Cute Car  2=Police Car  3=Ice Cream Truck  4=Redraw | ESC=Exit",
                       align="center", font=("Arial", 10, "normal"))

current_car = 1

def draw_current():
    """Draw the currently selected car"""
    if current_car == 1:
        draw_cute_car()
    elif current_car == 2:
        draw_police_car()
    elif current_car == 3:
        draw_ice_cream_truck()

def set_car_1(): global current_car; current_car = 1; draw_current()
def set_car_2(): global current_car; current_car = 2; draw_current()
def set_car_3(): global current_car; current_car = 3; draw_current()
def redraw(): draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_car_1, "1")
screen.onkey(set_car_2, "2")
screen.onkey(set_car_3, "3")
screen.onkey(redraw, "4")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        MORE CUTE CAR DESIGNS")
print("=" * 60)
print()
print("3 adorable vehicle designs with personality!")
print()
print("CAR DESIGNS:")
print("  1 - Cute Car: Pink cartoon car with eyes and smile")
print("  2 - Police Car: White and blue with light bar")
print("  3 - Ice Cream Truck: Cream-colored with ice cream on roof")
print()
print("SPECIAL FEATURES:")
print("  • Cute Car - Headlights look like eyes, smiling grille")
print("  • Cute Car - Heart decoration and antenna")
print("  • Police Car - Light bar, badge, stripe")
print("  • Ice Cream Truck - Ice cream cone decoration")
print()
print("CONTROLS:")
print("  1-3 - Select vehicle design")
print("  4   - Redraw current vehicle")
print("  ESC - Exit program")

# Draw default car
draw_cute_car()
screen.mainloop()