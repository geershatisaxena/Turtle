import turtle
t = turtle.Turtle()
t.speed(8)
t.pensize(4)
def dashed_line(length, dash_size, gap_size):
    """
    Draw a dashed line
    length: total length of the line
    dash_size: length of each dash
    gap_size: length of each gap
    """
    segments = length // (dash_size + gap_size)
    
    for _ in range(segments):
        t.forward(dash_size)
        t.penup()
        t.forward(gap_size)
        t.pendown()

dashed_line(300, 25, 15)
t.hideturtle()
turtle.done()
