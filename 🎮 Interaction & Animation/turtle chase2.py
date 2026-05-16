import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Turtle Chase - Cat chases Mouse!")
screen.bgcolor("lightgreen")
screen.tracer(0)  # Turn off auto refresh for smooth animation
screen.colormode(255)

# Create the chaser (Cat)
cat = turtle.Turtle()
cat.shape("turtle")
cat.color("red")
cat.penup()
cat.speed(0)
cat.goto(0, 0)

# Create the runner (Mouse)
mouse = turtle.Turtle()
mouse.shape("turtle")
mouse.color("blue")
mouse.penup()
mouse.speed(0)
mouse.goto(random.randint(-300, 300), random.randint(-200, 200))

# Create score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.color("darkblue")
score_display.write("Catch the blue turtle!", align="center", font=("Arial", 16, "bold"))

# Game variables
score = 0
game_over = False
cat_speed = 5  # Chaser speed
mouse_speed = 3  # Runner speed
escape_distance = 150  # Distance at which mouse tries to escape

def update_score():
    """Update the score display."""
    score_display.clear()
    score_display.write(f"Score: {score} | Chase the blue turtle!", 
                        align="center", font=("Arial", 16, "bold"))

def move_cat():
    """Move the cat towards the mouse."""
    global game_over, score, cat_speed
    
    if game_over:
        return
    
    # Get positions
    cat_x, cat_y = cat.position()
    mouse_x, mouse_y = mouse.position()
    
    # Calculate angle towards mouse
    angle = math.degrees(math.atan2(mouse_y - cat_y, mouse_x - cat_x))
    cat.setheading(angle)
    
    # Move cat forward
    cat.forward(cat_speed)
    
    # Check for collision (cat catches mouse)
    distance = math.sqrt((cat_x - mouse_x)**2 + (cat_y - mouse_y)**2)
    if distance < 20:  # Collision distance
        score += 1
        update_score()
        
        # Reset mouse to random position
        mouse.goto(random.randint(-350, 350), random.randint(-250, 250))
        
        # Increase difficulty (cat gets faster, mouse gets smarter)
        cat_speed += 0.3
        mouse_speed += 0.2
        
        # Add visual feedback for catch
        cat.color("darkred")
        screen.ontimer(lambda: cat.color("red"), 100)
        mouse.color("lightblue")
        screen.ontimer(lambda: mouse.color("blue"), 100)

def move_mouse():
    """Move mouse away from cat with random behavior."""
    global game_over, mouse_speed, cat_speed  # Added cat_speed here
    
    if game_over:
        return
    
    # Get positions
    cat_x, cat_y = cat.position()
    mouse_x, mouse_y = mouse.position()
    
    # Calculate distance and angle to cat
    distance = math.sqrt((cat_x - mouse_x)**2 + (cat_y - mouse_y)**2)
    angle_to_cat = math.degrees(math.atan2(cat_y - mouse_y, cat_x - mouse_x))
    
    # Mouse behavior based on distance
    if distance < escape_distance:
        # RUN AWAY! (move opposite direction from cat)
        escape_angle = angle_to_cat + 180
        mouse.setheading(escape_angle)
        mouse.forward(mouse_speed * 1.5)  # Run faster when scared
    else:
        # Random movement when safe
        if random.random() < 0.1:  # 10% chance to change direction
            mouse.setheading(random.randint(0, 360))
        mouse.forward(mouse_speed)
    
    # Keep mouse inside boundaries
    x, y = mouse.position()
    if x > 380:
        mouse.setx(380)
        mouse.setheading(random.randint(90, 270))
    elif x < -380:
        mouse.setx(-380)
        mouse.setheading(random.randint(-90, 90))
    
    if y > 280:
        mouse.sety(280)
        mouse.setheading(random.randint(180, 360))
    elif y < -280:
        mouse.sety(-280)
        mouse.setheading(random.randint(0, 180))

def check_boundaries():
    """Keep cat inside screen boundaries."""
    x, y = cat.position()
    
    # Bounce off walls
    if x > 380:
        cat.setx(380)
        cat.setheading(180)
        cat.forward(10)
    elif x < -380:
        cat.setx(-380)
        cat.setheading(0)
        cat.forward(10)
    
    if y > 280:
        cat.sety(280)
        cat.setheading(270)
        cat.forward(10)
    elif y < -280:
        cat.sety(-280)
        cat.setheading(90)
        cat.forward(10)

def reset_game():
    """Reset the game to start over."""
    global score, cat_speed, mouse_speed, game_over
    score = 0
    cat_speed = 5
    mouse_speed = 3
    game_over = False
    
    # Reset positions
    cat.goto(0, 0)
    cat.color("red")
    mouse.goto(random.randint(-300, 300), random.randint(-200, 200))
    mouse.color("blue")
    
    # Clear any game over text
    for item in screen.turtles():
        if item != cat and item != mouse and item != score_display:
            if item != instructions and hasattr(item, 'clear'):
                item.clear()
                item.hideturtle()
    
    update_score()
    print("Game reset! Chase the blue turtle!")

def end_game():
    """End the game."""
    global game_over
    game_over = True
    
    # Display game over message
    game_over_display = turtle.Turtle()
    game_over_display.hideturtle()
    game_over_display.penup()
    game_over_display.color("red")
    game_over_display.goto(0, 0)
    game_over_display.write(f"GAME OVER! Final Score: {score}", 
                            align="center", font=("Arial", 24, "bold"))
    
    screen.update()

def animate():
    """Main animation loop."""
    if not game_over:
        move_cat()
        move_mouse()
        check_boundaries()
        
        screen.update()
        screen.ontimer(animate, 20)  # ~50 FPS

# Create instructions turtle
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(0, -280)
instructions.color("darkgreen")
instructions.write("Red turtle chases Blue turtle | Press 'r' to reset | Press 'q' to quit", 
                   align="center", font=("Arial", 10, "normal"))

# Keyboard controls
def reset():
    reset_game()
    animate()  # Restart animation if game was over

def quit_game():
    screen.bye()

screen.listen()
screen.onkey(reset, "r")
screen.onkey(quit_game, "q")
screen.onkey(quit_game, "Q")

# Start the game
print("=" * 50)
print("TURTLE CHASE GAME")
print("=" * 50)
print("Red Turtle (Cat) chases Blue Turtle (Mouse)")
print("Catch the blue turtle to score points!")
print("Each catch makes the red turtle faster!")
print("")
print("Controls:")
print("  - Watch the automatic chase!")
print("  - Press 'r' to reset the game")
print("  - Press 'q' to quit")
print("=" * 50)

update_score()
animate()

# Keep window open
screen.mainloop()