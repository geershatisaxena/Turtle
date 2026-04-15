import turtle

# Setup
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
t.pensize(2)

# Function to draw a number
def draw_number(x, y, num):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor("white")
    t.write(str(num), align="center", font=("Arial", 12, "bold"))

# Draw multiplication table as colored squares
size = 40
table_size = 10

# Draw grid and fill with colors based on product
for row in range(1, table_size + 1):
    for col in range(1, table_size + 1):
        product = row * col
        x = col * size - 250
        y = -row * size + 200
        
        # Color based on product value
        if product < 20:
            t.fillcolor("lightgreen")
        elif product < 50:
            t.fillcolor("yellow")
        elif product < 80:
            t.fillcolor("orange")
        else:
            t.fillcolor("red")
        
        # Draw square
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        for _ in range(4):
            t.forward(size - 2)
            t.left(90)
        t.end_fill()
        
        # Draw product number
        draw_number(x + size/2, y - size/2, product)

# Add title
t.penup()
t.goto(0, 250)
t.pencolor("white")
t.write("MULTIPLICATION TABLE PATTERN", align="center", font=("Arial", 20, "bold"))

t.hideturtle()
turtle.done()