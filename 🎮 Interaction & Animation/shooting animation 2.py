import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Simple Shooting Animation - Projectile Motion")
screen.bgcolor("black")
screen.setup(width=1000, height=700)
screen.tracer(0)

# Create the cannon/base
cannon = turtle.Turtle()
cannon.speed(0)
cannon.penup()
cannon.hideturtle()

# Create the projectile (bullet)
projectile = turtle.Turtle()
projectile.speed(0)
projectile.shape("circle")
projectile.color("red")
projectile.shapesize(0.8, 0.8)
projectile.penup()

# Create target
target = turtle.Turtle()
target.speed(0)
target.shape("square")
target.color("green")
target.shapesize(1.5, 1.5)
target.penup()

# Create UI turtles
ui_turtle = turtle.Turtle()
ui_turtle.speed(0)
ui_turtle.color("white")
ui_turtle.penup()
ui_turtle.hideturtle()

score_turtle = turtle.Turtle()
score_turtle.speed(0)
ui_turtle.color("white")
ui_turtle.penup()
ui_turtle.hideturtle()

# Particle system for explosion effects
particles = []

# Game variables
score = 0
shots_fired = 0
hits = 0
is_shooting = False
bullet_x = 0
bullet_y = 0
bullet_vx = 0
bullet_vy = 0
gravity = -0.5
power = 15
angle = 45
target_x = 300
target_y = 0
target_speed = 2
target_direction = 1

# Target boundaries
target_left = -350
target_right = 350

# Cannon position
cannon_x = -400
cannon_y = -200

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
        speed = random.uniform(2, 5)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = random.randint(20, 40)
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
        # Fade out
        new_size = max(0.1, 0.3 * (1 - self.age / self.life))
        self.turtle.shapesize(new_size, new_size)
        return True

def create_explosion(x, y):
    """Create explosion particles"""
    colors = ["red", "orange", "yellow", "white"]
    for _ in range(25):
        particles.append(Particle(x, y, random.choice(colors)))

def draw_cannon():
    """Draw the cannon at its position"""
    cannon.clear()
    cannon.penup()
    cannon.goto(cannon_x, cannon_y)
    cannon.pendown()
    cannon.color("gray")
    cannon.begin_fill()
    cannon.fillcolor("darkgray")
    
    # Cannon base
    for _ in range(2):
        cannon.forward(40)
        cannon.left(90)
        cannon.forward(30)
        cannon.left(90)
    cannon.end_fill()
    
    # Cannon barrel
    cannon.penup()
    cannon.goto(cannon_x + 20, cannon_y + 15)
    cannon.pendown()
    cannon.color("silver")
    cannon.begin_fill()
    cannon.fillcolor("silver")
    cannon.setheading(angle)
    cannon.forward(50)
    cannon.left(90)
    cannon.forward(10)
    cannon.left(90)
    cannon.forward(50)
    cannon.left(90)
    cannon.forward(10)
    cannon.end_fill()
    cannon.penup()
    
    # Draw angle indicator
    cannon.goto(cannon_x + 20, cannon_y + 20)
    cannon.color("yellow")
    cannon.write(f"{angle}°", font=("Arial", 10, "normal"))

def draw_target():
    """Draw the target"""
    target.goto(target_x, target_y)
    target.showturtle()

def shoot():
    """Launch the projectile"""
    global is_shooting, bullet_x, bullet_y, bullet_vx, bullet_vy, shots_fired
    
    if not is_shooting:
        is_shooting = True
        shots_fired += 1
        
        # Calculate initial velocity components
        angle_rad = math.radians(angle)
        bullet_vx = power * math.cos(angle_rad)
        bullet_vy = power * math.sin(angle_rad)
        
        # Start position (tip of cannon)
        bullet_x = cannon_x + 20 + 50 * math.cos(angle_rad)
        bullet_y = cannon_y + 15 + 50 * math.sin(angle_rad)
        projectile.goto(bullet_x, bullet_y)
        projectile.showturtle()
        
        update_stats()

def update_projectile():
    """Update projectile position using physics"""
    global is_shooting, bullet_x, bullet_y, bullet_vx, bullet_vy, score, hits
    
    if is_shooting:
        # Update velocity (gravity affects vertical)
        bullet_vy += gravity
        
        # Update position
        bullet_x += bullet_vx
        bullet_y += bullet_vy
        
        projectile.goto(bullet_x, bullet_y)
        
        # Check collision with target
        if (abs(bullet_x - target_x) < 25 and 
            abs(bullet_y - target_y) < 25):
            # Hit!
            is_shooting = False
            projectile.hideturtle()
            hits += 1
            score += 10
            create_explosion(bullet_x, bullet_y)
            update_stats()
            show_message("🎯 HIT! +10 🎯", "green")
            # Move target to new position
            target_x = random.randint(-300, 300)
            target_y = random.randint(-100, 200)
            draw_target()
        
        # Check if out of bounds (miss)
        elif (bullet_x > 500 or bullet_x < -500 or 
              bullet_y < -350 or bullet_y > 400):
            is_shooting = False
            projectile.hideturtle()
            if bullet_y < -350:
                create_explosion(bullet_x, -350)
            show_message("💨 MISS! 💨", "red")

def update_target():
    """Move target back and forth"""
    global target_x, target_direction
    target_x += target_speed * target_direction
    
    if target_x > target_right:
        target_x = target_right
        target_direction = -1
    elif target_x < target_left:
        target_x = target_left
        target_direction = 1
    
    target.goto(target_x, target_y)

def update_particles():
    """Update all explosion particles"""
    for particle in particles[:]:
        if not particle.update():
            particles.remove(particle)

def show_message(text, color):
    """Display temporary message"""
    msg = turtle.Turtle()
    msg.speed(0)
    msg.color(color)
    msg.penup()
    msg.hideturtle()
    msg.goto(0, 250)
    msg.write(text, align="center", font=("Arial", 20, "bold"))
    screen.ontimer(lambda: msg.clear(), 1000)

def update_stats():
    """Update score display"""
    ui_turtle.clear()
    ui_turtle.goto(-450, 320)
    ui_turtle.write(f"🎯 SCORE: {score} 🎯", font=("Arial", 16, "bold"))
    ui_turtle.goto(-450, 290)
    ui_turtle.write(f"Shots: {shots_fired} | Hits: {hits} | Accuracy: {round(hits/shots_fired*100 if shots_fired>0 else 0)}%", 
                     font=("Arial", 12, "normal"))
    ui_turtle.goto(-450, 260)
    ui_turtle.write(f"Power: {power} | Angle: {angle}°", font=("Arial", 12, "normal"))

def increase_power():
    global power
    power = min(power + 2, 30)
    draw_cannon()
    update_stats()
    show_message(f"Power: {power}", "cyan")

def decrease_power():
    global power
    power = max(power - 2, 5)
    draw_cannon()
    update_stats()
    show_message(f"Power: {power}", "cyan")

def increase_angle():
    global angle
    angle = min(angle + 5, 85)
    draw_cannon()
    update_stats()

def decrease_angle():
    global angle
    angle = max(angle - 5, 0)
    draw_cannon()
    update_stats()

def reset_game():
    global score, shots_fired, hits, is_shooting
    score = 0
    shots_fired = 0
    hits = 0
    is_shooting = False
    projectile.hideturtle()
    update_stats()
    show_message("Game Reset!", "gold")

def draw_ground():
    """Draw ground line"""
    ground = turtle.Turtle()
    ground.speed(0)
    ground.color("green")
    ground.penup()
    ground.goto(-500, -250)
    ground.pendown()
    ground.pensize(3)
    ground.goto(500, -250)
    ground.hideturtle()

def draw_instructions():
    """Draw instruction panel"""
    instr = turtle.Turtle()
    instr.speed(0)
    instr.color("gray")
    instr.penup()
    instr.hideturtle()
    instr.goto(0, -330)
    instr.write("UP/DOWN: Angle | +/-: Power | SPACE: Shoot | R: Reset | ESC: Exit", 
               align="center", font=("Arial", 12, "normal"))

def draw_title():
    """Draw title"""
    title = turtle.Turtle()
    title.speed(0)
    title.color("gold")
    title.penup()
    title.hideturtle()
    title.goto(0, 360)
    title.write("💥 PROJECTILE MOTION SHOOTING GAME 💥", align="center", font=("Arial", 16, "bold"))

# Draw initial elements
draw_title()
draw_instructions()
draw_ground()
draw_cannon()
draw_target()
update_stats()

# Keyboard bindings
screen.listen()
screen.onkey(shoot, "space")
screen.onkey(increase_power, "plus")
screen.onkey(increase_power, "equal")
screen.onkey(decrease_power, "minus")
screen.onkey(increase_angle, "Up")
screen.onkey(decrease_angle, "Down")
screen.onkey(reset_game, "r")
screen.onkey(lambda: screen.bye(), "Escape")

print("=" * 60)
print("        SIMPLE SHOOTING ANIMATION")
print("=" * 60)
print()
print("Projectile motion physics with real gravity!")
print()
print("GAME INFO:")
print("  • Shoot the green target to score points")
print("  • Each hit: +10 points")
print("  • Target moves back and forth")
print("  • Physics includes gravity and angle")
print()
print("CONTROLS:")
print("  UP/DOWN   - Adjust cannon angle (0-85°)")
print("  +/-       - Adjust power (5-30)")
print("  SPACE     - Shoot!")
print("  R         - Reset game")
print("  ESC       - Exit")
print()
print("PHYSICS FORMULA:")
print("  x = v₀·cos(θ)·t")
print("  y = v₀·sin(θ)·t - ½·g·t²")
print()
print("Aim carefully and watch the arc!")

# Main animation loop
def animate():
    update_projectile()
    update_target()
    update_particles()
    screen.update()
    screen.ontimer(animate, 20)

# Start animation
animate()
screen.mainloop()