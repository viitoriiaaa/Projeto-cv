import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(color, points):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.end_fill()

def draw_ironman():
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.title("Homem de Ferro - Desenho Estilizado")

    # Capacete
    draw_circle("#8B0000", 120, 0, 100)  # contorno do capacete
    draw_circle("gold", 100, 0, 120)     # interior dourado

    # Olhos
    draw_rectangle("white", -40, 190, 25, 8)
    draw_rectangle("white", 15, 190, 25, 8)

    # Ombros
    draw_circle("#8B0000", 60, -100, 20)
    draw_circle("#8B0000", 60, 100, 20)

    # Corpo
    draw_rectangle("#8B0000", -60, 20, 120, 150)

    # Reator Arc (peito)
    draw_circle("cyan", 15, 0, -30)
    draw_circle("white", 7, 0, -30)

    turtle.hideturtle()
    turtle.done()

draw_ironman()
