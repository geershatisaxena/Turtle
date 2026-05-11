import turtle
import random
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Random Speed Turtle - Chaotic Movement")
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(0)

# Create the main turtle
turtle_obj = turtle.Turtle()
turtle_obj.shape("turtle")
turtle_obj.penup()
turtle_obj.goto(0, 0)
turtle_obj.pendown()
turtle_obj.speed(0)

# Trail effect
trail = turtle.Turtle()
trail.speed(0)
trail.penup()
trail.hideturtle()
trail.pensize(2)

# Particle system
particles = []

# Speed variables
current_speed = 3
min_speed = 1
max_speed = 15
speed_change_timer = 0
speed_change_interval = 30  # Initialize here

# Direction variables
current_angle = 90
angle_change_timer = 0
angle_change_interval = 20  # Initialize here

# Color variables
color_index = 0
rainbow_mode = True

# Trail variables
trail_positions = []
max_trail_length = 60
show_trail = True

# Size variables
current_size = 1.0
size_pulse = False
pulse_direction = 1

# Color palette
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta", "lime", "white", "gold", "coral", "teal", "violet"]

# Stats
total_distance = 0
direction_changes = 0
speed_changes = 0
max_speed_reached = 0
min_speed_reached = 999

# Message display
message_turtle = None
speed_history = []

def show_message(text, color):
    """Display a temporary message"""
    global message_turtle
    if message_turtle:
        message_turtle.clear()
    else:
        message_turtle = turtle.Turtle()
        message_turtle.speed(0)
        message_turtle.penup()
        message_turtle.hideturtle()
    
    message_turtle.color(color)
    message_turtle.goto(0, 280)
    message_turtle.write(text, align="center", font=("Arial", 12, "bold"))
    screen.ontimer(lambda: message_turtle.clear(), 1000)

class Particle:
    def __init__(self, x, y, color, speed_multiplier):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.shapesize(0.3, 0.3)
        self.turtle.penup()
        self.turtle.goto(x, y)
        
        angle = random.uniform(0, 2 * math.pi)
        velocity = random.uniform(2, 8) * min(speed_multiplier, 2)
        self.vx = math.cos(angle) * velocity
        self.vy = math.sin(angle) * velocity
        self.life = random.randint(20, 60)
        self.age = 0
        
    def update(self):
        self.age += 1
        self.turtle.goto(self.turtle.xcor() + self.vx, self.turtle.ycor() + self.vy)
        self.vx *= 0.97
        self.vy *= 0.97
        
        if self.age > self.life:
            self.turtle.hideturtle()
            self.turtle.clear()
            return False
        
        # Shrink effect
        if self.age > self.life * 0.6:
            new_size = max(0.1, 0.3 - (self.age - self.life * 0.6) * 0.02)
            self.turtle.shapesize(new_size, new_size)
        return True

def create_speed_burst(x, y, speed):
    """Create particles when speed changes"""
    color = random.choice(colors)
    multiplier = speed / 8
    num_particles = min(int(speed), 15)
    for _ in range(num_particles):
        particles.append(Particle(x, y, color, multiplier))

def update_trail():
    """Update the trail effect"""
    if show_trail:
        trail_positions.append((turtle_obj.xcor(), turtle_obj.ycor()))
        if len(trail_positions) > max_trail_length:
            trail_positions.pop(0)
        
        trail.clear()
        for i, pos in enumerate(trail_positions):
            alpha = i / max_trail_length
            if rainbow_mode:
                r = int(255 * (1 - alpha))
                g = int(255 * alpha)
                b = int(255 * (1 - abs(alpha - 0.5) * 2))
            else:
                r = int(255 * alpha)
                g = int(100 * alpha)
                b = int(255 * (1 - alpha))
            trail.penup()
            trail.goto(pos)
            trail.pendown()
            trail.color(f"#{min(r,255):02x}{min(g,255):02x}{min(b,255):02x}")
            trail.dot(3)

def randomize_speed():
    """Randomly change the turtle's speed"""
    global current_speed, speed_changes, speed_change_timer, max_speed_reached, min_speed_reached, speed_change_interval
    
    old_speed = current_speed
    current_speed = random.uniform(min_speed, max_speed)
    speed_changes += 1
    speed_change_timer = 0
    
    # Track min/max
    if current_speed > max_speed_reached:
        max_speed_reached = current_speed
    if current_speed < min_speed_reached:
        min_speed_reached = current_speed
    
    # Speed history for graph
    speed_history.append(current_speed)
    if len(speed_history) > 30:
        speed_history.pop(0)
    
    # Visual effect based on speed change
    speed_diff = abs(current_speed - old_speed)
    if speed_diff > 5:
        create_speed_burst(turtle_obj.xcor(), turtle_obj.ycor(), speed_diff)
    
    # Change interval for next change
    speed_change_interval = random.randint(20, 50)
    
    show_message(f"Speed: {current_speed:.1f}", colors[int(current_speed) % len(colors)])

def randomize_direction():
    """Randomly change direction"""
    global current_angle, direction_changes, angle_change_timer, angle_change_interval
    
    old_angle = current_angle
    # Change direction by random amount
    angle_change = random.uniform(-90, 90)
    current_angle = (current_angle + angle_change) % 360
    direction_changes += 1
    angle_change_timer = 0
    
    turtle_obj.setheading(current_angle)
    
    # Change interval for next change
    angle_change_interval = random.randint(15, 40)

def update_color():
    """Update color based on speed"""
    global color_index
    
    if rainbow_mode:
        # Faster color cycling at higher speeds
        color_index += current_speed / 40
        color_idx = int(color_index) % len(colors)
        turtle_obj.color(colors[color_idx])
    else:
        # Speed-based color mapping
        speed_ratio = (current_speed - min_speed) / (max_speed - min_speed)
        r = int(255 * speed_ratio)
        g = int(255 * (1 - abs(speed_ratio - 0.5) * 2))
        b = int(255 * (1 - speed_ratio))
        turtle_obj.color(f"#{r:02x}{g:02x}{b:02x}")

def update_size():
    """Update turtle size (pulse effect)"""
    global current_size, pulse_direction
    
    if size_pulse:
        # Pulse speed based on movement speed
        pulse_speed = 0.02 + (current_speed / 100)
        current_size += pulse_speed * pulse_direction
        if current_size >= 1.5:
            pulse_direction = -1
        elif current_size <= 0.8:
            pulse_direction = 1
        turtle_obj.shapesize(current_size, current_size)

def move_turtle():
    """Move the turtle and handle boundaries"""
    global total_distance
    
    # Move forward
    turtle_obj.forward(current_speed)
    
    # Update total distance
    total_distance += current_speed
    
    # Boundary checking with wrap around
    x, y = turtle_obj.xcor(), turtle_obj.ycor()
    wrapped = False
    
    if x > 450:
        turtle_obj.setx(-450)
        wrapped = True
    elif x < -450:
        turtle_obj.setx(450)
        wrapped = True
    
    if y > 350:
        turtle_obj.sety(-350)
        wrapped = True
    elif y < -350:
        turtle_obj.sety(350)
        wrapped = True
    
    if wrapped:
        create_speed_burst(turtle_obj.xcor(), turtle_obj.ycor(), current_speed)
        show_message("✨ WARP! ✨", "gold")

def update_particles():
    """Update all particles"""
    for particle in particles[:]:
        if not particle.update():
            particles.remove(particle)

def draw_boundary():
    """Draw a decorative boundary"""
    boundary = turtle.Turtle()
    boundary.speed(0)
    boundary.color("gray")
    boundary.penup()
    boundary.hideturtle()
    boundary.goto(-470, -370)
    boundary.pendown()
    boundary.pensize(2)
    for _ in range(2):
        boundary.forward(940)
        boundary.right(90)
        boundary.forward(740)
        boundary.right(90)
    boundary.penup()

# UI Turtles
stats_turtle = turtle.Turtle()
stats_turtle.speed(0)
stats_turtle.color("white")
stats_turtle.penup()
stats_turtle.hideturtle()

info_turtle = turtle.Turtle()
info_turtle.speed(0)
info_turtle.color("cyan")
info_turtle.penup()
info_turtle.hideturtle()

instructions_turtle = turtle.Turtle()
instructions_turtle.speed(0)
instructions_turtle.color("gray")
instructions_turtle.penup()
instructions_turtle.hideturtle()

def update_info():
    """Update the information display"""
    stats_turtle.clear()
    stats_turtle.goto(-450, 310)
    stats_turtle.write(f"Current Speed: {current_speed:.1f}", font=("Arial", 10, "bold"))
    stats_turtle.goto(-450, 290)
    stats_turtle.write(f"Speed Range: {min_speed:.0f} - {max_speed:.0f}", font=("Arial", 10, "normal"))
    stats_turtle.goto(-450, 270)
    stats_turtle.write(f"Total Distance: {total_distance:.0f} px", font=("Arial", 10, "normal"))
    stats_turtle.goto(-450, 250)
    stats_turtle.write(f"Speed Changes: {speed_changes}", font=("Arial", 10, "normal"))
    stats_turtle.goto(-450, 230)
    stats_turtle.write(f"Direction Changes: {direction_changes}", font=("Arial", 10, "normal"))

def draw_ui():
    """Draw the user interface"""
    info_turtle.clear()
    info_turtle.goto(0, 370)
    info_turtle.write("🎲 RANDOM SPEED TURTLE 🎲", align="center", font=("Arial", 16, "bold"))
    
    instructions_turtle.clear()
    instructions_turtle.goto(-450, -390)
    instructions_turtle.write("R=Rainbow  T=Trail  P=Pulse  +/-=SpeedRange  Space=Clear  S=Reset  ESC=Exit", 
                               font=("Arial", 8, "normal"))

def toggle_rainbow():
    global rainbow_mode
    rainbow_mode = not rainbow_mode
    show_message(f"Rainbow Mode: {'ON' if rainbow_mode else 'OFF'}", "yellow")

def toggle_trail():
    global show_trail
    show_trail = not show_trail
    if not show_trail:
        trail.clear()
        trail_positions.clear()
    show_message(f"Trail: {'ON' if show_trail else 'OFF'}", "cyan")

def toggle_pulse():
    global size_pulse, pulse_direction, current_size
    size_pulse = not size_pulse
    if not size_pulse:
        turtle_obj.shapesize(1.0, 1.0)
        current_size = 1.0
    show_message(f"Size Pulse: {'ON' if size_pulse else 'OFF'}", "magenta")

def increase_speed_range():
    global max_speed, min_speed
    max_speed = min(max_speed + 2, 25)
    min_speed = min(min_speed + 0.5, max_speed - 1)
    show_message(f"Speed Range: {min_speed:.0f}-{max_speed:.0f}", "lime")

def decrease_speed_range():
    global max_speed, min_speed, max_speed_reached, min_speed_reached
    min_speed = max(min_speed - 0.5, 0.5)
    max_speed = max(max_speed - 2, min_speed + 1)
    show_message(f"Speed Range: {min_speed:.0f}-{max_speed:.0f}", "lime")

def clear_drawing():
    turtle_obj.clear()
    show_message("Screen Cleared!", "white")

def reset_position():
    global current_angle, total_distance, speed_changes, direction_changes, trail_positions, particles, speed_history
    global max_speed_reached, min_speed_reached
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.pendown()
    turtle_obj.setheading(90)
    current_angle = 90
    total_distance = 0
    speed_changes = 0
    direction_changes = 0
    trail_positions.clear()
    speed_history.clear()
    max_speed_reached = current_speed
    min_speed_reached = current_speed
    for p in particles:
        p.turtle.hideturtle()
    particles.clear()
    trail.clear()
    turtle_obj.clear()
    show_message("Reset Complete!", "gold")

def animate():
    """Main animation loop"""
    global speed_change_timer, angle_change_timer
    
    # Update timers
    speed_change_timer += 1
    angle_change_timer += 1
    
    # Random speed change
    if speed_change_timer >= speed_change_interval:
        randomize_speed()
    
    # Random direction change
    if angle_change_timer >= angle_change_interval:
        randomize_direction()
    
    # Move the turtle
    move_turtle()
    
    # Update visual effects
    update_color()
    update_size()
    update_trail()
    update_particles()
    
    # Update UI
    update_info()
    
    # Update screen
    screen.update()
    
    # Schedule next frame
    screen.ontimer(animate, 20)

# Setup the scene
draw_boundary()
draw_ui()
update_info()

# Keyboard bindings
screen.listen()
screen.onkey(toggle_rainbow, "r")
screen.onkey(toggle_trail, "t")
screen.onkey(toggle_pulse, "p")
screen.onkey(increase_speed_range, "plus")
screen.onkey(increase_speed_range, "equal")
screen.onkey(decrease_speed_range, "minus")
screen.onkey(clear_drawing, "space")
screen.onkey(reset_position, "s")
screen.onkey(lambda: screen.bye(), "Escape")

# Set initial random direction and track min/max
turtle_obj.setheading(random.uniform(0, 360))
current_angle = turtle_obj.heading()
max_speed_reached = current_speed
min_speed_reached = current_speed

print("=" * 60)
print("        RANDOM SPEED TURTLE")
print("=" * 60)
print()
print("Watch the turtle move with random speed and direction changes!")
print()
print("FEATURES:")
print("  • Speed changes randomly every few seconds")
print("  • Direction changes randomly")
print("  • Rainbow color mode (press R)")
print("  • Trail effect (press T)")
print("  • Size pulse effect (press P)")
print("  • Particle bursts on speed changes")
print("  • Screen wrapping (teleport)")
print()
print("CONTROLS:")
print("  R     - Toggle rainbow mode")
print("  T     - Toggle trail effect")
print("  P     - Toggle size pulse")
print("  +/-   - Adjust speed range")
print("  SPACE - Clear drawing")
print("  S     - Reset position")
print("  ESC   - Exit")

# Start animation
animate()
screen.mainloop()