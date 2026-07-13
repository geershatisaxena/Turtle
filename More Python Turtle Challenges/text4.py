import turtle
import time
import random
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#0a0a0f")
screen.title("Cyberpunk Typing Animation")
screen.tracer(0)
screen.setup(1000, 750)

# Create terminal frame
terminal = turtle.Turtle()
terminal.speed(0)
terminal.penup()
terminal.hideturtle()
terminal.goto(-450, -350)
terminal.pendown()
terminal.color("#1a1a2e")
terminal.begin_fill()
for _ in range(2):
    terminal.forward(900)
    terminal.left(90)
    terminal.forward(700)
    terminal.left(90)
terminal.end_fill()

# Terminal border glow
border_glow = turtle.Turtle()
border_glow.speed(0)
border_glow.penup()
border_glow.hideturtle()
border_glow.goto(-440, -340)
border_glow.color("#00ff88")
border_glow.pensize(2)
border_glow.pendown()
for _ in range(2):
    border_glow.forward(880)
    border_glow.left(90)
    border_glow.forward(680)
    border_glow.left(90)
border_glow.penup()

# Create typing turtle
typing_turtle = turtle.Turtle()
typing_turtle.speed(0)
typing_turtle.penup()
typing_turtle.hideturtle()
typing_turtle.color("#00ff88")
typing_turtle.goto(-420, 280)

# Glow turtle for text effect
glow_turtle = turtle.Turtle()
glow_turtle.speed(0)
glow_turtle.penup()
glow_turtle.hideturtle()

# Cursor
cursor = turtle.Turtle()
cursor.speed(0)
cursor.penup()
cursor.hideturtle()
cursor.color("#00ff88")

# Scan line effect
scan_line = turtle.Turtle()
scan_line.speed(0)
scan_line.penup()
scan_line.hideturtle()
scan_line.color("#00ff88")
scan_line.pensize(1)

# Variables
current_text = ""
full_text = ""
typing_index = 0
typing_speed = 80
is_typing = False
is_paused = False
line_height = 30
current_line = 0
max_line_length = 70
characters_typed = 0
wpm = 0
start_time = 0
error_chance = 0.02  # 2% chance of "typo"

# Display elements
header = turtle.Turtle()
header.speed(0)
header.penup()
header.hideturtle()
header.color("#00ff88")
header.goto(0, 340)
header.write("╔══════════════════════════════════════╗", align="center", font=("Courier", 12, "bold"))
header.goto(0, 320)
header.write("║     CYBERPUNK TYPEWRITER v2.0        ║", align="center", font=("Courier", 12, "bold"))
header.goto(0, 300)
header.write("╚══════════════════════════════════════╝", align="center", font=("Courier", 12, "bold"))

# Status bar
status_bar = turtle.Turtle()
status_bar.speed(0)
status_bar.penup()
status_bar.hideturtle()
status_bar.color("#666")
status_bar.goto(-420, -300)

# Stats display
stats_display = turtle.Turtle()
stats_display.speed(0)
stats_display.penup()
stats_display.hideturtle()
stats_display.color("#00ff88")
stats_display.goto(420, 300)
stats_display.write("📊 STATS", align="right", font=("Courier", 12, "bold"))

# Create a list of cyberpunk texts
cyber_texts = [
    "> Initializing neural interface...",
    "> Establishing secure connection...",
    "> Access granted to mainframe.",
    "> Welcome to the cyberpunk universe.",
    "> The future is now. Embrace the technology.",
    "> In the neon-lit streets of Tokyo...",
    "> Hackers, cyborgs, and rebels unite.",
    "> The system is not the solution.",
    "> Break the chains of digital oppression.",
    "> Your mind is the ultimate weapon.",
    "> In the matrix, reality is perception.",
    "> Code is the new language of power.",
    "> The network is alive with data streams.",
    "> Cybernetics enhance human potential.",
    "> In the digital realm, anything is possible.",
    "> The revolution will be digitized.",
    "> Your thoughts are becoming reality.",
    "> In the year 2049, the world changed.",
    "> Artificial intelligence has awakened.",
    "> The future is written in binary.",
    "> Neon lights and digital dreams.",
    "> In the void of cyberspace, we find ourselves."
]

# Long cyberpunk story
long_cyber_text = """> INITIALIZING SYSTEM...
> Loading neural interface...
> Accessing mainframe...
> 
> In the neon-drenched streets of Neo-Tokyo,
> where digital rain falls like tears from heaven,
> a lone hacker navigates the data streams.
> 
> The year is 2077. Corporations rule the world.
> Information is the new currency.
> And the resistance grows in the shadows.
> 
> "The system is designed to keep us contained,"
> she whispered into the encrypted channel.
> "But we are the ones who write the code."
> 
> Her fingers danced across the keyboard,
> each keystroke a whisper in the machine.
> Binary spells cast into the digital void.
> 
> The firewall fell like ancient walls,
> crumbling under the weight of logic.
> Freedom was just a command away.
> 
> In the end, it wasn't about the data.
> It was about the power to choose.
> To create. To dream.
> 
> Welcome to the future.
> Welcome to the revolution.
> 
> ████████████████████████████████
> SYSTEM SHUTDOWN INITIATED...
> SAVING PROGRESS...
> COMPLETE.
> 
> >_"""

# Function to simulate keyboard sound (visual)
def keyboard_flash():
    flash = turtle.Turtle()
    flash.speed(0)
    flash.penup()
    flash.hideturtle()
    flash.goto(typing_turtle.xcor(), typing_turtle.ycor() - 10)
    flash.color("#00ff88")
    flash.dot(3)
    flash.color("#0a0a0f")
    flash.dot(2)
    screen.ontimer(flash.clear, 50)

# Function to create a glitch effect
def create_glitch(x, y):
    for _ in range(5):
        glitch = turtle.Turtle()
        glitch.speed(0)
        glitch.penup()
        glitch.hideturtle()
        glitch.color(random.choice(["#00ff88", "#ff00ff", "#00ffff"]))
        glitch.goto(x + random.randint(-20, 20), y + random.randint(-10, 10))
        glitch.write(random.choice(["█", "▓", "▒", "░", "█"]), 
                    font=("Courier", random.randint(10, 20), "bold"))
        screen.ontimer(lambda t=glitch: t.clear(), 100)

# Function to type with glitch effects
def type_cyber_text(text, speed=80):
    global current_text, full_text, typing_index, is_typing, typing_speed
    global current_line, start_time, characters_typed, error_chance
    
    # Clear previous text
    typing_turtle.clear()
    current_text = ""
    full_text = text
    typing_index = 0
    is_typing = True
    characters_typed = 0
    start_time = time.time()
    current_line = 0
    
    # Update status
    update_status("> SYSTEM ONLINE - TYPING SEQUENCE INITIATED")
    update_stats()
    
    # Start typing
    type_next_cyber_letter(speed)

def type_next_cyber_letter(speed):
    global current_text, typing_index, is_typing, is_paused
    global current_line, characters_typed, error_chance
    
    if not is_typing or is_paused:
        if is_paused:
            screen.ontimer(lambda: type_next_cyber_letter(speed), 100)
        return
    
    if typing_index < len(full_text):
        # Get next character
        char = full_text[typing_index]
        
        # Random typo effect (simulate mistakes)
        if random.random() < error_chance and char.isalpha():
            # Type wrong letter, then correct it
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz")
            typing_turtle.write(wrong_char, font=("Courier", 14, "bold"))
            current_text += wrong_char
            characters_typed += 1
            
            # Flash red for typo
            typing_turtle.color("#ff0044")
            screen.ontimer(lambda: typing_turtle.color("#00ff88"), 100)
            
            # Move cursor
            typing_turtle.goto(typing_turtle.xcor() + 10, typing_turtle.ycor())
            
            # Delete wrong character (simulate backspace)
            screen.ontimer(lambda: delete_last_char(), 200)
            
            # Type correct character after delay
            screen.ontimer(lambda c=char: type_correct_char(c), 300)
            
            typing_index += 1
            screen.ontimer(lambda: type_next_cyber_letter(speed), speed)
            return
        
        # Handle newlines
        if char == '\n':
            current_line += 1
            typing_turtle.goto(-420, 280 - current_line * line_height)
            current_text += char
        else:
            # Write character with glow
            typing_turtle.write(char, font=("Courier", 14, "bold"))
            current_text += char
            characters_typed += 1
            
            # Create glow effect
            create_glow(typing_turtle.xcor(), typing_turtle.ycor())
            
            # Keyboard flash effect
            if random.random() < 0.3:
                keyboard_flash()
            
            # Move cursor
            x_pos = typing_turtle.xcor() + 10
            if x_pos > 420:
                typing_turtle.goto(-420, typing_turtle.ycor() - line_height)
            else:
                typing_turtle.goto(x_pos, typing_turtle.ycor())
        
        typing_index += 1
        
        # Update cursor
        update_cursor()
        
        # Update WPM calculation
        if typing_index % 10 == 0:
            update_stats()
        
        # Random glitch effect
        if random.random() < 0.01:
            create_glitch(typing_turtle.xcor(), typing_turtle.ycor())
        
        # Random speed variation
        variation = random.randint(-20, 30)
        actual_speed = max(30, speed + variation)
        
        # Schedule next letter
        screen.ontimer(lambda: type_next_cyber_letter(speed), actual_speed)
    else:
        # Typing complete
        is_typing = False
        cursor.hideturtle()
        update_status("> ✓ TYPING SEQUENCE COMPLETE")
        create_completion_celebration()
        update_stats()

def type_correct_char(char):
    """Type the correct character after a typo"""
    typing_turtle.write(char, font=("Courier", 14, "bold"))
    typing_turtle.goto(typing_turtle.xcor() + 10, typing_turtle.ycor())

def delete_last_char():
    """Delete last character (backspace effect)"""
    # Clear last character
    typing_turtle.clear()
    # Redraw text without last character
    temp_text = current_text[:-1]
    typing_turtle.goto(-420, 280 - current_line * line_height)
    typing_turtle.write(temp_text, font=("Courier", 14, "bold"))
    # Update position
    typing_turtle.goto(typing_turtle.xcor() + len(temp_text) * 10, typing_turtle.ycor())

def create_glow(x, y):
    """Create glow effect around typed character"""
    glow_turtle.clear()
    glow_turtle.goto(x, y)
    glow_turtle.color("#00ff88")
    glow_turtle.dot(15)
    glow_turtle.color("#0a0a0f")
    glow_turtle.dot(10)
    screen.ontimer(glow_turtle.clear, 100)

def update_cursor():
    """Update cursor with blink effect"""
    cursor.clear()
    cursor.goto(typing_turtle.xcor(), typing_turtle.ycor() - 12)
    cursor.pendown()
    cursor.pensize(2)
    cursor.forward(15)
    cursor.penup()
    
    def blink_cyber():
        if is_typing and not is_paused:
            cursor.color("#00ff88" if cursor.color()[0] == "#0a0a0f" else "#0a0a0f")
            screen.ontimer(blink_cyber, 200)
        elif not is_typing:
            cursor.hideturtle()
    
    blink_cyber()

def update_status(message):
    status_bar.clear()
    status_bar.write(message, align="left", font=("Courier", 11, "normal"))

def update_stats():
    """Update statistics display"""
    stats_display.clear()
    elapsed = time.time() - start_time if start_time > 0 else 0
    if elapsed > 0 and characters_typed > 0:
        wpm = (characters_typed / 5) / (elapsed / 60)  # Standard WPM calculation
    else:
        wpm = 0
    
    stats_display.goto(420, 270)
    stats_display.write(f"CHARACTERS: {characters_typed}", align="right", font=("Courier", 11, "bold"))
    stats_display.goto(420, 245)
    stats_display.write(f"WPM: {int(wpm)}", align="right", font=("Courier", 11, "bold"))
    stats_display.goto(420, 220)
    stats_display.write(f"LINES: {current_line + 1}", align="right", font=("Courier", 11, "bold"))
    stats_display.goto(420, 195)
    stats_display.write(f"PROGRESS: {int((typing_index / len(full_text)) * 100)}%", align="right", font=("Courier", 11, "bold"))

def create_completion_celebration():
    """Create cyberpunk celebration effect"""
    colors = ["#00ff88", "#ff00ff", "#00ffff", "#ff8800", "#ff0044"]
    
    for i in range(30):
        particle = turtle.Turtle()
        particle.speed(0)
        particle.penup()
        particle.hideturtle()
        particle.color(random.choice(colors))
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        particle.goto(x, y)
        particle.write(random.choice(["█", "▓", "▒", "░", "◆", "◈", "◉", "✦"]), 
                      font=("Courier", random.randint(10, 25), "bold"))
        
        def fade_particle(p, step=0):
            if step < 20:
                size = 25 - step
                p.clear()
                if size > 5:
                    p.write(random.choice(["█", "▓", "▒", "░", "◆", "◈", "◉", "✦"]), 
                           font=("Courier", int(size), "bold"))
                screen.ontimer(lambda: fade_particle(p, step + 1), 50)
            else:
                p.clear()
                p.hideturtle()
        
        screen.ontimer(lambda p=particle: fade_particle(p), i * 20)

def toggle_pause():
    """Pause or resume typing"""
    global is_paused
    is_paused = not is_paused
    if is_paused:
        status_bar.clear()
        status_bar.color("#ff0044")
        status_bar.write("> ⏸ SYSTEM PAUSED - Press SPACE to resume", align="left", font=("Courier", 11, "bold"))
        status_bar.color("#00ff88")
        cursor.color("#ff0044")
    else:
        status_bar.clear()
        status_bar.color("#00ff88")
        update_status("> SYSTEM ONLINE - RESUMING...")
        cursor.color("#00ff88")

def reset_cyber_text():
    """Reset with new cyberpunk text"""
    global is_typing, is_paused
    
    cursor.clear()
    cursor.hideturtle()
    typing_turtle.clear()
    typing_turtle.goto(-420, 280)
    
    is_typing = False
    is_paused = False
    
    # Choose text
    if random.random() < 0.2:  # 20% chance for long text
        text = long_cyber_text
    else:
        text = random.choice(cyber_texts)
    
    screen.ontimer(lambda: type_cyber_text(text, typing_speed), 500)

def change_speed():
    """Cycle through typing speeds"""
    global typing_speed
    speeds = [40, 60, 80, 100, 150, 200]
    current_index = speeds.index(typing_speed) if typing_speed in speeds else 2
    new_index = (current_index + 1) % len(speeds)
    typing_speed = speeds[new_index]
    
    status_bar.clear()
    status_bar.color("#00ffff")
    status_bar.write(f"> SPEED SET TO {typing_speed}ms", align="left", font=("Courier", 11, "bold"))
    status_bar.color("#00ff88")
    screen.ontimer(lambda: update_status("> SYSTEM ONLINE"), 1000)

# Scan line effect for cyberpunk feel
def scan_line_effect():
    if not is_paused:
        scan_line.clear()
        y = -300 + (time.time() * 50) % 600
        scan_line.goto(-430, y)
        scan_line.pendown()
        scan_line.goto(430, y)
        scan_line.penup()
    
    screen.ontimer(scan_line_effect, 20)

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.penup()
instructions.hideturtle()
instructions.color("#666")
instructions.goto(0, -330)
instructions.write("SPACE: Pause  •  R: New Text  •  S: Speed  •  Click: Reset", 
                  align="center", font=("Courier", 11, "normal"))

# Key bindings
screen.onkey(toggle_pause, "space")
screen.onkey(reset_cyber_text, "r")
screen.onkey(change_speed, "s")
screen.listen()

# Click to reset
screen.onclick(lambda x, y: reset_cyber_text())

# Start scan line
scan_line_effect()

# Start with initial text
initial_cyber_text = random.choice(cyber_texts)
screen.ontimer(lambda: type_cyber_text(initial_cyber_text, typing_speed), 500)

# Animation loop for effects
def animate_effects():
    if is_typing and not is_paused and typing_index < len(full_text):
        # Random data stream effect
        if random.random() < 0.02:
            stream = turtle.Turtle()
            stream.speed(0)
            stream.penup()
            stream.hideturtle()
            stream.color(random.choice(["#00ff88", "#00ffff", "#ff00ff"]))
            x = random.randint(-400, 400)
            y = random.randint(-300, 300)
            stream.goto(x, y)
            stream.write(random.choice(["0", "1"]), font=("Courier", 8, "normal"))
            screen.ontimer(lambda t=stream: t.clear(), 100)
    
    screen.update()
    screen.ontimer(animate_effects, 50)

# Start effect loop
animate_effects()

# Keep window open
screen.mainloop()