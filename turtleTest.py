import random
import turtle

if __name__ == '__main__':
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor('black')

    turtle.pencolor('purple')
    for i in range(0,250, 2):
        turtle.forward(i * 100)
        turtle.right(179)

    turtle.pencolor('magenta')
    for i in range(250,500, 2):
        turtle.forward(i * 100)
        turtle.right(179)

    turtle.pencolor('violet')
    for i in range(500,750, 2):
        turtle.forward(i * 100)
        turtle.right(179)

    turtle.pencolor('white')
    for i in range(750, 922):
        turtle.forward(i * 100)
        turtle.right(179)

    turtle.pencolor('gray')
    for i in range(922, 1042, 2):
        turtle.forward(i * 100)
        turtle.right(179)

    turtle.pencolor('black')
    for i in range(1042, 1542):
        turtle.forward(i * 100)
        turtle.right(179)

    
