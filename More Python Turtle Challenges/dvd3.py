import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#1a1a2e")
screen.title("DVD Logo Bounce - Retro Edition")
screen.tracer(0)
screen.setup(800, 700)

# Create a gradient sky background
sky = turtle.Turtle()
sky.speed(0)
sky.penup()
sky.hideturtle()
sky.goto(-400, 350)
sky.pendown()
sky.color("#16213e")
sky.begin_fill()
sky.goto(400, 350)
sky.goto(400, -350)
sky.goto(-400, -350)
sky.goto(-400, 350)
sky.end_fill()

# Create subtle grid lines
grid = turtle.Turtle()
grid.speed(0)
grid.penup()
grid.hideturtle()
grid.color("white")
grid.pensize(0.5)
grid.pencolor("#2a2a4e")

for x in range(-350, 350, 50):
    grid.goto(x, -350)
    grid.pendown()
    grid.goto(x, 350)
    grid.penup()

for y in range(-350, 350, 50):
    grid.goto(-350, y)
    grid.pendown()
    grid.goto(350, y)
    grid.penup()

# Create DVD logo
logo = turtle.Turtle()
logo.speed(0)
logo.penup()
logo.hideturtle()

# Logo properties
logo_size = 80
x_pos = 0
y_pos = 0
x_speed = 4
y_speed = 3.5
color_index = 0

# Retro colors (Vaporwave style)
colors = [
    "#ff6b6b",  # Red
    "#ffd93d",  # Yellow
    "#6bcb77",  # Green
    "#4d96ff",  # Blue
    "#9b59b6",  # Purple
    "#ff6b9d",  # Pink
    "#00d2d3",  # Cyan
    "#f8a5c2",  # Light Pink
    "#778beb",  # Light Blue
    "#f3a683"   # Peach
]

# Glow effect
glow = turtle.Turtle()
glow.speed(0)
glow.penup()
glow.hideturtle()

# Trail with retro feel
trail_enabled = True
trail_length = 15
trail_positions = []

# Stars in background
stars = []
for _ in range(30):
    star = turtle.Turtle()
    star.speed(0)
    star.penup()
    star.hideturtle()
    star.color("white")
    star.goto(random.randint(-380, 380), random.randint(-340, 340))
    star.dot(random.randint(1, 3))
    stars.append(star)

# Score tracking
score = 0
high_score = 0

# Display elements
score_display = turtle.Turtle()
score_display.speed(0)
score_display.penup()
score_display.hideturtle()
score_display.color("white")
score_display.goto(-350, 320)

high_score_display = turtle.Turtle()
high_score_display.speed(0)
high_score_display.penup()
high_score_display.hideturtle()
high_score_display.color("gold")
high_score_display.goto(-350, 290)

bounce_counter = turtle.Turtle()
bounce_counter.speed(0)
bounce_counter.penup()
bounce_counter.hideturtle()
bounce_counter.color("#4d96ff")
bounce_counter.goto(350, 320)

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.penup()
instructions.hideturtle()
instructions.color("gray")
instructions.goto(0, -340)
instructions.write("Click: Toggle Trail • SPACE: Pause • R: Reset • C: Color • S: Speed Up", 
                  align="center", font=("Arial", 10, "normal"))

# Title with retro style
title = turtle.Turtle()
title.speed(0)
title.penup()
title.hideturtle()
title.color("#ff6b6b")
title.goto(0, 350)
title.write("📀 DVD LOGO", align="center", font=("Arial", 24, "bold"))
title.goto(0, 320)
title.color("#ffd93d")
title.write("~ RETRO BOUNCE ~", align="center", font=("Arial", 14, "normal"))

# Pause variables
paused = False
pause_text = None

def draw_dvd_logo(color):
    """Draw the DVD logo with retro styling"""
    logo.clear()
    logo.color(color)
    logo.penup()
    
    # Calculate positions
    left = x_pos - logo_size
    right = x_pos + logo_size
    top = y_pos + logo_size * 0.6
    bottom = y_pos - logo_size * 0.6
    
    # Draw outer glow
    glow.clear()
    glow.penup()
    glow.goto(x_pos, y_pos)
    glow.pendown()
    glow.color(color)
    glow.pensize(3)
    glow.circle(logo_size * 0.8)
    glow.penup()
    
    # Draw main logo background (rounded rectangle)
    logo.penup()
    logo.goto(left, bottom)
    logo.pendown()
    logo.begin_fill()
    
    # Rounded rectangle
    radius = 15
    for _ in range(2):
        logo.forward(logo_size * 2 - radius * 2)
        logo.circle(radius, 90)
        logo.forward(logo_size * 1.2 - radius * 2)
        logo.circle(radius, 90)
    logo.end_fill()
    logo.penup()
    
    # Draw inner highlight
    logo.goto(left + 10, bottom + 10)
    logo.pendown()
    logo.color("white")
    logo.pensize(1)
    logo.begin_fill()
    for _ in range(2):
        logo.forward(logo_size * 2 - 30)
        logo.circle(8, 90)
        logo.forward(logo_size * 1.2 - 30)
        logo.circle(8, 90)
    logo.end_fill()
    logo.penup()
    
    # Draw DVD text with shadow effect
    logo.goto(x_pos + 2, y_pos - 10)
    logo.color("black")
    logo.write("DVD", align="center", font=("Arial", 36, "bold"))
    
    logo.goto(x_pos - 2, y_pos - 14)
    logo.color("white")
    logo.write("DVD", align="center", font=("Arial", 36, "bold"))
    
    # Draw decorative lines
    logo.penup()
    logo.goto(x_pos - 50, y_pos - 45)
    logo.pendown()
    logo.color(color)
    logo.pensize(2)
    logo.circle(20)
    logo.penup()
    
    logo.goto(x_pos + 50, y_pos - 45)
    logo.pendown()
    logo.circle(20)
    logo.penup()

def update_trail():
    """Update trail effect"""
    # Clear old trail
    for t in screen.turtles():
        if hasattr(t, 'is_trail') and t.is_trail:
            t.clear()
            t.hideturtle()
            screen.turtles().remove(t)
    
    if not trail_enabled:
        return
    
    # Add current position
    trail_positions.append((x_pos, y_pos))
    if len(trail_positions) > trail_length:
        trail_positions.pop(0)
    
    # Create trail with glow effect
    for i, pos in enumerate(trail_positions):
        trail_t = turtle.Turtle()
        trail_t.speed(0)
        trail_t.penup()
        trail_t.hideturtle()
        trail_t.goto(pos[0], pos[1])
        trail_t.is_trail = True
        
        # Fade and size
        alpha = i / len(trail_positions)
        size = alpha * 3 + 1
        
        # Use current color with transparency (simulated)
        current_color = colors[color_index]
        trail_t.color(current_color)
        trail_t.shapesize(size / 15)
        trail_t.shape("circle")
        trail_t.showturtle()
        
        # Add to screen's turtles list
        screen.turtles().append(trail_t)

def bounce_effect(x, y):
    """Create retro particle effect on bounce"""
    for _ in range(15):
        particle = turtle.Turtle()
        particle.speed(0)
        particle.shape("circle")
        particle.color(random.choice(colors))
        particle.shapesize(random.uniform(0.1, 0.5))
        particle.penup()
        particle.goto(x + random.randint(-20, 20), y + random.randint(-20, 20))
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 5)
        
        particle_data = {
            "turtle": particle,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed + 1,
            "life": random.randint(15, 30),
            "rotation": random.uniform(-10, 10)
        }
        particles.append(particle_data)

# Particles system
particles = []

def update_particles():
    """Update particle effects"""
    for particle_data in particles[:]:
        particle_data["turtle"].goto(
            particle_data["turtle"].xcor() + particle_data["vx"],
            particle_data["turtle"].ycor() + particle_data["vy"]
        )
        particle_data["vy"] -= 0.15
        particle_data["life"] -= 1
        
        # Shrink and rotate
        life_ratio = particle_data["life"] / 30
        size = life_ratio * 0.5
        particle_data["turtle"].shapesize(max(0.05, size))
        particle_data["turtle"].right(particle_data["rotation"])
        
        if particle_data["life"] <= 0:
            particle_data["turtle"].hideturtle()
            particles.remove(particle_data)

def update_score():
    """Update score display"""
    global high_score
    
    score_display.clear()
    score_display.write(f"SCORE: {score}", align="left", font=("Arial", 14, "bold"))
    
    if score > high_score:
        high_score = score
    
    high_score_display.clear()
    high_score_display.write(f"🏆 BEST: {high_score}", align="left", font=("Arial", 14, "bold"))
    
    bounce_counter.clear()
    bounce_counter.write(f"💫 BOUNCES: {score}", align="right", font=("Arial", 14, "bold"))

def change_color():
    """Change logo color"""
    global color_index
    color_index = (color_index + 1) % len(colors)
    draw_dvd_logo(colors[color_index])

def toggle_trail():
    """Toggle trail effect"""
    global trail_enabled, trail_positions
    trail_enabled = not trail_enabled
    if not trail_enabled:
        trail_positions.clear()
        for t in screen.turtles():
            if hasattr(t, 'is_trail') and t.is_trail:
                t.clear()
                t.hideturtle()
                # Don't remove while iterating

def speed_up():
    """Increase speed"""
    global x_speed, y_speed
    x_speed *= 1.1
    y_speed *= 1.1
    # Cap speed
    x_speed = min(12, x_speed)
    y_speed = min(12, y_speed)

def reset_animation():
    """Reset the animation"""
    global x_pos, y_pos, x_speed, y_speed, score, color_index, paused, trail_enabled
    
    x_pos = 0
    y_pos = 0
    x_speed = 4
    y_speed = 3.5
    score = 0
    color_index = 0
    trail_enabled = True
    
    # Clear trail
    trail_positions.clear()
    for t in screen.turtles():
        if hasattr(t, 'is_trail') and t.is_trail:
            t.clear()
            t.hideturtle()
    
    # Clear particles
    for p in particles:
        p["turtle"].hideturtle()
    particles.clear()
    
    # Clear pause
    paused = False
    if pause_text:
        pause_text.clear()
        pause_text.hideturtle()
    
    draw_dvd_logo(colors[0])
    update_score()

def toggle_pause():
    """Pause/unpause animation"""
    global paused, pause_text
    paused = not paused
    if paused:
        if pause_text:
            pause_text.clear()
        pause_text = turtle.Turtle()
        pause_text.speed(0)
        pause_text.penup()
        pause_text.hideturtle()
        pause_text.goto(0, 0)
        pause_text.color("#ff6b6b")
        pause_text.write("⏸ PAUSED", align="center", font=("Arial", 40, "bold"))
        pause_text.goto(0, -40)
        pause_text.color("gray")
        pause_text.write("Press SPACE to resume", align="center", font=("Arial", 16, "normal"))
    else:
        if pause_text:
            pause_text.clear()
            pause_text.hideturtle()
            pause_text = None

# Corner detection effect
def create_corner_effect():
    """Special effect when hitting corner"""
    for _ in range(30):
        particle = turtle.Turtle()
        particle.speed(0)
        particle.shape("circle")
        particle.color(random.choice(colors))
        particle.shapesize(random.uniform(0.1, 0.6))
        particle.penup()
        particle.goto(x_pos + random.randint(-30, 30), y_pos + random.randint(-30, 30))
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        
        particle_data = {
            "turtle": particle,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "life": random.randint(20, 40),
            "rotation": random.uniform(-15, 15)
        }
        particles.append(particle_data)

# Main animation loop
def animate():
    global x_pos, y_pos, x_speed, y_speed, score, color_index
    
    if not paused:
        # Update position
        x_pos += x_speed
        y_pos += y_speed
        
        # Check boundaries with corner detection
        corner_bounce = False
        
        # Left wall
        if x_pos - logo_size <= -380:
            x_pos = -380 + logo_size
            x_speed *= -1
            color_index = (color_index + 1) % len(colors)
            draw_dvd_logo(colors[color_index])
            bounce_effect(x_pos, y_pos)
            score += 1
            update_score()
            if y_pos > 300 or y_pos < -300:
                corner_bounce = True
        
        # Right wall
        elif x_pos + logo_size >= 380:
            x_pos = 380 - logo_size
            x_speed *= -1
            color_index = (color_index + 1) % len(colors)
            draw_dvd_logo(colors[color_index])
            bounce_effect(x_pos, y_pos)
            score += 1
            update_score()
            if y_pos > 300 or y_pos < -300:
                corner_bounce = True
        
        # Top wall
        if y_pos + logo_size * 0.6 >= 310:
            y_pos = 310 - logo_size * 0.6
            y_speed *= -1
            color_index = (color_index + 1) % len(colors)
            draw_dvd_logo(colors[color_index])
            bounce_effect(x_pos, y_pos)
            score += 1
            update_score()
            if x_pos > 380 or x_pos < -380:
                corner_bounce = True
        
        # Bottom wall
        elif y_pos - logo_size * 0.6 <= -310:
            y_pos = -310 + logo_size * 0.6
            y_speed *= -1
            color_index = (color_index + 1) % len(colors)
            bounce_effect(x_pos, y_pos)
            score += 1
            update_score()
            if x_pos > 380 or x_pos < -380:
                corner_bounce = True
        
        # Corner effect
        if corner_bounce:
            create_corner_effect()
        
        # Update trail
        update_trail()
        
        # Update particles
        update_particles()
        
        # Randomly change color occasionally (1% chance per frame)
        if random.random() < 0.005:
            color_index = (color_index + 1) % len(colors)
            draw_dvd_logo(colors[color_index])
    
    screen.update()
    screen.ontimer(animate, 20)

# Draw initial logo
draw_dvd_logo(colors[0])
update_score()

# Key bindings
screen.onkey(toggle_pause, "space")
screen.onkey(reset_animation, "r")
screen.onkey(change_color, "c")
screen.onkey(toggle_trail, "t")
screen.onkey(speed_up, "s")
screen.listen()

# Click handler (toggle trail)
screen.onclick(lambda x, y: toggle_trail())

# Start animation
animate()

# Keep window open
screen.mainloop()