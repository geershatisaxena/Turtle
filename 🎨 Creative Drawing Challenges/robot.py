import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Robot Figure - Rectangles & Circles")
screen.bgcolor("#2C3E50")  # Dark blue-gray background
screen.setup(width=900, height=800)
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

def draw_square(x, y, size, color, fill=True):
    """Draw a square"""
    draw_rectangle(x, y, size, size, color, fill)

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

def draw_line(x1, y1, x2, y2, color, width=2):
    """Draw a line between two points"""
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.color(color)
    pen.pensize(width)
    pen.goto(x2, y2)
    pen.penup()

def draw_robot_basic():
    """Draw a basic friendly robot"""
    pen.clear()
    
    # === HEAD ===
    # Head rectangle
    draw_rectangle(-60, 80, 120, 100, "#7FB3D5")  # Light blue head
    
    # Face plate (inner rectangle)
    draw_rectangle(-45, 95, 90, 70, "#D4E6F1", True)
    
    # === EYES ===
    # Left eye
    draw_circle(-25, 135, 12, "#2C3E50")
    draw_circle(-25, 135, 6, "#FFFFFF")
    
    # Right eye
    draw_circle(25, 135, 12, "#2C3E50")
    draw_circle(25, 135, 6, "#FFFFFF")
    
    # Eye highlights (sparkle)
    draw_circle(-28, 140, 2, "#FFFFFF")
    draw_circle(22, 140, 2, "#FFFFFF")
    
    # === MOUTH ===
    # Smile (line)
    draw_line(-25, 115, 25, 115, "#2C3E50", 3)
    
    # === ANTENNA ===
    draw_line(0, 180, 0, 150, "#7FB3D5", 4)
    draw_circle(0, 185, 8, "#FF6B6B")  # Antenna ball
    
    # === NECK ===
    draw_rectangle(-15, 75, 30, 15, "#5D6D7E")
    
    # === BODY ===
    draw_rectangle(-75, -50, 150, 125, "#E74C3C")  # Red body
    
    # Chest panel
    draw_rectangle(-50, -20, 100, 70, "#C0392B")
    
    # Chest buttons
    draw_circle(-25, 15, 8, "#2ECC71")  # Green button
    draw_circle(25, 15, 8, "#F1C40F")   # Yellow button
    draw_circle(0, -10, 8, "#3498DB")   # Blue button
    
    # === ARMS ===
    # Left arm
    draw_rectangle(-130, -30, 55, 40, "#7FB3D5")
    draw_circle(-130, 10, 12, "#5D6D7E")  # Shoulder joint
    draw_circle(-75, -30, 10, "#5D6D7E")  # Elbow joint
    
    # Right arm
    draw_rectangle(75, -30, 55, 40, "#7FB3D5")
    draw_circle(130, 10, 12, "#5D6D7E")   # Shoulder joint
    draw_circle(75, -30, 10, "#5D6D7E")   # Elbow joint
    
    # Hands
    draw_circle(-130, -10, 10, "#E74C3C")
    draw_circle(130, -10, 10, "#E74C3C")
    
    # === LEGS ===
    # Left leg
    draw_rectangle(-45, -150, 35, 100, "#5D6D7E")
    draw_circle(-28, -155, 15, "#34495E")  # Left foot
    
    # Right leg
    draw_rectangle(10, -150, 35, 100, "#5D6D7E")
    draw_circle(28, -155, 15, "#34495E")   # Right foot
    
    # === DECORATIONS ===
    # Belly button
    draw_circle(0, -35, 6, "#F1C40F")
    
    # Head bolts
    draw_circle(-50, 130, 4, "#5D6D7E")
    draw_circle(50, 130, 4, "#5D6D7E")
    draw_circle(-50, 105, 4, "#5D6D7E")
    draw_circle(50, 105, 4, "#5D6D7E")
    
    screen.update()

def draw_robot_warrior():
    """Draw a warrior robot with armor"""
    pen.clear()
    
    # === HEAD (helmet style) ===
    draw_rectangle(-65, 80, 130, 110, "#95A5A6")
    draw_rectangle(-55, 90, 110, 90, "#2C3E50")
    
    # Visor (single glowing eye)
    draw_rectangle(-40, 120, 80, 30, "#3498DB")
    draw_rectangle(-30, 125, 60, 20, "#85C1E9")
    
    # === ANTENNA (crest) ===
    draw_line(0, 190, -30, 210, "#E74C3C", 5)
    draw_line(0, 190, 30, 210, "#E74C3C", 5)
    draw_circle(-30, 215, 6, "#E74C3C")
    draw_circle(30, 215, 6, "#E74C3C")
    
    # === BODY (armor) ===
    draw_rectangle(-80, -60, 160, 140, "#7F8C8D")
    draw_rectangle(-70, -50, 140, 120, "#95A5A6")
    
    # Chest armor plate
    draw_rectangle(-55, -30, 110, 80, "#34495E")
    
    # Power core
    draw_circle(0, 5, 18, "#2ECC71")
    draw_circle(0, 5, 10, "#27AE60")
    draw_circle(0, 5, 5, "#FFFFFF")
    
    # Shoulder pads
    draw_rectangle(-100, -20, 30, 50, "#E74C3C")
    draw_rectangle(70, -20, 30, 50, "#E74C3C")
    
    # === ARMS (with weapons) ===
    # Left arm (cannon)
    draw_rectangle(-130, -40, 40, 35, "#95A5A6")
    draw_rectangle(-160, -35, 35, 25, "#E74C3C")
    draw_circle(-160, -22, 8, "#F1C40F")  # Cannon glow
    
    # Right arm (shield)
    draw_rectangle(90, -45, 40, 45, "#95A5A6")
    draw_rectangle(85, -50, 50, 55, "#E74C3C")
    
    # === LEGS (heavy duty) ===
    draw_rectangle(-50, -150, 40, 90, "#7F8C8D")
    draw_rectangle(10, -150, 40, 90, "#7F8C8D")
    
    # Knee joints
    draw_circle(-30, -100, 12, "#34495E")
    draw_circle(30, -100, 12, "#34495E")
    
    # Feet (claws)
    draw_rectangle(-55, -160, 50, 20, "#E74C3C")
    draw_rectangle(5, -160, 50, 20, "#E74C3C")
    
    screen.update()

def draw_robot_friendly():
    """Draw a cute, friendly helper robot"""
    pen.clear()
    
    # === HEAD ===
    draw_rectangle(-55, 90, 110, 95, "#FFB6C1")  # Pink head
    
    # Face
    draw_rectangle(-45, 100, 90, 75, "#FFF0F5")
    
    # === EYES (big anime-style) ===
    draw_circle(-25, 140, 15, "#2C3E50")
    draw_circle(25, 140, 15, "#2C3E50")
    draw_circle(-25, 140, 10, "#FFFFFF")
    draw_circle(25, 140, 10, "#FFFFFF")
    draw_circle(-22, 143, 4, "#2C3E50")
    draw_circle(28, 143, 4, "#2C3E50")
    
    # === BLUSH ===
    draw_circle(-40, 115, 8, "#FFB6C1")
    draw_circle(40, 115, 8, "#FFB6C1")
    
    # === MOUTH (happy) ===
    draw_line(-20, 115, 20, 115, "#2C3E50", 3)
    draw_line(-20, 115, -10, 108, "#2C3E50", 2)
    draw_line(20, 115, 10, 108, "#2C3E50", 2)
    
    # === EARS ===
    draw_circle(-60, 135, 15, "#FFB6C1")
    draw_circle(60, 135, 15, "#FFB6C1")
    draw_circle(-60, 135, 8, "#FF69B4")
    draw_circle(60, 135, 8, "#FF69B4")
    
    # === ANTENNA (heart-shaped) ===
    draw_line(0, 185, 0, 160, "#FF69B4", 4)
    # Heart antenna
    pen.penup()
    pen.goto(-8, 185)
    pen.pendown()
    pen.color("#FF1493")
    pen.begin_fill()
    pen.fillcolor("#FF1493")
    pen.left(45)
    pen.forward(10)
    pen.circle(5, 180)
    pen.right(90)
    pen.circle(5, 180)
    pen.forward(10)
    pen.end_fill()
    
    # === NECK ===
    draw_rectangle(-15, 80, 30, 15, "#FFB6C1")
    
    # === BODY ===
    draw_rectangle(-65, -40, 130, 120, "#FFB6C1")
    
    # Belly (lighter)
    draw_rectangle(-50, -30, 100, 100, "#FFF0F5")
    
    # Heart on chest
    pen.penup()
    pen.goto(0, -5)
    pen.pendown()
    pen.color("#FF1493")
    pen.begin_fill()
    pen.fillcolor("#FF1493")
    pen.left(45)
    pen.forward(12)
    pen.circle(6, 180)
    pen.right(90)
    pen.circle(6, 180)
    pen.forward(12)
    pen.end_fill()
    
    # === ARMS (rounded) ===
    draw_rectangle(-110, -20, 45, 35, "#FFB6C1")
    draw_rectangle(65, -20, 45, 35, "#FFB6C1")
    
    # Hands (hearts again)
    pen.penup()
    pen.goto(-90, -8)
    pen.pendown()
    pen.color("#FF1493")
    pen.begin_fill()
    pen.fillcolor("#FF1493")
    pen.left(45)
    pen.forward(8)
    pen.circle(3, 180)
    pen.right(90)
    pen.circle(3, 180)
    pen.forward(8)
    pen.end_fill()
    
    pen.penup()
    pen.goto(90, -8)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("#FF1493")
    pen.left(45)
    pen.forward(8)
    pen.circle(3, 180)
    pen.right(90)
    pen.circle(3, 180)
    pen.forward(8)
    pen.end_fill()
    
    # === LEGS ===
    draw_rectangle(-40, -150, 30, 110, "#FFB6C1")
    draw_rectangle(10, -150, 30, 110, "#FFB6C1")
    
    # Feet (shoes)
    draw_rectangle(-45, -160, 40, 20, "#FF69B4")
    draw_rectangle(5, -160, 40, 20, "#FF69B4")
    
    # Knee pads (hearts)
    pen.penup()
    pen.goto(-25, -100)
    pen.pendown()
    pen.color("#FF1493")
    pen.begin_fill()
    pen.fillcolor("#FF1493")
    pen.left(45)
    pen.forward(6)
    pen.circle(2.5, 180)
    pen.right(90)
    pen.circle(2.5, 180)
    pen.forward(6)
    pen.end_fill()
    
    pen.penup()
    pen.goto(25, -100)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("#FF1493")
    pen.left(45)
    pen.forward(6)
    pen.circle(2.5, 180)
    pen.right(90)
    pen.circle(2.5, 180)
    pen.forward(6)
    pen.end_fill()
    
    screen.update()

def draw_robot_space():
    """Draw a space explorer robot"""
    pen.clear()
    
    # === HEAD (astronaut helmet) ===
    draw_circle(0, 145, 60, "#BDC3C7")
    draw_circle(0, 145, 50, "#ECF0F1")
    
    # Visor (gold)
    draw_rectangle(-35, 120, 70, 45, "#F39C12")
    draw_rectangle(-30, 125, 60, 35, "#F1C40F")
    
    # === EYES inside visor ===
    draw_circle(-15, 140, 6, "#2C3E50")
    draw_circle(15, 140, 6, "#2C3E50")
    
    # === BODY (space suit) ===
    draw_rectangle(-60, -40, 120, 150, "#ECF0F1")
    
    # Suit details
    draw_rectangle(-50, -30, 100, 130, "#BDC3C7")
    
    # Oxygen tank (backpack)
    draw_rectangle(60, -20, 30, 100, "#95A5A6")
    draw_rectangle(-90, -20, 30, 100, "#95A5A6")
    
    # Control panel on chest
    draw_rectangle(-35, 10, 70, 50, "#34495E")
    draw_circle(-15, 30, 6, "#2ECC71")
    draw_circle(15, 30, 6, "#E74C3C")
    draw_circle(0, 15, 6, "#3498DB")
    
    # === ARMS (space suit arms) ===
    draw_rectangle(-100, -20, 40, 35, "#ECF0F1")
    draw_rectangle(60, -20, 40, 35, "#ECF0F1")
    
    # Gloves
    draw_circle(-100, -10, 12, "#95A5A6")
    draw_circle(100, -10, 12, "#95A5A6")
    
    # === LEGS ===
    draw_rectangle(-45, -150, 35, 110, "#ECF0F1")
    draw_rectangle(10, -150, 35, 110, "#ECF0F1")
    
    # Boots
    draw_rectangle(-50, -160, 45, 20, "#95A5A6")
    draw_rectangle(5, -160, 45, 20, "#95A5A6")
    
    # === DECORATIONS ===
    # Flag on arm
    draw_rectangle(85, 5, 25, 15, "#E74C3C")
    draw_rectangle(85, 5, 10, 15, "#FFFFFF")
    draw_rectangle(95, 5, 10, 15, "#3498DB")
    
    # Antenna
    draw_line(0, 200, 0, 220, "#BDC3C7", 3)
    draw_circle(0, 225, 5, "#E74C3C")
    
    screen.update()

def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 370)
    title.write("🤖 ROBOT FIGURE - RECTANGLES & CIRCLES 🤖", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("white")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -390)
    instructions.write("1=Friendly Robot  2=Warrior Robot  3=Cute Helper  4=Space Robot | ESC=Exit",
                       align="center", font=("Arial", 12, "normal"))

current_robot = 1

def draw_current():
    """Draw the currently selected robot"""
    if current_robot == 1:
        draw_robot_basic()
    elif current_robot == 2:
        draw_robot_warrior()
    elif current_robot == 3:
        draw_robot_friendly()
    elif current_robot == 4:
        draw_robot_space()

def set_robot_1(): global current_robot; current_robot = 1; draw_current()
def set_robot_2(): global current_robot; current_robot = 2; draw_current()
def set_robot_3(): global current_robot; current_robot = 3; draw_current()
def set_robot_4(): global current_robot; current_robot = 4; draw_current()

# Keyboard bindings
screen.listen()
screen.onkey(set_robot_1, "1")
screen.onkey(set_robot_2, "2")
screen.onkey(set_robot_3, "3")
screen.onkey(set_robot_4, "4")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        ROBOT FIGURE - RECTANGLES & CIRCLES")
print("=" * 60)
print()
print("4 different robot designs using only basic shapes!")
print()
print("ROBOT DESIGNS:")
print("  1 - Friendly Robot: Classic helper robot with smile")
print("  2 - Warrior Robot: Battle robot with cannon and shield")
print("  3 - Cute Helper: Adorable heart-themed robot")
print("  4 - Space Robot: Astronaut-style explorer")
print()
print("SHAPES USED:")
print("  • Rectangles - Head, body, arms, legs, chest panels")
print("  • Circles - Eyes, joints, buttons, wheels, decorations")
print("  • Lines - Antennas, smiles, details")
print("  • Custom shapes - Hearts for cute robot")
print()
print("CONTROLS:")
print("  1-4 - Select robot design")
print("  ESC - Exit program")

# Draw default robot
draw_robot_basic()
screen.mainloop()