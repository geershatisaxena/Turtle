import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("DVD Logo Bouncing Animation")
screen.tracer(0)
screen.setup(800, 700)

# Create DVD logo text
logo = turtle.Turtle()
logo.speed(0)
logo.penup()
logo.hideturtle()

# Logo properties
logo_width = 120
logo_height = 60
x_pos = 0
y_pos = 0
x_speed = 3
y_speed = 4
color_index = 0
colors = ["red", "blue", "green", "yellow", "purple", "cyan", "orange", "pink", "lime", "gold"]

# Trail effect
trail_enabled = True
trail_length = 20
trail_positions = []
trail_turtles = []

# Shadow
shadow = turtle.Turtle()
shadow.speed(0)
shadow.penup()
shadow.hideturtle()
shadow.color("dark gray")

# Score counter
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.penup()
score_display.hideturtle()
score_display.color("white")
score_display.goto(-350, 300)

# Speed display
speed_display = turtle.Turtle()
speed_display.speed(0)
speed_display.penup()
speed_display.hideturtle()
speed_display.color("white")
speed_display.goto(-350, 270)

# Color display
color_display = turtle.Turtle()
color_display.speed(0)
color_display.penup()
color_display.hideturtle()
color_display.color("white")
color_display.goto(-350, 240)

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.penup()
instructions.hideturtle()
instructions.color("gray")
instructions.goto(0, -320)
instructions.write("Click: Toggle Trail • SPACE: Pause • R: Reset • C: Change Color", 
                  align="center", font=("Arial", 12, "normal"))

# Title
title = turtle.Turtle()
title.speed(0)
title.penup()
title.hideturtle()
title.color("white")
title.goto(0, 320)
title.write("📀 DVD LOGO BOUNCE", align="center", font=("Arial", 20, "bold"))

# Pause variables
paused = False
pause_text = None

def draw_dvd_logo(color):
    """Draw the DVD logo with given color"""
    logo.clear()
    logo.color(color)
    logo.penup()
    
    # Calculate logo position (centered)
    logo_x = x_pos - logo_width / 2
    logo_y = y_pos - logo_height / 2
    
    # Draw DVD text
    logo.goto(x_pos, y_pos)
    logo.pendown()
    
    # Draw a rounded rectangle background
    logo.penup()
    logo.goto(logo_x, logo_y)
    logo.pendown()
    logo.begin_fill()
    
    # Rounded rectangle
    corner_radius = 10
    for i in range(2):
        logo.forward(logo_width - corner_radius * 2)
        logo.circle(corner_radius, 90)
        logo.forward(logo_height - corner_radius * 2)
        logo.circle(corner_radius, 90)
    logo.end_fill()
    logo.penup()
    
    # Draw DVD text
    logo.goto(x_pos, y_pos - 8)
    logo.color("white")
    logo.write("DVD", align="center", font=("Arial", 28, "bold"))
    
    # Draw decorative disc lines
    logo.penup()
    logo.goto(x_pos - 30, y_pos - 35)
    logo.color(color)
    logo.pendown()
    logo.circle(10)
    logo.penup()
    logo.goto(x_pos + 30, y_pos - 35)
    logo.pendown()
    logo.circle(10)
    logo.penup()

def update_trail():
    """Update the trail effect"""
    # Clear old trail turtles
    for t in trail_turtles:
        t.clear()
        t.hideturtle()
    trail_turtles.clear()
    
    if not trail_enabled:
        return
    
    # Add current position to trail
    trail_positions.append((x_pos, y_pos))
    if len(trail_positions) > trail_length:
        trail_positions.pop(0)
    
    # Create trail with fading effect
    for i, pos in enumerate(trail_positions):
        trail_t = turtle.Turtle()
        trail_t.speed(0)
        trail_t.penup()
        trail_t.hideturtle()
        trail_t.goto(pos[0], pos[1])
        
        # Fade based on position in trail
        alpha = i / len(trail_positions)
        size = alpha * 2 + 0.5
        
        # Use current color with fading
        current_color = colors[color_index]
        trail_t.color(current_color)
        trail_t.shapesize(size / 10)
        trail_t.shape("circle")
        trail_t.showturtle()
        trail_turtles.append(trail_t)

def update_score():
    """Update score display"""
    score_display.clear()
    score_display.write(f"🏆 Score: {score}", align="left", font=("Arial", 14, "bold"))
    
    speed_display.clear()
    total_speed = math.sqrt(x_speed**2 + y_speed**2)
    speed_display.write(f"⚡ Speed: {total_speed:.1f}", align="left", font=("Arial", 14, "bold"))
    
    color_display.clear()
    color_display.write(f"🎨 Color: {colors[color_index].upper()}", align="left", font=("Arial", 14, "bold"))

def bounce_effect(x, y):
    """Create particles on bounce"""
    for _ in range(10):
        particle = turtle.Turtle()
        particle.speed(0)
        particle.shape("circle")
        particle.color(colors[color_index])
        particle.shapesize(random.uniform(0.1, 0.4))
        particle.penup()
        particle.goto(x, y)
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 4)
        
        particle_data = {
            "turtle": particle,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "life": random.randint(10, 25)
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
        particle_data["vy"] -= 0.1
        particle_data["life"] -= 1
        
        # Shrink and fade
        size = particle_data["life"] / 25
        particle_data["turtle"].shapesize(max(0.05, size * 0.4))
        
        if particle_data["life"] <= 0:
            particle_data["turtle"].hideturtle()
            particles.remove(particle_data)

def change_color():
    """Change the logo color"""
    global color_index
    color_index = (color_index + 1) % len(colors)
    draw_dvd_logo(colors[color_index])
    update_score()

def toggle_trail():
    """Toggle trail effect on/off"""
    global trail_enabled, trail_positions
    trail_enabled = not trail_enabled
    if not trail_enabled:
        trail_positions.clear()
        for t in trail_turtles:
            t.clear()
            t.hideturtle()
        trail_turtles.clear()

def reset_animation():
    """Reset the animation"""
    global x_pos, y_pos, x_speed, y_speed, score, color_index, paused
    global trail_positions, particles, trail_enabled
    
    x_pos = 0
    y_pos = 0
    x_speed = 3 + random.uniform(-0.5, 0.5)
    y_speed = 4 + random.uniform(-0.5, 0.5)
    score = 0
    color_index = 0
    
    # Clear trail
    trail_positions.clear()
    for t in trail_turtles:
        t.clear()
        t.hideturtle()
    trail_turtles.clear()
    trail_enabled = True
    
    # Clear particles
    for p in particles:
        p["turtle"].hideturtle()
    particles.clear()
    
    # Clear pause
    paused = False
    if pause_text:
        pause_text.clear()
        pause_text.hideturtle()
    
    draw_dvd_logo(colors[color_index])
    update_score()

def toggle_pause():
    """Pause/unpause the animation"""
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
        pause_text.color("red")
        pause_text.write("⏸ PAUSED", align="center", font=("Arial", 40, "bold"))
        pause_text.goto(0, -40)
        pause_text.write("Press SPACE to resume", align="center", font=("Arial", 16, "normal"))
    else:
        if pause_text:
            pause_text.clear()
            pause_text.hideturtle()
            pause_text = None

# Main animation loop
def animate():
    global x_pos, y_pos, x_speed, y_speed, score, color_index
    
    if not paused:
        # Update position
        x_pos += x_speed
        y_pos += y_speed
        
        # Check boundaries and bounce
        bounced = False
        
        # Left wall
        if x_pos - logo_width/2 <= -380:
            x_pos = -380 + logo_width/2
            x_speed *= -1
            bounced = True
            color_index = (color_index + 1) % len(colors)
            draw_dvd_logo(colors[color_index])
            bounce_effect(x_pos, y_pos)
            score += 1
            update_score()
        
        # Right wall
        elif x_pos + logo_width/2 >= 380:
            x_pos = 380 - logo_width/2
            x_speed *= -1
            bounced = True
            color_index = (color_index + 1) % len(colors)
            draw_dvd_logo(colors[color_index])
            bounce_effect(x_pos, y_pos)
            score += 1
            update_score()
        
        # Top wall
        if y_pos + logo_height/2 >= 310:
            y_pos = 310 - logo_height/2
            y_speed *= -1
            bounced = True
            color_index = (color_index + 1) % len(colors)
            draw_dvd_logo(colors[color_index])
            bounce_effect(x_pos, y_pos)
            score += 1
            update_score()
        
        # Bottom wall
        elif y_pos - logo_height/2 <= -310:
            y_pos = -310 + logo_height/2
            y_speed *= -1
            bounced = True
            color_index = (color_index + 1) % len(colors)
            draw_dvd_logo(colors[color_index])
            bounce_effect(x_pos, y_pos)
            score += 1
            update_score()
        
        # Update shadow
        shadow.goto(x_pos, -300)
        shadow_size = 0.5 + (y_pos + 310) / 600
        shadow.shapesize(shadow_size)
        
        # Update trail
        update_trail()
        
        # Update particles
        update_particles()
        
        # Slightly randomize speed occasionally
        if random.random() < 0.001:
            x_speed += random.uniform(-0.2, 0.2)
            y_speed += random.uniform(-0.2, 0.2)
            # Limit speed
            x_speed = max(1, min(8, x_speed))
            y_speed = max(1, min(8, y_speed))
    
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
screen.listen()

# Click handlers
screen.onclick(lambda x, y: toggle_trail())

# Start animation
animate()

# Keep window open
screen.mainloop()