import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Simple Car - Turtle Shapes")
screen.bgcolor("#87CEEB")  # Sky blue
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Color palette
colors = {
    "body": "#FF0000",      # Red body
    "body_dark": "#CC0000", # Darker red for depth
    "windows": "#87CEEB",   # Light blue windows
    "windows_dark": "#5F9EA0", # Darker window tint
    "wheels": "#333333",    # Dark gray wheels
    "wheel_rim": "#CCCCCC", # Silver rims
    "headlight": "#FFFF99", # Yellow headlight
    "taillight": "#FF6600", # Orange taillight
    "grill": "#666666",     # Gray grill
    "exhaust": "#888888",   # Silver exhaust pipe
    "details": "#000000"    # Black details
}

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

def draw_car():
    """Draw the complete car"""
    pen.clear()
    
    # === CAR BODY ===
    # Main body (rectangle)
    draw_rectangle(-120, -40, 240, 60, colors["body"])
    
    # Car roof (rectangle - smaller, on top)
    draw_rectangle(-60, 20, 120, 40, colors["body_dark"])
    
    # === WINDSHIELD AND WINDOWS ===
    # Front windshield
    draw_rectangle(-50, 25, 50, 30, colors["windows"])
    
    # Rear window
    draw_rectangle(0, 25, 50, 30, colors["windows"])
    
    # Window divider (pillar)
    pen.penup()
    pen.goto(0, 20)
    pen.pendown()
    pen.color(colors["body"])
    pen.pensize(4)
    pen.goto(0, 55)
    pen.penup()
    
    # === WHEELS ===
    # Back wheel
    draw_circle(-70, -40, 20, colors["wheels"])
    draw_circle(-70, -40, 10, colors["wheel_rim"])
    
    # Front wheel
    draw_circle(70, -40, 20, colors["wheels"])
    draw_circle(70, -40, 10, colors["wheel_rim"])
    
    # === HEADLIGHT ===
    draw_circle(-115, -15, 8, colors["headlight"])
    
    # === TAILLIGHT ===
    draw_circle(115, -15, 8, colors["taillight"])
    
    # === GRILL ===
    draw_rectangle(-120, -30, 10, 25, colors["grill"])
    
    # === EXHAUST PIPE ===
    pen.penup()
    pen.goto(100, -45)
    pen.pendown()
    pen.color(colors["exhaust"])
    pen.pensize(6)
    pen.goto(120, -45)
    pen.penup()
    
    # === DOOR LINE ===
    pen.penup()
    pen.goto(0, -15)
    pen.pendown()
    pen.color(colors["details"])
    pen.pensize(2)
    pen.goto(0, 20)
    pen.penup()
    
    # === DOOR HANDLE ===
    pen.penup()
    pen.goto(20, 5)
    pen.pendown()
    pen.color(colors["details"])
    pen.pensize(3)
    pen.goto(35, 5)
    pen.penup()
    
    # === HOOD DETAIL ===
    pen.penup()
    pen.goto(-80, -10)
    pen.pendown()
    pen.color(colors["details"])
    pen.pensize(2)
    pen.goto(-40, -10)
    pen.penup()
    
    # === GROUND SHADOW ===
    pen.penup()
    pen.goto(-140, -60)
    pen.pendown()
    pen.color("gray")
    pen.pensize(1)
    pen.goto(140, -60)
    pen.penup()
    
    screen.update()

def draw_sport_car():
    """Draw a sportier car design"""
    pen.clear()
    
    # Car body (sleeker)
    pen.penup()
    pen.goto(-130, -30)
    pen.pendown()
    pen.color("#FF4500")  # Orange-red
    pen.begin_fill()
    pen.fillcolor("#FF4500")
    pen.goto(-130, 10)
    pen.goto(-90, 30)
    pen.goto(90, 30)
    pen.goto(130, 10)
    pen.goto(130, -30)
    pen.goto(-130, -30)
    pen.end_fill()
    
    # Windows
    pen.penup()
    pen.goto(-80, 10)
    pen.pendown()
    pen.color("#333333")
    pen.begin_fill()
    pen.fillcolor("#333333")
    pen.goto(-80, 28)
    pen.goto(0, 28)
    pen.goto(0, 10)
    pen.goto(-80, 10)
    pen.end_fill()
    
    pen.penup()
    pen.goto(0, 10)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("#333333")
    pen.goto(0, 28)
    pen.goto(80, 28)
    pen.goto(80, 10)
    pen.goto(0, 10)
    pen.end_fill()
    
    # Wheels
    draw_circle(-70, -30, 22, "#222222")
    draw_circle(-70, -30, 12, "#CCCCCC")
    draw_circle(70, -30, 22, "#222222")
    draw_circle(70, -30, 12, "#CCCCCC")
    
    # Spoiler
    pen.penup()
    pen.goto(120, 5)
    pen.pendown()
    pen.color("#333333")
    pen.begin_fill()
    pen.fillcolor("#333333")
    pen.goto(130, 5)
    pen.goto(130, 20)
    pen.goto(120, 25)
    pen.goto(120, 5)
    pen.end_fill()
    
    # Headlight
    draw_circle(-125, -5, 6, "#FFFF99")
    
    # Taillight
    draw_circle(125, -5, 6, "#FF0000")
    
    screen.update()

def draw_classic_car():
    """Draw a vintage classic car"""
    pen.clear()
    
    # Main body
    draw_rectangle(-140, -35, 280, 45, "#006400")  # Dark green
    
    # Fenders (curved wheel arches)
    pen.penup()
    pen.goto(-95, -35)
    pen.pendown()
    pen.color("#006400")
    pen.begin_fill()
    pen.fillcolor("#006400")
    pen.setheading(-90)
    pen.circle(25, 180)
    pen.goto(-95, -35)
    pen.end_fill()
    
    pen.penup()
    pen.goto(95, -35)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("#006400")
    pen.setheading(-90)
    pen.circle(25, 180)
    pen.goto(95, -35)
    pen.end_fill()
    
    # Cabin/roof
    pen.penup()
    pen.goto(-40, 10)
    pen.pendown()
    pen.color("#006400")
    pen.begin_fill()
    pen.fillcolor("#006400")
    pen.goto(-40, 50)
    pen.goto(40, 50)
    pen.goto(70, 10)
    pen.goto(-40, 10)
    pen.end_fill()
    
    # Windows
    pen.penup()
    pen.goto(-30, 15)
    pen.pendown()
    pen.color="#ADD8E6"
    pen.begin_fill()
    pen.fillcolor="#ADD8E6"
    pen.goto(-30, 45)
    pen.goto(0, 45)
    pen.goto(0, 15)
    pen.goto(-30, 15)
    pen.end_fill()
    
    pen.penup()
    pen.goto(5, 15)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor="#ADD8E6"
    pen.goto(5, 45)
    pen.goto(30, 45)
    pen.goto(50, 15)
    pen.goto(5, 15)
    pen.end_fill()
    
    # Wheels with whitewall tires
    draw_circle(-70, -30, 22, "#444444")
    draw_circle(-70, -30, 18, "#CCCCCC")
    draw_circle(-70, -30, 10, "#888888")
    draw_circle(70, -30, 22, "#444444")
    draw_circle(70, -30, 18, "#CCCCCC")
    draw_circle(70, -30, 10, "#888888")
    
    # Headlights (round, classic)
    draw_circle(-135, -5, 9, "#FFFFCC")
    draw_circle(-135, -5, 6, "#FFFF99")
    
    # Bumpers
    pen.penup()
    pen.goto(-145, -20)
    pen.pendown()
    pen.color("#CCCCCC")
    pen.pensize(5)
    pen.goto(-145, -5)
    pen.penup()
    pen.goto(145, -20)
    pen.pendown()
    pen.goto(145, -5)
    
    screen.update()

def draw_race_car():
    """Draw a race car with spoiler and racing stripes"""
    pen.clear()
    
    # Low profile body
    pen.penup()
    pen.goto(-140, -30)
    pen.pendown()
    pen.color("#1E90FF")
    pen.begin_fill()
    pen.fillcolor("#1E90FF")
    pen.goto(-140, -5)
    pen.goto(-100, 15)
    pen.goto(100, 15)
    pen.goto(140, -5)
    pen.goto(140, -30)
    pen.goto(-140, -30)
    pen.end_fill()
    
    # Racing stripes
    pen.penup()
    pen.goto(-130, -15)
    pen.pendown()
    pen.color("white")
    pen.pensize(8)
    pen.goto(130, -15)
    
    pen.penup()
    pen.goto(-120, -5)
    pen.pendown()
    pen.pensize(5)
    pen.goto(120, -5)
    
    # Cockpit
    pen.penup()
    pen.goto(-50, -5)
    pen.pendown()
    pen.color("#333333")
    pen.begin_fill()
    pen.fillcolor("#333333")
    pen.goto(-50, 12)
    pen.goto(0, 12)
    pen.goto(0, -5)
    pen.goto(-50, -5)
    pen.end_fill()
    
    pen.penup()
    pen.goto(0, -5)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("#333333")
    pen.goto(0, 12)
    pen.goto(50, 12)
    pen.goto(50, -5)
    pen.goto(0, -5)
    pen.end_fill()
    
    # Racing wheels
    draw_circle(-80, -30, 20, "#111111")
    draw_circle(-80, -30, 12, "#DDDDDD")
    draw_circle(80, -30, 20, "#111111")
    draw_circle(80, -30, 12, "#DDDDDD")
    
    # Large spoiler
    pen.penup()
    pen.goto(100, 5)
    pen.pendown()
    pen.color("#333333")
    pen.begin_fill()
    pen.fillcolor("#333333")
    pen.goto(130, 5)
    pen.goto(130, 25)
    pen.goto(110, 30)
    pen.goto(100, 25)
    pen.goto(100, 5)
    pen.end_fill()
    
    # Headlights
    draw_circle(-135, -10, 5, "#FFFF00")
    draw_circle(-135, -10, 3, "white")
    
    # Tailpipe (flame effect)
    pen.penup()
    pen.goto(135, -20)
    pen.pendown()
    pen.color("#FF6600")
    pen.pensize(4)
    pen.goto(150, -20)
    
    screen.update()

def draw_title():
    """Draw title and instructions"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("darkblue")
    title.penup()
    title.hideturtle()
    title.goto(0, 270)
    title.write("🚗 SIMPLE CAR USING TURTLE SHAPES 🚗", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("darkblue")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -280)
    instructions.write("1=Standard Car  2=Sports Car  3=Classic Car  4=Race Car  5=Redraw | ESC=Exit",
                       align="center", font=("Arial", 10, "normal"))

current_car = 1

def draw_current():
    """Draw the currently selected car"""
    if current_car == 1:
        draw_car()
    elif current_car == 2:
        draw_sport_car()
    elif current_car == 3:
        draw_classic_car()
    elif current_car == 4:
        draw_race_car()

def set_car_1(): global current_car; current_car = 1; draw_current()
def set_car_2(): global current_car; current_car = 2; draw_current()
def set_car_3(): global current_car; current_car = 3; draw_current()
def set_car_4(): global current_car; current_car = 4; draw_current()
def redraw(): draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_car_1, "1")
screen.onkey(set_car_2, "2")
screen.onkey(set_car_3, "3")
screen.onkey(set_car_4, "4")
screen.onkey(redraw, "5")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        SIMPLE CAR USING TURTLE SHAPES")
print("=" * 60)
print()
print("4 different car designs built from basic shapes!")
print()
print("CAR DESIGNS:")
print("  1 - Standard Car: Classic sedan with windows and wheels")
print("  2 - Sports Car: Sleek design with spoiler")
print("  3 - Classic Car: Vintage style with whitewall tires")
print("  4 - Race Car: Racing stripes and aerodynamics")
print()
print("SHAPES USED:")
print("  • Rectangles - Car body, windows, spoiler")
print("  • Circles - Wheels, headlights, taillights")
print("  • Lines - Details, exhaust, ground shadow")
print("  • Polygons - Windshields, custom shapes")
print()
print("CONTROLS:")
print("  1-4 - Select car design")
print("  5   - Redraw current car")
print("  ESC - Exit program")

# Draw default car
draw_car()
screen.mainloop()