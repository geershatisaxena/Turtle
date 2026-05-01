import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Keyboard-Controlled Turtle Movement")
screen.bgcolor("darkblue")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off animation for smoother movement

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("lime")
player.penup()
player.speed(0)

# Movement variables
moving_forward = False
moving_backward = False
rotating_left = False
rotating_right = False

# Speed settings
move_speed = 5
rotate_speed = 10

# Trail drawing mode
drawing_mode = False

# Create UI display
ui_display = turtle.Turtle()
ui_display.speed(0)
ui_display.color("white")
ui_display.penup()
ui_display.hideturtle()

# Create decoration stars
stars = []
for _ in range(50):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("yellow")
    star.shapesize(0.3)
    star.penup()
    star.goto(random.randint(-380, 380), random.randint(-280, 280))
    stars.append(star)

def update_ui():
    """Update the on-screen information display"""
    ui_display.clear()
    ui_display.goto(-380, 260)
    ui_display.write(f"Position: ({int(player.xcor())}, {int(player.ycor())}) | "
                     f"Angle: {int(player.heading())}° | "
                     f"Drawing: {'ON' if drawing_mode else 'OFF'} | "
                     f"Speed: {move_speed}",
                     font=("Arial", 10, "normal"))

# Movement control functions
def start_forward():
    global moving_forward
    moving_forward = True

def stop_forward():
    global moving_forward
    moving_forward = False

def start_backward():
    global moving_backward
    moving_backward = True

def stop_backward():
    global moving_backward
    moving_backward = False

def start_rotate_left():
    global rotating_left
    rotating_left = True

def stop_rotate_left():
    global rotating_left
    rotating_left = False

def start_rotate_right():
    global rotating_right
    rotating_right = True

def stop_rotate_right():
    global rotating_right
    rotating_right = False

# Action functions
def toggle_pen():
    """Toggle drawing mode on/off"""
    global drawing_mode
    if drawing_mode:
        player.penup()
        drawing_mode = False
    else:
        player.pendown()
        drawing_mode = True
    update_ui()

def change_color():
    """Change turtle color"""
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "white"]
    current_color = player.color()[0]
    next_index = (colors.index(current_color) + 1) % len(colors)
    player.color(colors[next_index])
    update_ui()

def increase_speed():
    global move_speed
    move_speed = min(move_speed + 1, 15)
    update_ui()

def decrease_speed():
    global move_speed
    move_speed = max(move_speed - 1, 2)
    update_ui()

def clear_drawing():
    """Clear all drawings but keep turtle position"""
    player.clear()
    update_ui()

def reset_position():
    """Reset turtle to center with default settings"""
    was_drawing = drawing_mode
    if was_drawing:
        player.penup()
    player.goto(0, 0)
    player.setheading(0)
    player.clear()
    if was_drawing:
        player.pendown()
    update_ui()

def teleport_to_click(x, y):
    """Teleport turtle to mouse click position"""
    was_drawing = drawing_mode
    if was_drawing:
        player.penup()
    player.goto(x, y)
    if was_drawing:
        player.pendown()
    update_ui()

def quit_game():
    """Exit the game"""
    screen.bye()

# Keyboard bindings
screen.listen()

# Movement bindings (press and hold)
screen.onkeypress(start_forward, "Up")
screen.onkeyrelease(stop_forward, "Up")
screen.onkeypress(start_backward, "Down")
screen.onkeyrelease(stop_backward, "Down")
screen.onkeypress(start_rotate_left, "Left")
screen.onkeyrelease(stop_rotate_left, "Left")
screen.onkeypress(start_rotate_right, "Right")
screen.onkeyrelease(stop_rotate_right, "Right")

# Action bindings (press once)
screen.onkey(toggle_pen, "space")
screen.onkey(change_color, "c")
screen.onkey(increase_speed, "plus")
screen.onkey(increase_speed, "equal")  # For keyboards without separate plus key
screen.onkey(decrease_speed, "minus")
screen.onkey(clear_drawing, "Delete")
screen.onkey(clear_drawing, "d")
screen.onkey(reset_position, "r")
screen.onkey(quit_game, "Escape")

screen.onclick(teleport_to_click)

# Initial UI and instructions
update_ui()

# Print instructions to console
print("=== KEYBOARD-CONTROLLED TURTLE MOVEMENT SYSTEM ===")
print()
print("MOVEMENT CONTROLS:")
print("  Arrow Up    - Move forward (hold)")
print("  Arrow Down  - Move backward (hold)")
print("  Arrow Left  - Rotate left (hold)")
print("  Arrow Right - Rotate right (hold)")
print()
print("ACTION CONTROLS:")
print("  Space       - Toggle drawing mode (pen up/down)")
print("  C           - Change turtle color")
print("  + or =      - Increase movement speed")
print("  -           - Decrease movement speed")
print("  D or Delete - Clear all drawings")
print("  R           - Reset position to center")
print("  Click       - Teleport to mouse position")
print("  Escape      - Exit program")
print()
print("Try drawing shapes by moving while drawing mode is ON!")
print("The turtle leaves a trail when drawing mode is active.")

def move_turtle():
    """Update turtle position based on current movement flags"""
    if moving_forward:
        player.forward(move_speed)
    if moving_backward:
        player.backward(move_speed)
    if rotating_left:
        player.left(rotate_speed)
    if rotating_right:
        player.right(rotate_speed)
    
    # Keep turtle on screen (wrap around edges)
    x = player.xcor()
    y = player.ycor()
    
    if x > 390:
        player.setx(-390)
    elif x < -390:
        player.setx(390)
    if y > 290:
        player.sety(-290)
    elif y < -290:
        player.sety(290)
    
    # Update UI with current position
    update_ui()
    
    # Update the screen
    screen.update()
    
    # Call this function again after a short delay
    screen.ontimer(move_turtle, 20)

# Start the continuous movement check
move_turtle()

# Keep the window open
screen.mainloop()