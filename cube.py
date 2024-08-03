import turtle


def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)


def draw_cube():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(5)

    # Draw the first square
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.color("blue")
    draw_square(t, 100)

    # Draw the second square (shifted)
    t.penup()
    t.goto(-30, -30)
    t.pendown()
    draw_square(t, 100)

    # Connect the corners to form the cube
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.goto(-30, -30)

    t.penup()
    t.goto(50, -50)
    t.pendown()
    t.goto(70, -30)

    t.penup()
    t.goto(50, 50)
    t.pendown()
    t.goto(70, 70)

    t.penup()
    t.goto(-50, 50)
    t.pendown()
    t.goto(-30, 70)

    # Hide the turtle
    t.hideturtle()

    # Keep the window open until closed by the user
    turtle.done()


draw_cube()
