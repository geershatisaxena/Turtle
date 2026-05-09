import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Mouse-Following Turtle - Cursor Follower")
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.tracer(0)

# Create the follower turtle
follower = turtle.Turtle()
follower.speed(0)
follower.penup()
follower.shape("turtle")
follower.color("lime")
follower.shapesize(1.5, 1.5)

# Create decorative elements (particles, trail, etc.)
particles = []
trail = []
trail_length = 20
trail_turtles = []

# Animation state
current_mode = 1  # 1=Normal, 2=Trail, 3=Particles, 4=ColorCycle, 5=SizePulse
target_x = 0
target_y = 0
smoothness = 0.1
color_index = 0
pulse_scale = 1
pulse_direction = 1

# Color palette for cycling
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime"]

def create_trail_turtles():
    """Create turtles for trail effect"""
    global trail_turtles
    for _ in range(trail_length):
        t = turtle.Turtle()
        t.speed(0)
        t.shape("circle")
        t.color("cyan")
        t.shapesize(0.3, 0.3)
        t.penup()
        t.hideturtle()
        trail_turtles.append(t)

def create_particle():
    """Create a single particle"""
    particle = turtle.Turtle()
    particle.speed(0)
    particle.shape("circle")
    particle.color(random.choice(colors))
    particle.shapesize(random.uniform(0.2, 0.5))
    particle.penup()
    particle.goto(follower.xcor(), follower.ycor())
    
    # Random velocity
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(2, 6)
    particle.vx = math.cos(angle) * speed
    particle.vy = math.sin(angle) * speed
    particle.life = random.randint(20, 50)
    particle.age = 0
    
    particles.append(particle)

def update_particles():
    """Update all particles"""
    for particle in particles[:]:
        particle.age += 1
        particle.goto(particle.xcor() + particle.vx, particle.ycor() + particle.vy)
        particle.vx *= 0.98
        particle.vy -= 0.15  # Gravity effect
        
        # Shrink and fade
        if particle.age > particle.life * 0.6:
            new_size = max(0.05, particle.shapesize()[0] - 0.02)
            particle.shapesize(new_size)
        
        if particle.age >= particle.life:
            particle.hideturtle()
            particle.clear()
            particles.remove(particle)

def update_trail(x, y):
    """Update the trail positions"""
    trail.append((x, y))
    if len(trail) > trail_length:
        trail.pop(0)
    
    for i, pos in enumerate(trail):
        if i < len(trail_turtles):
            t = trail_turtles[i]
            t.goto(pos)
            t.showturtle()
            # Fade out older trail points
            alpha = i / len(trail)
            t.color(f"#{int(255 * (1 - alpha)):02x}{int(255 * alpha):02x}{int(255 * (1 - alpha)):02x}")
            t.shapesize(0.5 - alpha * 0.3, 0.5 - alpha * 0.3)

def mouse_move(x, y):
    """Called when mouse moves - sets target position"""
    global target_x, target_y
    target_x = x
    target_y = y
    
    # Add particles in certain modes when moving
    if current_mode == 3 and random.random() < 0.3:
        create_particle()

def update_follower():
    """Smoothly move follower toward mouse position"""
    global color_index, pulse_scale, pulse_direction
    
    # Get current position
    cx, cy = follower.xcor(), follower.ycor()
    
    # Calculate distance to target
    dx = target_x - cx
    dy = target_y - cy
    distance = math.sqrt(dx*dx + dy*dy)
    
    # Smooth movement (ease-in effect)
    if distance > 1:
        move_x = dx * smoothness
        move_y = dy * smoothness
        follower.goto(cx + move_x, cy + move_y)
    
    # Set heading direction (face the direction of movement)
    if distance > 5:
        angle = math.degrees(math.atan2(dy, dx))
        follower.setheading(angle)
    
    # Mode-specific effects
    if current_mode == 1:
        # Normal mode - simple follow
        pass
        
    elif current_mode == 2:
        # Trail mode - update trail
        update_trail(follower.xcor(), follower.ycor())
        
    elif current_mode == 3:
        # Particle mode - add extra particles when moving fast
        if distance > 10 and random.random() < 0.2:
            create_particle()
            
    elif current_mode == 4:
        # Color cycle mode
        color_index += 0.05
        color_idx = int(color_index) % len(colors)
        follower.color(colors[color_idx])
        
    elif current_mode == 5:
        # Size pulse mode
        pulse_scale += 0.03 * pulse_direction
        if pulse_scale >= 1.3:
            pulse_direction = -1
        elif pulse_scale <= 0.7:
            pulse_direction = 1
        follower.shapesize(1.5 * pulse_scale, 1.5 * pulse_scale)
    
    # Update particles
    update_particles()
    
    # Update screen
    screen.update()
    
    # Call again
    screen.ontimer(update_follower, 16)  # ~60 FPS

def set_mode_normal():
    global current_mode, trail_turtles, particles
    current_mode = 1
    follower.color("lime")
    follower.shapesize(1.5, 1.5)
    # Hide trail turtles
    for t in trail_turtles:
        t.hideturtle()
    # Clear particles
    for p in particles:
        p.hideturtle()
    particles.clear()
    update_info()

def set_mode_trail():
    global current_mode
    current_mode = 2
    follower.color("cyan")
    follower.shapesize(1.5, 1.5)
    update_info()

def set_mode_particles():
    global current_mode
    current_mode = 3
    follower.color("magenta")
    follower.shapesize(1.5, 1.5)
    update_info()

def set_mode_colorcycle():
    global current_mode, color_index
    current_mode = 4
    color_index = 0
    follower.shapesize(1.5, 1.5)
    update_info()

def set_mode_pulse():
    global current_mode, pulse_scale, pulse_direction
    current_mode = 5
    pulse_scale = 1
    pulse_direction = 1
    follower.color("gold")
    update_info()

def toggle_smoothness():
    global smoothness
    if smoothness == 0.1:
        smoothness = 0.05
        update_info()
    elif smoothness == 0.05:
        smoothness = 0.2
        update_info()
    else:
        smoothness = 0.1
        update_info()

def reset():
    """Reset the follower to center"""
    global target_x, target_y, trail, particles
    target_x = 0
    target_y = 0
    follower.goto(0, 0)
    # Clear trail
    for t in trail_turtles:
        t.hideturtle()
    trail.clear()
    # Clear particles
    for p in particles:
        p.hideturtle()
    particles.clear()
    update_info()

def draw_ui():
    """Draw user interface elements"""
    ui = turtle.Turtle()
    ui.speed(0)
    ui.color("white")
    ui.penup()
    ui.hideturtle()
    
    # Title
    ui.goto(0, 320)
    ui.write("🐭 MOUSE-FOLLOWING TURTLE 🐭", align="center", font=("Arial", 18, "bold"))
    
    # Instructions
    ui.goto(0, 290)
    ui.write("1=Normal  2=Trail  3=Particles  4=ColorCycle  5=SizePulse   S=Smoothness   R=Reset   ESC=Exit",
             align="center", font=("Arial", 10, "normal"))
    
    return ui

def update_info():
    """Update the info display"""
    info = turtle.Turtle()
    info.speed(0)
    info.color("cyan")
    info.penup()
    info.hideturtle()
    info.goto(-400, -330)
    info.clear()
    
    modes = ["NORMAL", "TRAIL", "PARTICLES", "COLOR CYCLE", "SIZE PULSE"]
    smooth_text = "SLOW" if smoothness < 0.08 else "FAST" if smoothness > 0.15 else "NORMAL"
    
    info.write(f"Mode: {modes[current_mode-1]} | Smoothness: {smooth_text}", font=("Arial", 12, "bold"))

def draw_border():
    """Draw a decorative border"""
    border = turtle.Turtle()
    border.speed(0)
    border.color("gray")
    border.penup()
    border.hideturtle()
    border.goto(-430, -350)
    border.pendown()
    border.pensize(2)
    for _ in range(2):
        border.forward(860)
        border.right(90)
        border.forward(700)
        border.right(90)
    border.penup()

# Create trail turtles
create_trail_turtles()

# Draw UI elements
draw_border()
draw_ui()
update_info()

# Mouse binding - use ondrag for continuous tracking or onclick for click
# For mouse movement without clicking, we use screen.onmouse
def on_mouse_move(event):
    """Handle mouse movement"""
    x = event.x - screen.window_width() // 2
    y = screen.window_height() // 2 - event.y
    mouse_move(x, y)

# Bind mouse movement using canvas
canvas = screen.getcanvas()
canvas.bind('<Motion>', on_mouse_move)

# Keyboard bindings
screen.listen()
screen.onkey(set_mode_normal, "1")
screen.onkey(set_mode_trail, "2")
screen.onkey(set_mode_particles, "3")
screen.onkey(set_mode_colorcycle, "4")
screen.onkey(set_mode_pulse, "5")
screen.onkey(toggle_smoothness, "s")
screen.onkey(reset, "r")
screen.onkey(lambda: screen.bye(), "Escape")

print("=" * 60)
print("        MOUSE-FOLLOWING TURTLE")
print("=" * 60)
print()
print("The turtle follows your mouse cursor smoothly!")
print()
print("MODES (Press 1-5):")
print("  1 - NORMAL: Basic cursor following")
print("  2 - TRAIL: Leaves a fading trail behind")
print("  3 - PARTICLES: Creates particle effects while moving")
print("  4 - COLOR CYCLE: Colors cycle through rainbow")
print("  5 - SIZE PULSE: Turtle size pulses like a heartbeat")
print()
print("CONTROLS:")
print("  1-5   - Change follow mode")
print("  S     - Toggle smoothness (Slow/Normal/Fast)")
print("  R     - Reset position to center")
print("  ESC   - Exit program")
print()
print("Move your mouse around the screen!")

# Start the follower update loop
update_follower()

screen.mainloop()