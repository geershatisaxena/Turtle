import turtle
import time
import datetime
import math

# Setup the screen
screen = turtle.Screen()
screen.title("Real-Time Analog Clock")
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.tracer(0)
screen.bgpic("nopic")  # Clear any background image

# Create clock face turtle
clock_face = turtle.Turtle()
clock_face.speed(0)
clock_face.penup()
clock_face.hideturtle()

# Create hand turtles
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

# Create digital display turtle
digital_display = turtle.Turtle()
digital_display.speed(0)
digital_display.penup()
digital_display.hideturtle()

# Create date display turtle
date_display = turtle.Turtle()
date_display.speed(0)
date_display.penup()
date_display.hideturtle()

# Setup hands
for hand in [hour_hand, minute_hand, second_hand]:
    hand.speed(0)
    hand.penup()
    hand.hideturtle()

# Clock parameters
radius = 250
center_x = 0
center_y = 0

def draw_clock_face():
    """Draw the clock face with numbers and tick marks"""
    clock_face.clear()
    
    # Draw outer circle
    clock_face.penup()
    clock_face.goto(center_x, center_y - radius)
    clock_face.pendown()
    clock_face.pensize(5)
    clock_face.color("white")
    clock_face.circle(radius)
    
    # Draw inner circle
    clock_face.penup()
    clock_face.goto(center_x, center_y - (radius - 10))
    clock_face.pendown()
    clock_face.pensize(2)
    clock_face.circle(radius - 10)
    
    # Draw hour tick marks and numbers
    for hour in range(1, 13):
        angle = 90 - (hour * 30)  # 30 degrees per hour, start from 12 o'clock
        radian = math.radians(angle)
        
        # Tick mark positions
        inner_x = center_x + (radius - 20) * math.cos(radian)
        inner_y = center_y + (radius - 20) * math.sin(radian)
        outer_x = center_x + radius * math.cos(radian)
        outer_y = center_y + radius * math.sin(radian)
        
        # Draw tick mark
        clock_face.penup()
        clock_face.goto(inner_x, inner_y)
        clock_face.pendown()
        clock_face.pensize(4)
        clock_face.goto(outer_x, outer_y)
        
        # Draw hour numbers
        num_x = center_x + (radius - 45) * math.cos(radian)
        num_y = center_y + (radius - 45) * math.sin(radian)
        clock_face.penup()
        clock_face.goto(num_x - 12, num_y - 10)
        clock_face.color("cyan")
        clock_face.write(str(hour), font=("Arial", 20, "bold"))
    
    # Draw minute tick marks
    for minute in range(1, 61):
        if minute % 5 != 0:  # Skip hour marks
            angle = 90 - (minute * 6)  # 6 degrees per minute
            radian = math.radians(angle)
            
            inner_x = center_x + (radius - 15) * math.cos(radian)
            inner_y = center_y + (radius - 15) * math.sin(radian)
            outer_x = center_x + (radius - 5) * math.cos(radian)
            outer_y = center_y + (radius - 5) * math.sin(radian)
            
            clock_face.penup()
            clock_face.goto(inner_x, inner_y)
            clock_face.pendown()
            clock_face.pensize(2)
            clock_face.goto(outer_x, outer_y)
    
    # Draw center dot
    clock_face.penup()
    clock_face.goto(center_x, center_y - 8)
    clock_face.pendown()
    clock_face.color("red")
    clock_face.begin_fill()
    clock_face.circle(8)
    clock_face.end_fill()
    
    # Draw decorative ring
    clock_face.penup()
    clock_face.goto(center_x, center_y - (radius - 60))
    clock_face.pendown()
    clock_face.color("gray")
    clock_face.pensize(1)
    clock_face.circle(radius - 60)

def draw_hand(hand_turtle, angle, length, width, color):
    """Draw a clock hand at specified angle"""
    hand_turtle.clear()
    hand_turtle.penup()
    hand_turtle.goto(center_x, center_y)
    hand_turtle.setheading(90 - angle)  # 0 degrees is pointing right, we want up
    hand_turtle.color(color)
    hand_turtle.pensize(width)
    hand_turtle.pendown()
    hand_turtle.forward(length)
    hand_turtle.penup()
    
    # Draw arrow head for hour and minute hands
    if width >= 4:
        hand_turtle.goto(center_x, center_y)
        hand_turtle.setheading(90 - angle + 15)
        hand_turtle.pendown()
        hand_turtle.forward(15)
        hand_turtle.penup()
        hand_turtle.goto(center_x, center_y)
        hand_turtle.setheading(90 - angle - 15)
        hand_turtle.pendown()
        hand_turtle.forward(15)
        hand_turtle.penup()

def update_digital_display(hour, minute, second):
    """Update digital time display"""
    digital_display.clear()
    digital_display.goto(center_x, center_y - radius - 50)
    digital_display.color("lime")
    
    # Format time with leading zeros
    time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
    digital_display.write(time_str, align="center", font=("Courier", 30, "bold"))

def update_date_display():
    """Update date display"""
    date_display.clear()
    date_display.goto(center_x, center_y + radius + 40)
    date_display.color("yellow")
    
    now = datetime.datetime.now()
    date_str = now.strftime("%B %d, %Y")
    day_str = now.strftime("%A")
    
    date_display.write(f"{date_str}\n{day_str}", align="center", font=("Arial", 16, "bold"))

def draw_tick_marks_for_seconds():
    """Draw tick marks for each second (decorative)"""
    for second in range(60):
        angle = 90 - (second * 6)
        radian = math.radians(angle)
        
        inner_x = center_x + (radius - 10) * math.cos(radian)
        inner_y = center_y + (radius - 10) * math.sin(radian)
        outer_x = center_x + radius * math.cos(radian)
        outer_y = center_y + radius * math.sin(radian)
        
        clock_face.penup()
        clock_face.goto(inner_x, inner_y)
        clock_face.pendown()
        clock_face.pensize(1 if second % 5 != 0 else 2)
        clock_face.color("lightgray")
        clock_face.goto(outer_x, outer_y)

def draw_decorative_clock():
    """Draw decorative elements around the clock"""
    decor = turtle.Turtle()
    decor.speed(0)
    decor.penup()
    decor.hideturtle()
    
    # Draw corner ornaments
    corners = [(-350, 350), (350, 350), (-350, -350), (350, -350)]
    for x, y in corners:
        decor.goto(x, y)
        decor.pendown()
        decor.color("gold")
        decor.pensize(3)
        decor.begin_fill()
        decor.fillcolor("#333333")
        for _ in range(4):
            decor.forward(30)
            decor.right(90)
        decor.end_fill()
        decor.penup()

def animate_clock():
    """Main animation loop - updates clock every second"""
    draw_decorative_clock()
    draw_clock_face()
    draw_tick_marks_for_seconds()
    
    last_second = -1
    
    while True:
        # Get current time
        now = datetime.datetime.now()
        hour = now.hour % 12  # Convert to 12-hour format
        minute = now.minute
        second = now.second
        microsecond = now.microsecond
        
        # Calculate angles (for smooth second hand movement)
        hour_angle = (hour * 30) + (minute * 0.5)  # 30 degrees per hour + 0.5 per minute
        minute_angle = minute * 6  # 6 degrees per minute
        second_angle = second * 6 + (microsecond / 1000000) * 6  # Smooth second movement
        
        # Draw hands
        draw_hand(hour_hand, hour_angle, radius * 0.5, 8, "white")
        draw_hand(minute_hand, minute_angle, radius * 0.7, 6, "white")
        draw_hand(second_hand, second_angle, radius * 0.85, 2, "red")
        
        # Update displays
        update_digital_display(now.hour, minute, second)
        update_date_display()
        
        # Update screen
        screen.update()
        
        # Wait until next second (approximately)
        time.sleep(0.05)

# Title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 380)
title.write("⏰ REAL-TIME ANALOG CLOCK ⏰", align="center", font=("Arial", 18, "bold"))

# Instructions
instructions = turtle.Turtle()
instructions.speed(0)
instructions.color("gray")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, -380)
instructions.write("Showing real system time | ESC to exit", align="center", font=("Arial", 10, "normal"))

# Keyboard binding
screen.listen()
screen.onkey(lambda: screen.bye(), "Escape")

# Print console information
print("=" * 50)
print("        REAL-TIME ANALOG CLOCK")
print("=" * 50)
print()
print("Features:")
print("  • Real system time (updates every second)")
print("  • Smooth second hand movement")
print("  • Digital time display")
print("  • Date and day display")
print("  • Hour, minute, and second tick marks")
print()
print("The clock shows your computer's current time")
print("Press ESC to exit")
print()

# Run the clock
try:
    animate_clock()
except KeyboardInterrupt:
    screen.bye()
except turtle.Terminator:
    pass

screen.mainloop()