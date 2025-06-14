import turtle

# Função para desenhar um círculo preenchido
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y - radius)  # ajustar para desenhar a partir do centro
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Configurações iniciais
turtle.speed(0)
turtle.bgcolor("white")
turtle.title("Desenho do Mickey Mouse")

# Cabeça
draw_circle("black", 100, 0, 0)

# Orelhas
draw_circle("black", 60, -70, 120)  # orelha esquerda
draw_circle("black", 60, 70, 120)   # orelha direita

# Finalizar
turtle.hideturtle()
turtle.done()
