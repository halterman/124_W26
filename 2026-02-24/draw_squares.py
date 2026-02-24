import turtle

def square(x: int, y: int, color: str) -> None:
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()


def stop_sign(x: int, y: int) -> None:
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    for _ in range(8):
        turtle.forward(100)
        turtle.left(45)
    turtle.end_fill()
    turtle.pencolor('white')
    turtle.penup()
    turtle.setposition(x - 60, y + 70)
    turtle.pendown()
    turtle.write('STOP', font=('Arial', 64, 'normal'))
    turtle.right(45)
    turtle.width(5)
    for _ in range(8):
        turtle.forward(92)
        turtle.left(45)
    


turtle.title('Drawing some squares')
turtle.tracer(False)
square(100, 200, 'green')
square(-100, 0, 'blue')
stop_sign(200, -100)
turtle.update()
turtle.done()
