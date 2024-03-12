import turtle

# Function to draw a red pyramid
def draw_pyramid(size):
    turtle.fillcolor("red")
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

# Function to draw the letter 'M' in Neofetch style
def draw_m(size):
    turtle.penup()
    turtle.goto(-size * 2, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.right(135)
    turtle.forward(size * 2.83)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size * 2.83)
    turtle.right(135)
    turtle.forward(size * 2)

# Function to draw the letter 'e' in Neofetch style
def draw_e(size):
    turtle.penup()
    turtle.goto(-size * 1.2, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.right(90)
    turtle.circle(-size, 180)
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.left(90)
    turtle.forward(size)
    turtle.penup()
    turtle.goto(-size * 1.2, -size)
    turtle.pendown()
    turtle.forward(size)

# Function to draw the letter 'l' in Neofetch style
def draw_l(size):
    turtle.penup()
    turtle.goto(-size * 0.5, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(size * 2)
    turtle.backward(size * 2)

# Function to draw the letter 'o' in Neofetch style
def draw_o(size):
    turtle.penup()
    turtle.goto(size * 1.5, 0)
    turtle.pendown()
    turtle.circle(size)

# Function to draw Neofetch 'Mellow'
def draw_neofetch_text(size):
    draw_m(size)
    turtle.penup()
    turtle.forward(size * 0.5)
    turtle.pendown()
    draw_e(size)
    turtle.penup()
    turtle.forward(size * 0.5)
    turtle.pendown()
    draw_l(size)
    turtle.penup()
    turtle.forward(size * 0.5)
    turtle.pendown()
    draw_l(size)
    turtle.penup()
    turtle.forward(size * 0.5)
    turtle.pendown()
    draw_o(size)
    turtle.penup()

# Main function
def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    # Draw red pyramids of various sizes
    for size in range(50, 201, 50):
        turtle.goto(-size / 2, -size / 2)
        draw_pyramid(size)

    # Draw Neofetch 'Mellow'
    turtle.penup()
    turtle.goto(-350, -250)
    turtle.pendown()
    draw_neofetch_text(50)

    turtle.done()

if __name__ == "__main__":
    main()
