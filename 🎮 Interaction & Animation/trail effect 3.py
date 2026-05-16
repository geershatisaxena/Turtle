import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Fire Snake - Living Trail Animation")
screen.bgcolor("black")
screen.tracer(0)

# Trail particle system
class FireParticle:
    def __init__(self, x, y, color, size=8):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.shapesize(size/10)
        self.turtle.speed(0)
        
        self.lifetime = random.randint(20, 40)
        self.age = 0
        self.initial_size = size
        self.drift_x = random.uniform(-0.5, 0.5)  # Slight drift
        self.drift_y = random.uniform(-0.5, 0.5)
        
    def update(self):
        self.age += 1
        if self.age >= self.lifetime:
            return False
            
        # Drift slowly
        x, y = self.turtle.position()
        self.turtle.goto(x + self.drift_x, y + self.drift_y)
        
        # Shrink and fade
        progress = self.age / self.lifetime
        new_size = max(0.1, (self.initial_size/10) * (1 - progress))
        self.turtle.shapesize(new_size)
        
        # Fade color to dark red then black
        if progress < 0.5:
            brightness = 1 - progress * 0.5
            self.turtle.color((brightness, brightness * 0.3, 0))
        else:
            brightness = 0.5 - (progress - 0.5)
            self.turtle.color((brightness * 0.5, 0, 0))
        
        return True
    
    def remove(self):
        self.turtle.hideturtle()
        self.turtle.clear()

# ============================================
# FIRE SNAKE - The Main Attraction
# ============================================
class FireSnake:
    def __init__(self):
        self.segments = []
        self.num_segments = 20
        self.segment_distance = 12
        self.create_snake()
        
        # Head movement
        self.head_angle = 0
        self.head_speed = 3
        self.wave_amplitude = 30
        self.wave_frequency = 0.1
        self.time = 0
        
        # Color gradient for snake body
        self.colors = ["red", "orange", "yellow", "gold", "orange", "red"]
        
    def create_snake(self):
        """Create the snake body segments."""
        for i in range(self.num_segments):
            segment = turtle.Turtle()
            segment.shape("circle")
            segment.penup()
            segment.speed(0)
            segment.color(self.colors[i % len(self.colors)])
            segment.shapesize(0.8 - (i * 0.02))  # Tapered body
            self.segments.append(segment)
            
    def update(self):
        """Update snake position with wave motion."""
        self.time += 0.05
        
        # Calculate head position with figure-8 pattern
        t = self.time
        head_x = math.sin(t * 0.5) * 200
        head_y = math.cos(t * 0.8) * 150
        
        # Add some random movement to head
        head_x += math.sin(t * 2) * 20
        head_y += math.cos(t * 1.5) * 15
        
        # Move head
        self.segments[0].goto(head_x, head_y)
        
        # Create fire trail at head
        fire_color = random.choice(["red", "orange", "yellow"])
        particle = FireParticle(head_x, head_y, fire_color, random.uniform(6, 10))
        globals()['trail_particles'].append(particle)
        
        # Move body segments to follow head
        for i in range(1, self.num_segments):
            # Get position of segment ahead
            prev_x, prev_y = self.segments[i-1].position()
            
            # Calculate direction to previous segment
            curr_x, curr_y = self.segments[i].position()
            dx = prev_x - curr_x
            dy = prev_y - curr_y
            distance = math.sqrt(dx*dx + dy*dy)
            
            if distance > self.segment_distance:
                # Move towards previous segment
                angle = math.atan2(dy, dx)
                new_x = curr_x + math.cos(angle) * (distance - self.segment_distance)
                new_y = curr_y + math.sin(angle) * (distance - self.segment_distance)
                self.segments[i].goto(new_x, new_y)
            
            # Create trail from body segments too
            if i % 3 == 0 and random.random() < 0.3:
                body_color = self.colors[i % len(self.colors)]
                particle = FireParticle(curr_x, curr_y, body_color, random.uniform(4, 7))
                globals()['trail_particles'].append(particle)

# ============================================
# GALACTIC SPINNER - Another cool effect
# ============================================
class GalacticSpinner:
    def __init__(self):
        self.spinner = turtle.Turtle()
        self.spinner.shape("turtle")
        self.spinner.color("cyan")
        self.spinner.penup()
        self.spinner.speed(0)
        self.angle = 0
        self.radius = 20
        self.growing = True
        self.color_index = 0
        self.colors = ["cyan", "magenta", "yellow", "lime", "purple", "blue"]
        
    def update(self):
        # Spiral motion
        rad_angle = math.radians(self.angle)
        x = math.cos(rad_angle) * self.radius
        y = math.sin(rad_angle) * self.radius * 0.6  # Elliptical
        
        self.spinner.goto(x, y)
        
        # Create colorful trail
        color = self.colors[self.color_index % len(self.colors)]
        particle = FireParticle(x, y, color, random.uniform(5, 9))
        globals()['trail_particles'].append(particle)
        
        # Update parameters
        self.angle += 12
        
        if self.growing:
            self.radius += 2
            if self.radius >= 180:
                self.growing = False
        else:
            self.radius -= 2
            if self.radius <= 20:
                self.growing = True
                
        self.color_index += 1

# ============================================
# PARTICLE EXPLOSION - Interactive effect
# ============================================
class ParticleExplosion:
    def __init__(self):
        self.exploding = False
        
    def explode(self, x, y):
        """Create explosion at mouse click."""
        for _ in range(100):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 12)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            
            # Create custom particle with velocity
            class ExplosionParticle(FireParticle):
                def __init__(self, x, y, vx, vy, color, size):
                    super().__init__(x, y, color, size)
                    self.vx = vx
                    self.vy = vy
                    self.gravity = -0.2
                    
                def update(self):
                    self.age += 1
                    if self.age >= self.lifetime:
                        return False
                    
                    # Apply physics
                    self.vy += self.gravity
                    x, y = self.turtle.position()
                    self.turtle.goto(x + self.vx, y + self.vy)
                    
                    # Shrink and fade
                    progress = self.age / self.lifetime
                    new_size = max(0.1, (self.initial_size/10) * (1 - progress))
                    self.turtle.shapesize(new_size)
                    brightness = 1 - progress
                    self.turtle.color((brightness, brightness * 0.3, 0))
                    
                    return True
            
            color = random.choice(["red", "orange", "yellow", "gold"])
            particle = ExplosionParticle(x, y, vx, vy, color, random.uniform(4, 8))
            globals()['trail_particles'].append(particle)

# ============================================
# AURORA WAVES - Beautiful wave pattern
# ============================================
class AuroraWaves:
    def __init__(self):
        self.wave_turtles = []
        self.num_waves = 8
        self.create_waves()
        self.time = 0
        
    def create_waves(self):
        """Create multiple wave turtles."""
        for i in range(self.num_waves):
            wave = turtle.Turtle()
            wave.shape("circle")
            wave.penup()
            wave.speed(0)
            wave.color(self.get_aurora_color(i))
            wave.shapesize(0.5)
            self.wave_turtles.append(wave)
            
    def get_aurora_color(self, index):
        colors = ["#00ff88", "#00ffcc", "#00ccff", "#0088ff", 
                  "#00ffaa", "#33ffcc", "#66ffdd", "#99ffee"]
        return colors[index % len(colors)]
        
    def update(self):
        self.time += 0.03
        
        for i, wave in enumerate(self.wave_turtles):
            # Wave motion formula
            offset = i * 0.5
            x = math.sin(self.time * 1.5 + offset) * 300
            y = math.cos(self.time * 1.2 + offset * 0.7) * 150
            wave.goto(x, y)
            
            # Create trail with aurora colors
            particle = FireParticle(x, y, self.get_aurora_color(i), random.uniform(3, 6))
            globals()['trail_particles'].append(particle)

# ============================================
# Main Program
# ============================================

trail_particles = []
current_animation = None
animation_running = True

def update_all():
    """Global update function."""
    global animation_running, trail_particles
    
    if not animation_running:
        return
        
    # Update current animation
    if current_animation:
        current_animation.update()
    
    # Update trail particles
    active_particles = []
    for particle in trail_particles:
        if particle.update():
            active_particles.append(particle)
        else:
            particle.remove()
    trail_particles = active_particles
    
    screen.update()
    screen.ontimer(update_all, 25)

def start_fire_snake():
    global current_animation, trail_particles, animation_running
    trail_particles.clear()
    animation_running = True
    current_animation = FireSnake()
    screen.bgcolor("black")
    print("🔥 FIRE SNAKE ACTIVE! 🔥")
    print("Watch the glowing snake leave a fiery trail!")

def start_galactic_spinner():
    global current_animation, trail_particles, animation_running
    trail_particles.clear()
    animation_running = True
    current_animation = GalacticSpinner()
    screen.bgcolor("darkblue")
    print("🌀 GALACTIC SPINNER ACTIVE! 🌀")
    print("Hypnotic spiral with rainbow trail!")

def start_aurora_waves():
    global current_animation, trail_particles, animation_running
    trail_particles.clear()
    animation_running = True
    current_animation = AuroraWaves()
    screen.bgcolor("black")
    print("🌊 AURORA WAVES ACTIVE! 🌊")
    print("Beautiful northern lights effect!")

def start_explosion_mode():
    global animation_running
    trail_particles.clear()
    animation_running = True
    explosion = ParticleExplosion()
    
    def on_click(x, y):
        explosion.explode(x, y)
        print(f"💥 BOOM! Explosion at ({x}, {y})")
    
    screen.onclick(on_click)
    current_animation = None  # No continuous animation
    screen.bgcolor("black")
    print("💣 EXPLOSION MODE ACTIVE! 💣")
    print("Click anywhere for particle explosions!")

def stop_animation():
    global animation_running
    animation_running = False
    print("Animation stopped.")

def show_menu():
    """Display interactive menu."""
    # Clear everything
    for particle in trail_particles:
        particle.remove()
    trail_particles.clear()
    
    screen.clear()
    screen.bgcolor("black")
    
    menu = turtle.Turtle()
    menu.hideturtle()
    menu.penup()
    menu.color("lime")
    
    menu_items = [
        "✨ UNIQUE TRAIL EFFECTS MENU ✨",
        "",
        "1 - 🔥 FIRE SNAKE (Living creature with fiery trail)",
        "2 - 🌀 GALACTIC SPINNER (Hypnotic spiral rainbow)",
        "3 - 🌊 AURORA WAVES (Northern lights effect)",
        "4 - 💣 PARTICLE EXPLOSIONS (Click for fireworks)",
        "",
        "Press S to stop animation",
        "Press M for this menu",
        "Press Q to quit",
        "",
        "Made with Turtle Graphics"
    ]
    
    y = 250
    for item in menu_items:
        menu.goto(0, y)
        menu.write(item, align="center", font=("Arial", 13, "bold"))
        y -= 30
    
    screen.update()

# Keyboard controls
screen.listen()
screen.onkey(start_fire_snake, "1")
screen.onkey(start_galactic_spinner, "2")
screen.onkey(start_aurora_waves, "3")
screen.onkey(start_explosion_mode, "4")
screen.onkey(stop_animation, "s")
screen.onkey(stop_animation, "S")
screen.onkey(show_menu, "m")
screen.onkey(show_menu, "M")
screen.onkey(screen.bye, "q")
screen.onkey(screen.bye, "Q")

# Show menu and start
show_menu()
print("\n" + "="*60)
print("🎆 FIRE SNAKE & UNIQUE TRAIL EFFECTS 🎆")
print("="*60)
print("\n🔹 FOUR COMPLETELY DIFFERENT ANIMATIONS:")
print("  1. Fire Snake - Living, undulating creature")
print("  2. Galactic Spinner - Expanding rainbow spiral")
print("  3. Aurora Waves - Flowing northern lights")
print("  4. Particle Explosions - Click for fireworks!")
print("\n⌨️  Press number keys (1-4) to start!")
print("   Press M for menu, Q to quit")
print("="*60)

# Start update loop
update_all()
screen.mainloop()