import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Color-Changing Bouncing Shape")
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.tracer(0)

# Create the bouncing shape
shape = turtle.Turtle()
shape.speed(0)
shape.penup()
shape.shapesize(2, 2)

# Trail effect for the shape
trail = turtle.Turtle()
trail.speed(0)
trail.penup()
trail.hideturtle()
trail.pensize(2)

# Particle system for collision effects
particles = []

# Shape settings
current_shape = "circle"  # circle, square, triangle, star
shape_types = ["circle", "square", "triangle", "star"]

# Position and velocity
x, y = 0, 0
dx = 4
dy = 5

# Boundaries
boundary_left = -420
boundary_right = 420
boundary_top = 320
boundary_bottom = -320

# Color settings
color_mode = "rainbow"  # rainbow, speed, bounce, custom
custom_color = "cyan"
color_index = 0
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime", "white", "gold"]

# Trail settings
show_trail = True
trail_positions = []
max_trail_length = 30

# Size settings
current_size = 2.0
size_pulse = False
pulse_direction = 1

# Animation control
running = True
frame = 0

# Stats
bounce_count = 0
color_changes = 0
max_speed = 0

class Particle:
    def __init__(self, x, y, color):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.shapesize(0.3, 0.3)
        self.turtle.penup()
        self.turtle.goto(x, y)
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = random.randint(20, 50)
        self.age = 0
        
    def update(self):
        self.age += 1
        self.turtle.goto(self.turtle.xcor() + self.vx, self.turtle.ycor() + self.vy)
        self.vx *= 0.98
        self.vy *= 0.98
        
        if self.age > self.life:
            self.turtle.hideturtle()
            self.turtle.clear()
            return False
        # Shrink effect
        new_size = max(0.1, 0.3 * (1 - self.age / self.life))
        self.turtle.shapesize(new_size, new_size)
        return True

def create_collision_effect(x, y):
    """Create particles at collision point"""
    for _ in range(15):
        particles.append(Particle(x, y, random.choice(colors)))

def update_trail():
    """Update the trail effect"""
    if show_trail:
        trail_positions.append((shape.xcor(), shape.ycor()))
        if len(trail_positions) > max_trail_length:
            trail_positions.pop(0)
        
        trail.clear()
        for i, pos in enumerate(trail_positions):
            alpha = i / max_trail_length
            trail.penup()
            trail.goto(pos)
            trail.pendown()
            brightness = int(255 * (1 - alpha))
            trail.color(f"#{brightness:02x}{brightness//2:02x}{255:02x}")
            trail.dot(4 - int(alpha * 3))

def update_color():
    """Update the shape's color based on current mode"""
    global color_index, color_changes
    
    if color_mode == "rainbow":
        # Continuous rainbow cycling
        color_index += 0.03
        color = colors[int(color_index) % len(colors)]
        shape.color(color)
        
    elif color_mode == "speed":
        # Color based on current speed
        speed = math.sqrt(dx*dx + dy*dy)
        speed_ratio = min(speed / 15, 1)
        r = int(255 * speed_ratio)
        g = int(255 * (1 - speed_ratio))
        b = int(255 * (1 - abs(speed_ratio - 0.5) * 2))
        shape.color(f"#{r:02x}{g:02x}{b:02x}")
        
    elif color_mode == "bounce":
        # Color changes on each bounce
        pass  # Color changes in boundary check
        
    elif color_mode == "custom":
        shape.color(custom_color)

def change_color_mode():
    """Cycle through color modes"""
    global color_mode
    modes = ["rainbow", "speed", "bounce", "custom"]
    idx = modes.index(color_mode)
    color_mode = modes[(idx + 1) % len(modes)]
    show_message(f"Color Mode: {color_mode.upper()}", "yellow")

def set_custom_color():
    """Cycle through custom colors"""
    global custom_color, color_mode
    colors_list = ["cyan", "lime", "magenta", "yellow", "white", "orange", "pink", "purple"]
    idx = colors_list.index(custom_color) if custom_color in colors_list else 0
    custom_color = colors_list[(idx + 1) % len(colors_list)]
    if color_mode == "custom":
        shape.color(custom_color)
    show_message(f"Custom Color: {custom_color}", custom_color)

def toggle_trail():
    """Toggle trail effect"""
    global show_trail
    show_trail = not show_trail
    if not show_trail:
        trail.clear()
        trail_positions.clear()
    show_message(f"Trail: {'ON' if show_trail else 'OFF'}", "cyan")

def toggle_pulse():
    """Toggle size pulse effect"""
    global size_pulse
    size_pulse = not size_pulse
    show_message(f"Size Pulse: {'ON' if size_pulse else 'OFF'}", "magenta")

def change_shape():
    """Cycle through shapes"""
    global current_shape
    idx = shape_types.index(current_shape)
    current_shape = shape_types[(idx + 1) % len(shape_types)]
    shape.shape(current_shape)
    show_message(f"Shape: {current_shape.upper()}", "gold")

def increase_speed():
    """Increase speed"""
    global dx, dy, max_speed
    dx *= 1.1
    dy *= 1.1
    speed = math.sqrt(dx*dx + dy*dy)
    if speed > max_speed:
        max_speed = speed
    show_message(f"Speed UP! ({speed:.1f})", "lime")

def decrease_speed():
    """Decrease speed"""
    global dx, dy
    dx *= 0.9
    dy *= 0.9
    speed = math.sqrt(dx*dx + dy*dy)
    show_message(f"Speed DOWN! ({speed:.1f})", "orange")

def reset_speed():
    """Reset speed to default"""
    global dx, dy
    dx = 4
    dy = 5
    show_message("Speed Reset!", "white")

def increase_size():
    """Increase shape size"""
    global current_size
    current_size = min(current_size + 0.2, 3.5)
    shape.shapesize(current_size, current_size)
    show_message(f"Size: {current_size:.1f}", "cyan")

def decrease_size():
    """Decrease shape size"""
    global current_size
    current_size = max(current_size - 0.2, 0.8)
    shape.shapesize(current_size, current_size)
    show_message(f"Size: {current_size:.1f}", "cyan")

def clear_trail():
    """Clear the trail"""
    global trail_positions
    trail_positions.clear()
    trail.clear()
    show_message("Trail Cleared!", "white")

def reset_position():
    """Reset shape to center"""
    global x, y
    x, y = 0, 0
    shape.goto(x, y)
    show_message("Position Reset!", "gold")

def update_size_pulse():
    """Update size pulse effect"""
    global pulse_direction, current_size
    
    if size_pulse:
        current_size += 0.02 * pulse_direction
        if current_size >= 2.3:
            pulse_direction = -1
        elif current_size <= 1.7:
            pulse_direction = 1
        shape.shapesize(current_size, current_size)

def draw_boundary():
    """Draw the boundary walls"""
    boundary = turtle.Turtle()
    boundary.speed(0)
    boundary.color("gray")
    boundary.penup()
    boundary.hideturtle()
    boundary.goto(boundary_left, boundary_bottom)
    boundary.pendown()
    boundary.pensize(3)
    for _ in range(2):
        boundary.forward(boundary_right - boundary_left)
        boundary.right(90)
        boundary.forward(boundary_top - boundary_bottom)
        boundary.right(90)
    boundary.penup()

def show_message(text, color):
    """Display a temporary message"""
    msg = turtle.Turtle()
    msg.speed(0)
    msg.color(color)
    msg.penup()
    msg.hideturtle()
    msg.goto(0, 350)
    msg.write(text, align="center", font=("Arial", 14, "bold"))
    screen.ontimer(lambda: msg.clear(), 1200)

def update_info():
    """Update info display"""
    info = turtle.Turtle()
    info.speed(0)
    info.color("white")
    info.penup()
    info.hideturtle()
    info.goto(-450, 320)
    info.clear()
    
    speed = math.sqrt(dx*dx + dy*dy)
    info.write(f"🎨 COLOR-CHANGING BOUNCING SHAPE 🎨", font=("Arial", 12, "bold"))
    info.goto(-450, 295)
    info.write(f"Shape: {current_shape.upper()} | Color Mode: {color_mode.upper()} | Speed: {speed:.1f}", font=("Arial", 10, "normal"))
    info.goto(-450, 270)
    info.write(f"Bounces: {bounce_count} | Trail: {'ON' if show_trail else 'OFF'} | Pulse: {'ON' if size_pulse else 'OFF'}", font=("Arial", 10, "normal"))
    info.goto(-450, 245)
    info.write("Controls: S=Shape C=ColorMode M=CustomColor T=Trail P=Pulse +/-=Speed R=ResetSpeed", font=("Arial", 8, "normal"))
    info.goto(-450, 220)
    info.write("[ ]=Size  V=SpeedUp B=SpeedDown X=ClearTrail Z=ResetPos ESC=Exit", font=("Arial", 8, "normal"))

def animate():
    """Main animation loop"""
    global x, y, dx, dy, bounce_count, color_index, frame
    
    if not running:
        return
    
    # Update position
    x += dx
    y += dy
    
    # Boundary checking
    half_size = 25 * current_size
    bounced = False
    
    # Check left/right boundaries
    if x + half_size >= boundary_right:
        x = boundary_right - half_size
        dx = -dx
        bounced = True
        create_collision_effect(x, y)
    elif x - half_size <= boundary_left:
        x = boundary_left + half_size
        dx = -dx
        bounced = True
        create_collision_effect(x, y)
    
    # Check top/bottom boundaries
    if y + half_size >= boundary_top:
        y = boundary_top - half_size
        dy = -dy
        bounced = True
        create_collision_effect(x, y)
    elif y - half_size <= boundary_bottom:
        y = boundary_bottom + half_size
        dy = -dy
        bounced = True
        create_collision_effect(x, y)
    
    # Update bounce count and color on bounce
    if bounced:
        bounce_count += 1
        if color_mode == "bounce":
            color_index = (color_index + 1) % len(colors)
            shape.color(colors[color_index])
    
    # Update position
    shape.goto(x, y)
    
    # Update color
    update_color()
    
    # Update size pulse
    update_size_pulse()
    
    # Update trail
    update_trail()
    
    # Update particles
    for particle in particles[:]:
        if not particle.update():
            particles.remove(particle)
    
    # Update info display periodically
    frame += 1
    if frame % 10 == 0:
        update_info()
    
    # Update screen
    screen.update()
    
    # Schedule next frame
    screen.ontimer(animate, 16)

def draw_instructions():
    """Draw instruction panel at bottom"""
    instr = turtle.Turtle()
    instr.speed(0)
    instr.color("gray")
    instr.penup()
    instr.hideturtle()
    instr.goto(0, -370)
    instr.write("S=Shape  C=ColorMode  M=CustomColor  T=Trail  P=Pulse  +/-=Speed  R=ResetSpeed  []=Size  V=SpeedUp  B=SpeedDown  X=ClearTrail  Z=ResetPos  ESC=Exit",
               align="center", font=("Arial", 8, "normal"))

# Initialize
shape.shape("circle")
shape.color("cyan")
shape.shapesize(2, 2)
shape.goto(0, 0)

# Draw boundary and instructions
draw_boundary()
draw_instructions()
update_info()

# Keyboard bindings
screen.listen()
screen.onkey(change_shape, "s")
screen.onkey(change_color_mode, "c")
screen.onkey(set_custom_color, "m")
screen.onkey(toggle_trail, "t")
screen.onkey(toggle_pulse, "p")
screen.onkey(increase_speed, "v")
screen.onkey(decrease_speed, "b")
screen.onkey(reset_speed, "r")
screen.onkey(increase_size, "bracketright")
screen.onkey(increase_size, "bracketright")
screen.onkey(decrease_size, "bracketleft")
screen.onkey(clear_trail, "x")
screen.onkey(reset_position, "z")
screen.onkey(lambda: screen.bye(), "Escape")

# Also bind plus/minus keys
screen.onkey(increase_speed, "plus")
screen.onkey(increase_speed, "equal")
screen.onkey(decrease_speed, "minus")

print("=" * 60)
print("        COLOR-CHANGING BOUNCING SHAPE")
print("=" * 60)
print()
print("A dynamic shape that bounces off walls and changes colors!")
print()
print("COLOR MODES:")
print("  • RAINBOW - Continuously cycles through colors")
print("  • SPEED   - Color changes based on velocity")
print("  • BOUNCE  - New color on each wall hit")
print("  • CUSTOM  - Manual color selection")
print()
print("SHAPES (Press S):")
print("  • Circle, Square, Triangle, Star")
print()
print("CONTROLS:")
print("  S     - Change shape")
print("  C     - Change color mode")
print("  M     - Cycle custom colors")
print("  T     - Toggle trail effect")
print("  P     - Toggle size pulse")
print("  +/-   - Increase/decrease speed")
print("  V/B   - Speed up / Slow down")
print("  R     - Reset speed")
print("  [/]   - Decrease/Increase size")
print("  X     - Clear trail")
print("  Z     - Reset position")
print("  ESC   - Exit")
print()
print("Watch as the shape bounces, changes color, and leaves a trail!")

# Start animation
animate()
screen.mainloop()