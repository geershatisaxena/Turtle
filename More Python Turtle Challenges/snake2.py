import turtle
import math
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#0a0a0f")
screen.title("Glowing Snake Trail Effect")
screen.tracer(0)
screen.setup(900, 750)

# Create snake trail system
class SnakeTrail:
    def __init__(self):
        self.segments = []
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("circle")
        self.head.color("#00ff88")
        self.head.shapesize(1.2)
        self.head.penup()
        
        # Trail segments
        self.max_segments = 50
        self.segment_length = 12
        self.angle = 0
        self.speed = 2
        self.x = 0
        self.y = 0
        self.glow_effect = True
        self.trail_color = "#00ff88"
        self.direction = 0  # 0=right, 90=up, 180=left, 270=down
        
        # Create initial segments
        for i in range(self.max_segments):
            segment = turtle.Turtle()
            segment.speed(0)
            segment.shape("circle")
            segment.color(self.get_gradient_color(i))
            segment.shapesize(0.6 - (i / self.max_segments) * 0.4)
            segment.penup()
            segment.goto(-i * self.segment_length, 0)
            self.segments.append(segment)
        
        # Head glow
        self.head_glow = turtle.Turtle()
        self.head_glow.speed(0)
        self.head_glow.shape("circle")
        self.head_glow.color("#00ff88")
        self.head_glow.shapesize(2)
        self.head_glow.penup()
        self.head_glow.hideturtle()
        
        # Trail particles
        self.particles = []
        
        # Trail trail (visual effect)
        self.trail_effect = []
        
    def get_gradient_color(self, index):
        """Get color based on position in trail"""
        ratio = 1 - (index / self.max_segments)
        # Gradient from bright green to dark blue
        r = 0
        g = int(255 * ratio)
        b = int(255 * (1 - ratio) * 0.5)
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def move(self):
        """Move the snake trail"""
        # Calculate new head position
        if self.direction == 0:  # Right
            self.x += self.speed
        elif self.direction == 90:  # Up
            self.y += self.speed
        elif self.direction == 180:  # Left
            self.x -= self.speed
        elif self.direction == 270:  # Down
            self.y -= self.speed
        
        # Update head position
        self.head.goto(self.x, self.y)
        
        # Update glow
        if self.glow_effect:
            self.head_glow.goto(self.x, self.y)
            self.head_glow.showturtle()
            glow_size = 2 + math.sin(time.time() * 2) * 0.3
            self.head_glow.shapesize(glow_size)
        
        # Update segments (each segment follows the one in front)
        for i in range(len(self.segments) - 1, 0, -1):
            prev_seg = self.segments[i - 1]
            curr_seg = self.segments[i]
            
            # Move towards previous segment
            dx = prev_seg.xcor() - curr_seg.xcor()
            dy = prev_seg.ycor() - curr_seg.ycor()
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist > self.segment_length:
                ratio = self.segment_length / dist
                new_x = curr_seg.xcor() + dx * ratio
                new_y = curr_seg.ycor() + dy * ratio
                curr_seg.goto(new_x, new_y)
            
            # Update color
            curr_seg.color(self.get_gradient_color(i))
        
        # First segment follows head
        if len(self.segments) > 0:
            first_seg = self.segments[0]
            dx = self.x - first_seg.xcor()
            dy = self.y - first_seg.ycor()
            dist = math.sqrt(dx**2 + dy**2)
            
            if dist > self.segment_length:
                ratio = self.segment_length / dist
                new_x = first_seg.xcor() + dx * ratio
                new_y = first_seg.ycor() + dy * ratio
                first_seg.goto(new_x, new_y)
        
        # Create particles
        if random.random() < 0.1:
            self.create_particle(self.x, self.y)
        
        # Update particles
        self.update_particles()
        
        # Create trail effect
        if random.random() < 0.05:
            self.trail_effect.append({
                "x": self.x,
                "y": self.y,
                "life": 20,
                "size": random.randint(3, 8)
            })
        
        self.update_trail_effect()
    
    def create_particle(self, x, y):
        """Create a particle at given position"""
        particle = turtle.Turtle()
        particle.speed(0)
        particle.shape("circle")
        particle.color(random.choice(["#00ff88", "#00ffff", "#88ff00"]))
        particle.shapesize(random.uniform(0.2, 0.5))
        particle.penup()
        particle.goto(x + random.randint(-10, 10), y + random.randint(-10, 10))
        
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(1, 3)
        
        particle_data = {
            "turtle": particle,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "life": random.randint(20, 40),
            "max_life": 40
        }
        self.particles.append(particle_data)
    
    def update_particles(self):
        """Update all particles"""
        for particle_data in self.particles[:]:
            particle_data["turtle"].goto(
                particle_data["turtle"].xcor() + particle_data["vx"],
                particle_data["turtle"].ycor() + particle_data["vy"]
            )
            particle_data["life"] -= 1
            
            # Fade and shrink
            life_ratio = particle_data["life"] / particle_data["max_life"]
            size = life_ratio * 0.5
            particle_data["turtle"].shapesize(max(0.05, size))
            
            if particle_data["life"] <= 0:
                particle_data["turtle"].hideturtle()
                self.particles.remove(particle_data)
    
    def update_trail_effect(self):
        """Update visual trail effect"""
        for effect in self.trail_effect[:]:
            effect["life"] -= 1
            effect["size"] += 0.2
            
            if effect["life"] <= 0:
                self.trail_effect.remove(effect)
    
    def draw_trail_effect(self):
        """Draw the trail effect"""
        for effect in self.trail_effect:
            trail = turtle.Turtle()
            trail.speed(0)
            trail.penup()
            trail.hideturtle()
            trail.goto(effect["x"], effect["y"])
            alpha = effect["life"] / 20
            trail.color(f"#{int(0):02x}{int(255 * alpha):02x}{int(128 * alpha):02x}")
            trail.dot(effect["size"])
            screen.ontimer(trail.clear, 100)
    
    def change_direction(self, direction):
        """Change snake direction"""
        # Prevent reversing
        if abs(self.direction - direction) != 180:
            self.direction = direction
    
    def change_color(self):
        """Change trail color"""
        colors = ["#00ff88", "#ff00ff", "#00ffff", "#ff8800", "#ff0044", "#88ff00"]
        self.trail_color = random.choice(colors)
        self.head.color(self.trail_color)
        self.head_glow.color(self.trail_color)
    
    def toggle_glow(self):
        """Toggle glow effect"""
        self.glow_effect = not self.glow_effect
        if not self.glow_effect:
            self.head_glow.hideturtle()

# Create snake trail
snake = SnakeTrail()

# Create background decoration
def create_background():
    # Create grid
    grid = turtle.Turtle()
    grid.speed(0)
    grid.penup()
    grid.hideturtle()
    grid.color("#1a1a2e")
    grid.pensize(0.5)
    
    for x in range(-400, 400, 50):
        grid.goto(x, -350)
        grid.pendown()
        grid.goto(x, 350)
        grid.penup()
    
    for y in range(-350, 350, 50):
        grid.goto(-400, y)
        grid.pendown()
        grid.goto(400, y)
        grid.penup()
    
    # Create border
    border = turtle.Turtle()
    border.speed(0)
    border.penup()
    border.hideturtle()
    border.goto(-420, -370)
    border.pendown()
    border.color("#00ff88")
    border.pensize(2)
    for _ in range(2):
        border.forward(840)
        border.left(90)
        border.forward(740)
        border.left(90)
    
    # Create corner decorations
    for x in [-420, 420]:
        for y in [-370, 370]:
            corner = turtle.Turtle()
            corner.speed(0)
            corner.penup()
            corner.hideturtle()
            corner.goto(x, y)
            corner.color("#00ff88")
            corner.write("♦", align="center", font=("Arial", 16, "bold"))

create_background()

# Display elements
title = turtle.Turtle()
title.speed(0)
title.penup()
title.hideturtle()
title.color("#00ff88")
title.goto(0, 380)
title.write("🐍 GLOWING SNAKE TRAIL", align="center", font=("Arial", 22, "bold"))

subtitle = turtle.Turtle()
subtitle.speed(0)
subtitle.penup()
subtitle.hideturtle()
subtitle.color("#666")
subtitle.goto(0, 350)
subtitle.write("Interactive Snake with Glowing Trail Effect", align="center", font=("Arial", 12, "normal"))

# Controls display
controls = turtle.Turtle()
controls.speed(0)
controls.penup()
controls.hideturtle()
controls.color("#666")
controls.goto(0, -390)
controls.write("↑↓←→: Move  •  C: Change Color  •  G: Toggle Glow  •  +/−: Speed  •  R: Reset", 
              align="center", font=("Arial", 11, "normal"))

# Stats display
stats = turtle.Turtle()
stats.speed(0)
stats.penup()
stats.hideturtle()
stats.color("#00ff88")
stats.goto(-400, 350)

def update_stats():
    stats.clear()
    stats.write(f"Segments: {len(snake.segments)}", align="left", font=("Arial", 12, "normal"))
    stats.goto(-400, 325)
    stats.write(f"Speed: {snake.speed:.1f}", align="left", font=("Arial", 12, "normal"))
    stats.goto(-400, 300)
    stats.write(f"Particles: {len(snake.particles)}", align="left", font=("Arial", 12, "normal"))

# Function to handle key presses
def move_up():
    snake.change_direction(90)

def move_down():
    snake.change_direction(270)

def move_left():
    snake.change_direction(180)

def move_right():
    snake.change_direction(0)

def change_color():
    snake.change_color()

def toggle_glow():
    snake.toggle_glow()

def speed_up():
    snake.speed = min(8, snake.speed + 0.5)
    update_stats()

def speed_down():
    snake.speed = max(0.5, snake.speed - 0.5)
    update_stats()

def reset_snake():
    global snake
    # Clear old snake
    for segment in snake.segments:
        segment.clear()
        segment.hideturtle()
    for particle in snake.particles:
        particle["turtle"].clear()
        particle["turtle"].hideturtle()
    
    # Create new snake
    snake = SnakeTrail()
    update_stats()

# Key bindings
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(change_color, "c")
screen.onkey(toggle_glow, "g")
screen.onkey(speed_up, "plus")
screen.onkey(speed_down, "minus")
screen.onkey(reset_snake, "r")
screen.listen()

# Boundary checking
def check_boundaries():
    if snake.x > 400:
        snake.x = -400
        snake.head.goto(snake.x, snake.y)
    elif snake.x < -400:
        snake.x = 400
        snake.head.goto(snake.x, snake.y)
    
    if snake.y > 350:
        snake.y = -350
        snake.head.goto(snake.x, snake.y)
    elif snake.y < -350:
        snake.y = 350
        snake.head.goto(snake.x, snake.y)

# Animation loop
def animate():
    # Move snake
    snake.move()
    
    # Check boundaries (wrap around)
    check_boundaries()
    
    # Draw trail effect
    snake.draw_trail_effect()
    
    # Update stats every 30 frames
    if random.random() < 0.01:
        update_stats()
    
    screen.update()
    screen.ontimer(animate, 20)

# Click to reset
screen.onclick(lambda x, y: reset_snake())

# Start animation
update_stats()
animate()

# Keep window open
screen.mainloop()