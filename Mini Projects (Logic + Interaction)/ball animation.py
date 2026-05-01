import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Bouncing Ball Animation")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic updates for smooth animation

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)

# Ball properties
ball_x = 0
ball_y = 0
ball_dx = 3   # Horizontal velocity (pixels per frame)
ball_dy = 3   # Vertical velocity (pixels per frame)

# Boundary limits (ball radius is approximately 10 pixels)
boundary_left = -380
boundary_right = 380
boundary_top = 280
boundary_bottom = -280

# Create boundaries (visual walls)
boundary_drawer = turtle.Turtle()
boundary_drawer.speed(0)
boundary_drawer.color("white")
boundary_drawer.penup()
boundary_drawer.goto(boundary_left, boundary_bottom)
boundary_drawer.pendown()
boundary_drawer.goto(boundary_right, boundary_bottom)
boundary_drawer.goto(boundary_right, boundary_top)
boundary_drawer.goto(boundary_left, boundary_top)
boundary_drawer.goto(boundary_left, boundary_bottom)
boundary_drawer.penup()
boundary_drawer.hideturtle()

# Create shadow effect (optional)
shadow = turtle.Turtle()
shadow.shape("circle")
shadow.color("gray")
shadow.penup()
shadow.shapesize(1, 1, 1)

# UI display
info_display = turtle.Turtle()
info_display.speed(0)
info_display.color("yellow")
info_display.penup()
info_display.hideturtle()

def update_info():
    """Update on-screen information"""
    info_display.clear()
    info_display.goto(-380, 310)
    info_display.write(f"Position: ({ball_x}, {ball_y}) | Velocity: ({ball_dx}, {ball_dy})",
                       font=("Arial", 10, "normal"))

# Control variables
animation_running = True
gravity_enabled = False
gravity = -0.2
bounce_damping = 1.0  # Perfect bounce (1.0) or dampened (0.9 for energy loss)

def toggle_animation():
    """Pause or resume the animation"""
    global animation_running
    animation_running = not animation_running
    if animation_running:
        animate()

def toggle_gravity():
    """Toggle gravity effect on/off"""
    global gravity_enabled, ball_dy
    gravity_enabled = not gravity_enabled
    if not gravity_enabled and ball_dy > 5:
        ball_dy = 3  # Reset to normal speed when turning off gravity

def increase_speed():
    """Increase ball speed"""
    global ball_dx, ball_dy
    ball_dx *= 1.2
    ball_dy *= 1.2
    # Cap maximum speed
    max_speed = 15
    ball_dx = max(min(ball_dx, max_speed), -max_speed)
    ball_dy = max(min(ball_dy, max_speed), -max_speed)

def decrease_speed():
    """Decrease ball speed"""
    global ball_dx, ball_dy
    ball_dx *= 0.8
    ball_dy *= 0.8
    # Minimum speed threshold
    if abs(ball_dx) < 0.5:
        ball_dx = 3 if ball_dx >= 0 else -3
    if abs(ball_dy) < 0.5:
        ball_dy = 3 if ball_dy >= 0 else -3

def change_color():
    """Change ball color randomly"""
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "lime"]
    import random
    ball.color(random.choice(colors))

def reset_ball():
    """Reset ball to center with default velocity"""
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x = 0
    ball_y = 0
    ball_dx = 3
    ball_dy = 3
    ball.goto(ball_x, ball_y)

def animate():
    """Main animation loop"""
    global ball_x, ball_y, ball_dx, ball_dy, animation_running
    
    if not animation_running:
        return
    
    # Apply gravity if enabled
    if gravity_enabled:
        ball_dy += gravity
    
    # Update position
    ball_x += ball_dx
    ball_y += ball_dy
    
    # Boundary checking with bouncing
    # Left/Right boundaries
    if ball_x >= boundary_right:
        ball_x = boundary_right
        ball_dx = -ball_dx * bounce_damping
    elif ball_x <= boundary_left:
        ball_x = boundary_left
        ball_dx = -ball_dx * bounce_damping
    
    # Top/Bottom boundaries
    if ball_y >= boundary_top:
        ball_y = boundary_top
        ball_dy = -ball_dy * bounce_damping
        if gravity_enabled and abs(ball_dy) < 1:
            ball_dy = 0  # Stop bouncing if too slow
    elif ball_y <= boundary_bottom:
        ball_y = boundary_bottom
        ball_dy = -ball_dy * bounce_damping
        if gravity_enabled and abs(ball_dy) < 1:
            ball_dy = 0
    
    # Update ball position
    ball.goto(ball_x, ball_y)
    
    # Update shadow position (offset for effect)
    shadow.goto(ball_x - 5, ball_y - 5)
    
    # Update UI
    update_info()
    
    # Refresh screen
    screen.update()
    
    # Schedule next frame
    screen.ontimer(animate, 16)  # ~60 FPS

# Draw background grid (optional)
grid = turtle.Turtle()
grid.speed(0)
grid.color("gray")
grid.pensize(0.5)
grid.penup()
grid.hideturtle()

# Draw center lines
grid.goto(-400, 0)
grid.pendown()
grid.goto(400, 0)
grid.penup()
grid.goto(0, -300)
grid.pendown()
grid.goto(0, 300)
grid.penup()

# Draw instruction panel
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("lightgray")
instructions.penup()
instructions.hideturtle()
instructions.goto(-380, -280)
instructions.write("CONTROLS: SPACE=Pause  G=Gravity  +/-=Speed  C=Color  R=Reset  ESC=Exit",
                   font=("Arial", 10, "normal"))

# Keyboard bindings
screen.listen()
screen.onkey(toggle_animation, "space")
screen.onkey(toggle_gravity, "g")
screen.onkey(increase_speed, "plus")
screen.onkey(increase_speed, "equal")
screen.onkey(decrease_speed, "minus")
screen.onkey(change_color, "c")
screen.onkey(reset_ball, "r")
screen.onkey(lambda: exit(), "Escape")

# Print instructions to console
print("=== BOUNCING BALL ANIMATION ===")
print()
print("The ball moves inside boundaries and bounces off walls")
print()
print("CONTROLS:")
print("  SPACE - Pause / Resume animation")
print("  G     - Toggle gravity effect (ball falls down)")
print("  + / = - Increase ball speed")
print("  -     - Decrease ball speed")
print("  C     - Change ball color")
print("  R     - Reset ball position")
print("  ESC   - Exit program")
print()
print("Try enabling gravity to see realistic falling and bouncing!")

# Start animation
update_info()
animate()

# Keep window open
screen.mainloop()