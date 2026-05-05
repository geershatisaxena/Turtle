import turtle
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Cartoon Face - Basic Shapes")
screen.bgcolor("lightblue")
screen.setup(width=800, height=800)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Color palette
colors = {
    "skin": "#FFE0BD",
    "skin_dark": "#FFD4A8",
    "eye_white": "white",
    "eye_black": "#2C2C2C",
    "pupil": "black",
    "mouth": "#E74C3C",
    "tongue": "#FF6B6B",
    "cheek": "#FFB3BA",
    "hair": "#8B4513",
    "hair_dark": "#5C3317",
    "eyebrow": "#5C3317",
    "nose": "#FFB07C",
    "hat": "#FF0000",
    "hat_band": "#FFFFFF"
}

def draw_circle(x, y, radius, color, fill=True):
    """Draw a circle at given position"""
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

def draw_arc(x, y, radius, start_angle, end_angle, color, thickness=3):
    """Draw an arc (part of a circle)"""
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(start_angle)
    pen.pendown()
    pen.color(color)
    pen.pensize(thickness)
    pen.circle(radius, end_angle - start_angle)
    pen.penup()

def draw_ellipse(x, y, width, height, color, fill=True):
    """Draw an ellipse using stretching"""
    pen.penup()
    pen.goto(x, y - height/2)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    # Draw ellipse by scaling circle
    for angle in range(0, 360, 10):
        rad = math.radians(angle)
        px = x + (width/2) * math.cos(rad)
        py = y + (height/2) * math.sin(rad)
        if angle == 0:
            pen.goto(px, py)
        else:
            pen.goto(px, py)
    
    if fill:
        pen.end_fill()
    pen.penup()

def draw_rectangle(x, y, width, height, color, fill=True):
    """Draw a rectangle"""
    pen.penup()
    pen.goto(x - width/2, y - height/2)
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

def draw_triangle(x, y, base, height, color, fill=True):
    """Draw an equilateral triangle"""
    pen.penup()
    pen.goto(x - base/2, y - height/2)
    pen.pendown()
    pen.color(color)
    if fill:
        pen.begin_fill()
        pen.fillcolor(color)
    
    for _ in range(3):
        pen.forward(base)
        pen.left(120)
    
    if fill:
        pen.end_fill()
    pen.penup()

def draw_face():
    """Draw the main cartoon face using basic shapes"""
    
    # Head (circle)
    draw_circle(0, 0, 200, colors["skin"])
    
    # Hair (semi-circle on top)
    pen.penup()
    pen.goto(-180, 100)
    pen.pendown()
    pen.color(colors["hair"])
    pen.begin_fill()
    pen.fillcolor(colors["hair"])
    pen.setheading(0)
    pen.circle(180, 180)
    pen.goto(-180, 100)
    pen.end_fill()
    pen.penup()
    
    # Hair spikes (triangles)
    spike_positions = [(-120, 160), (-60, 180), (0, 185), (60, 180), (120, 160)]
    for x, y in spike_positions:
        draw_triangle(x, y, 30, 40, colors["hair"])
    
    # Left eye (white part)
    draw_ellipse(-70, 40, 60, 70, colors["eye_white"])
    
    # Right eye (white part)
    draw_ellipse(70, 40, 60, 70, colors["eye_white"])
    
    # Left iris
    draw_circle(-70, 40, 20, colors["eye_black"])
    
    # Right iris
    draw_circle(70, 40, 20, colors["eye_black"])
    
    # Left pupil (with highlight)
    draw_circle(-65, 35, 8, colors["pupil"])
    draw_circle(-72, 48, 4, "white")
    
    # Right pupil (with highlight)
    draw_circle(75, 35, 8, colors["pupil"])
    draw_circle(68, 48, 4, "white")
    
    # Eyebrows
    pen.penup()
    pen.goto(-100, 90)
    pen.pendown()
    pen.color(colors["eyebrow"])
    pen.pensize(5)
    pen.setheading(-10)
    pen.circle(50, 60)
    pen.penup()
    
    pen.goto(100, 90)
    pen.pendown()
    pen.setheading(190)
    pen.circle(50, 60)
    pen.penup()
    
    # Nose (triangle)
    draw_triangle(0, -10, 30, 25, colors["nose"])
    
    # Nose highlight
    pen.penup()
    pen.goto(-5, 5)
    pen.dot(5, "white")
    
    # Mouth (arc - smile)
    draw_arc(0, -60, 80, 200, 340, colors["mouth"], 5)
    
    # Tongue
    pen.penup()
    pen.goto(-20, -115)
    pen.pendown()
    pen.color(colors["tongue"])
    pen.begin_fill()
    pen.fillcolor(colors["tongue"])
    pen.setheading(-90)
    pen.circle(20, 180)
    pen.end_fill()
    pen.penup()
    
    # Cheeks (ellipses)
    draw_ellipse(-110, -30, 50, 30, colors["cheek"])
    draw_ellipse(110, -30, 50, 30, colors["cheek"])
    
    # Blush dots on cheeks
    pen.penup()
    pen.goto(-115, -30)
    pen.dot(8, "#FF9999")
    pen.goto(-105, -35)
    pen.dot(6, "#FF9999")
    pen.goto(115, -30)
    pen.dot(8, "#FF9999")
    pen.goto(105, -35)
    pen.dot(6, "#FF9999")

def draw_alternative_face():
    """Draw a different cartoon face style"""
    
    # Head (square/rounded)
    draw_rectangle(0, 0, 350, 350, colors["skin"])
    
    # Eyes (large circles)
    draw_circle(-80, 50, 45, "white")
    draw_circle(80, 50, 45, "white")
    draw_circle(-80, 50, 25, "#2C2C2C")
    draw_circle(80, 50, 25, "#2C2C2C")
    draw_circle(-80, 50, 12, "black")
    draw_circle(80, 50, 12, "black")
    draw_circle(-86, 58, 6, "white")
    draw_circle(74, 58, 6, "white")
    
    # Eyebrows
    pen.penup()
    pen.goto(-115, 110)
    pen.pendown()
    pen.color("#5C3317")
    pen.pensize(6)
    pen.setheading(0)
    pen.forward(70)
    pen.penup()
    
    pen.goto(45, 110)
    pen.pendown()
    pen.forward(70)
    pen.penup()
    
    # Nose (small oval)
    draw_ellipse(0, 10, 20, 25, colors["nose"])
    
    # Mouth (open smile)
    pen.penup()
    pen.goto(-60, -50)
    pen.pendown()
    pen.color(colors["mouth"])
    pen.begin_fill()
    pen.fillcolor(colors["mouth"])
    pen.setheading(-60)
    pen.circle(60, 120)
    pen.goto(-60, -50)
    pen.end_fill()
    
    # Teeth
    pen.penup()
    pen.goto(-20, -60)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.fillcolor("white")
    pen.setheading(0)
    pen.forward(40)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
    pen.forward(20)
    pen.end_fill()
    pen.penup()
    
    # Freckles
    for x in [-40, -20, 0, 20, 40]:
        pen.goto(x - 60, -20)
        pen.dot(4, "#FFB07C")
        pen.goto(x + 60, -20)
        pen.dot(4, "#FFB07C")
    
    # Hat
    draw_rectangle(0, 140, 300, 40, colors["hat"])
    draw_rectangle(0, 120, 200, 30, colors["hat"])
    
    # Hat band
    draw_rectangle(0, 135, 310, 12, colors["hat_band"])

def draw_surprised_face():
    """Draw a surprised cartoon face"""
    
    # Head (circle)
    draw_circle(0, 0, 180, colors["skin"])
    
    # Eyes (very large circles)
    draw_circle(-60, 40, 40, "white")
    draw_circle(60, 40, 40, "white")
    draw_circle(-60, 40, 25, "black")
    draw_circle(60, 40, 25, "black")
    draw_circle(-65, 48, 10, "white")
    draw_circle(55, 48, 10, "white")
    
    # Raised eyebrows
    pen.penup()
    pen.goto(-95, 95)
    pen.pendown()
    pen.color("#5C3317")
    pen.pensize(5)
    pen.setheading(10)
    pen.circle(40, 50)
    pen.penup()
    
    pen.goto(95, 95)
    pen.pendown()
    pen.setheading(170)
    pen.circle(40, 50)
    pen.penup()
    
    # Nose
    draw_circle(0, -5, 12, colors["nose"])
    
    # Mouth (O shape - surprised)
    draw_circle(0, -80, 35, colors["mouth"])
    draw_circle(0, -80, 25, "#8B0000")
    
    # Sweat drop
    pen.penup()
    pen.goto(150, 80)
    pen.pendown()
    pen.color("#00BFFF")
    pen.begin_fill()
    pen.fillcolor("#00BFFF")
    pen.setheading(-60)
    pen.circle(10, 180)
    pen.end_fill()
    pen.penup()

def draw_cute_face():
    """Draw an anime/cute style face"""
    
    # Head (wide oval)
    draw_ellipse(0, 0, 350, 300, colors["skin"])
    
    # Blush
    draw_ellipse(-100, -20, 70, 40, colors["cheek"])
    draw_ellipse(100, -20, 70, 40, colors["cheek"])
    
    # Eyes (large with sparkle)
    draw_ellipse(-75, 50, 70, 80, "white")
    draw_ellipse(75, 50, 70, 80, "white")
    draw_circle(-75, 50, 30, "#2C2C2C")
    draw_circle(75, 50, 30, "#2C2C2C")
    
    # Eye sparkles
    draw_circle(-85, 65, 10, "white")
    draw_circle(65, 65, 10, "white")
    draw_circle(-70, 35, 6, "white")
    draw_circle(80, 35, 6, "white")
    
    # Nose (tiny)
    draw_circle(0, 5, 8, colors["nose"])
    
    # Mouth (small "w" shape)
    pen.penup()
    pen.goto(-20, -40)
    pen.pendown()
    pen.color(colors["mouth"])
    pen.pensize(4)
    pen.setheading(-30)
    pen.circle(15, 60)
    pen.setheading(210)
    pen.circle(15, 60)
    pen.penup()
    
    # Hair (bangs)
    pen.penup()
    pen.goto(-150, 150)
    pen.pendown()
    pen.color(colors["hair"])
    pen.begin_fill()
    pen.fillcolor(colors["hair"])
    pen.setheading(0)
    pen.circle(150, 90)
    pen.goto(-150, 150)
    pen.end_fill()
    pen.penup()
    
    # Side hairs
    draw_ellipse(-160, 50, 40, 100, colors["hair"])
    draw_ellipse(160, 50, 40, 100, colors["hair"])

# UI Controls
def draw_title():
    title = turtle.Turtle()
    title.speed(0)
    title.color("darkblue")
    title.penup()
    title.hideturtle()
    title.goto(0, 370)
    title.write("🎭 CARTOON FACE - BASIC SHAPES 🎭", align="center", font=("Arial", 18, "bold"))
    
    instructions = turtle.Turtle()
    instructions.speed(0)
    instructions.color("darkblue")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, -380)
    instructions.write("1=Happy Face  2=Alternative Face  3=Surprised Face  4=Cute Face | R=Redraw | ESC=Exit",
                       align="center", font=("Arial", 10, "normal"))

current_face = 1

def draw_current_face():
    """Draw the currently selected face"""
    pen.clear()
    
    if current_face == 1:
        draw_face()
    elif current_face == 2:
        draw_alternative_face()
    elif current_face == 3:
        draw_surprised_face()
    elif current_face == 4:
        draw_cute_face()
    
    screen.update()

def set_face_1(): global current_face; current_face = 1; draw_current_face()
def set_face_2(): global current_face; current_face = 2; draw_current_face()
def set_face_3(): global current_face; current_face = 3; draw_current_face()
def set_face_4(): global current_face; current_face = 4; draw_current_face()
def redraw(): draw_current_face()

# Keyboard bindings
screen.listen()
screen.onkey(set_face_1, "1")
screen.onkey(set_face_2, "2")
screen.onkey(set_face_3, "3")
screen.onkey(set_face_4, "4")
screen.onkey(redraw, "r")
screen.onkey(lambda: screen.bye(), "Escape")

draw_title()

print("=" * 60)
print("        CARTOON FACE - BASIC SHAPES")
print("=" * 60)
print()
print("Faces drawn using only basic geometric shapes!")
print()
print("FACES:")
print("  1 - Happy Face: Classic smiley with blush and eyebrows")
print("  2 - Alternative Face: Square face with hat and freckles")
print("  3 - Surprised Face: Wide eyes and O-shaped mouth")
print("  4 - Cute Face: Anime-style with sparkly eyes")
print()
print("SHAPES USED:")
print("  • Circles - Head, eyes, pupils, nose")
print("  • Arcs - Smile, eyebrows")
print("  • Ellipses - Cheeks, eye whites")
print("  • Rectangles - Hat, alternative head")
print("  • Triangles - Hair spikes, nose")
print()
print("CONTROLS:")
print("  1-4   - Select face style")
print("  R     - Redraw")
print("  ESC   - Exit")

# Draw default face
draw_face()
screen.mainloop()