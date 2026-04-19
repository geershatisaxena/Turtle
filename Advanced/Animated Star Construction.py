import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Understanding the COMPLETE Star")
screen.setup(800, 600)
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def draw_and_label_star():
    """Draw a star and explain what makes it COMPLETE"""
    
    # Draw a faint outline of the complete star first
    t.pencolor("gray")
    t.pensize(1)
    t.penup()
    t.goto(0, -100)
    t.pendown()
    
    # Draw complete star outline quickly
    for _ in range(5):
        t.forward(150)
        t.right(144)  # 180 - 180/5 = 144 degrees
    t.penup()
    
    # Now draw it again with colors and labels
    t.goto(0, -100)
    t.pendown()
    t.pensize(3)
    
    # The star has 5 points, each point has 2 lines = 10 lines total
    lines_info = []
    
    for point in range(5):
        # First line of the point
        t.pencolor("red")
        t.forward(150)
        lines_info.append(f"Line {point*2+1}: Point {point+1} - Outer edge")
        screen.update()
        time.sleep(0.8)
        
        # Add label for this line
        label_t = turtle.Turtle()
        label_t.hideturtle()
        label_t.penup()
        label_t.goto(t.xcor(), t.ycor() + 10)
        label_t.color("red")
        label_t.write(f"Point {point+1}", font=("Arial", 10, "bold"))
        
        # Turn to draw the point
        t.right(144)  # The sharp angle of the star point
        t.pencolor("orange")
        t.forward(150)
        lines_info.append(f"Line {point*2+2}: Point {point+1} - Return edge")
        screen.update()
        time.sleep(0.8)
        
        # Turn to next point
        t.left(72)  # 180 - 360/5 = 72 degrees
        
        label_t.clear()
    
    return lines_info

# Create explanation area
explanation = turtle.Turtle()
explanation.hideturtle()
explanation.penup()
explanation.color("cyan")
explanation.goto(0, 250)
explanation.write("A COMPLETE star has 5 points = 10 lines total", 
                  align="center", font=("Arial", 16, "bold"))
screen.update()
time.sleep(2)
explanation.clear()

# Draw the star and get line information
lines = draw_and_label_star()

# Final explanation
final_t = turtle.Turtle()
final_t.hideturtle()
final_t.penup()
final_t.color("yellow")
final_t.goto(0, -200)
final_t.write("COMPLETE STAR: All 5 points (10 lines) drawn!", 
              align="center", font=("Arial", 14, "bold"))
final_t.goto(0, -230)
final_t.write("✓ Point 1: Lines 1-2  ✓ Point 2: Lines 3-4", 
              align="center", font=("Arial", 12, "normal"))
final_t.goto(0, -260)
final_t.write("✓ Point 3: Lines 5-6  ✓ Point 4: Lines 7-8  ✓ Point 5: Lines 9-10", 
              align="center", font=("Arial", 12, "normal"))
screen.update()

t.hideturtle()
screen.mainloop()