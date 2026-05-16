import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Tag! You're It! - Catch the Computer Turtle")
screen.bgcolor("darkblue")
screen.tracer(0)
screen.colormode(255)

# Create player turtle (controlled by you)
player = turtle.Turtle()
player.shape("turtle")
player.color("gold")
player.penup()
player.speed(0)
player.goto(0, 0)

# Create computer turtle (runs away)
computer = turtle.Turtle()
computer.shape("turtle")
computer.color("red")
computer.penup()
computer.speed(0)
computer.goto(random.randint(-300, 300), random.randint(-200, 200))

# Create score display
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.color("white")
score_turtle.goto(0, 260)

# Create timer display
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.color("cyan")
timer_turtle.goto(-350, 260)

# Game variables
score = 0
time_left = 30
game_active = True
player_speed = 8
computer_speed = 4
difficulty_level = 1

def update_score():
    """Update score display."""
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 18, "bold"))

def update_timer():
    """Update timer display."""
    timer_turtle.clear()
    timer_turtle.write(f"Time: {int(time_left)}s", align="left", font=("Arial", 18, "bold"))

def move_player():
    """Move player with arrow keys."""
    if not game_active:
        return
    
    # Get current position
    x, y = player.position()
    
    # Boundary checking
    if x > 370:
        player.setx(370)
    elif x < -370:
        player.setx(-370)
    
    if y > 270:
        player.sety(270)
    elif y < -270:
        player.sety(-270)

def move_computer():
    """Computer turtle runs away from player."""
    if not game_active:
        return
    
    # Get positions
    player_x, player_y = player.position()
    comp_x, comp_y = computer.position()
    
    # Calculate distance and angle to player
    distance = math.sqrt((player_x - comp_x)**2 + (player_y - comp_y)**2)
    angle_to_player = math.degrees(math.atan2(player_y - comp_y, player_x - comp_x))
    
    # Computer behavior based on distance and difficulty
    if distance < 100:
        # RUN AWAY fast!
        escape_angle = angle_to_player + 180
        computer.setheading(escape_angle)
        computer.forward(computer_speed * 1.8)
    elif distance < 200:
        # Run away slower
        escape_angle = angle_to_player + 180
        computer.setheading(escape_angle)
        computer.forward(computer_speed * 1.2)
    else:
        # Random movement when far away
        if random.random() < 0.05:  # 5% chance to change direction
            computer.setheading(random.randint(0, 360))
        computer.forward(computer_speed)
    
    # Keep computer in bounds
    x, y = computer.position()
    if x > 370:
        computer.setx(370)
        computer.setheading(random.randint(90, 270))
    elif x < -370:
        computer.setx(-370)
        computer.setheading(random.randint(-90, 90))
    
    if y > 270:
        computer.sety(270)
        computer.setheading(random.randint(180, 360))
    elif y < -270:
        computer.sety(-270)
        computer.setheading(random.randint(0, 180))

def check_collision():
    """Check if player caught the computer."""
    global score, computer_speed, difficulty_level
    
    if not game_active:
        return
    
    # Check distance between turtles
    distance = math.sqrt((player.xcor() - computer.xcor())**2 + 
                        (player.ycor() - computer.ycor())**2)
    
    if distance < 25:  # Caught!
        score += 1
        update_score()
        
        # Teleport computer to random location
        computer.goto(random.randint(-350, 350), random.randint(-250, 250))
        
        # Increase difficulty every 5 catches
        if score % 5 == 0:
            difficulty_level += 1
            computer_speed += 0.8
            print(f"⚡ Difficulty increased! Computer speed: {computer_speed:.1f}")
        
        # Visual feedback
        computer.color("orange")
        screen.ontimer(lambda: computer.color("red"), 150)
        player.color("lime")
        screen.ontimer(lambda: player.color("gold"), 150)
        
        # Add sparkle effect
        sparkle = turtle.Turtle()
        sparkle.shape("circle")
        sparkle.color("yellow")
        sparkle.shapesize(0.5)
        sparkle.penup()
        sparkle.goto(computer.xcor(), computer.ycor())
        screen.ontimer(sparkle.clear, 200)
        screen.ontimer(sparkle.hideturtle, 200)

def countdown():
    """Game timer countdown."""
    global time_left, game_active
    
    if time_left > 0 and game_active:
        time_left -= 0.1
        update_timer()
        screen.ontimer(countdown, 100)
    elif time_left <= 0 and game_active:
        game_active = False
        game_over()

def game_over():
    """End the game and show results."""
    # Display game over message
    game_over_turtle = turtle.Turtle()
    game_over_turtle.hideturtle()
    game_over_turtle.penup()
    game_over_turtle.color("red")
    game_over_turtle.goto(0, 50)
    game_over_turtle.write("GAME OVER!", align="center", font=("Arial", 32, "bold"))
    
    game_over_turtle.goto(0, -20)
    game_over_turtle.color("yellow")
    game_over_turtle.write(f"Final Score: {score}", align="center", font=("Arial", 24, "bold"))
    
    game_over_turtle.goto(0, -70)
    game_over_turtle.color("white")
    game_over_turtle.write("Press 'r' to play again or 'q' to quit", 
                          align="center", font=("Arial", 14, "normal"))
    
    # Add rating based on score
    rating = ""
    if score >= 20:
        rating = "🏆 LEGENDARY! 🏆"
    elif score >= 15:
        rating = "⭐ AMAZING! ⭐"
    elif score >= 10:
        rating = "👍 GOOD JOB! 👍"
    elif score >= 5:
        rating = "👌 NOT BAD! 👌"
    else:
        rating = "💪 KEEP PRACTICING! 💪"
    
    game_over_turtle.goto(0, -120)
    game_over_turtle.write(rating, align="center", font=("Arial", 16, "bold"))
    
    screen.update()

def reset_game():
    """Reset the game to start over."""
    global score, time_left, game_active, computer_speed, difficulty_level
    
    score = 0
    time_left = 30
    game_active = True
    computer_speed = 4
    difficulty_level = 1
    
    # Reset positions
    player.goto(0, 0)
    player.color("gold")
    computer.goto(random.randint(-300, 300), random.randint(-200, 200))
    computer.color("red")
    
    # Clear game over messages
    for item in screen.turtles():
        if item not in [player, computer, score_turtle, timer_turtle, instructions_turtle]:
            if hasattr(item, 'clear'):
                item.clear()
                item.hideturtle()
    
    update_score()
    update_timer()
    print("Game reset! Catch the red turtle!")
    
    # Restart animations
    countdown()
    animate()

def up():
    if game_active:
        player.setheading(90)
        player.forward(player_speed)
        move_player()

def down():
    if game_active:
        player.setheading(270)
        player.forward(player_speed)
        move_player()

def left():
    if game_active:
        player.setheading(180)
        player.forward(player_speed)
        move_player()

def right():
    if game_active:
        player.setheading(0)
        player.forward(player_speed)
        move_player()

def quit_game():
    screen.bye()

def animate():
    """Main animation loop."""
    if game_active:
        move_computer()
        check_collision()
        screen.update()
        screen.ontimer(animate, 20)

# Create instructions
instructions_turtle = turtle.Turtle()
instructions_turtle.hideturtle()
instructions_turtle.penup()
instructions_turtle.goto(0, -280)
instructions_turtle.color("lightgray")
instructions_turtle.write("Use ARROW KEYS to catch the RED turtle! | Press 'r' to reset | Press 'q' to quit", 
                          align="center", font=("Arial", 10, "normal"))

# Keyboard bindings
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(reset_game, "r")
screen.onkey(reset_game, "R")
screen.onkey(quit_game, "q")
screen.onkey(quit_game, "Q")

# Instructions
print("=" * 50)
print("TAG! YOU'RE IT! - Turtle Chase Game")
print("=" * 50)
print("🐢 You are the GOLD turtle")
print("🎯 Catch the RED turtle before time runs out!")
print("⚡ Gets harder every 5 catches (computer gets faster)")
print("")
print("CONTROLS:")
print("  ↑ - Move Up")
print("  ↓ - Move Down")
print("  ← - Move Left")
print("  → - Move Right")
print("  R - Reset Game")
print("  Q - Quit")
print("")
print("READY? GO! 🏃‍♂️")
print("=" * 50)

# Start game
update_score()
update_timer()
countdown()
animate()

# Keep window open
screen.mainloop()