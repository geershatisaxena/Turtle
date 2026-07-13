import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball with Increasing Height - Enhanced")
screen.tracer(0)
screen.setup(800, 700)

# Create ground with gradient effect
ground = turtle.Turtle()
ground.speed(0)
ground.penup()
ground.goto(-400, -250)
ground.pendown()
ground.color("dark green")
ground.begin_fill()
ground.goto(400, -250)
ground.goto(400, -300)
ground.goto(-400, -300)
ground.goto(-400, -250)
ground.end_fill()
ground.hideturtle()

# Create decorative ground line
ground_line = turtle.Turtle()
ground_line.speed(0)
ground_line.penup()
ground_line.goto(-400, -250)
ground_line.pendown()
ground_line.color("lime green")
ground_line.pensize(3)
ground_line.goto(400, -250)
ground_line.hideturtle()

# Create ball with glow effect
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.shapesize(1.8)
ball.penup()

# Glow effect for ball
glow = turtle.Turtle()
glow.speed(0)
glow.shape("circle")
glow.color("orange")
glow.shapesize(2.5)
glow.penup()
glow.hideturtle()

# Ball physics variables
ball_x = 0
ball_y = -230
velocity_y = 0
velocity_x = 3
gravity = -0.6
bounce_count = 0
max_bounce_height = 30
height_increment = 8
elasticity = 0.85  # Energy loss factor

# Trail with gradient colors
trail_turtles = []
trail_positions = []
MAX_TRAIL = 30

# Shadow
shadow = turtle.Turtle()
shadow.speed(0)
shadow.shape("circle")
shadow.color("gray")
shadow.shapesize(0.3)
shadow.penup()

# Create stars background
stars = []
def create_stars():
    for _ in range(50):
        star = turtle.Turtle()
        star.speed(0)
        star.penup()
        star.hideturtle()
        star.color("white")
        star.goto(random.randint(-380, 380), random.randint(-240, 300))
        star.dot(random.randint(1, 3))
        stars.append(star)
create_stars()

# Create moon
moon = turtle.Turtle()
moon.speed(0)
moon.penup()
moon.color("light yellow")
moon.goto(300, 250)
moon.shape("circle")
moon.shapesize(3)
moon.hideturtle()

# Display elements
counter_display = turtle.Turtle()
counter_display.speed(0)
counter_display.penup()
counter_display.hideturtle()
counter_display.color("white")
counter_display.goto(-350, 280)

height_display = turtle.Turtle()
height_display.speed(0)
height_display.penup()
height_display.hideturtle()
height_display.color("white")
height_display.goto(-350, 250)

speed_display = turtle.Turtle()
speed_display.speed(0)
speed_display.penup()
speed_display.hideturtle()
speed_display.color("white")
speed_display.goto(-350, 220)

# Energy meter
energy_meter = turtle.Turtle()
energy_meter.speed(0)
energy_meter.penup()
energy_meter.hideturtle()

def update_displays():
    counter_display.clear()
    counter_display.write(f"🏆 Bounces: {bounce_count}", align="left", font=("Arial", 14, "bold"))
    
    height_display.clear()
    current_height = (ball_y + 230) * 0.4
    height_display.write(f"📏 Height: {current_height:.1f}", align="left", font=("Arial", 14, "bold"))
    
    speed_display.clear()
    speed_display.write(f"⚡ Speed: {abs(velocity_y):.1f}", align="left", font=("Arial", 14, "bold"))

def draw_energy_meter():
    energy_meter.clear()
    # Background
    energy_meter.goto(-300, -270)
    energy_meter.pendown()
    energy_meter.color("dark gray")
    energy_meter.begin_fill()
    energy_meter.goto(-300, -250)
    energy_meter.goto(300, -250)
    energy_meter.goto(300, -270)
    energy_meter.goto(-300, -270)
    energy_meter.end_fill()
    energy_meter.penup()
    
    # Energy bar
    max_energy = max_bounce_height * 0.4
    current_energy = (ball_y + 230) * 0.4
    if max_energy > 0:
        percentage = min(1, current_energy / max_energy)
        energy_meter.goto(-300, -270)
        energy_meter.pendown()
        
        # Color gradient from red to green
        if percentage < 0.5:
            r = 1
            g = percentage * 2
            b = 0
        else:
            r = 1 - (percentage - 0.5) * 2
            g = 1
            b = 0
            
        energy_meter.color((r, g, b))
        energy_meter.begin_fill()
        energy_meter.goto(-300, -250)
        energy_meter.goto(-300 + percentage * 600, -250)
        energy_meter.goto(-300 + percentage * 600, -270)
        energy_meter.goto(-300, -270)
        energy_meter.end_fill()
        energy_meter.penup()
        
        # Label
        energy_meter.goto(0, -285)
        energy_meter.color("white")
        energy_meter.write(f"Energy: {current_energy:.1f} / {max_energy:.1f}", 
                          align="center", font=("Arial", 10, "normal"))

# Particles system
particles = []

def create_burst_particles():
    # Create explosion of particles on bounce
    colors = ["red", "orange", "yellow", "gold", "white"]
    for _ in range(15):
        particle = turtle.Turtle()
        particle.speed(0)
        particle.shape("circle")
        particle.color(random.choice(colors))
        particle.shapesize(random.uniform(0.2, 0.6))
        particle.penup()
        particle.goto(ball_x + random.randint(-15, 15), ball_y)
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        
        particle_data = {
            "turtle": particle,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed + 2,
            "life": random.randint(15, 30),
            "max_life": 30
        }
        particles.append(particle_data)

def update_particles():
    for particle_data in particles[:]:
        # Update position
        particle_data["turtle"].goto(
            particle_data["turtle"].xcor() + particle_data["vx"],
            particle_data["turtle"].ycor() + particle_data["vy"]
        )
        particle_data["vy"] -= 0.15
        particle_data["life"] -= 1
        
        # Fade and shrink
        life_ratio = particle_data["life"] / particle_data["max_life"]
        size = life_ratio * 0.6
        particle_data["turtle"].shapesize(max(0.1, size))
        
        # Fade color
        if life_ratio < 0.3:
            particle_data["turtle"].color("gray")
        
        if particle_data["life"] <= 0:
            particle_data["turtle"].hideturtle()
            particles.remove(particle_data)

# Trail system
def update_trail():
    # Add current position to trail
    trail_positions.append((ball_x, ball_y))
    if len(trail_positions) > MAX_TRAIL:
        trail_positions.pop(0)
    
    # Clear old trail turtles
    for t in trail_turtles:
        t.clear()
        t.hideturtle()
    trail_turtles.clear()
    
    # Create new trail with gradient
    for i, pos in enumerate(trail_positions):
        trail_t = turtle.Turtle()
        trail_t.speed(0)
        trail_t.penup()
        trail_t.hideturtle()
        trail_t.goto(pos[0], pos[1])
        
        # Size and color based on position in trail
        alpha = i / len(trail_positions)
        size = alpha * 0.5 + 0.1
        
        # Color from red to orange to yellow
        if alpha < 0.5:
            r = 1
            g = alpha * 2
            b = 0
        else:
            r = 1 - (alpha - 0.5) * 2
            g = 1
            b = 0
        
        trail_t.color((r, g, b))
        trail_t.dot(size * 8)
        trail_turtles.append(trail_t)

# Shockwave effect
shockwaves = []

def create_shockwave():
    wave = turtle.Turtle()
    wave.speed(0)
    wave.penup()
    wave.hideturtle()
    wave.goto(ball_x, -250)
    wave.color("white")
    
    wave_data = {
        "turtle": wave,
        "radius": 5,
        "max_radius": 80,
        "speed": 3,
        "active": True
    }
    shockwaves.append(wave_data)

def update_shockwaves():
    for wave_data in shockwaves[:]:
        if not wave_data["active"]:
            continue
        
        wave_data["radius"] += wave_data["speed"]
        wave_data["turtle"].clear()
        
        if wave_data["radius"] >= wave_data["max_radius"]:
            wave_data["active"] = False
            wave_data["turtle"].hideturtle()
            shockwaves.remove(wave_data)
            continue
        
        # Draw shockwave ring
        wave_data["turtle"].penup()
        wave_data["turtle"].goto(ball_x, -250 - wave_data["radius"])
        wave_data["turtle"].pendown()
        wave_data["turtle"].pensize(3 - (wave_data["radius"] / wave_data["max_radius"]) * 3)
        wave_data["turtle"].color((1, 1 - wave_data["radius"]/wave_data["max_radius"], 0))
        wave_data["turtle"].circle(wave_data["radius"])
        wave_data["turtle"].penup()

# Bounce effect with flash
def bounce_flash():
    flash = turtle.Turtle()
    flash.speed(0)
    flash.penup()
    flash.goto(ball_x, -250)
    flash.color("yellow")
    flash.shape("circle")
    flash.shapesize(3)
    flash.showturtle()
    
    def animate_flash(step=0):
        if step < 8:
            size = 3 - step * 0.35
            flash.shapesize(max(0.1, size))
            flash.color(f"{(1 - step/8) * 0.8}")
            screen.ontimer(lambda: animate_flash(step + 1), 30)
        else:
            flash.hideturtle()
    
    animate_flash()

# Main animation loop
def animate():
    global ball_x, ball_y, velocity_y, velocity_x, bounce_count, max_bounce_height
    
    # Apply gravity
    velocity_y += gravity
    
    # Update position
    ball_x += velocity_x
    ball_y += velocity_y
    
    # Bounce off walls with glow effect
    if ball_x > 380:
        ball_x = 380
        velocity_x *= -elasticity
        # Wall bounce particles
        for _ in range(5):
            create_wall_particle(ball_x, ball_y)
    elif ball_x < -380:
        ball_x = -380
        velocity_x *= -elasticity
        for _ in range(5):
            create_wall_particle(ball_x, ball_y)
    
    # Bounce off ground
    if ball_y <= -230:
        ball_y = -230
        
        # Increase max height
        max_bounce_height += height_increment
        
        # Calculate new velocity
        velocity_y = math.sqrt(2 * abs(gravity) * max_bounce_height)
        bounce_count += 1
        
        # Create effects
        create_burst_particles()
        create_shockwave()
        bounce_flash()
        
        # Randomize horizontal movement slightly
        velocity_x += random.uniform(-0.5, 0.5)
        velocity_x = max(-6, min(6, velocity_x))
        
        # Update displays
        update_displays()
        draw_energy_meter()
    
    # Update ball position
    ball.goto(ball_x, ball_y)
    
    # Update glow
    glow.goto(ball_x, ball_y)
    glow.showturtle()
    glow_color = 0.5 + (ball_y + 230) / 500
    glow.color((glow_color, glow_color * 0.5, 0))
    
    # Update shadow
    shadow.goto(ball_x, -250)
    shadow_size = 0.3 + (ball_y + 230) / 400
    shadow.shapesize(shadow_size)
    
    # Update trail
    update_trail()
    
    # Update particles
    update_particles()
    
    # Update shockwaves
    update_shockwaves()
    
    screen.update()
    screen.ontimer(animate, 20)

def create_wall_particle(x, y):
    particle = turtle.Turtle()
    particle.speed(0)
    particle.shape("circle")
    particle.color("cyan")
    particle.shapesize(0.3)
    particle.penup()
    particle.goto(x, y)
    
    particle_data = {
        "turtle": particle,
        "vx": random.uniform(-2, 2),
        "vy": random.uniform(-2, 2),
        "life": random.randint(10, 20),
        "max_life": 20
    }
    particles.append(particle_data)

# Title
title = turtle.Turtle()
title.speed(0)
title.penup()
title.hideturtle()
title.color("white")
title.goto(0, 320)
title.write("🎯 BOUNCING BALL", align="center", font=("Arial", 24, "bold"))

subtitle = turtle.Turtle()
subtitle.speed(0)
subtitle.penup()
subtitle.hideturtle()
subtitle.color("gray")
subtitle.goto(0, 290)
subtitle.write("Each bounce goes higher!", align="center", font=("Arial", 14, "normal"))

# Controls
controls = turtle.Turtle()
controls.speed(0)
controls.penup()
controls.hideturtle()
controls.color("light gray")
controls.goto(0, -320)
controls.write("🔄 Click to reset • ␣ SPACE to pause • R to reset", 
              align="center", font=("Arial", 12, "normal"))

# Pause functionality
paused = False
pause_text = None

def toggle_pause():
    global paused, pause_text
    paused = not paused
    if paused:
        if pause_text:
            pause_text.clear()
        pause_text = turtle.Turtle()
        pause_text.speed(0)
        pause_text.penup()
        pause_text.hideturtle()
        pause_text.goto(0, 100)
        pause_text.color("yellow")
        pause_text.write("⏸ PAUSED", align="center", font=("Arial", 40, "bold"))
        pause_text.goto(0, 60)
        pause_text.write("Press SPACE to resume", align="center", font=("Arial", 16, "normal"))
    else:
        if pause_text:
            pause_text.clear()
            pause_text.hideturtle()
            pause_text = None

def reset_animation():
    global ball_x, ball_y, velocity_y, velocity_x, bounce_count, max_bounce_height
    global trail_positions, particles, shockwaves, paused, pause_text
    
    # Reset ball
    ball_x = 0
    ball_y = -230
    velocity_y = 0
    velocity_x = 3
    bounce_count = 0
    max_bounce_height = 30
    
    # Clear trail
    trail_positions.clear()
    for t in trail_turtles:
        t.clear()
        t.hideturtle()
    trail_turtles.clear()
    
    # Clear particles
    for p in particles:
        p["turtle"].hideturtle()
    particles.clear()
    
    # Clear shockwaves
    for s in shockwaves:
        s["turtle"].clear()
        s["turtle"].hideturtle()
    shockwaves.clear()
    
    # Clear pause
    paused = False
    if pause_text:
        pause_text.clear()
        pause_text.hideturtle()
        pause_text = None
    
    # Update displays
    update_displays()
    draw_energy_meter()

# Key bindings
screen.onkey(toggle_pause, "space")
screen.onkey(reset_animation, "r")
screen.listen()

# Click to reset
screen.onclick(lambda x, y: reset_animation())

# Initial setup
update_displays()
draw_energy_meter()

# Start animation
animate()

# Keep window open
screen.mainloop()