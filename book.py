import turtle


def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_book():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(5)

    # Draw the cover of the book
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    draw_rectangle(t, 100, 150, "brown")

    # Draw the pages of the book
    t.penup()
    t.goto(-45, -45)
    t.pendown()
    draw_rectangle(t, 90, 140, "white")

    # Draw the spine of the book
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.color("black")
    t.width(3)
    t.left(90)
    t.forward(150)

    # Hide the turtle
    t.hideturtle()

    # Keep the window open until closed by the user
    turtle.done()


draw_book()
