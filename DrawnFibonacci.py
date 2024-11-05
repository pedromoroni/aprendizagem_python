import turtle

def calcfib(num=1):
    valor1 = 0
    valor2 = 1
    valor3 = 0
    if num == 0:
        return 0
    elif num == 1:
        return 1
    for i in range(0, num-1):
        valor3 = valor1 + valor2
        valor1 = valor2
        valor2 = valor3
    return valor2

turtle.pencolor('white')
turtle.bgcolor('black')
turtle.hideturtle()
turtle.speed(0)

turtle.left(90)

for x in range(11, 0, -1):
    n = calcfib(x)
    print(calcfib(x))
    for y in range(4):
        turtle.forward(n)
        turtle.right(90)
    turtle.forward(n)
    if x != 0:
        turtle.right(90)
        turtle.forward(n)

turtle.penup()
turtle.home()
turtle.pendown()

turtle.left(90)

for x in range(11, 0, -1):
    n = calcfib(x)
    turtle.circle(-n, 90)


turtle.done()