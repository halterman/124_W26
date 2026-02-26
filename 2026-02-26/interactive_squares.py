import turtle

def square(x: float, y: float) -> None:
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()
    # print(f'x = {x} and y = {y}')

def twice(x: float) -> float:
    return 2 * x

turtle.title('Drawing some squares')
turtle.tracer(False)
print(twice(6))
turtle.onscreenclick(square)
turtle.update()
turtle.mainloop()
