import turtle


def draw_square():
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(5)

    # Draw the square
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    t.color("blue")
    for _ in range(4):
        t.forward(100)
        t.left(90)

    # Hide the turtle
    t.hideturtle()

    # Keep the window open until closed by the user
    turtle.done()


draw_square()
