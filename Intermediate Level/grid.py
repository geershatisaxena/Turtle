import turtle

# Setup
turtle.speed(0)
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

# Grid settings
size = 400  # Total size of grid
rows = 8
cols = 8
cell_size = size / rows

# Draw grid
for row in range(rows):
    for col in range(cols):
        # Fill color for chessboard pattern
        if (row + col) % 2 == 0:
            turtle.fillcolor("crimson")
        else:
            turtle.fillcolor("lime")
        
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(cell_size)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(cell_size)
    
    # Move to next row
    turtle.backward(size)
    turtle.right(90)
    turtle.forward(cell_size)
    turtle.left(90)

turtle.hideturtle()
turtle.done()