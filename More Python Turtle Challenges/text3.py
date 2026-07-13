import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#1a1a2e")
screen.title("Typing Text Animation")
screen.tracer(0)
screen.setup(900, 700)

# Create the typing turtle
typing_turtle = turtle.Turtle()
typing_turtle.speed(0)
typing_turtle.penup()
typing_turtle.hideturtle()
typing_turtle.color("#00d2d3")
typing_turtle.goto(-350, 200)

# Cursor turtle
cursor = turtle.Turtle()
cursor.speed(0)
cursor.penup()
cursor.hideturtle()
cursor.color("white")

# Create a glow effect for text
glow = turtle.Turtle()
glow.speed(0)
glow.penup()
glow.hideturtle()

# Text variables
current_text = ""
full_text = ""
typing_index = 0
typing_speed = 100  # Milliseconds between letters
is_typing = False
is_paused = False
text_lines = []
current_line = 0
line_height = 40

# Display elements
status_display = turtle.Turtle()
status_display.speed(0)
status_display.penup()
status_display.hideturtle()
status_display.color("gray")
status_display.goto(-350, -320)

progress_display = turtle.Turtle()
progress_display.speed(0)
progress_display.penup()
progress_display.hideturtle()
progress_display.goto(350, -320)

title_display = turtle.Turtle()
title_display.speed(0)
title_display.penup()
title_display.hideturtle()
title_display.color("#ff6b6b")
title_display.goto(0, 340)
title_display.write("⌨️ TYPING ANIMATION", align="center", font=("Arial", 24, "bold"))

subtitle = turtle.Turtle()
subtitle.speed(0)
subtitle.penup()
subtitle.hideturtle()
subtitle.color("gray")
subtitle.goto(0, 310)
subtitle.write("Letter by Letter Typewriter Effect", align="center", font=("Arial", 14, "normal"))

# Text presets
text_presets = [
    "Hello! Welcome to the typing animation.",
    "This is a letter by letter typewriter effect.",
    "It looks just like someone is typing in real time.",
    "You can customize the speed and text content.",
    "Press SPACE to pause or resume typing.",
    "Press R to restart with a new text.",
    "Press S to change typing speed.",
    "The cursor blinks to show typing position.",
    "This is so cool! 😊",
    "Python and Turtle make a great combination!",
    "Programming is fun and creative.",
    "You can create amazing animations with code.",
    "Every letter appears one by one...",
    "Just like a real typewriter!",
    "The possibilities are endless.",
    "Keep coding and exploring! 🚀"
]

# Sample longer text (for demonstration)
long_text = """In the beginning, there was nothing but darkness.
Then came the light of creation.
With every keystroke, a new world emerges.
Letters form words, words form sentences,
and sentences tell stories.
This is the magic of writing - 
breathing life into thoughts,
one character at a time.

The typewriter clicks and clacks,
a rhythmic dance of expression.
Each letter holds meaning,
each word carries weight,
and together they create
something beautiful.

So type away, dear writer,
for your words have power.
They can inspire, educate,
entertain, and transform.
Never underestimate
the impact of your voice."""

# Function to get random text
def get_random_text():
    return random.choice(text_presets)

# Function to type text letter by letter
def type_text(text, speed=100):
    global current_text, full_text, typing_index, is_typing, typing_speed
    global current_line, text_lines
    
    # Clear previous text
    typing_turtle.clear()
    current_text = ""
    full_text = text
    typing_index = 0
    is_typing = True
    
    # Split text into lines if needed
    text_lines = text.split('\n')
    current_line = 0
    
    # Update status
    update_status(f"Typing... ({len(text)} characters)")
    update_progress(0)
    
    # Start typing animation
    type_next_letter(speed)

def type_next_letter(speed):
    global current_text, typing_index, is_typing, is_paused
    global current_line
    
    if not is_typing or is_paused:
        if is_paused:
            screen.ontimer(lambda: type_next_letter(speed), 100)
        return
    
    if typing_index < len(full_text):
        # Get next character
        char = full_text[typing_index]
        
        # Handle newlines
        if char == '\n':
            current_line += 1
            typing_turtle.goto(-350, 200 - current_line * line_height)
            current_text += char
        else:
            # Write the character
            typing_turtle.write(char, font=("Courier", 16, "normal"))
            current_text += char
            # Move cursor position
            x_pos = typing_turtle.xcor() + 12
            if x_pos > 350:
                typing_turtle.goto(-350, typing_turtle.ycor() - line_height)
            else:
                typing_turtle.goto(x_pos, typing_turtle.ycor())
        
        typing_index += 1
        
        # Update cursor position
        update_cursor()
        
        # Update progress
        progress = int((typing_index / len(full_text)) * 100)
        update_progress(progress)
        
        # Random slight delay variation for natural feel
        variation = random.randint(-20, 20)
        actual_speed = max(30, speed + variation)
        
        # Schedule next letter
        screen.ontimer(lambda: type_next_letter(speed), actual_speed)
    else:
        # Typing complete
        is_typing = False
        cursor.hideturtle()
        update_status("✅ Typing complete!")
        create_completion_effect()

def update_cursor():
    """Update cursor position and blink"""
    cursor.clear()
    cursor.goto(typing_turtle.xcor(), typing_turtle.ycor() - 18)
    cursor.pendown()
    cursor.pensize(2)
    cursor.forward(15)
    cursor.penup()
    cursor.goto(typing_turtle.xcor(), typing_turtle.ycor() - 18)
    
    # Blink animation
    def blink_cursor(state=True):
        if is_typing and not is_paused:
            if state:
                cursor.color("white")
            else:
                cursor.color("#1a1a2e")  # Same as background
            screen.ontimer(lambda: blink_cursor(not state), 300)
        else:
            if not is_typing:
                cursor.hideturtle()
    
    blink_cursor(True)

def update_status(message):
    status_display.clear()
    status_display.write(message, align="left", font=("Arial", 12, "normal"))

def update_progress(progress):
    progress_display.clear()
    progress_display.write(f"Progress: {progress}%", align="right", font=("Arial", 12, "normal"))

def create_completion_effect():
    """Create celebration effect when typing completes"""
    # Create sparkles
    for _ in range(20):
        sparkle = turtle.Turtle()
        sparkle.speed(0)
        sparkle.penup()
        sparkle.hideturtle()
        sparkle.color(random.choice(["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff", "#9b59b6"]))
        x = random.randint(-350, 350)
        y = random.randint(-300, 300)
        sparkle.goto(x, y)
        sparkle.dot(random.randint(3, 8))
        
        # Fade out sparkles
        def fade_sparkle(t, step=0):
            if step < 10:
                size = 8 - step * 0.8
                t.dot(max(0, size))
                screen.ontimer(lambda: fade_sparkle(t, step + 1), 50)
            else:
                t.clear()
                t.hideturtle()
        
        screen.ontimer(lambda s=sparkle: fade_sparkle(s), random.randint(0, 200))

def toggle_pause():
    """Pause or resume typing"""
    global is_paused
    is_paused = not is_paused
    if is_paused:
        status_display.clear()
        status_display.color("#ff6b6b")
        status_display.write("⏸ PAUSED - Press SPACE to resume", align="left", font=("Arial", 12, "bold"))
        status_display.color("gray")
        cursor.color("#ff6b6b")
    else:
        status_display.clear()
        status_display.color("gray")
        update_status("Typing...")
        cursor.color("white")

def reset_with_new_text():
    """Reset animation with new random text"""
    global is_typing, is_paused
    
    # Reset cursor
    cursor.clear()
    cursor.hideturtle()
    
    # Clear all text
    typing_turtle.clear()
    typing_turtle.goto(-350, 200)
    
    # Reset variables
    is_typing = False
    is_paused = False
    
    # Choose random text
    if random.random() < 0.3:  # 30% chance for long text
        text = long_text
    else:
        text = get_random_text()
    
    # Start typing
    screen.ontimer(lambda: type_text(text, typing_speed), 500)

def change_speed():
    """Change typing speed"""
    global typing_speed
    speeds = [50, 80, 100, 150, 200, 300]
    current_index = speeds.index(typing_speed) if typing_speed in speeds else 2
    new_index = (current_index + 1) % len(speeds)
    typing_speed = speeds[new_index]
    
    # Update status
    status_display.clear()
    status_display.color("#ffd93d")
    status_display.write(f"Speed: {typing_speed}ms", align="left", font=("Arial", 12, "bold"))
    status_display.color("gray")
    screen.ontimer(lambda: update_status("Typing..."), 1000)

def speed_up():
    """Increase typing speed"""
    global typing_speed
    typing_speed = max(30, typing_speed - 10)
    update_status(f"Speed: {typing_speed}ms")

def slow_down():
    """Decrease typing speed"""
    global typing_speed
    typing_speed = min(500, typing_speed + 10)
    update_status(f"Speed: {typing_speed}ms")

# Create a keyboard visual
def draw_keyboard():
    keyboard = turtle.Turtle()
    keyboard.speed(0)
    keyboard.penup()
    keyboard.hideturtle()
    keyboard.goto(-380, -280)
    keyboard.color("#2a2a4e")
    keyboard.pendown()
    keyboard.begin_fill()
    for _ in range(2):
        keyboard.forward(760)
        keyboard.left(90)
        keyboard.forward(40)
        keyboard.left(90)
    keyboard.end_fill()
    keyboard.penup()
    
    # Keyboard keys (decorative)
    keys = ["SPACE", "R", "S", "P", "↑", "↓"]
    x_positions = [-300, -150, -50, 50, 150, 250]
    
    for key, x in zip(keys, x_positions):
        keyboard.goto(x - 20, -260)
        keyboard.color("#3a3a5e")
        keyboard.pendown()
        keyboard.begin_fill()
        for _ in range(2):
            keyboard.forward(40)
            keyboard.left(90)
            keyboard.forward(20)
            keyboard.left(90)
        keyboard.end_fill()
        keyboard.penup()
        keyboard.goto(x, -250)
        keyboard.color("gray")
        keyboard.write(key, align="center", font=("Arial", 8, "normal"))

# Draw keyboard
draw_keyboard()

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.penup()
instructions.hideturtle()
instructions.color("gray")
instructions.goto(0, -295)
instructions.write("SPACE: Pause  •  R: New Text  •  S: Change Speed  •  ↑: Faster  •  ↓: Slower", 
                  align="center", font=("Arial", 10, "normal"))

# Function to create a typing sound effect (visual)
def create_typing_effect():
    """Create visual effect when typing"""
    if is_typing and not is_paused:
        # Small glow at cursor position
        glow.clear()
        glow.goto(typing_turtle.xcor(), typing_turtle.ycor() - 10)
        glow.color("#00d2d3")
        glow.dot(5)
        glow.color("#1a1a2e")
        glow.dot(3)
        
        # Schedule glow removal
        screen.ontimer(lambda: glow.clear(), 50)

# Key bindings
screen.onkey(toggle_pause, "space")
screen.onkey(reset_with_new_text, "r")
screen.onkey(change_speed, "s")
screen.onkey(speed_up, "Up")
screen.onkey(slow_down, "Down")
screen.listen()

# Click to restart
screen.onclick(lambda x, y: reset_with_new_text())

# Start with initial text
initial_text = "Welcome to the typing animation! Press SPACE to pause, R for new text."
screen.ontimer(lambda: type_text(initial_text, typing_speed), 500)

# Main animation loop (for cursor and effects)
def animate():
    # Create typing effect (visual feedback)
    if is_typing and not is_paused and typing_index < len(full_text):
        # Small visual feedback at cursor
        if random.random() < 0.3:
            create_typing_effect()
    
    screen.update()
    screen.ontimer(animate, 50)

# Start animation loop
animate()

# Keep window open
screen.mainloop()