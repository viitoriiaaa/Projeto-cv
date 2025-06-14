import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_bow():
    # Laço vermelho da Minnie
    turtle.penup()
    turtle.goto(-25, 160)
    turtle.setheading(0)
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(15, 180)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.circle(15, 180)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(25, 160)
    turtle.setheading(180)
    turtle.begin_fill()
    turtle.circle(15, 180)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.circle(15, 180)
    turtle.end_fill()


def draw_minnie():
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.title("Minnie Mouse - Desenho Estilizado")

    # Orelhas
    draw_circle("black", 60, -60, 120)
    draw_circle("black", 60, 60, 120)

    # Cabeça
    draw_circle("black", 100, 0, 0)

    # Rosto (parte clara)
    draw_circle("#fce4d6", 70, 0, 20)

    # Olhos
    draw_circle("white", 10, -20, 60)
    draw_circle("white", 10, 20, 60)
    draw_circle("black", 5, -20, 60)
    draw_circle("black", 5, 20, 60)

    # Nariz
    draw_circle("black", 7, 0, 40)

    # Boca (sorriso)
    turtle.penup()
    turtle.goto(-25, 20)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.pensize(3)
    turtle.pencolor("black")
    turtle.circle(30, 120)

    # Laço
    draw_bow()

    turtle.hideturtle()
    turtle.done()

draw_minnie()
