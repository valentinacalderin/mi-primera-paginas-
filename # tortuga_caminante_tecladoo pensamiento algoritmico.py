# tortuga_caminante_teclado.py
import turtle
import math

# --------- Configuración de la ventana -------------
WIDTH, HEIGHT = 800, 400
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Tortuga caminante con teclado")
screen.bgcolor("skyblue")
screen.tracer(0, 0)

# "Lápiz" que dibuja la tortuga
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

# --------- Estado de la animación ------------------
x, y = 0, -30
phase = 0.0
speed_px = 3
dx, dy = 0, 0

# --------- Parámetros de la tortuga ----------------
body_radius = 40
head_radius = 18
leg_w, leg_h = 10, 22
leg_offset_x = 22
leg_offset_y = -10

# --------- Funciones de dibujo ---------------------
def draw_circle(t, cx, cy, r, color):
    t.goto(cx, cy - r)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()

def draw_rect(t, cx, cy, w, h, angle, color):
    t.goto(cx, cy)
    t.setheading(angle)
    t.forward(-w/2)
    t.right(90)
    t.forward(h/2)
    t.left(90)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()
    t.penup()

def draw_turtle(pen, x, y, phase):
    pen.clear()

    # Cuerpo
    draw_circle(pen, x, y, body_radius, "#2E8B57")

    # Caparazón
    pen.goto(x, y + 10)
    pen.pendown()
    pen.fillcolor("#3CB371")
    pen.begin_fill()
    pen.setheading(45)
    pen.circle(body_radius + 6, 90)
    pen.left(90)
    pen.circle(body_radius + 6, 90)
    pen.end_fill()
    pen.penup()

    # Cabeza
    head_x = x + body_radius + head_radius - 6
    draw_circle(pen, head_x, y + 8, head_radius, "#2E8B57")

    # Ojo
    pen.goto(head_x + 6, y + 18)
    pen.dot(6, "black")

    # Cola
    pen.goto(x - body_radius - 6, y)
    pen.setheading(200)
    pen.pendown()
    pen.fillcolor("#2E8B57")
    pen.begin_fill()
    for _ in range(3):
        pen.forward(12)
        pen.left(120)
    pen.end_fill()
    pen.penup()

    # Piernas animadas
    leg_phase = [
        math.sin(phase),
        math.sin(phase + math.pi),
        math.sin(phase + math.pi / 2),
        math.sin(phase + 3 * math.pi / 2)
    ]

    coords = [
        (x + leg_offset_x, y + leg_offset_y),
        (x - leg_offset_x, y + leg_offset_y),
        (x + leg_offset_x - 6, y + leg_offset_y - 4),
        (x - leg_offset_x + 6, y + leg_offset_y - 4)
    ]

    for i, (lx, ly) in enumerate(coords):
        angle = leg_phase[i] * 30
        lift = leg_phase[i] * 6
        draw_rect(pen, lx, ly + lift, leg_w, leg_h, angle, "#8B4513")

# --------- Controles de teclado --------------------
def move_up():
    global dx, dy
    dx, dy = 0, speed_px

def move_down():
    global dx, dy
    dx, dy = 0, -speed_px

def move_right():
    global dx, dy
    dx, dy = speed_px, 0

def move_left():
    global dx, dy
    dx, dy = -speed_px, 0

def stop():
    global dx, dy
    dx, dy = 0, 0

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(stop, "space")

# --------- Bucle principal -------------------------
def step():
    global x, y, phase

    if dx != 0 or dy != 0:
        x += dx
        y += dy
        phase += 0.18

    # Límites de pantalla
    x = max(-WIDTH//2 + 60, min(WIDTH//2 - 60, x))
    y = max(-HEIGHT//2 + 60, min(HEIGHT//2 - 60, y))

    draw_turtle(pen, x, y, phase)
    screen.update()
    screen.ontimer(step, 20)

# --------- Inicio ---------------------------------
draw_turtle(pen, x, y, phase)
screen.update()
screen.ontimer(step, 20)
screen.mainloop()
