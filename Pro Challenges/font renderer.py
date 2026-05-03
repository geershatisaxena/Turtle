import turtle
import time

# Setup the screen
screen = turtle.Screen()
screen.title("Custom Font Renderer - Turtle Lines")
screen.bgcolor("black")
screen.setup(width=1000, height=700)
screen.tracer(0)

# Create the drawing turtle
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# UI elements
info_display = turtle.Turtle()
info_display.speed(0)
info_display.color("white")
info_display.penup()
info_display.hideturtle()

# Font settings
current_color = "cyan"
current_size = 20
current_text = "TURTLE"
spacing = 5

# Character definitions using line drawing (each character is a list of drawing commands)
# Each command: (pen_down, x_offset, y_offset)
# or for arc: ("arc", radius, angle, direction)

def draw_A(x, y, size):
    """Draw letter A"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    # Left diagonal
    pen.goto(x + size * 0.5, y + size)
    # Right diagonal
    pen.goto(x + size, y)
    pen.penup()
    # Horizontal bar
    pen.goto(x + size * 0.2, y + size * 0.5)
    pen.pendown()
    pen.goto(x + size * 0.8, y + size * 0.5)
    pen.penup()

def draw_B(x, y, size):
    """Draw letter B"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    # Vertical line
    pen.goto(x, y + size)
    # Top curve
    pen.goto(x + size * 0.7, y + size * 0.8)
    pen.goto(x + size, y + size * 0.6)
    pen.goto(x + size, y + size * 0.5)
    # Middle bar
    pen.goto(x, y + size * 0.5)
    # Bottom curve
    pen.goto(x + size * 0.7, y + size * 0.3)
    pen.goto(x + size, y + size * 0.1)
    pen.goto(x, y)
    pen.penup()

def draw_C(x, y, size):
    """Draw letter C"""
    pen.penup()
    pen.goto(x + size, y)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y + size)
    pen.goto(x + size, y + size)
    pen.penup()

def draw_D(x, y, size):
    """Draw letter D"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x + size * 0.7, y + size)
    pen.goto(x + size, y + size * 0.5)
    pen.goto(x + size * 0.7, y)
    pen.goto(x, y)
    pen.penup()

def draw_E(x, y, size):
    """Draw letter E"""
    pen.penup()
    pen.goto(x + size, y)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y + size)
    pen.goto(x + size, y + size)
    pen.penup()
    pen.goto(x, y + size * 0.5)
    pen.pendown()
    pen.goto(x + size * 0.7, y + size * 0.5)
    pen.penup()

def draw_F(x, y, size):
    """Draw letter F"""
    pen.penup()
    pen.goto(x + size, y)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y + size)
    pen.goto(x + size, y + size)
    pen.penup()
    pen.goto(x, y + size * 0.5)
    pen.pendown()
    pen.goto(x + size * 0.7, y + size * 0.5)
    pen.penup()

def draw_G(x, y, size):
    """Draw letter G"""
    pen.penup()
    pen.goto(x + size, y)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y + size)
    pen.goto(x + size, y + size)
    pen.goto(x + size, y + size * 0.5)
    pen.goto(x + size * 0.6, y + size * 0.5)
    pen.penup()

def draw_H(x, y, size):
    """Draw letter H"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y + size)
    pen.penup()
    pen.goto(x + size, y)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.penup()
    pen.goto(x, y + size * 0.5)
    pen.pendown()
    pen.goto(x + size, y + size * 0.5)
    pen.penup()

def draw_I(x, y, size):
    """Draw letter I"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.penup()
    pen.goto(x + size * 0.5, y + size)
    pen.pendown()
    pen.goto(x + size * 0.5, y)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + size, y)
    pen.penup()

def draw_J(x, y, size):
    """Draw letter J"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.penup()
    pen.goto(x + size, y + size)
    pen.pendown()
    pen.goto(x + size, y + size * 0.3)
    pen.goto(x + size * 0.5, y)
    pen.goto(x, y + size * 0.3)
    pen.penup()

def draw_K(x, y, size):
    """Draw letter K"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y + size)
    pen.penup()
    pen.goto(x, y + size * 0.6)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.penup()
    pen.goto(x, y + size * 0.4)
    pen.pendown()
    pen.goto(x + size, y)
    pen.penup()

def draw_L(x, y, size):
    """Draw letter L"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x + size, y)
    pen.penup()

def draw_M(x, y, size):
    """Draw letter M"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x + size * 0.5, y + size * 0.5)
    pen.goto(x + size, y + size)
    pen.goto(x + size, y)
    pen.penup()

def draw_N(x, y, size):
    """Draw letter N"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x + size, y)
    pen.goto(x + size, y + size)
    pen.penup()

def draw_O(x, y, size):
    """Draw letter O"""
    pen.penup()
    pen.goto(x + size, y)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y + size)
    pen.goto(x + size, y + size)
    pen.goto(x + size, y)
    pen.penup()

def draw_P(x, y, size):
    """Draw letter P"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x + size * 0.7, y + size)
    pen.goto(x + size, y + size * 0.7)
    pen.goto(x, y + size * 0.5)
    pen.penup()

def draw_Q(x, y, size):
    """Draw letter Q"""
    pen.penup()
    pen.goto(x + size, y)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y + size)
    pen.goto(x + size, y + size)
    pen.goto(x + size, y)
    pen.penup()
    pen.goto(x + size * 0.6, y + size * 0.3)
    pen.pendown()
    pen.goto(x + size, y)
    pen.penup()

def draw_R(x, y, size):
    """Draw letter R"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x + size * 0.7, y + size)
    pen.goto(x + size, y + size * 0.7)
    pen.goto(x, y + size * 0.5)
    pen.penup()
    pen.goto(x + size * 0.5, y + size * 0.4)
    pen.pendown()
    pen.goto(x + size, y)
    pen.penup()

def draw_S(x, y, size):
    """Draw letter S"""
    pen.penup()
    pen.goto(x + size, y + size)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x, y + size * 0.6)
    pen.goto(x + size, y + size * 0.4)
    pen.goto(x + size, y)
    pen.goto(x, y)
    pen.penup()

def draw_T(x, y, size):
    """Draw letter T"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.penup()
    pen.goto(x + size * 0.5, y + size)
    pen.pendown()
    pen.goto(x + size * 0.5, y)
    pen.penup()

def draw_U(x, y, size):
    """Draw letter U"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x + size, y)
    pen.goto(x + size, y + size)
    pen.penup()

def draw_V(x, y, size):
    """Draw letter V"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size * 0.5, y)
    pen.goto(x + size, y + size)
    pen.penup()

def draw_W(x, y, size):
    """Draw letter W"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size * 0.3, y)
    pen.goto(x + size * 0.5, y + size * 0.4)
    pen.goto(x + size * 0.7, y)
    pen.goto(x + size, y + size)
    pen.penup()

def draw_X(x, y, size):
    """Draw letter X"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size, y)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.penup()

def draw_Y(x, y, size):
    """Draw letter Y"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size * 0.5, y + size * 0.5)
    pen.goto(x + size, y + size)
    pen.penup()
    pen.goto(x + size * 0.5, y + size * 0.5)
    pen.pendown()
    pen.goto(x + size * 0.5, y)
    pen.penup()

def draw_Z(x, y, size):
    """Draw letter Z"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.goto(x, y)
    pen.goto(x + size, y)
    pen.penup()

# Number definitions
def draw_0(x, y, size):
    """Draw number 0"""
    pen.penup()
    pen.goto(x + size, y)
    pen.pendown()
    pen.goto(x, y)
    pen.goto(x, y + size)
    pen.goto(x + size, y + size)
    pen.goto(x + size, y)
    pen.penup()

def draw_1(x, y, size):
    """Draw number 1"""
    pen.penup()
    pen.goto(x + size * 0.3, y + size)
    pen.pendown()
    pen.goto(x + size * 0.5, y + size)
    pen.goto(x + size * 0.5, y)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + size, y)
    pen.penup()

def draw_2(x, y, size):
    """Draw number 2"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.goto(x + size, y + size * 0.5)
    pen.goto(x, y + size * 0.5)
    pen.goto(x, y)
    pen.goto(x + size, y)
    pen.penup()

def draw_3(x, y, size):
    """Draw number 3"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.goto(x + size, y + size * 0.5)
    pen.goto(x + size * 0.5, y + size * 0.5)
    pen.goto(x + size, y + size * 0.5)
    pen.goto(x + size, y)
    pen.goto(x, y)
    pen.penup()

def draw_4(x, y, size):
    """Draw number 4"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x, y + size * 0.5)
    pen.goto(x + size, y + size * 0.5)
    pen.penup()
    pen.goto(x + size, y + size)
    pen.pendown()
    pen.goto(x + size, y)
    pen.penup()

def draw_5(x, y, size):
    """Draw number 5"""
    pen.penup()
    pen.goto(x + size, y + size)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x, y + size * 0.5)
    pen.goto(x + size, y + size * 0.5)
    pen.goto(x + size, y)
    pen.goto(x, y)
    pen.penup()

def draw_6(x, y, size):
    """Draw number 6"""
    pen.penup()
    pen.goto(x + size, y + size)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x, y)
    pen.goto(x + size, y)
    pen.goto(x + size, y + size * 0.5)
    pen.goto(x, y + size * 0.5)
    pen.penup()

def draw_7(x, y, size):
    """Draw number 7"""
    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.goto(x + size, y + size)
    pen.goto(x + size * 0.5, y)
    pen.penup()

def draw_8(x, y, size):
    """Draw number 8"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x, y + size)
    pen.goto(x + size, y + size)
    pen.goto(x + size, y)
    pen.goto(x, y)
    pen.penup()
    pen.goto(x, y + size * 0.5)
    pen.pendown()
    pen.goto(x + size, y + size * 0.5)
    pen.penup()

def draw_9(x, y, size):
    """Draw number 9"""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + size, y)
    pen.goto(x + size, y + size)
    pen.goto(x, y + size)
    pen.goto(x, y + size * 0.5)
    pen.goto(x + size, y + size * 0.5)
    pen.penup()

# Character mapping
char_drawers = {
    'A': draw_A, 'B': draw_B, 'C': draw_C, 'D': draw_D, 'E': draw_E,
    'F': draw_F, 'G': draw_G, 'H': draw_H, 'I': draw_I, 'J': draw_J,
    'K': draw_K, 'L': draw_L, 'M': draw_M, 'N': draw_N, 'O': draw_O,
    'P': draw_P, 'Q': draw_Q, 'R': draw_R, 'S': draw_S, 'T': draw_T,
    'U': draw_U, 'V': draw_V, 'W': draw_W, 'X': draw_X, 'Y': draw_Y,
    'Z': draw_Z,
    '0': draw_0, '1': draw_1, '2': draw_2, '3': draw_3, '4': draw_4,
    '5': draw_5, '6': draw_6, '7': draw_7, '8': draw_8, '9': draw_9
}

def render_text(text, x, y, size, color, spacing=5):
    """Render a string of text using custom font"""
    pen.color(color)
    pen.pensize(max(2, size // 10))
    
    current_x = x
    for char in text.upper():
        if char in char_drawers:
            char_drawers[char](current_x, y, size)
            current_x += size + spacing
        elif char == ' ':
            current_x += size + spacing

def update_info():
    """Update on-screen information"""
    info_display.clear()
    info_display.goto(-450, 320)
    info_display.write("CUSTOM FONT RENDERER - Turtle Lines", font=("Arial", 14, "bold"))
    info_display.goto(-450, 295)
    info_display.write(f"Text: {current_text} | Color: {current_color} | Size: {current_size}", 
                       font=("Arial", 10, "normal"))
    info_display.goto(-450, 270)
    info_display.write("Type your text in the console window!", font=("Arial", 10, "normal"))

def draw_demo():
    """Draw a demo of all characters"""
    pen.clear()
    y_offset = 150
    render_text("ABCDEFGHIJKLMNOPQRSTUVWXYZ", -400, y_offset + 60, 15, "cyan", 3)
    render_text("0123456789", -400, y_offset + 20, 15, "yellow", 3)
    render_text("TURTLE GRAPHICS", -400, y_offset - 30, 20, "lime", 5)
    render_text("CUSTOM FONT RENDERER", -400, y_offset - 80, 18, "magenta", 5)
    update_info()

def clear_screen():
    """Clear all drawings"""
    pen.clear()
    update_info()

def change_color():
    """Cycle through colors"""
    global current_color
    colors = ["cyan", "lime", "yellow", "magenta", "orange", "pink", "white", "red", "blue"]
    current_index = colors.index(current_color) if current_color in colors else 0
    current_color = colors[(current_index + 1) % len(colors)]

def increase_size():
    """Increase font size"""
    global current_size
    current_size = min(current_size + 5, 50)
    clear_screen()
    render_text(current_text, -400, 0, current_size, current_color, 8)
    update_info()

def decrease_size():
    """Decrease font size"""
    global current_size
    current_size = max(current_size - 5, 10)
    clear_screen()
    render_text(current_text, -400, 0, current_size, current_color, 8)
    update_info()

def set_text():
    """Get text input from user"""
    global current_text
    user_text = screen.textinput("Enter Text", "Type something to render:")
    if user_text:
        current_text = user_text[:30]  # Limit length
        clear_screen()
        render_text(current_text, -400, 0, current_size, current_color, 8)
        update_info()

# Draw border
def draw_border():
    border = turtle.Turtle()
    border.speed(0)
    border.color("gray")
    border.penup()
    border.goto(-470, -330)
    border.pendown()
    border.pensize(2)
    for _ in range(2):
        border.forward(940)
        border.right(90)
        border.forward(680)
        border.right(90)
    border.hideturtle()

# Title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 340)
title.write("CUSTOM FONT RENDERER", align="center", font=("Arial", 18, "bold"))

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("gray")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, -320)
instructions.write("T: Type Text | C: Change Color | +/-: Size | D: Demo | ESC: Exit", 
                   align="center", font=("Arial", 12, "normal"))

# Draw initial elements
draw_border()
draw_demo()

# Keyboard bindings
screen.listen()
screen.onkey(set_text, "t")
screen.onkey(change_color, "c")
screen.onkey(increase_size, "plus")
screen.onkey(increase_size, "equal")
screen.onkey(decrease_size, "minus")
screen.onkey(lambda: [clear_screen(), draw_demo()], "d")
screen.onkey(lambda: screen.bye(), "Escape")

print("=" * 50)
print("     CUSTOM FONT RENDERER")
print("=" * 50)
print()
print("Renders text using turtle line drawing (no built-in fonts!)")
print()
print("CONTROLS:")
print("  T     - Type custom text in console window")
print("  C     - Change color")
print("  +/-   - Increase/Decrease font size")
print("  D     - Demo (show all characters)")
print("  ESC   - Exit program")
print()
print("Letters A-Z and numbers 0-9 are available!")

screen.mainloop()