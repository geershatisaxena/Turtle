import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Keyboard Arrow Drawing - Interactive Art")
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.shape("circle")
pen.shapesize(1.5, 1.5)

# Drawing state
drawing = False
current_color = "cyan"
pen_size = 3
current_shape = "circle"
show_trail = False
rainbow_mode = False
rainbow_index = 0

# Color palette
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime", "white"]
color_index = 2  # Start with cyan

# Trail particles
trail_particles = []

# Position tracking for movement
x, y = 0, 0
angle = 0

class TrailParticle:
    def __init__(self, x, y, color, size):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.shapesize(size/10, size/10)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.life = 30
        self.age = 0
        
    def update(self):
        self.age += 1
        if self.age > self.life:
            self.turtle.hideturtle()
            self.turtle.clear()
            return False
        # Fade out
        alpha = 1 - (self.age / self.life)
        self.turtle.shapesize(alpha * 0.3, alpha * 0.3)
        return True

def create_trail(x, y):
    """Create a trail particle"""
    if show_trail:
        particle = TrailParticle(x, y, current_color, pen_size)
        trail_particles.append(particle)

def update_trails():
    """Update all trail particles"""
    for particle in trail_particles[:]:
        if not particle.update():
            trail_particles.remove(particle)

def draw_circle_shape(x, y, size):
    """Draw a circle stamp"""
    pen.penup()
    pen.goto(x, y)
    pen.color(current_color)
    pen.dot(size * 2)

def draw_square_shape(x, y, size):
    """Draw a square stamp"""
    pen.penup()
    pen.goto(x - size, y - size)
    pen.pendown()
    pen.color(current_color)
    pen.begin_fill()
    pen.fillcolor(current_color)
    for _ in range(4):
        pen.forward(size * 2)
        pen.left(90)
    pen.end_fill()
    pen.penup()

def draw_triangle_shape(x, y, size):
    """Draw a triangle stamp"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.color(current_color)
    pen.begin_fill()
    pen.fillcolor(current_color)
    for _ in range(3):
        pen.forward(size * 2)
        pen.left(120)
    pen.end_fill()
    pen.penup()

def draw_star_shape(x, y, size):
    """Draw a star stamp"""
    pen.penup()
    pen.goto(x, y - size)
    pen.pendown()
    pen.color(current_color)
    pen.begin_fill()
    pen.fillcolor(current_color)
    for _ in range(5):
        pen.forward(size * 1.5)
        pen.right(144)
        pen.forward(size * 1.5)
        pen.left(72)
    pen.end_fill()
    pen.penup()

def draw_heart_shape(x, y, size):
    """Draw a heart stamp"""
    pen.penup()
    pen.goto(x, y - size)
    pen.setheading(0)
    pen.pendown()
    pen.color(current_color)
    pen.begin_fill()
    pen.fillcolor(current_color)
    pen.left(45)
    pen.forward(size)
    pen.circle(size/2, 180)
    pen.right(90)
    pen.circle(size/2, 180)
    pen.forward(size)
    pen.end_fill()
    pen.penup()

def draw_shape(x, y):
    """Draw the current shape at position"""
    size = pen_size
    if current_shape == "circle":
        draw_circle_shape(x, y, size)
    elif current_shape == "square":
        draw_square_shape(x, y, size)
    elif current_shape == "triangle":
        draw_triangle_shape(x, y, size)
    elif current_shape == "star":
        draw_star_shape(x, y, size)
    elif current_shape == "heart":
        draw_heart_shape(x, y, size)

def move_up():
    """Move turtle up and draw"""
    global y
    y += pen_size
    if drawing:
        pen.goto(x, y)
        draw_shape(x, y)
        create_trail(x, y)
    else:
        pen.goto(x, y)
    update_ui()

def move_down():
    """Move turtle down and draw"""
    global y
    y -= pen_size
    if drawing:
        pen.goto(x, y)
        draw_shape(x, y)
        create_trail(x, y)
    else:
        pen.goto(x, y)
    update_ui()

def move_left():
    """Move turtle left and draw"""
    global x
    x -= pen_size
    if drawing:
        pen.goto(x, y)
        draw_shape(x, y)
        create_trail(x, y)
    else:
        pen.goto(x, y)
    update_ui()

def move_right():
    """Move turtle right and draw"""
    global x
    x += pen_size
    if drawing:
        pen.goto(x, y)
        draw_shape(x, y)
        create_trail(x, y)
    else:
        pen.goto(x, y)
    update_ui()

def toggle_drawing():
    """Toggle drawing mode on/off"""
    global drawing
    drawing = not drawing
    if drawing:
        pen.color(current_color)
        pen.pensize(pen_size)
        update_ui("DRAWING")
    else:
        update_ui("PEN UP")

def change_color():
    """Cycle through colors"""
    global current_color, color_index, rainbow_mode, rainbow_index
    if rainbow_mode:
        rainbow_mode = False
    color_index = (color_index + 1) % len(colors)
    current_color = colors[color_index]
    pen.color(current_color)
    update_ui(f"Color: {current_color.upper()}")

def previous_color():
    """Go to previous color"""
    global current_color, color_index, rainbow_mode
    if rainbow_mode:
        rainbow_mode = False
    color_index = (color_index - 1) % len(colors)
    current_color = colors[color_index]
    pen.color(current_color)
    update_ui(f"Color: {current_color.upper()}")

def increase_size():
    """Increase pen/shape size"""
    global pen_size
    pen_size = min(pen_size + 2, 30)
    pen.pensize(pen_size)
    update_ui(f"Size: {pen_size}")

def decrease_size():
    """Decrease pen/shape size"""
    global pen_size
    pen_size = max(pen_size - 2, 2)
    pen.pensize(pen_size)
    update_ui(f"Size: {pen_size}")

def next_shape():
    """Cycle through shapes"""
    global current_shape
    shapes = ["circle", "square", "triangle", "star", "heart"]
    idx = shapes.index(current_shape)
    current_shape = shapes[(idx + 1) % len(shapes)]
    update_ui(f"Shape: {current_shape.upper()}")

def toggle_rainbow():
    """Toggle rainbow mode"""
    global rainbow_mode, color_index
    rainbow_mode = not rainbow_mode
    if rainbow_mode:
        update_ui("🌈 RAINBOW MODE ON 🌈")
    else:
        update_ui("Rainbow mode OFF")

def clear_screen():
    """Clear all drawings"""
    pen.clear()
    # Clear trail particles
    for particle in trail_particles:
        particle.turtle.hideturtle()
    trail_particles.clear()
    update_ui("Screen Cleared!")

def reset_position():
    """Reset turtle position to center"""
    global x, y
    x, y = 0, 0
    pen.goto(x, y)
    update_ui("Position Reset")

def toggle_trail():
    """Toggle trail effect"""
    global show_trail
    show_trail = not show_trail
    update_ui(f"Trail: {'ON' if show_trail else 'OFF'}")

def update_ui(message=None):
    """Update the UI display"""
    ui_display.clear()
    ui_display.goto(-480, 360)
    ui_display.write("🎨 KEYBOARD ARROW DRAWING 🎨", font=("Arial", 14, "bold"))
    ui_display.goto(-480, 335)
    status = "DRAWING" if drawing else "PEN UP"
    ui_display.write(f"Status: {status} | Color: {current_color.upper()} | Size: {pen_size} | Shape: {current_shape.upper()}", 
                     font=("Arial", 10, "normal"))
    ui_display.goto(-480, 310)
    ui_display.write("Controls: Arrow Keys=Move/Draw | Space=Pen Up/Down | R=Rainbow | C/T=Next/Prev Color | +/-=Size | S=Shape | D=Clear | P=Reset | L=Trail | ESC=Exit",
                     font=("Arial", 8, "normal"))
    
    if message:
        msg_display.goto(0, -350)
        msg_display.clear()
        msg_display.write(message, align="center", font=("Arial", 12, "bold"))
        screen.ontimer(lambda: msg_display.clear(), 1500)

def update_rainbow():
    """Update rainbow color cycle"""
    global rainbow_index, current_color, color_index
    if rainbow_mode and drawing:
        rainbow_index += 0.5
        color_index = int(rainbow_index) % len(colors)
        current_color = colors[color_index]
        pen.color(current_color)
        update_ui()

def animate():
    """Main animation loop"""
    update_rainbow()
    update_trails()
    screen.update()
    screen.ontimer(animate, 50)

# Create UI turtles
ui_display = turtle.Turtle()
ui_display.speed(0)
ui_display.color("white")
ui_display.penup()
ui_display.hideturtle()

msg_display = turtle.Turtle()
msg_display.speed(0)
msg_display.color("yellow")
msg_display.penup()
msg_display.hideturtle()

# Draw border
border = turtle.Turtle()
border.speed(0)
border.color("gray")
border.penup()
border.hideturtle()
border.goto(-490, -370)
border.pendown()
border.pensize(2)
for _ in range(2):
    border.forward(980)
    border.right(90)
    border.forward(760)
    border.right(90)

# Keyboard bindings - Movement
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Action bindings
screen.onkey(toggle_drawing, "space")
screen.onkey(change_color, "c")
screen.onkey(previous_color, "t")
screen.onkey(increase_size, "plus")
screen.onkey(increase_size, "equal")
screen.onkey(decrease_size, "minus")
screen.onkey(next_shape, "s")
screen.onkey(toggle_rainbow, "r")
screen.onkey(clear_screen, "d")
screen.onkey(reset_position, "p")
screen.onkey(toggle_trail, "l")
screen.onkey(lambda: screen.bye(), "Escape")

# Initial setup
pen.goto(0, 0)
pen.color(current_color)
pen.pensize(pen_size)
update_ui()

print("=" * 60)
print("        KEYBOARD ARROW DRAWING")
print("=" * 60)
print()
print("Create art using only your keyboard!")
print()
print("MOVEMENT & DRAWING:")
print("  ⬆️ Arrow Up    - Move up (draws if pen is down)")
print("  ⬇️ Arrow Down  - Move down (draws if pen is down)")
print("  ⬅️ Arrow Left  - Move left (draws if pen is down)")
print("  ➡️ Arrow Right - Move right (draws if pen is down)")
print()
print("SHAPES (Press S to cycle):")
print("  • Circle • Square • Triangle • Star • Heart")
print()
print("CONTROLS:")
print("  SPACE - Toggle pen up/down")
print("  C     - Next color")
print("  T     - Previous color")
print("  R     - Rainbow mode (colors cycle automatically)")
print("  +/-   - Increase/Decrease brush/shape size")
print("  S     - Change drawing shape")
print("  D     - Clear entire drawing")
print("  P     - Reset position to center")
print("  L     - Toggle trail effect")
print("  ESC   - Exit program")
print()
print("Press SPACE to start drawing, then use arrow keys!")

# Start animation
animate()
screen.mainloop()