import turtle
import math
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Glowing Animated Heart")
screen.bgcolor("#1a0a2e")
screen.setup(width=900, height=800)
screen.tracer(0)
screen.register_shape("heart", ((-10, 5), (-5, 10), (0, 8), (5, 10), (10, 5), (8, -2), (5, -8), (0, -12), (-5, -8), (-8, -2)))

# Create turtles
heart_turtle = turtle.Turtle()
heart_turtle.speed(0)
heart_turtle.penup()
heart_turtle.hideturtle()

# Background gradient effect
bg_turtle = turtle.Turtle()
bg_turtle.speed(0)
bg_turtle.penup()
bg_turtle.hideturtle()

# Particle system
particles = []

# Heart animation variables
pulse = 0
pulse_direction = 1
glow_intensity = 0
rotation_angle = 0

# Heart colors
heart_colors = ["#ff3366", "#ff0066", "#ff3399", "#ff66b2", "#ff3366"]
current_color_index = 0

def draw_gradient_background():
    """Draw a beautiful gradient sunset background"""
    bg_turtle.clear()
    
    # Draw gradient sky
    for i in range(30):
        y = -350 + i * 25
        # Color transitions from dark purple to pink to orange
        if i < 10:
            r, g, b = 26 + i * 2, 10 + i, 46 - i
        elif i < 20:
            r, g, b = 46 + (i - 10) * 8, 20 + (i - 10) * 5, 36 + (i - 10) * 2
        else:
            r, g, b = 126 + (i - 20) * 5, 70 + (i - 20) * 3, 56 - (i - 20)
        
        bg_turtle.color(f"#{int(r):02x}{int(g):02x}{int(b):02x}")
        bg_turtle.penup()
        bg_turtle.goto(-450, y)
        bg_turtle.pendown()
        bg_turtle.begin_fill()
        for _ in range(2):
            bg_turtle.forward(900)
            bg_turtle.right(90)
            bg_turtle.forward(25)
            bg_turtle.right(90)
        bg_turtle.end_fill()
    
    # Draw stars
    bg_turtle.color("white")
    for _ in range(100):
        x = random.randint(-430, 430)
        y = random.randint(100, 380)
        bg_turtle.penup()
        bg_turtle.goto(x, y)
        bg_turtle.dot(random.randint(1, 3))

def draw_heart_alternative(x, y, size, color, rotation=0):
    """Heart drawing using circles and triangle - most reliable method"""
    heart_turtle.clear()
    heart_turtle.penup()
    heart_turtle.goto(x, y - size * 8)
    heart_turtle.color(color)
    heart_turtle.fillcolor(color)
    heart_turtle.pendown()
    heart_turtle.begin_fill()
    
    # Draw two circles for the top lobes
    heart_turtle.setheading(rotation)
    heart_turtle.circle(size * 6, 180)
    heart_turtle.left(180)
    heart_turtle.circle(size * 6, 180)
    
    # Draw triangle for the bottom point
    heart_turtle.left(180)
    heart_turtle.forward(size * 12)
    heart_turtle.left(90)
    heart_turtle.forward(size * 8)
    heart_turtle.left(45)
    heart_turtle.forward(size * 14)
    
    heart_turtle.end_fill()
    heart_turtle.penup()

def draw_glow_effect(x, y, size, intensity):
    """Draw a glowing aura around the heart"""
    glow_turtle = turtle.Turtle()
    glow_turtle.speed(0)
    glow_turtle.penup()
    glow_turtle.hideturtle()
    
    for i in range(3, 0, -1):
        alpha = intensity * (i / 3)
        glow_color = f"#{int(255 * (1 - i/5)):02x}{int(100 * (1 - i/5)):02x}{int(150 * (1 - i/5)):02x}"
        glow_turtle.color(glow_color)
        glow_turtle.goto(x, y - size * 5)
        glow_turtle.pendown()
        glow_turtle.circle(size * (12 + i * 2))
        glow_turtle.penup()
    
    glow_turtle.clear()

class Particle:
    def __init__(self, x, y):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(random.choice(["#ff6699", "#ff3399", "#ff0066", "#ff99cc", "#ffccdd"]))
        self.turtle.shapesize(random.uniform(0.1, 0.4))
        self.turtle.penup()
        self.turtle.goto(x, y)
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 8)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = random.randint(30, 80)
        self.age = 0
        
    def update(self):
        self.age += 1
        self.turtle.goto(self.turtle.xcor() + self.vx, self.turtle.ycor() + self.vy)
        self.vx *= 0.98
        self.vy -= 0.15
        
        # Fade out
        if self.age > self.life * 0.6:
            new_size = max(0.05, self.turtle.shapesize()[0] - 0.02)
            self.turtle.shapesize(new_size)
        
        return self.age < self.life
    
    def cleanup(self):
        self.turtle.hideturtle()
        self.turtle.clear()

def create_heart_burst(x, y):
    """Create a burst of particles from the heart"""
    for _ in range(60):
        particles.append(Particle(x + random.randint(-30, 30), 
                                   y + random.randint(-30, 30)))

def draw_romantic_text(frame):
    """Draw romantic messages that change over time"""
    text_turtle = turtle.Turtle()
    text_turtle.speed(0)
    text_turtle.penup()
    text_turtle.hideturtle()
    
    messages = [
        "❤️ BE MINE ❤️",
        "✨ FOREVER ✨",
        "💕 TRUE LOVE 💕",
        "🌸 YOU & ME 🌸",
        "⭐ SOULMATES ⭐",
        "🌹 FOREVER 🌹"
    ]
    
    index = (frame // 180) % len(messages)
    
    # Clear previous text area
    text_turtle.goto(0, -320)
    text_turtle.clear()
    text_turtle.write(messages[index], align="center", font=("Georgia", 20, "bold"))
    
    # Subtitle
    text_turtle.goto(0, -360)
    text_turtle.write("Press SPACE: Burst | C: Color | +: Bigger | -: Smaller | G: Glow | ESC: Exit",
                      align="center", font=("Arial", 10, "normal"))

class FloatingHeart:
    def __init__(self, x, y, size, color):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.color(color)
        self.turtle.fillcolor(color)
        self.size = size
        self.angle = 0
        
    def draw(self):
        self.turtle.clear()
        self.turtle.pendown()
        self.turtle.begin_fill()
        
        # Draw small heart
        self.turtle.setheading(0)
        self.turtle.circle(self.size, 180)
        self.turtle.left(180)
        self.turtle.circle(self.size, 180)
        self.turtle.left(180)
        self.turtle.forward(self.size * 2)
        self.turtle.left(90)
        self.turtle.forward(self.size * 1.3)
        self.turtle.left(45)
        self.turtle.forward(self.size * 2.3)
        
        self.turtle.end_fill()
        self.turtle.penup()
        
    def update_position(self, x, y):
        self.turtle.goto(x, y)
        self.draw()
        
    def cleanup(self):
        self.turtle.hideturtle()
        self.turtle.clear()

# Animation variables
heart_size = 2.0
target_size = 2.0
show_glow = True
frame_count = 0

def change_color():
    global current_color_index
    current_color_index = (current_color_index + 1) % len(heart_colors)

def increase_size():
    global target_size, heart_size
    target_size = min(target_size + 0.2, 3.5)

def decrease_size():
    global target_size, heart_size
    target_size = max(target_size - 0.2, 1.2)

def toggle_glow():
    global show_glow
    show_glow = not show_glow

def add_burst():
    create_heart_burst(0, 50)

def draw_heart_animation():
    """Main animation loop"""
    global pulse, pulse_direction, heart_size, frame_count, target_size
    
    # Draw background once
    draw_gradient_background()
    
    # Create floating hearts as custom drawn objects
    floating_hearts = []
    heart_colors_list = ["#ff6699", "#ff3399", "#ff0066", "#ff99cc", "#ffccdd"]
    for i in range(12):
        fh = FloatingHeart(0, 0, 4, heart_colors_list[i % len(heart_colors_list)])
        floating_hearts.append(fh)
    
    # Text turtle
    text_turtle = turtle.Turtle()
    text_turtle.speed(0)
    text_turtle.penup()
    text_turtle.hideturtle()
    
    while True:
        # Smooth size transition
        if abs(heart_size - target_size) > 0.01:
            heart_size += (target_size - heart_size) * 0.1
        
        # Pulsing effect
        pulse += 0.05 * pulse_direction
        if pulse >= 1:
            pulse_direction = -1
        elif pulse <= 0:
            pulse_direction = 1
        
        dynamic_size = heart_size + pulse * 0.15
        
        # Rotate slightly during pulse
        rotation = math.sin(frame_count * 0.05) * 3
        
        # Draw main heart
        current_color = heart_colors[current_color_index]
        
        # Add glow effect
        if show_glow:
            draw_glow_effect(0, 50, dynamic_size, pulse + 0.5)
        
        # Draw the heart
        draw_heart_alternative(0, 50, dynamic_size, current_color, rotation)
        
        # Update particles
        for particle in particles[:]:
            if not particle.update():
                particle.cleanup()
                particles.remove(particle)
        
        # Animate floating hearts
        for i, fh in enumerate(floating_hearts):
            angle = frame_count * 0.02 + i * math.pi / 6
            radius = 150 + math.sin(frame_count * 0.03 + i) * 20
            x = math.cos(angle) * radius
            y = math.sin(angle) * radius + 50
            fh.update_position(x, y)
        
        # Draw romantic text
        messages = [
            "❤️ BE MINE ❤️",
            "✨ FOREVER ✨",
            "💕 TRUE LOVE 💕",
            "🌸 YOU & ME 🌸",
            "⭐ SOULMATES ⭐",
            "🌹 FOREVER 🌹"
        ]
        index = (frame_count // 180) % len(messages)
        
        text_turtle.clear()
        text_turtle.goto(0, -320)
        text_turtle.write(messages[index], align="center", font=("Georgia", 20, "bold"))
        
        text_turtle.goto(0, -360)
        text_turtle.write("Press SPACE: Burst | C: Color | +: Bigger | -: Smaller | G: Glow | ESC: Exit",
                          align="center", font=("Arial", 10, "normal"))
        
        # Occasionally add small sparkles
        if frame_count % 30 == 0:
            for _ in range(3):
                angle = random.uniform(0, 2 * math.pi)
                radius = random.uniform(60, 120)
                x = math.cos(angle) * radius
                y = math.sin(angle) * radius + 50
                particles.append(Particle(x, y))
        
        # Special burst on frame counts
        if frame_count % 300 == 0 and frame_count > 0:
            create_heart_burst(0, 50)
        
        frame_count += 1
        screen.update()
        turtle.time.sleep(0.025)

# Keyboard bindings
screen.listen()
screen.onkey(change_color, "c")
screen.onkey(increase_size, "plus")
screen.onkey(increase_size, "equal")
screen.onkey(decrease_size, "minus")
screen.onkey(add_burst, "space")
screen.onkey(toggle_glow, "g")
screen.onkey(lambda: screen.bye(), "Escape")

print("=" * 50)
print("     GLOWING ANIMATED HEART")
print("=" * 50)
print()
print("A beautiful animated heart with glow effects and particles!")
print()
print("CONTROLS:")
print("  SPACE   - Create particle burst")
print("  C       - Change heart color")
print("  + / -   - Increase/Decrease heart size")
print("  G       - Toggle glow effect")
print("  ESC     - Exit program")
print()
print("Watch the heart pulse, rotate, and attract floating hearts!")

# Run the animation
try:
    draw_heart_animation()
except KeyboardInterrupt:
    screen.bye()
except turtle.Terminator:
    pass

screen.mainloop()