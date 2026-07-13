import turtle
import math
import random
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#0a0a1a")
screen.title("Rainbow Snake Trail - Multi-Color Effect")
screen.tracer(0)
screen.setup(1000, 800)

# Create enhanced snake trail system
class RainbowSnake:
    def __init__(self):
        self.segments = []
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("circle")
        self.head.shapesize(1.5)
        self.head.penup()
        
        # Head glow layers
        self.head_glows = []
        for i in range(3):
            glow = turtle.Turtle()
            glow.speed(0)
            glow.shape("circle")
            glow.color("#ffffff")
            glow.shapesize(2.5 - i * 0.6)
            glow.penup()
            glow.hideturtle()
            self.head_glows.append(glow)
        
        # Trail properties
        self.max_segments = 80
        self.segment_length = 10
        self.angle = 0
        self.speed = 3
        self.x = 0
        self.y = 0
        self.direction = 0
        self.hue_offset = 0
        self.movement_pattern = 0  # 0=free, 1=wave, 2=spiral
        self.tail_length = self.max_segments
        
        # Create initial segments
        for i in range(self.max_segments):
            segment = turtle.Turtle()
            segment.speed(0)
            segment.shape("circle")
            hue = (i / self.max_segments) * 360
            segment.color(self.hsv_to_rgb(hue, 1, 1))
            segment.shapesize(0.8 - (i / self.max_segments) * 0.6)
            segment.penup()
            segment.goto(-i * self.segment_length, random.randint(-10, 10))
            self.segments.append(segment)
        
        # Sparkle system
        self.sparkles = []
        
        # Trail path (for drawing path effect)
        self.path = []
        self.max_path = 200
        
        # Secondary trail (ghost trail)
        self.ghost_segments = []
        self.create_ghost_trail()
        
    def hsv_to_rgb(self, h, s, v):
        """Convert HSV to RGB hex color"""
        h = h / 360
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
    
    def create_ghost_trail(self):
        """Create ghost trail effect"""
        for i in range(30):
            ghost = turtle.Turtle()
            ghost.speed(0)
            ghost.shape("circle")
            ghost.color("#444466")
            ghost.shapesize(0.3)
            ghost.penup()
            ghost.hideturtle()
            self.ghost_segments.append(ghost)
    
    def move(self):
        """Move the snake with dynamic pattern"""
        # Update movement pattern
        self.movement_pattern = (self.movement_pattern + 0.001) % 3
        
        # Calculate new position based on direction and pattern
        if self.movement_pattern < 1:  # Free movement
            dx = math.cos(math.radians(self.direction)) * self.speed
            dy = math.sin(math.radians(self.direction)) * self.speed
        elif self.movement_pattern < 2:  # Wave movement
            wave = math.sin(self.x * 0.02 + time.time()) * 0.5
            dx = math.cos(math.radians(self.direction + wave)) * self.speed
            dy = math.sin(math.radians(self.direction + wave)) * self.speed
        else:  # Spiral movement
            spiral = time.time() * 0.05
            dx = math.cos(spiral) * self.speed * 0.7
            dy = math.sin(spiral) * self.speed * 0.7
        
        self.x += dx
        self.y += dy
        
        # Update head position
        self.head.goto(self.x, self.y)
        
        # Update head glows with pulse
        pulse = math.sin(time.time() * 3) * 0.3 + 0.7
        for i, glow in enumerate(self.head_glows):
            glow.goto(self.x, self.y)
            glow.showturtle()
            size = 2.5 - i * 0.6
            glow.shapesize(size * pulse)
            glow.color(self.hsv_to_rgb((self.hue_offset + i * 30) % 360, 1, 0.5 + i * 0.2))
        
        # Update segments with rainbow colors
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
            
            # Update color with rainbow gradient
            hue = (self.hue_offset + i * 1.5) % 360
            curr_seg.color(self.hsv_to_rgb(hue, 1, 1))
            
            # Size variation
            size_ratio = 1 - (i / self.max_segments)
            curr_seg.shapesize(0.8 * size_ratio + 0.2)
        
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
        
        # Update ghost trail
        self.update_ghost_trail()
        
        # Create sparkles along the trail
        if random.random() < 0.3:
            self.create_sparkle(self.x, self.y)
        
        # Update sparkles
        self.update_sparkles()
        
        # Update path
        self.path.append((self.x, self.y))
        if len(self.path) > self.max_path:
            self.path.pop(0)
        
        # Update hue offset for rainbow animation
        self.hue_offset = (self.hue_offset + 0.5) % 360
    
    def update_ghost_trail(self):
        """Update ghost trail segments"""
        if len(self.segments) > 0:
            for i, ghost in enumerate(self.ghost_segments):
                if i < len(self.segments):
                    # Ghost follows behind main segments
                    index = min(i * 3, len(self.segments) - 1)
                    seg = self.segments[index]
                    ghost.goto(seg.xcor() + random.randint(-5, 5), 
                              seg.ycor() + random.randint(-5, 5))
                    ghost.showturtle()
                    ghost.color(f"#{i*2:02x}{i*2:02x}{40+i*3:02x}")
                    ghost.shapesize(0.3 + (1 - i/len(self.ghost_segments)) * 0.2)
    
    def create_sparkle(self, x, y):
        """Create a sparkle effect"""
        sparkle = turtle.Turtle()
        sparkle.speed(0)
        sparkle.shape("circle")
        hue = (self.hue_offset + random.randint(0, 360)) % 360
        sparkle.color(self.hsv_to_rgb(hue, 1, 1))
        sparkle.shapesize(random.uniform(0.1, 0.4))
        sparkle.penup()
        sparkle.goto(x + random.randint(-20, 20), y + random.randint(-20, 20))
        
        sparkle_data = {
            "turtle": sparkle,
            "vx": random.uniform(-2, 2),
            "vy": random.uniform(-2, 2),
            "life": random.randint(15, 35),
            "max_life": 35,
            "rotation": random.uniform(-5, 5)
        }
        self.sparkles.append(sparkle_data)
    
    def update_sparkles(self):
        """Update sparkle effects"""
        for sparkle_data in self.sparkles[:]:
            sparkle_data["turtle"].goto(
                sparkle_data["turtle"].xcor() + sparkle_data["vx"],
                sparkle_data["turtle"].ycor() + sparkle_data["vy"]
            )
            sparkle_data["life"] -= 1
            sparkle_data["turtle"].right(sparkle_data["rotation"])
            
            # Fade and shrink
            life_ratio = sparkle_data["life"] / sparkle_data["max_life"]
            size = life_ratio * 0.4
            sparkle_data["turtle"].shapesize(max(0.05, size))
            
            if sparkle_data["life"] <= 0:
                sparkle_data["turtle"].hideturtle()
                self.sparkles.remove(sparkle_data)
    
    def change_direction(self, direction):
        """Change snake direction"""
        if abs(self.direction - direction) != 180:
            self.direction = direction
    
    def toggle_pattern(self):
        """Change movement pattern"""
        self.movement_pattern = (self.movement_pattern + 1) % 3
    
    def change_speed(self, delta):
        """Change speed"""
        self.speed = max(0.5, min(8, self.speed + delta))
    
    def reset(self):
        """Reset snake"""
        self.x = 0
        self.y = 0
        self.direction = 0
        self.hue_offset = 0
        self.path.clear()

# Create snake
snake = RainbowSnake()

# Create star background
def create_starfield():
    stars = []
    for _ in range(100):
        star = turtle.Turtle()
        star.speed(0)
        star.penup()
        star.hideturtle()
        star.color("white")
        star.goto(random.randint(-450, 450), random.randint(-380, 380))
        star.dot(random.randint(1, 3))
        stars.append(star)
    return stars

stars = create_starfield()

# Create animated background rings
rings = []
def create_rings():
    for i in range(3):
        ring = turtle.Turtle()
        ring.speed(0)
        ring.penup()
        ring.hideturtle()
        ring.color(f"#{i*30:02x}{i*40:02x}{80:02x}")
        ring.goto(0, 0)
        ring.pendown()
        ring.circle(100 + i * 80)
        ring.penup()
        rings.append(ring)

create_rings()

# Display elements
title = turtle.Turtle()
title.speed(0)
title.penup()
title.hideturtle()
title.color("#ff88ff")
title.goto(0, 400)
title.write("🌈 RAINBOW SNAKE TRAIL", align="center", font=("Arial", 24, "bold"))

subtitle = turtle.Turtle()
subtitle.speed(0)
subtitle.penup()
subtitle.hideturtle()
subtitle.color("#8888ff")
subtitle.goto(0, 370)
subtitle.write("Multi-Color Glowing Snake with Dynamic Patterns", align="center", font=("Arial", 13, "normal"))

# Controls
controls = turtle.Turtle()
controls.speed(0)
controls.penup()
controls.hideturtle()
controls.color("#6666aa")
controls.goto(0, -420)
controls.write("↑↓←→: Move  •  P: Pattern  •  +/−: Speed  •  R: Reset  •  Click: Sparkle Burst", 
              align="center", font=("Arial", 11, "normal"))

# Stats display
stats = turtle.Turtle()
stats.speed(0)
stats.penup()
stats.hideturtle()
stats.color("#88ff88")
stats.goto(-450, 380)

def update_stats():
    stats.clear()
    patterns = ["Free", "Wave", "Spiral"]
    stats.write(f"Segments: {len(snake.segments)}", align="left", font=("Arial", 11, "normal"))
    stats.goto(-450, 355)
    stats.write(f"Speed: {snake.speed:.1f}", align="left", font=("Arial", 11, "normal"))
    stats.goto(-450, 330)
    stats.write(f"Pattern: {patterns[int(snake.movement_pattern)]}", align="left", font=("Arial", 11, "normal"))
    stats.goto(-450, 305)
    stats.write(f"Sparkles: {len(snake.sparkles)}", align="left", font=("Arial", 11, "normal"))

# Function to create sparkle burst on click
def sparkle_burst(x, y):
    for _ in range(30):
        snake.create_sparkle(x, y)
    update_stats()

# Key bindings
screen.onkey(lambda: snake.change_direction(90), "Up")
screen.onkey(lambda: snake.change_direction(270), "Down")
screen.onkey(lambda: snake.change_direction(180), "Left")
screen.onkey(lambda: snake.change_direction(0), "Right")
screen.onkey(snake.toggle_pattern, "p")
screen.onkey(lambda: snake.change_speed(0.5), "plus")
screen.onkey(lambda: snake.change_speed(-0.5), "minus")
screen.onkey(snake.reset, "r")
screen.listen()

# Click handler
screen.onclick(sparkle_burst)

# Animation loop
frame_count = 0

def animate():
    global frame_count
    
    # Move snake
    snake.move()
    
    # Wrap around edges
    if snake.x > 450:
        snake.x = -450
        snake.head.goto(snake.x, snake.y)
    elif snake.x < -450:
        snake.x = 450
        snake.head.goto(snake.x, snake.y)
    
    if snake.y > 380:
        snake.y = -380
        snake.head.goto(snake.x, snake.y)
    elif snake.y < -380:
        snake.y = 380
        snake.head.goto(snake.x, snake.y)
    
    # Animate rings
    for i, ring in enumerate(rings):
        ring.clear()
        ring.penup()
        ring.goto(0, 0)
        ring.pendown()
        ring.color(f"#{i*20:02x}{i*30:02x}{80 + int(math.sin(time.time() + i) * 20):02x}")
        ring.circle(100 + i * 80 + math.sin(time.time() + i) * 10)
        ring.penup()
    
    # Update stats
    if frame_count % 30 == 0:
        update_stats()
    
    frame_count += 1
    screen.update()
    screen.ontimer(animate, 20)

# Start animation
update_stats()
animate()

# Keep window open
screen.mainloop()