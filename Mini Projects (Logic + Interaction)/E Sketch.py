import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Etch-A-Sketch Drawing Tool")
screen.bgcolor("lightgray")
screen.setup(width=900, height=700)
screen.tracer(0)

# Create the drawing pen (etch-a-sketch stylus)
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(0)
pen.pensize(3)
pen.color("black")
pen.penup()

# Create the etch-a-sketch frame
frame = turtle.Turtle()
frame.speed(0)
frame.color("darkred")
frame.penup()
frame.goto(-350, 280)
frame.pendown()
frame.pensize(8)
frame.begin_fill()
frame.fillcolor("darkred")
for _ in range(2):
    frame.forward(700)
    frame.right(90)
    frame.forward(550)
    frame.right(90)
frame.end_fill()
frame.penup()

# Inner screen (drawing area)
inner_screen = turtle.Turtle()
inner_screen.speed(0)
inner_screen.color("black")
inner_screen.penup()
inner_screen.goto(-340, 270)
inner_screen.pendown()
inner_screen.pensize(3)
for _ in range(2):
    inner_screen.forward(680)
    inner_screen.right(90)
    inner_screen.forward(530)
    inner_screen.right(90)
inner_screen.penup()
inner_screen.hideturtle()

# Knobs visual
left_knob = turtle.Turtle()
left_knob.speed(0)
left_knob.shape("circle")
left_knob.color("silver")
left_knob.shapesize(2, 2)
left_knob.penup()
left_knob.goto(-280, -300)

right_knob = turtle.Turtle()
right_knob.speed(0)
right_knob.shape("circle")
right_knob.color("silver")
right_knob.shapesize(2, 2)
right_knob.penup()
right_knob.goto(280, -300)

# Title on the frame
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 310)
title.write("ETCH-A-SKETCH", align="center", font=("Arial", 18, "bold"))

# Instructions display
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("white")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, -320)
instructions.write("ARROW KEYS: Draw Lines | SPACE: Clear | C: Change Color | +/-: Pen Size | ESC: Exit",
                   align="center", font=("Arial", 12, "normal"))

# Drawing state
drawing = False
current_color = "black"
colors = ["black", "red", "blue", "green", "orange", "purple", "cyan", "magenta", "yellow", "pink"]
color_index = 0

# Position tracking
x, y = 0, 0
pen.goto(0, 0)
pen.pendown()
drawing = True

def update_ui():
    """Update color and status display"""
    status.clear()
    status.goto(-330, -350)
    status.write(f"Color: {current_color.upper()} | Pen Size: {pen.pensize()}",
                 font=("Arial", 10, "normal"))

# Movement functions
def move_up():
    if drawing:
        pen.setheading(90)
        pen.forward(10)

def move_down():
    if drawing:
        pen.setheading(270)
        pen.forward(10)

def move_left():
    if drawing:
        pen.setheading(180)
        pen.forward(10)

def move_right():
    if drawing:
        pen.setheading(0)
        pen.forward(10)

def clear_screen():
    """Clear the drawing area"""
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    update_ui()

def change_color():
    """Cycle through colors"""
    global current_color, color_index
    color_index = (color_index + 1) % len(colors)
    current_color = colors[color_index]
    pen.color(current_color)
    update_ui()

def increase_pen_size():
    """Increase pen thickness"""
    new_size = min(pen.pensize() + 2, 20)
    pen.pensize(new_size)
    update_ui()

def decrease_pen_size():
    """Decrease pen thickness"""
    new_size = max(pen.pensize() - 2, 1)
    pen.pensize(new_size)
    update_ui()

def toggle_drawing():
    """Toggle pen up/down (lift stylus)"""
    global drawing
    drawing = not drawing
    if drawing:
        pen.pendown()
    else:
        pen.penup()
    update_ui()

def reset_position():
    """Reset pen to center without clearing drawing"""
    pen.penup()
    pen.goto(0, 0)
    if drawing:
        pen.pendown()
    update_ui()

def shake_to_clear():
    """Simulate shaking the Etch-a-Sketch to clear"""
    # Animate shake effect
    original_pos = pen.pos()
    for _ in range(5):
        pen.penup()
        pen.goto(10, 10)
        screen.update()
        pen.goto(-10, -10)
        screen.update()
    pen.goto(original_pos)
    clear_screen()
    if drawing:
        pen.pendown()

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(clear_screen, "space")
screen.onkey(change_color, "c")
screen.onkey(increase_pen_size, "plus")
screen.onkey(increase_pen_size, "equal")
screen.onkey(decrease_pen_size, "minus")
screen.onkey(toggle_drawing, "p")
screen.onkey(reset_position, "r")
screen.onkey(shake_to_clear, "s")
screen.onkey(lambda: screen.bye(), "Escape")

# Status display
status = turtle.Turtle()
status.speed(0)
status.color("white")
status.penup()
status.hideturtle()

# Console instructions
print("=== ETCH-A-SKETCH DRAWING TOOL ===")
print()
print("CONTROLS:")
print("  Arrow Keys  - Draw lines (move the turtle)")
print("  SPACE       - Clear the screen")
print("  C           - Change color")
print("  +/-         - Increase/Decrease pen size")
print("  P           - Toggle pen up/down (lift stylus)")
print("  R           - Reset position to center")
print("  S           - Shake to clear (with animation)")
print("  ESC         - Exit program")
print()
print("Tip: Keep the arrow keys pressed for continuous drawing!")
print("The classic Etch-a-Sketch feel - press C to change colors!")

# Initial setup
update_ui()
screen.update()

# Keep window open
screen.mainloop()