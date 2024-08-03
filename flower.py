import turtle


# Function to draw a petal
def draw_petal():
    turtle.color("red")
    turtle.begin_fill()
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.end_fill()


# Function to draw the flower
def draw_flower():
    turtle.speed(10)
    turtle.bgcolor("white")

    # Draw the center of the flower
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    # Draw the petals
    for _ in range(6):
        draw_petal()
        turtle.left(60)

    # Draw the stem
    turtle.color("green")
    turtle.width(10)
    turtle.right(90)
    turtle.forward(300)


# Set up the turtle
turtle.setup(800, 600)
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()

# Draw the flower
draw_flower()

# Hide the turtle and display the window
turtle.hideturtle()
turtle.done()
